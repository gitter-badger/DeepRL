#!/usr/bin/env python
# -*- coding: utf8 -*-

from ActionSelection.ActionSelection import ActionSelection
import numpy as np

class ContinuousActionSelection(ActionSelection):
    """Selection of an action in a continuous action space"""
    def __init__(self):
        super(ContinuousActionSelection, self).__init__()

    def select_action(mu, sigma):
        return np.random.normal(mu, sigma)
