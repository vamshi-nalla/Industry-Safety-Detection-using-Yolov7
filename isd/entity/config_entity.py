import os
from dataclasses import dataclass
from datetime import datetime
from isd.constant.training_pipeline import *

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = os.path.join(ARTIFACTS_DIR,TIMESTAMP)


training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig() 