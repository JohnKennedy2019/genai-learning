import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_FILE = PROJECT_ROOT / "logs" / "application.log"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger()