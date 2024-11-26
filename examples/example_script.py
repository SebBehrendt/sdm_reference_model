from datetime import datetime
import json
from pathlib import Path
import uuid

import aas_middleware

from sdm_reference_model import product, procedure, resources

from sdm_reference_model.reference_model import ReferenceModel


procedure_1 = procedure.Procedure(
    id="Pressen_1_manuell",
    description="Manuelles Pressen 1",
    procedure_information=procedure.ProcedureInformation(
        id="Pressen_1_manuell_Information",
        description="Manuelles Pressen 1 Information",
        procedure_type=procedure.ProcedureTypeEnum.PRODUCTION,
    ),
    process_attributes=None,
    execution_model=procedure.ExecutionModel(
        id="Pressen_1_manuell_Execution_Model",
        description="Manuelles Pressen 1 Execution Model",
        schedule=None,
        exeuction_log=[
            procedure.Event(
                id_short="u" + str(uuid.uuid1()).replace("-", "_"),
                time=datetime.now().isoformat(),
                resource_id="Station_Pressen_1_manuell",
                procedure_id="Pressen_1_manuell",
                procedure_type=procedure.ProcedureTypeEnum.PRODUCTION,
                activity=procedure.ActivityTypeEnum.START,
                product_id="Stellmotor_12392",
            ),
            procedure.Event(
                id_short="u" + str(uuid.uuid1()).replace("-", "_"),
                time=datetime.now().isoformat(),
                resource_id="Station_Pressen_1_manuell",
                procedure_id="Pressen_1_manuell",
                procedure_type=procedure.ProcedureTypeEnum.PRODUCTION,
                activity=procedure.ActivityTypeEnum.START,
                product_id="Stellmotor_12334",
            ),
        ],
    ),
    procedure_emission=procedure.ProcedureConsumption(
        id="Pressen_1_manuell_Emission",
        description="Manuelles Pressen 1 Emission",
        power_consumption=47.9,
        water_consumption=0.0,
    ),
)


procedure_2 = procedure.Procedure(
    id="Pressen_3_automatisch",
    description="Automatisches Pressen 3",
    procedure_information=procedure.ProcedureInformation(
        id="Pressen_3_automatisch_Information",
        description="Automatisches Pressen 3 Information",
        procedure_type=procedure.ProcedureTypeEnum.PRODUCTION,
    ),
    process_attributes=None,
    execution_model=procedure.ExecutionModel(
        id="Pressen_3_automatisch_Execution_Model",
        description="Automatisches Pressen 3 Execution Model",
        schedule=None,
        exeuction_log=[
            procedure.Event(
                id_short="u" + str(uuid.uuid1()).replace("-", "_"),
                time=datetime.now().isoformat(),
                resource_id="Station_Pressen_3_automatisch",
                procedure_id="Pressen_3_automatisch",
                procedure_type=procedure.ProcedureTypeEnum.PRODUCTION,
                activity=procedure.ActivityTypeEnum.START,
                product_id="Stellmotor_12392",
            ),
            procedure.Event(
                id_short="u" + str(uuid.uuid1()).replace("-", "_"),
                time=datetime.now().isoformat(),
                resource_id="Station_Pressen_3_automatisch",
                procedure_id="Pressen_3_automatisch",
                procedure_type=procedure.ProcedureTypeEnum.PRODUCTION,
                activity=procedure.ActivityTypeEnum.START,
                product_id="Stellmotor_12334",
            ),
        ],
    ),
    procedure_emission=procedure.ProcedureConsumption(
        id="Pressen_3_automatisch_Emission",
        description="Automatisches Pressen 3 Emission",
        power_consumption=897.4,
        water_consumption=0.0,
    ),
)

procedures = [procedure_1, procedure_2]

resource_1 = resources.Resource(
    id="Station_Pressen_1_Manuell",
    description="Station Pressen 1 (Manuell)",
    resource_information=resources.ResourceInformation(
        id="Station_Pressen_1_Manuell_Information",
        description="Station Pressen 1 (Manuell) Information",
        manufacturer="wbk Institut für Produktionstechnik",
        production_level="Station",
        resource_type="Manufacturing",
    ),
    product_reference=resources.ProductReference(
        id="Station_Pressen_1_Manuell_Product_Reference",
        description="Station Pressen 1 (Manuell) Product Reference",
        product_reference_id="wbk_manuelle_Pressstation",
    ),
)

resource_2 = resources.Resource(
    id="Station_Pressen_3_Automatisch",
    description="Station Pressen 3 (Automatisch)",
    resource_information=resources.ResourceInformation(
        id="Station_Pressen_3_Automatisch_Information",
        description="Station Pressen 3 (Automatisch) Information",
        manufacturer="Bosch",
        production_level="Station",
        resource_type="Manufacturing",
    ),
    product_reference=resources.ProductReference(
        id="Station_Pressen_3_Automatisch_Product_Reference",
        description="Station Pressen 3 (Automatisch) Product Reference",
        product_reference_id="Bosch_automatische_Pressstation",
    ),
)

resource = [resource_1, resource_2]

product_manuelle_station = product.Product(
    id="wbk_manuelle_Pressstation",
    description="Manuelle Pressstation",
    product_information=product.ProductInformation(
        id="wbk_manuelle_Pressstation_Information",
        manufacturer="wbk Institut für Produktionstechnik",
        product_type="Manuelle_Pressstation",
        maintenance_manual="https://www.wbk.kit.edu/downloads/Manuelle_Pressstation_WBK.pdf",
        operating_manual="https://www.wbk.kit.edu/downloads/Manuelle_Pressstation_WBK.pdf",
        disassembly_manual="https://www.wbk.kit.edu/downloads/Manuelle_Pressstation_WBK.pdf",
        green_house_gas_emission=product.GreenHouseGasEmission(
            id_short="wbk_manuelle_Pressstation_GreenHouseGasEmission",
            description="Manuelle Pressstation GreenHouseGasEmission",
            emission_scope_one=0,
            emission_scope_two=0,
            emission_scope_three=200,
        ),
    ),
)

product_automatische_station = product.Product(
    id="Bosch_automatische_Pressstation",
    description="Automatische Pressstation",
    product_information=product.ProductInformation(
        id="Bosch_automatische_Pressstation_Information",
        manufacturer="Bosch",
        product_type="Automatische_Pressstation",
        maintenance_manual="https://www.bosch.de/pressstation/automatisch",
        operating_manual="https://www.bosch.de/pressstation/automatisch",
        disassembly_manual="https://www.bosch.de/pressstation/automatisch",
        green_house_gas_emission=product.GreenHouseGasEmission(
            id_short="Bosch_automatische_Pressstation_GreenHouseGasEmission",
            description="Automatische Pressstation GreenHouseGasEmission",
            emission_scope_one=0,
            emission_scope_two=0,
            emission_scope_three=600,
        ),
    ),
)

stell_motor_12392 = product.Product(
    id="Stellmotor_12392",
    description="Stellmotor 12392",
    product_information=product.ProductInformation(
        id="Stellmotor_12392_Information",
        manufacturer="Bosch",
        product_type="Stellmotor_lang",
        maintenance_manual="https://www.bosch.de/Stellmotor/Wartungsanleitung.pdf",
        operating_manual="https://www.bosch.de/Stellmotor/Betriebsanleitung.pdf",
        disassembly_manual="https://www.bosch.de/Stellmotor/Disassembly.pdf",
        green_house_gas_emission=product.GreenHouseGasEmission(
            id_short="Stellmotor_12392_GreenHouseGasEmission",
            description="Stellmotor 12392 GreenHouseGasEmission",
            emission_scope_one=0.02342,
            emission_scope_two=0.12303,
            emission_scope_three=5.794,
        ),
    ),
    bom=product.BOM(
        id="Stellmotor_12392_BOM",
        description="Stellmotor 12392 BOM",
        sub_products=[
            product.SubProduct(
                id_short="Stellmotor_12392_BOM_SubProduct_1",
                description="Stellmotor 12392 BOM SubProduct 1",
                quantity=1,
                product_type="Poltopf_lang",
                product_id="Poltopf_lang_897964",
                product_use_type=product.ProductUseType.ASSEMBLED,
            ),
            product.SubProduct(
                id_short="Stellmotor_12392_BOM_SubProduct_2",
                description="Stellmotor 12392 BOM SubProduct 2",
                quantity=2,
                product_type="Magnete_lang",
                product_id="Magnete_lang_12345",
                product_use_type=product.ProductUseType.ASSEMBLED,
            ),
        ],
    ),
)

stell_motor_12334 = product.Product(
    id="Stellmotor_12334",
    description="Stellmotor 12334",
    product_information=product.ProductInformation(
        id="Stellmotor_12334_Information",
        manufacturer="Bosch",
        product_type="Stellmotor_kurz",
        maintenance_manual="https://www.bosch.de/Stellmotor/Wartungsanleitung.pdf",
        operating_manual="https://www.bosch.de/Stellmotor/Betriebsanleitung.pdf",
        disassembly_manual="https://www.bosch.de/Stellmotor/Disassembly.pdf",
        green_house_gas_emission=product.GreenHouseGasEmission(
            id_short="Stellmotor_12334_GreenHouseGasEmission",
            description="Stellmotor 12334 GreenHouseGasEmission",
            emission_scope_one=0.024712,
            emission_scope_two=0.15502,
            emission_scope_three=8.794,
        ),
    ),
    bom=product.BOM(
        id="Stellmotor_12334_BOM",
        description="Stellmotor 12334 BOM",
        sub_products=[
            product.SubProduct(
                id_short="Stellmotor_12334_BOM_SubProduct_1",
                description="Stellmotor 12334 BOM SubProduct 1",
                quantity=1,
                product_type="Poltopf_kurz",
                product_id="Poltopf_kurz_9897964",
                product_use_type=product.ProductUseType.ASSEMBLED,
            ),
            product.SubProduct(
                id_short="Stellmotor_12334_BOM_SubProduct_2",
                description="Stellmotor 12334 BOM SubProduct 2",
                quantity=2,
                product_type="Magnete_kurz",
                product_id="Magnete_kurz_12345",
                product_use_type=product.ProductUseType.ASSEMBLED,
            ),
        ],
    ),
)


products = [
    stell_motor_12334,
    stell_motor_12392,
    product_automatische_station,
    product_manuelle_station,
]

all_aas = procedures + resource + products

reference_model = ReferenceModel.from_models(*all_aas)

with open(Path(__file__).parent / "pydantic_reference_model.json", "w") as f:
    f.write(reference_model.json())

basyx_model = aas_middleware.formatting.BasyxFormatter().serialize(reference_model)
aas_json = aas_middleware.formatting.AasJsonFormatter().serialize(reference_model)

with open(Path(__file__).parent / "aas_reference_model.json", "w") as f:
    f.write(json.dumps(aas_json, indent=4))
