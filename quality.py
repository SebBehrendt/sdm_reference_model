from aas_middleware import AAS, Submodel, SubmodelElementCollection, Reference

from submodules.sdm_reference_model.procedure import ProcedureExecutionData

class QualityFeature(SubmodelElementCollection):
    feature_type: str
    function: str
    # upper_warning_limit: float
    # lower_warning_limit: float
    # upper_control_limit: float
    # lower_control_limit: float
    target_value: float
    upper_tolerance: float
    lower_tolerance: float
    unit: str
    # sample_size: Optional[int]
    production_execution_log: list[ProcedureExecutionData]
    measurement_log: list[ProcedureExecutionData]


class QualityData(Submodel):
    quality_features: list[QualityFeature]

# TODO: think about if quality could be a submodel of a product?
# This would be create because in the events of a product are already
# referenced in the TrackingData submodel of the product.
class Quality(AAS):
    quality_data: QualityData
