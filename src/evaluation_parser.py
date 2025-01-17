from typing import Dict, List, Optional
from dataclasses import dataclass
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


@dataclass
class MetricResult:
    metric_name: str
    score: float
    passed: bool
    actual_value: str
    labels: List[str]
    threshold_score: str
    custom_labels: List[str]
    status: str
    error_message: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict) -> "MetricResult":
        try:
            evaluation_details = data.get("evaluation_details", {})
            metrics_config = data.get("metrics_config", {})

            try:
                score = float(data.get("score", 0))
            except (ValueError, TypeError):
                logging.warning(
                    f"Invalid score value for metric {data.get('metric_name', 'UNKNOWN')}"
                )
                score = 0.0

            try:
                labels = evaluation_details.get("metric_labels", []) or []
                if not isinstance(labels, list):
                    labels = [str(labels)]
            except Exception as e:
                logging.warning(f"Error processing labels: {str(e)}")
                labels = ["Unknown"]

            return cls(
                metric_name=data.get("metric_name", "UNKNOWN"),
                score=score,
                passed=data.get("passed", False),
                actual_value=str(evaluation_details.get("actual_value", "N/A")),
                labels=labels,
                threshold_score=str(evaluation_details.get("threshold_score", "N/A")),
                custom_labels=metrics_config.get("custom_labels", []),
                status=data.get("metric_evaluation_status", "UNKNOWN"),
                error_message=data.get("error_message"),
            )
        except Exception as e:
            logging.error(f"Error parsing metric result: {str(e)}")
            return cls(
                metric_name="ERROR",
                score=0.0,
                passed=False,
                actual_value="N/A",
                labels=["Error"],
                threshold_score="N/A",
                custom_labels=[],
                status="ERROR",
                error_message=f"Parser Error: {str(e)}",
            )

    def __str__(self) -> str:
        try:
            status_symbol = "✅" if self.passed else "❌"
            result = [
                f"{status_symbol} {self.metric_name}:",
                f"  Score: {self.score:.2f}",
                f"  Status: {self.status}",
            ]

            if self.labels:
                result.append(f"  Labels: {', '.join(self.labels)}")

            if self.error_message:
                result.append(f"  ⚠️ Error: {self.error_message}")

            if self.threshold_score != "N/A":
                result.append(f"  Threshold: {self.threshold_score}")

            return "\n".join(result)
        except Exception as e:
            return f"❌ Error formatting metric result: {str(e)}"


class EvaluationParser:
    def __init__(self, evaluation_data: Dict):
        try:
            self.status = evaluation_data.get("status", "UNKNOWN")
            self.message = evaluation_data.get("message", "No message available")
            self.remaining_credits = evaluation_data.get("remaining_credits", "N/A")

            # Safely process results
            results = evaluation_data.get("results", [])
            if not isinstance(results, list):
                logging.error("Results data is not a list")
                results = []

            self.results = []
            for result in results:
                try:
                    self.results.append(MetricResult.from_dict(result))
                except Exception as e:
                    logging.error(f"Error processing individual result: {str(e)}")
                    # Add an error result instead of failing
                    self.results.append(
                        MetricResult(
                            metric_name="ERROR",
                            score=0.0,
                            passed=False,
                            actual_value="N/A",
                            labels=["Error"],
                            threshold_score="N/A",
                            custom_labels=[],
                            status="ERROR",
                            error_message=f"Failed to process result: {str(e)}",
                        )
                    )
        except Exception as e:
            logging.error(f"Error initializing EvaluationParser: {str(e)}")
            self.status = "ERROR"
            self.message = f"Parser initialization failed: {str(e)}"
            self.remaining_credits = "N/A"
            self.results = []

    def get_passed_metrics(self) -> List[MetricResult]:
        return [r for r in self.results if r.passed]

    def get_failed_metrics(self) -> List[MetricResult]:
        return [r for r in self.results if not r.passed]

    def __str__(self) -> str:
        try:
            status_color = "🟢" if self.status == 200 else "🔴"
            result = [
                f"{status_color} Status: {self.status}",
                f"📝 Message: {self.message}",
                f"💳 Remaining Credits: {self.remaining_credits}",
                "\n📊 Results:",
            ]

            if self.results:
                for metric in self.results:
                    result.append(str(metric))
            else:
                result.append("No results available")

            return "\n".join(result)
        except Exception as e:
            return f"❌ Error formatting evaluation results: {str(e)}"
