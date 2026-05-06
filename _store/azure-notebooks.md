---
aid: azure-notebooks
name: Azure Notebooks
description: Azure Notebooks was a free hosted service to develop and run Jupyter notebooks in the cloud with no installation required. The service was retired on October 9, 2020. Users are recommended to migrate to Azure Machine Learning, Visual Studio Code with Jupyter extension, or GitHub Codespaces for equivalent functionality.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Cloud Computing
  - Data Science
  - Jupyter
  - Notebooks
  - Python
  - Retired
url: https://raw.githubusercontent.com/api-evangelist/azure-notebooks/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis: []
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/machine-learning/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-1st-experiment-sdk-setup
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: StatusPage
    url: https://status.azure.com/
  - type: Features
    data:
      - name: Service Retired
        description: Azure Notebooks was retired on October 9, 2020. Migrate to Azure Machine Learning or GitHub Codespaces.
      - name: Migration Guidance
        description: Microsoft recommends Azure Machine Learning for interactive notebook experiences with Azure compute.
      - name: Alternative Services
        description: Jupyter notebooks are available through Azure Machine Learning, Visual Studio Code, and GitHub Codespaces.
  - type: Integrations
    data:
      - name: Azure Machine Learning
        description: Successor service for hosted Jupyter notebook experiences with Azure compute resources.
      - name: GitHub Codespaces
        description: Cloud-based development environments with Jupyter notebook support.
      - name: Visual Studio Code
        description: Local IDE with Jupyter notebook extension and Azure compute connectivity.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
