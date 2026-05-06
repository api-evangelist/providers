---
aid: google-colab
name: Google Colab
description: Google Colab (Colaboratory) is a hosted Jupyter notebook environment that provides free access to computing resources including GPUs and TPUs, with APIs for managing notebooks, runtimes, and integration with Google Drive for collaborative data science and machine learning workflows.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-colab/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Collaboration
  - Data Science
  - Google Cloud
  - Jupyter
  - Machine Learning
  - Notebooks
  - Python
apis:
  - name: Colab API via Google Drive API
    description: Google Colab notebooks are stored as files in Google Drive with the MIME type application/vnd.google.colaboratory. The Google Drive API provides programmatic access to create, read, update, delete, share, and organize Colab notebooks. Developers can use the Drive API to list notebooks, manage permissions for collaboration, copy templates, and integrate Colab notebooks into automated workflows.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.google.com/drive/api/guides/about-sdk
    baseURL: https://www.googleapis.com/drive/v3
    tags:
      - File Management
      - Google Drive
      - Notebooks
    properties:
      - type: Documentation
        url: https://developers.google.com/drive/api/reference/rest/v3
      - type: OpenAPI
        url: openapi/colab-drive-openapi.yml
      - type: JSONSchema
        url: json-schema/google-colab-notebook-schema.json
  - name: Colab Runtime and Kernel Management
    description: Google Colab provides internal APIs for managing notebook runtimes and kernels, including connecting to hosted runtimes, local runtimes, and custom GCE VM backends. The runtime API handles kernel lifecycle (connect, interrupt, restart), resource allocation (GPU/TPU), and execution of notebook cells. These capabilities are exposed through the Colab UI and the colab Python package.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://research.google.com/colaboratory/faq.html
    baseURL: https://colab.research.google.com
    tags:
      - GPU
      - Kernels
      - Runtime
      - TPU
    properties:
      - type: Documentation
        url: https://research.google.com/colaboratory/faq.html
  - name: Colab Enterprise API
    description: The Colab Enterprise API on Google Cloud provides managed notebook runtimes integrated with Vertex AI. It enables creating and managing notebook execution schedules, runtime templates, and managed runtimes within Google Cloud projects. The API supports enterprise governance features including VPC Service Controls, customer-managed encryption keys, and IAM-based access control.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/colab/docs
    baseURL: https://notebooks.googleapis.com
    tags:
      - Enterprise
      - Managed Notebooks
      - Vertex AI
    properties:
      - type: Documentation
        url: https://cloud.google.com/colab/docs/reference/rest
common:
  - type: GettingStarted
    url: https://colab.research.google.com/notebooks/welcome.ipynb
  - type: Pricing
    url: https://colab.research.google.com/signup
  - type: Authentication
    url: https://developers.google.com/drive/api/guides/about-auth
  - type: Support
    url: https://research.google.com/colaboratory/faq.html
  - type: Status
    url: https://status.cloud.google.com
  - type: JSON-LD
    url: json-ld/google-colab-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
