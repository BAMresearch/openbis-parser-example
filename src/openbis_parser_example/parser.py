import os
import time

from bam_masterdata.datamodel.object_types import ExperimentalStep
from bam_masterdata.parsing import AbstractParser


class OpenbisParserExample(AbstractParser):
    def parse(self, files, collection, logger):
        delay_seconds = float(os.getenv("OPENBIS_PARSER_EXAMPLE_DELAY_SECONDS", "0"))
        if delay_seconds > 0:
            logger.info("Artificial parser delay enabled.", delay_seconds=delay_seconds)
            time.sleep(delay_seconds)

        synthesis = ExperimentalStep(name="Synthesis")
        synthesis_id = collection.add(synthesis)
        measurement = ExperimentalStep(name="Measurement")
        measurement_id = collection.add(measurement)
        _ = collection.add_relationship(synthesis_id, measurement_id)
        logger.info(
            "Parsing finished: Added examples synthesis and measurement experimental steps."
        )
