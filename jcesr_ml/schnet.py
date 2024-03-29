"""Utilities for using models based on SchNet"""

from schnetpack.atomistic import Atomwise
from schnetpack import Properties

class Moleculewise(Atomwise):
    """Make predictions of molecule properties based on a fingerprint of the whole molecule"""

    def forward(self, inputs):
        atom_mask = inputs[Properties.atom_mask]

        # Pool over atoms
        inputs['representation'] = self.atom_pool(inputs['representation'], atom_mask)

        # run prediction
        y = self.out_net(inputs)
        y = self.standardize(y)

        # collect results
        result = {self.property: y}

        if self.derivative:
            sign = -1.0 if self.negative_dr else 1.0
            dy = grad(
                result[self.property],
                inputs[Properties.R],
                grad_outputs=torch.ones_like(result[self.property]),
                create_graph=self.create_graph,
                retain_graph=True,
            )[0]
            result[self.derivative] = sign * dy
        return result
