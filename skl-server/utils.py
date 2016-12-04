import pandas as pd

from dataframe_pb2 import ColumnProto
from dataframe_pb2 import DataType
from dataframe_pb2 import DataFrameProto
from dataframe_pb2 import DataFrameShapeProto


DTYPE_MAP = {
  pd.np.dtype('int64'): DataType.Value('DT_INT64'),
  pd.np.dtype('float64'): DataType.Value('DT_DOUBLE'),
  pd.np.dtype('float32'): DataType.Value('DT_DOUBLE'),
  pd.np.dtype('bool'): DataType.Value('DT_BOOL'),
  pd.np.dtype('str'): DataType.Value('DT_STRING'),
  pd.np.dtype('object'): DataType.Value('DT_STRING')}


PROTO_FIELD_MAP = {
  DataType.Value('DT_INT64'): 'int_val',
  DataType.Value('DT_DOUBLE'): 'double_val',
  DataType.Value('DT_STRING'): 'string_val',
  DataType.Value('DT_BOOL'): 'bool_val'
  }


def pandas_to_proto(df):
    """Converts a pandas.DataFrame `df` to a DataFrameProto.

    FIXME: This function is quite slow::

        >>> n, m = 10, 1000
        >>> df = pd.DataFrame(columns=map(str, range(m)),
        ...        data=pd.np.random.rand(n, m))
        >>> %timeit pandas_to_proto(df)
        1 loop, best of 3: 536 ms per loop

    """
    proto_cols = {}
    n_rows = df.shape[0]
    for col_name in df:
        col = df[col_name]
        dtype = df.dtypes[col_name]
        proto_dtype = DTYPE_MAP[dtype]
        proto_field = PROTO_FIELD_MAP[proto_dtype]
        kw = {'dtype': proto_dtype,
              'n_rows': n_rows,
              proto_field: col}
        proto_col = ColumnProto(**kw)
        proto_cols[col_name] = proto_col
    proto_shape = DataFrameShapeProto(n_rows=df.shape[0], n_columns=df.shape[1])
    return DataFrameProto(shape=proto_shape, columns=proto_cols, index=df.index)
