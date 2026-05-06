---
aid: pytorch
name: PyTorch
description: APIs and resources for PyTorch, an open source machine learning framework for tensor computation and deep learning developed by Meta.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Deep Learning
  - Machine Learning
  - Neural Networks
  - Open Source
  - Python
url: https://raw.githubusercontent.com/api-evangelist/pytorch/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: pytorch:pytorch-core-api
    name: PyTorch Core API
    description: Core PyTorch library for tensor computation and deep learning.
    humanURL: https://pytorch.org/docs/stable/index.html
    tags:
      - Deep Learning
      - Machine Learning
      - Tensors
    properties:
      - type: Documentation
        url: https://pytorch.org/docs/stable/index.html
      - type: GettingStarted
        url: https://pytorch.org/get-started/locally/
      - type: APIReference
        url: https://pytorch.org/docs/stable/torch.html
      - type: GitHub
        url: https://github.com/pytorch/pytorch
  - aid: pytorch:torchvision
    name: TorchVision API
    description: Computer vision library for PyTorch with datasets, models, and transforms.
    humanURL: https://pytorch.org/vision/stable/index.html
    tags:
      - Computer Vision
      - Image Processing
      - Models
    properties:
      - type: Documentation
        url: https://pytorch.org/vision/stable/index.html
      - type: GitHub
        url: https://github.com/pytorch/vision
      - type: Models
        url: https://pytorch.org/vision/stable/models.html
  - aid: pytorch:torchtext
    name: TorchText API
    description: Natural language processing library for PyTorch.
    humanURL: https://pytorch.org/text/stable/index.html
    tags:
      - NLP
      - Text Processing
    properties:
      - type: Documentation
        url: https://pytorch.org/text/stable/index.html
      - type: GitHub
        url: https://github.com/pytorch/text
  - aid: pytorch:torchaudio
    name: TorchAudio API
    description: Audio processing library for PyTorch.
    humanURL: https://pytorch.org/audio/stable/index.html
    tags:
      - Audio
      - Speech Recognition
    properties:
      - type: Documentation
        url: https://pytorch.org/audio/stable/index.html
      - type: GitHub
        url: https://github.com/pytorch/audio
      - type: Tutorials
        url: https://pytorch.org/audio/stable/tutorials.html
  - aid: pytorch:pytorch-hub
    name: PyTorch Hub API
    description: Pre-trained model repository and discovery API.
    humanURL: https://pytorch.org/hub/
    tags:
      - Pre-Trained Models
      - Model Hub
      - Transfer Learning
    properties:
      - type: Documentation
        url: https://pytorch.org/docs/stable/hub.html
      - type: Models
        url: https://pytorch.org/hub/research-models
common:
  - type: Blog
    url: https://pytorch.org/blog/
  - type: Community
    url: https://pytorch.org/community
  - type: Forums
    url: https://discuss.pytorch.org/
  - type: GitHubOrganization
    url: https://github.com/pytorch
  - type: GettingStarted
    url: https://pytorch.org/get-started/pytorch-2.0/
  - type: Website
    url: https://pytorch.org
  - type: Ecosystem
    url: https://pytorch.org/ecosystem
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
