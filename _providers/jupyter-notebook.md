---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 40
  human_in_the_loop: 6
  name: Jupyter Notebook Agentic Access
  operation_count: 70
  slug: jupyter-notebook-agentic-access
  summary_line: 70 operations · 40 acting · 6 human-in-the-loop
api_count: 3
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
artifact_total: 46
asyncapis:
- description: 'The Jupyter Kernel Messaging Protocol defines the WebSocket-based communication between Jupyter clients (notebooks, consoles) and computational kernels. Messages are exchanged over WebSocket channels '
  name: Jupyter Kernel Messaging Protocol
  slug: jupyter-kernel-messaging-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway API
  slug: open-jupyter-kernel-gateway-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization API
  slug: open-jupyter-notebook-authorization-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Config API
  slug: open-jupyter-notebook-config-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Contents API
  slug: open-jupyter-notebook-contents-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization General API
  slug: open-jupyter-notebook-general-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Groups API
  slug: open-jupyter-notebook-groups-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Hub API
  slug: open-jupyter-notebook-hub-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Kernels API
  slug: open-jupyter-notebook-kernels-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Kernelspecs API
  slug: open-jupyter-notebook-kernelspecs-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Proxy API
  slug: open-jupyter-notebook-proxy-api
- collection_type: open
  name: Jupyter Notebook REST API
  slug: open-jupyter-notebook-rest-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Services API
  slug: open-jupyter-notebook-services-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Sessions API
  slug: open-jupyter-notebook-sessions-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Terminals API
  slug: open-jupyter-notebook-terminals-api
- collection_type: open
  name: Jupyter Notebook Jupyter Kernel Gateway Authorization Users API
  slug: open-jupyter-notebook-users-api
- collection_type: open
  name: Jupyter Notebook JupyterHub REST API
  slug: open-jupyterhub-rest-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/jupyter-notebook-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jupyter/jupyter_client/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/jupyter/jupyter_client/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/jupyter/jupyter_client/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/jupyter/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/jupyter/jupyter_client/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/jupyter/jupyter_client/blob/main/LICENSE
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
overview: 'Jupyter Notebook publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Jupyter Kernel Messaging Protocol, Authorization API, Config API, and 11 more. Tagged areas include Data Science, Interactive Computing, Jupyter, Machine-Learning, and Notebooks.


  The Jupyter Notebook catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Jupyter Notebook''s developer surface includes authentication, documentation, getting-started guide, engineering blog, support, YouTube channel, Stack Overflow tag, and 15 more developer resources.'
plans:
- name: Jupyter Notebook Plans Pricing
  plan_count: 1
  slug: jupyter-notebook-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Jupyter Notebook Rate Limits
  slug: jupyter-notebook-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Jupyter Notebook API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: jupyter-notebook-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Jupyter Notebook API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jupyter-notebook-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 69.9
    developer_ergonomics: 40.5
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 65.0
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Machine-Learning
- Notebooks
- Python
website: https://jupyter.org
---
