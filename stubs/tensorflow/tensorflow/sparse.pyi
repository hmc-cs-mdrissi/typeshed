from _typeshed import Incomplete
from typing_extensions import TypeAlias

from tensorflow import Tensor, TensorShape, _TensorCompatible
from tensorflow.dtypes import DType

_SparseTensorCompatible: TypeAlias = _TensorCompatible | SparseTensor

class SparseTensor:
    indices: Tensor
    values: Tensor
    dense_shape: Tensor
    shape: TensorShape
    dtype: DType
    name: str
    def __init__(self, indices: _TensorCompatible, values: _TensorCompatible, dense_shape: _TensorCompatible) -> None: ...
    def get_shape(self) -> TensorShape: ...
    # Many arithmetic operations are not directly supported. Some have alternatives like tf.sparse.add instead of +.
    def __div__(self, y: _SparseTensorCompatible) -> SparseTensor: ...
    def __truediv__(self, y: _SparseTensorCompatible) -> SparseTensor: ...
    def __mul__(self, y: _SparseTensorCompatible) -> SparseTensor: ...
    def __rmul__(self, y: _SparseTensorCompatible) -> SparseTensor: ...
    def __getattr__(self, name: str) -> Incomplete: ...

def __getattr__(name: str) -> Incomplete: ...