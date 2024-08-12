from __future__ import annotations
from typing import Literal, Type, Union, Optional, List

from pydantic import BaseModel

from .processes import Process
from .procedure import Procedure, TimeModel
from .product import Product
from .resources import Resource
from .order import Order
from .change_scenario import ChangeScenario
from aas_middleware.model.data_model import DataModel, NESTED_DICT


class ReferenceModel(DataModel):
    products: List[Product] = []
    resources: List[Resource] = []
    procedures: List[Procedure] = []
    processes: List[Process] = []
    orders: List[Order] = []
    change_scenario: Optional[ChangeScenario] = None

    def from_dict(self, data: NESTED_DICT) -> None:
        # self.super().from_dict(data=data, types=[Product, Resource, Procedure, Process, Order, ChangeScenario])
        # use the from dict of the super class
        super(ReferenceModel, self).from_dict(data=data, types=[Product, Resource, Procedure, Process, Order, ChangeScenario])
        self.products = self.get_models_of_type(Product)
        self.resources = self.get_models_of_type(Resource)
        self.procedures = self.get_models_of_type(Procedure)
        self.processes = self.get_models_of_type(Process)
        self.orders = self.get_models_of_type(Order)
        change_scenarios = self.get_models_of_type(ChangeScenario)
        if change_scenarios:
            self.change_scenario = change_scenarios.pop()
        else:
            self.change_scenario = None


    @classmethod
    def from_models(cls, *models: List[Union[Product, Resource, Procedure, Process, Order, ChangeScenario]]) -> ReferenceModel:
        instance = cls()
        for model in models:
            if isinstance(model, Product):
                instance.products.append(model)
            elif isinstance(model, Resource):
                instance.resources.append(model)
            elif isinstance(model, Procedure):
                instance.procedures.append(model)
            elif isinstance(model, Process):
                instance.processes.append(model)
            elif isinstance(model, Order):
                instance.orders.append(model)
            elif isinstance(model, ChangeScenario):
                instance.change_scenario = model
            instance.add(model)
        return instance