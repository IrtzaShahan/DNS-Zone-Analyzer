"""
Production Entry Point for DNS-Zone-Analyzer
Category: SYS
"""
import sys
import logging
from . import core

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def bootstrap():
    logger.info("Bootstrapping subsystem...")
    app = core.Engine()
    try:
        app.start()
    except KeyboardInterrupt:
        logger.warning("Graceful shutdown.")
    except Exception as e:
        logger.error(f"Fatal crash: {e}")
        sys.exit(1)

if __name__ == "__main__":
    bootstrap()
