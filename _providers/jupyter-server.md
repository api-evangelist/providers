---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Jupyter Server Agentic Access
  operation_count: 31
  slug: jupyter-server-agentic-access
  summary_line: 31 operations · 17 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: File checkpoint (snapshot) management.
  name: Jupyter Server Checkpoints API
  slug: jupyter-server-checkpoints-api
- description: Server configuration sections.
  name: Jupyter Server Config API
  slug: jupyter-server-config-api
- description: Notebook and file management operations.
  name: Jupyter Server Contents API
  slug: jupyter-server-contents-api
- description: Server information, identity, and status.
  name: Jupyter Server General API
  slug: jupyter-server-general-api
- description: Kernel lifecycle management.
  name: Jupyter Server Kernels API
  slug: jupyter-server-kernels-api
- description: Available kernel specifications.
  name: Jupyter Server Kernelspecs API
  slug: jupyter-server-kernelspecs-api
- description: Notebook-kernel session management.
  name: Jupyter Server Sessions API
  slug: jupyter-server-sessions-api
- description: Terminal session management.
  name: Jupyter Server Terminals API
  slug: jupyter-server-terminals-api
artifact_total: 20
collections:
- collection_type: open
  name: Jupyter Server REST API
  slug: open-jupyter-server-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jupyter-server-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupyter-server-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jupyter-server-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/project-jupyter
- group: company
  title: ''
  type: Website
  url: https://jupyter-server.readthedocs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://jupyter-server.readthedocs.io/en/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://jupyter-server.readthedocs.io/en/latest/users/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jupyter-server
- group: other
  title: ''
  type: Repository
  url: https://github.com/jupyter-server/jupyter_server
- group: operate
  title: ''
  type: Community
  url: https://discourse.jupyter.org/
- group: auth
  title: ''
  type: Security
  url: https://jupyter.org/security
- group: company
  title: ''
  type: Blog
  url: https://blog.jupyter.org/feed
created: '2025-02-06'
description: Jupyter Server is the backend that powers Jupyter Notebook, JupyterLab, and other Jupyter web applications. It provides the core REST API for managing kernels, sessions, contents, terminals, and configuration, and it hosts the WebSocket endpoints used to communicate with kernels via the Jupyter messaging protocol.
finops:
- name: Jupyter Server Finops
  service_category: API
  slug: jupyter-server-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupyter-server.png
json_schemas:
- name: Jupyter Server Contents Model
  property_count: 11
  slug: jupyter-server-contents-model
- name: Jupyter Server Kernel
  property_count: 5
  slug: jupyter-server-kernel
- name: Jupyter Server Session
  property_count: 5
  slug: jupyter-server-session
jsonld:
- class_count: 6
  name: Jupyter Server Context
  property_count: 0
  slug: jupyter-server-context
layout: provider
modified: '2026-05-19'
name: Jupyter Server
nav: Providers
network: true
overview: 'Jupyter Server publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Checkpoints API, Config API, Contents API, and 5 more. Tagged areas include Compute, Interactive Computing, Kernels, Notebooks, and Portable.


  The Jupyter Server catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Jupyter Server''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Jupyter Server Plans Pricing
  plan_count: 3
  slug: jupyter-server-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Jupyter Server Rate Limits
  slug: jupyter-server-rate-limits
rules:
- name: Jupyter Server API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: jupyter-server-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.8
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jupyter-server/refs/heads/main/screenshots/jupyter-server-2026-06-20T183848.png
security:
- kind: authentication
  name: Jupyter Server Authentication
  slug: jupyter-server-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Jupyter Server Domain Security
  slug: jupyter-server-domain-security
  summary_line: TLSv1.3 · HSTS
slug: jupyter-server
tags:
- Compute
- Interactive Computing
- Kernels
- Notebooks
- Portable
- Workbooks
website: https://jupyter-server.readthedocs.io/
---
