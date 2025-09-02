

# utils/logger.py

import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,  # You can change to DEBUG or ERROR as needed
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Optional: create a logger object
logger = logging.getLogger(__name__)