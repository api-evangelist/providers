---
aid: apache-tvm
name: Apache TVM
description: Apache TVM is an open-source compiler framework for deep learning that provides performance portability across diverse hardware backends including CPUs, GPUs, FPGAs, and specialized accelerators (ARM, NVIDIA, AMD, Qualcomm). It automatically optimizes deep learning models from frameworks like TensorFlow, PyTorch, ONNX, MXNet, and Keras for deployment on edge and cloud targets. TVM is an Apache Software Foundation top-level project.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Compiler
  - Deep Learning
  - Edge Computing
  - Model Optimization
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-tvm/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-tvm:apache-tvm-python-api
    name: Apache TVM Python API
    description: The TVM Python API provides a comprehensive interface for model compilation, optimization, and deployment. Key modules include tvm.relay for defining and optimizing computational graphs, tvm.auto_scheduler for auto-tuning operator schedules, tvm.micro for microcontroller deployment (MicroTVM), and tvm.rpc for remote deployment and profiling. The tvmc command-line tool provides a simplified interface for common TVM workflows.
    humanURL: https://tvm.apache.org/docs/reference/api/python/
    tags:
      - Python
      - Deep Learning
      - Model Optimization
      - Compiler
    properties:
      - type: Documentation
        url: https://tvm.apache.org/docs/reference/api/python/
      - type: SDK
        url: https://pypi.org/project/apache-tvm/
        title: Python Package (PyPI)
  - aid: apache-tvm:apache-tvm-rpc-api
    name: Apache TVM RPC API
    description: The TVM RPC (Remote Procedure Call) system enables remote compilation, deployment, and profiling of optimized models on target devices. It provides server/client APIs for uploading and executing compiled modules on remote hardware, tracking performance metrics, and running AutoTVM/AutoScheduler tuning jobs against real hardware targets.
    humanURL: https://tvm.apache.org/docs/how_to/work_with_microtvm/
    tags:
      - RPC
      - Remote
      - Profiling
      - Hardware
    properties:
      - type: Documentation
        url: https://tvm.apache.org/docs/how_to/work_with_microtvm/
common:
  - type: GitHubRepository
    url: https://github.com/apache/tvm
  - type: Documentation
    url: https://tvm.apache.org/docs/
  - type: Portal
    url: https://tvm.apache.org/
  - type: GettingStarted
    url: https://tvm.apache.org/docs/get_started/
  - type: ReleaseNotes
    url: https://github.com/apache/tvm/releases
  - type: Support
    url: https://discuss.tvm.apache.org/
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Multi-Framework Support
        description: Import models from TensorFlow, PyTorch, ONNX, MXNet, Keras, and other frameworks.
      - name: Hardware-Specific Optimization
        description: Automatic operator scheduling and kernel fusion for CPUs, GPUs, and custom accelerators.
      - name: Auto-Tuning
        description: AutoTVM and AutoScheduler for automated hyperparameter optimization of compute kernels.
      - name: MicroTVM
        description: Deploy optimized models on microcontrollers and bare-metal devices without an OS.
      - name: BYOC Framework
        description: Bring Your Own Codegen framework for integrating custom hardware accelerators.
      - name: Relay IR
        description: High-level intermediate representation for end-to-end model optimization.
  - type: UseCases
    data:
      - name: Edge AI Deployment
        description: Deploy optimized deep learning models on edge devices and microcontrollers.
      - name: Model Serving Optimization
        description: Optimize inference performance for cloud GPU/CPU model serving.
      - name: Cross-Platform Deployment
        description: Compile a single model for multiple hardware targets from one codebase.
      - name: Custom Accelerator Integration
        description: Integrate custom AI accelerators using TVM's BYOC framework.
  - type: Integrations
    data:
      - name: ONNX
        description: Import and optimize ONNX models from any ONNX-compatible ML framework.
      - name: PyTorch
        description: TorchScript to TVM compilation for PyTorch model optimization.
      - name: TensorFlow
        description: TensorFlow and TFLite model import and optimization.
      - name: NVIDIA CUDA
        description: CUDA/cuDNN backend for NVIDIA GPU kernel generation and optimization.
      - name: ARM
        description: ARM CPU (Cortex-A, Cortex-M) and ARM Mali GPU backend support.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
