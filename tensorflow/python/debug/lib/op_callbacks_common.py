# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
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
"""Common utilities and settings used by tfdbg v2's op callbacks."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# The ops that are skipped by tfdbg v2's op callbacks.
# They belong to TensorFlow's control flow ops (e.g., "Enter", "StatelessIf")
# and ops that wrap nested tf.function calls.
OP_CALLBACK_SKIP_OPS = (
    # TODO(b/139668453): The following skipped ops are related to a limitation
    # in the op callback.
    b"Enter",
    b"Exit",
    b"Identity",
    b"If",
    b"Merge",
    b"NextIteration",
    b"StatelessIf",
    b"StatefulPartitionedCall",
    b"Switch",
    b"While",
)
