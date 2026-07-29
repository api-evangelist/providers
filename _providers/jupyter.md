---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Jupyter Agentic Access
  operation_count: 30
  slug: jupyter-agentic-access
  summary_line: 30 operations · 17 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: Backend that powers Jupyter Notebook, JupyterLab, and other Jupyter web applications. Exposes the core REST API and the WebSocket messaging endpoints used to communicate with kernels.
  name: Jupyter Server
  slug: jupyter-server
- description: Multi-user server for Jupyter notebooks. Manages authentication, spawns and proxies multiple instances of the single-user Jupyter notebook server, and exposes a REST API for users, groups, services, t
  name: JupyterHub
  slug: jupyterhub
- description: Next-generation web-based interactive development environment for notebooks, code, and data, with a JupyterLab Server REST API for settings, workspaces, themes, translations, and licenses.
  name: JupyterLab
  slug: jupyterlab
- description: The Config API from Jupyter — 1 operation(s) for config.
  name: Jupyter Config API
  slug: jupyter-config-api
- description: The Contents API from Jupyter — 3 operation(s) for contents.
  name: Jupyter Contents API
  slug: jupyter-contents-api
- description: The Jupyter Server REST API API from Jupyter — 1 operation(s) for jupyter server rest api.
  name: Jupyter Jupyter Server REST API API
  slug: jupyter-jupyter-server-rest-api-api
- description: The Kernels API from Jupyter — 4 operation(s) for kernels.
  name: Jupyter Kernels API
  slug: jupyter-kernels-api
- description: The Kernelspecs API from Jupyter — 1 operation(s) for kernelspecs.
  name: Jupyter Kernelspecs API
  slug: jupyter-kernelspecs-api
- description: The Me API from Jupyter — 1 operation(s) for me.
  name: Jupyter Me API
  slug: jupyter-me-api
- description: The Sessions API from Jupyter — 2 operation(s) for sessions.
  name: Jupyter Sessions API
  slug: jupyter-sessions-api
- description: The Status API from Jupyter — 1 operation(s) for status.
  name: Jupyter Status API
  slug: jupyter-status-api
- description: The Terminals API from Jupyter — 2 operation(s) for terminals.
  name: Jupyter Terminals API
  slug: jupyter-terminals-api
artifact_total: 19
collections:
- collection_type: open
  name: Jupyter Server REST API
  slug: open-jupyter
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jupyter-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jupyter-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupyter-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/project-jupyter
- group: company
  title: ''
  type: Website
  url: https://jupyter.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jupyter.org/
- group: company
  title: ''
  type: Blog
  url: https://blog.jupyter.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jupyter
- group: operate
  title: ''
  type: Community
  url: https://jupyter.org/community
- group: operate
  title: ''
  type: Support
  url: https://discourse.jupyter.org/
- group: auth
  title: ''
  type: Security
  url: https://jupyter.org/security
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ProjectJupyter
created: '2024-01-01'
description: Project Jupyter is an open-source initiative that develops the software, open standards, and services for interactive computing across dozens of programming languages. The Jupyter ecosystem includes Jupyter Notebook, JupyterLab, Jupyter Server, JupyterHub, the Jupyter messaging protocol, and supporting client libraries.
finops:
- name: Jupyter Finops
  service_category: API
  slug: jupyter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupyter.png
layout: provider
modified: '2026-05-19'
name: Jupyter
nav: Providers
network: true
overview: 'Jupyter publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Config API, Contents API, Jupyter Server REST API API, and 6 more. Tagged areas include Data Science, Education, Interactive Computing, Notebooks, and Python.


  Jupyter''s developer surface includes documentation, engineering blog, support, YouTube channel, and 8 more developer resources.'
plans:
- name: Jupyter Plans Pricing
  plan_count: 3
  slug: jupyter-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Jupyter Rate Limits
  slug: jupyter-rate-limits
score:
  band: thin
  composite: 32.9
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 37.3
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jupyter/refs/heads/main/screenshots/jupyter-2026-06-20T183836.png
security:
- kind: domain-security
  name: Jupyter Domain Security
  slug: jupyter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jupyter Vulnerability Disclosure
  slug: jupyter-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jupyter
tags:
- Data Science
- Education
- Interactive Computing
- Notebooks
- Python
- Scientific Computing
website: https://jupyter.org
---
