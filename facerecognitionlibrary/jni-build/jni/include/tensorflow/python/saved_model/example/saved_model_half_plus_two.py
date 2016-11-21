## Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Exports an example linear regression inference graph.

Exports a TensorFlow graph to /tmp/saved_model/half_plus_two/ based on the
SavedModel format.

This graph calculates,
  y = a*x + b
where a and b are variables with a=0.5 and b=2.

Output from this program is typically used to exercise SavedModel load and
execution code.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from tensorflow.core.protobuf import meta_graph_pb2
from tensorflow.python.saved_model import builder as saved_model_builder
from tensorflow.python.saved_model import constants
from tensorflow.python.saved_model import utils


def _generate_saved_model_for_half_plus_two(export_dir, as_text=False):
  """Generates SavedModel for half plus two.

  Args:
    export_dir: The directory to which the SavedModel should be written.
    as_text: Writes the SavedModel protocol buffer in text format to disk.
  """
  builder = saved_model_builder.SavedModelBuilder(export_dir)

  with tf.Session(graph=tf.Graph()) as sess:
    # Set up the model parameters as variables to exercise variable loading
    # functionality upon restore.
    a = tf.Variable(0.5, name="a")
    b = tf.Variable(2.0, name="b")

    # Create a placeholder for serialized tensorflow.Example messages to be fed.
    serialized_tf_example = tf.placeholder(tf.string, name="tf_example")

    # Parse the tensorflow.Example looking for a feature named "x" with a single
    # floating point value.
    feature_configs = {"x": tf.FixedLenFeature([1], dtype=tf.float32),}
    tf_example = tf.parse_example(serialized_tf_example, feature_configs)
    # Use tf.identity() to assign name
    x = tf.identity(tf_example["x"], name="x")
    y = tf.add(tf.mul(a, x), b, name="y")

    # Set up the signature for regression with input and output tensor
    # specification.
    input_tensor = meta_graph_pb2.TensorInfo()
    input_tensor.name = serialized_tf_example.name
    signature_inputs = {"input": input_tensor}

    output_tensor = meta_graph_pb2.TensorInfo()
    output_tensor.name = tf.identity(y).name
    signature_outputs = {"output": output_tensor}
    signature_def = utils.build_signature_def(signature_inputs,
                                              signature_outputs, "regression")

    # Initialize all variables and then save the SavedModel.
    sess.run(tf.initialize_all_variables())
    builder.add_meta_graph_and_variables(
        sess, [constants.TAG_SERVING],
        signature_def_map={"regression": signature_def})
    builder.save(as_text)


def main(_):
  export_dir_pb = "/tmp/saved_model/half_plus_two"
  _generate_saved_model_for_half_plus_two(export_dir_pb)

  export_dir_pbtxt = "/tmp/saved_model/half_plus_two_pbtxt"
  _generate_saved_model_for_half_plus_two(export_dir_pbtxt, as_text=True)


if __name__ == "__main__":
  tf.app.run()
