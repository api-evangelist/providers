---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 40
  human_in_the_loop: 6
  name: Jupyter Notebook Agentic Access
  operation_count: 70
  slug: jupyter-notebook-agentic-access
  summary_line: 70 operations · 40 acting · 6 human-in-the-loop
api_count: 14
apis:
- description: WebSocket-based messaging protocol for communication between Jupyter clients and computational kernels. Supports code execution, introspection, completion, and rich output over shell, IOPub, stdin, an
  name: Jupyter Kernel Messaging Protocol
  slug: jupyter-kernel-messaging
- description: Token verification and authorization checks.
  name: Jupyter Notebook Authorization API
  slug: jupyter-notebook-authorization-api
- description: Server configuration section management.
  name: Jupyter Notebook Config API
  slug: jupyter-notebook-config-api
- description: File and directory management including notebooks, files, directories, and checkpoints.
  name: Jupyter Notebook Contents API
  slug: jupyter-notebook-contents-api
- description: General gateway information.
  name: Jupyter Notebook General API
  slug: jupyter-notebook-general-api
- description: Group management for organizing users.
  name: Jupyter Notebook Groups API
  slug: jupyter-notebook-groups-api
- description: Hub lifecycle management.
  name: Jupyter Notebook Hub API
  slug: jupyter-notebook-hub-api
- description: Kernel lifecycle management on the gateway. The gateway may enforce kernel limits and seed kernels.
  name: Jupyter Notebook Kernels API
  slug: jupyter-notebook-kernels-api
- description: Kernel specification listing and retrieval.
  name: Jupyter Notebook Kernelspecs API
  slug: jupyter-notebook-kernelspecs-api
- description: Configurable HTTP proxy routing table management.
  name: Jupyter Notebook Proxy API
  slug: jupyter-notebook-proxy-api
- description: The Services API from Jupyter Notebook — 2 operation(s) for services.
  name: Jupyter Notebook Services API
  slug: jupyter-notebook-services-api
- description: Session management for associating notebooks with running kernels.
  name: Jupyter Notebook Sessions API
  slug: jupyter-notebook-sessions-api
- description: Terminal session management on the server.
  name: Jupyter Notebook Terminals API
  slug: jupyter-notebook-terminals-api
- description: User management including creation, deletion, server management, and token management.
  name: Jupyter Notebook Users API
  slug: jupyter-notebook-users-api
artifact_total: 32
asyncapis:
- description: 'The Jupyter Kernel Messaging Protocol defines the WebSocket-based communication between Jupyter clients (notebooks, consoles) and computational kernels. Messages are exchanged over WebSocket channels '
  name: Jupyter Kernel Messaging Protocol
  slug: jupyter-kernel-messaging-asyncapi
collections:
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway API
  slug: open-jupyter-kernel-gateway-api
- collection_type: open
  name: Jupyter Notebook REST API
  slug: open-jupyter-notebook-rest-api
- collection_type: open
  name: Jupyter Notebook JupyterHub REST API
  slug: open-jupyterhub-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jupyter-notebook-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jupyter-notebook-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupyter-notebook-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jupyter-notebook-authentication.yml
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
  url: https://docs.jupyter.org/en/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jupyter.org/en/latest/start/index.html
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
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/jupyter-notebook
created: '2024-01-15'
description: Jupyter Notebook is the original open-source web application for creating and sharing computational documents that contain live code, equations, visualizations, and narrative text. The Jupyter Notebook server exposes a REST API for managing notebooks, files, kernels, sessions, and terminals, and uses the WebSocket-based Jupyter messaging protocol to communicate with kernels.
finops:
- name: Jupyter Notebook Finops
  service_category: Open-Source Data Science / Notebooks
  slug: jupyter-notebook-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupyter-notebook.png
json_schemas:
- name: Jupyter Contents Model
  property_count: 12
  slug: jupyter-contents-model
- name: Jupyter Kernel Message
  property_count: 6
  slug: jupyter-kernel-message
- name: Jupyter Kernel Specification
  property_count: 3
  slug: jupyter-kernel-spec
- name: Jupyter Notebook Document
  property_count: 4
  slug: jupyter-notebook-document
jsonld:
- class_count: 3
  name: Jupyter Notebook Context
  property_count: 44
  slug: jupyter-notebook-context
layout: provider
modified: '2026-05-19'
name: Jupyter Notebook
nav: Providers
network: true
overview: 'Jupyter Notebook publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Jupyter Kernel Messaging Protocol, Authorization API, Config API, and 11 more. Tagged areas include Data Science, Interactive Computing, Jupyter, Machine Learning, and Notebooks.


  The Jupyter Notebook catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Jupyter Notebook''s developer surface includes authentication, documentation, getting-started guide, engineering blog, support, YouTube channel, Stack Overflow tag, and 8 more developer resources.'
plans:
- name: Jupyter Notebook Plans Pricing
  plan_count: 1
  slug: jupyter-notebook-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 2
  name: Jupyter Notebook Rate Limits
  slug: jupyter-notebook-rate-limits
rules:
- name: Jupyter Notebook API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: jupyter-notebook-asyncapi-spectral-rules
- name: Jupyter Notebook API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jupyter-notebook-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.1
  delta: 3.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 78.1
    developer_ergonomics: 37.0
    discoverability: 87.5
    governance: 65.8
    operational_transparency: 36.8
  previous_composite: 50.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jupyter-notebook/refs/heads/main/screenshots/jupyter-notebook-2026-06-20T183838.png
security:
- kind: authentication
  name: Jupyter Notebook Authentication
  slug: jupyter-notebook-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Jupyter Notebook Domain Security
  slug: jupyter-notebook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jupyter Notebook Vulnerability Disclosure
  slug: jupyter-notebook-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jupyter-notebook
tags:
- Data Science
- Interactive Computing
- Jupyter
- Machine Learning
- Notebooks
- Python
website: https://jupyter.org
---
