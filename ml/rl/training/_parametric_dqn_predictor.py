#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

import logging

from ml.rl.training.sandboxed_predictor import SandboxedRLPredictor


logger = logging.getLogger(__name__)


class _ParametricDQNPredictor(SandboxedRLPredictor):
    def predict(self, float_state_features, int_state_features, actions):
        assert not int_state_features, "Not implemented"

        float_examples = []
        for i in range(len(float_state_features)):
            float_examples.append({**float_state_features[i], **actions[i]})

        return super(_ParametricDQNPredictor, self).predict(float_examples)
