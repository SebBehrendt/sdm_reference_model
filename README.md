SebBehrendt: @workspace Please write a markdown documentation how to use the repo to model a production system and all assets. also sow how a serialization to AAS can be done.
# TODO: rework the documentation!
# SDM Reference Model

The SDM Reference Model provides a reference model for describing a production system and its assets using the Asset Administration Shell (AAS) framework. The model includes various components such as products, resources, procedures, processes, orders, and change scenarios.

## Installation

To install the reference model, just run the following command:

```sh
pip install sdm-reference-model
```

Note that the packages requires python 3.10 or higher.

## Modeling a Production System

To model a production system, you need to define various components such as products, resources, procedures, and processes. Below is an example of how to create these components and serialize them to AAS.

### Example Script

The following example script demonstrates how to model a production system and serialize it to AAS:

```python
import asyncio
from datetime import datetime
import json
from pathlib import Path
import uuid

import aas_middleware

from sdm_reference_model import product, procedure, resources
from sdm_reference_model.reference_model import ReferenceModel

# Define procedures
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
            ),
        ],
    ),
)

# Define products
stell_motor_12334 = product.Product(
    id="Stellmotor_12334",
    description="Stellmotor 12334",
    product_information=product.ProductInformation(
        id="Stellmotor_12334_Information",
        manufacturer="Manufacturer A",
    ),
)

# Add more products, resources, and procedures as needed
products = [
    stell_motor_12334,
    # Add other products here
]

procedures = [procedure_1]
resources = []  # Add resources here

# Combine all components into a reference model
all_aas = procedures + resources + products
reference_model = ReferenceModel.from_models(*all_aas)

# Serialize to JSON
with open(Path(__file__).parent / "pydantic_reference_model.json", "w") as f:
    f.write(reference_model.json())

# Serialize to AAS
basyx_model = aas_middleware.formatting.BasyxFormatter().serialize(reference_model)
aas_json = aas_middleware.formatting.AasJsonFormatter().serialize(reference_model)

with open(Path(__file__).parent / "aas_reference_model.json", "w") as f:
    f.write(json.dumps(aas_json, indent=4))
```


The script will generate two files in the `examples` directory:
    - `pydantic_reference_model.json`: The reference model serialized to JSON.
    - `aas_reference_model.json`: The reference model serialized to AAS JSON format.

## Conclusion

This documentation provides an overview of how to use the repository to model a production system and serialize it to AAS. You can extend the example script to include more components and customize the model as needed.