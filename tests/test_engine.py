"""
 pyfuzzylite (TM), a fuzzy logic control library in Python.
 Copyright (C) 2010-2017 FuzzyLite Limited. All rights reserved.
 Author: Juan Rada-Vilela, Ph.D. <jcrada@fuzzylite.com>

 This file is part of pyfuzzylite.

 pyfuzzylite is free software: you can redistribute it and/or modify it under
 the terms of the FuzzyLite License included with the software.

 You should have received a copy of the FuzzyLite License along with
 pyfuzzylite. If not, see <http://www.fuzzylite.com/license/>.

 pyfuzzylite is a trademark of FuzzyLite Limited
 fuzzylite is a registered trademark of FuzzyLite Limited.
"""

import unittest

from fuzzylite import *
from tests.assert_component import ComponentAssert


class EngineAssert(ComponentAssert):
    def has_type(self, expected: Engine.Type):
        type = self.actual.infer_type()
        self.test.assertEqual(type, expected,
                              f"expected engine of type {expected}, but found {type}")
        return self

    def is_ready(self, expected: bool, status: str = ""):
        ready, message = self.actual.is_ready()
        self.test.assertEqual(ready, expected, (f"expected engine {'*not*' if not expected else ''} to be ready,"
                                                f"but was {'*not*' if not ready else ''} ready"))
        self.test.assertEqual(message, status)

    def has_n_inputs(self, n: int):
        n_inputs = len(self.actual.inputs)
        self.test.assertEqual(n_inputs, n, f"expected {n} input variable{'' if n == 1 else 's'}, but found {n_inputs}")
        return self

    def has_inputs_named(self, names=List[str]):
        self.test.assertSequenceEqual([iv.name for iv in self.actual.inputs], names)
        return self

    def has_n_outputs(self, n: int):
        n_outputs = len(self.actual.outputs)
        self.test.assertEqual(n_outputs, n,
                              f"expected {n} output variable{'' if n == 1 else 's'}, but found {n_outputs}")
        return self

    def has_outputs_named(self, names=List[str]):
        self.test.assertSequenceEqual([ov.name for ov in self.actual.outputs], names)
        return self

    def has_n_blocks(self, n: int):
        n_blocks = len(self.actual.blocks)
        self.test.assertEqual(n_blocks, n, f"expected {n} rule block{'' if n == 1 else 's'}, but found {n_blocks}")
        return self

    def has_blocks_named(self, names=List[str]):
        self.test.assertSequenceEqual([rb.name for rb in self.actual.blocks], names)
        return self


class TestEngine(unittest.TestCase):
    def test_engine(self):
        flc = Engine("name", "description")
        EngineAssert(self, flc) \
            .has_name("name").has_description("description") \
            .has_n_inputs(0).has_inputs_named([]) \
            .has_n_outputs(0).has_outputs_named([]) \
            .has_n_blocks(0).has_blocks_named([])

    def test_inputs(self):
        flc = Engine("name", "description",
                     [InputVariable("A"), InputVariable("B")])
        EngineAssert(self, flc) \
            .has_name("name").has_description("description") \
            .has_n_inputs(2).has_inputs_named(["A", "B"])

        flc.inputs = []
        EngineAssert(self, flc).has_n_inputs(0).has_inputs_named([])

        flc.inputs = [InputVariable("X"), InputVariable("Y"), InputVariable("Z")]
        EngineAssert(self, flc).has_n_inputs(3).has_inputs_named(["X", "Y", "Z"])

        names = ["X", "Y", "Z"]
        for i, iv in enumerate(flc.inputs):
            self.assertEqual(iv.name, names[i])

    def test_outputs(self):
        flc = Engine("name", "description", [],
                     [OutputVariable("A"), OutputVariable("B")])
        EngineAssert(self, flc) \
            .has_name("name").has_description("description") \
            .has_n_outputs(2).has_outputs_named(["A", "B"])

        flc.outputs = []
        EngineAssert(self, flc).has_n_outputs(0).has_outputs_named([])

        flc.outputs = [OutputVariable("X"), OutputVariable("Y"), OutputVariable("Z")]
        EngineAssert(self, flc).has_n_outputs(3).has_outputs_named(["X", "Y", "Z"])

        names = ["X", "Y", "Z"]
        for i, iv in enumerate(flc.outputs):
            self.assertEqual(iv.name, names[i])