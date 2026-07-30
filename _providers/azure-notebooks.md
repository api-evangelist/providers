---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-notebooks-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/machine-learning/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-1st-experiment-sdk-setup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2024-01-01'
description: Azure Notebooks was a free hosted service to develop and run Jupyter notebooks in the cloud with no installation required. The service was retired on October 9, 2020. Users are recommended to migrate to Azure Machine Learning, Visual Studio Code with Jupyter extension, or GitHub Codespaces for equivalent functionality.
features:
- description: Azure Notebooks was retired on October 9, 2020. Migrate to Azure Machine Learning or GitHub Codespaces.
  name: Service Retired
- description: Microsoft recommends Azure Machine Learning for interactive notebook experiences with Azure compute.
  name: Migration Guidance
- description: Jupyter notebooks are available through Azure Machine Learning, Visual Studio Code, and GitHub Codespaces.
  name: Alternative Services
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-notebooks.png
integrations:
- description: Successor service for hosted Jupyter notebook experiences with Azure compute resources.
  name: Azure Machine Learning
- description: Cloud-based development environments with Jupyter notebook support.
  name: GitHub Codespaces
- description: Local IDE with Jupyter notebook extension and Azure compute connectivity.
  name: Visual Studio Code
layout: provider
modified: '2026-04-19'
name: Azure Notebooks
nav: Providers
network: true
overview: 'Azure Notebooks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Azure, Cloud Computing, Data Science, Jupyter, and Notebooks.


  Azure Notebooks'' developer surface includes developer portal, documentation, getting-started guide, and 5 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 16.9
  delta: -1.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 18.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-notebooks/refs/heads/main/screenshots/azure-notebooks-2026-06-20T172906.png
security:
- kind: domain-security
  name: Azure Notebooks Domain Security
  slug: azure-notebooks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-notebooks
tags:
- Azure
- Cloud Computing
- Data Science
- Jupyter
- Notebooks
- Python
- Retired
website: https://portal.azure.com
---
