---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Jupyter Server Agentic Access
  operation_count: 31
  slug: jupyter-server-agentic-access
  summary_line: 31 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: http://localhost:8888/api
  baseurl_source: declared
  description: File checkpoint (snapshot) management.
  name: Jupyter Server Checkpoints API
  slug: jupyter-server-checkpoints-api
- baseURL: http://localhost:8888/api
  baseurl_source: declared
  description: Server configuration sections.
  name: Jupyter Server Config API
  slug: jupyter-server-config-api
- baseURL: http://localhost:8888/api
  baseurl_source: declared
  description: Notebook and file management operations.
  name: Jupyter Server Contents API
  slug: jupyter-server-contents-api
- baseURL: http://localhost:8888/api
  baseurl_source: declared
  description: Server information, identity, and status.
  name: Jupyter Server General API
  slug: jupyter-server-general-api
- baseURL: http://localhost:8888/api
  baseurl_source: declared
  description: Kernel lifecycle management.
  name: Jupyter Server Kernels API
  slug: jupyter-server-kernels-api
- baseURL: http://localhost:8888/api
  baseurl_source: declared
  description: Available kernel specifications.
  name: Jupyter Server Kernelspecs API
  slug: jupyter-server-kernelspecs-api
- baseURL: http://localhost:8888/api
  baseurl_source: declared
  description: Notebook-kernel session management.
  name: Jupyter Server Sessions API
  slug: jupyter-server-sessions-api
- baseURL: http://localhost:8888/api
  baseurl_source: declared
  description: Terminal session management.
  name: Jupyter Server Terminals API
  slug: jupyter-server-terminals-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jupyter Server REST Checkpoints API
  slug: open-jupyter-server-checkpoints-api
- collection_type: open
  name: Jupyter Server REST Checkpoints Config API
  slug: open-jupyter-server-config-api
- collection_type: open
  name: Jupyter Server REST Checkpoints Contents API
  slug: open-jupyter-server-contents-api
- collection_type: open
  name: Jupyter Server REST Checkpoints General API
  slug: open-jupyter-server-general-api
- collection_type: open
  name: Jupyter Server REST Checkpoints Kernels API
  slug: open-jupyter-server-kernels-api
- collection_type: open
  name: Jupyter Server REST Checkpoints Kernelspecs API
  slug: open-jupyter-server-kernelspecs-api
- collection_type: open
  name: Jupyter Server REST API
  slug: open-jupyter-server-rest-api
- collection_type: open
  name: Jupyter Server REST Checkpoints Sessions API
  slug: open-jupyter-server-sessions-api
- collection_type: open
  name: Jupyter Server REST Checkpoints Terminals API
  slug: open-jupyter-server-terminals-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jupyter-server/jupyter_server/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/jupyter-server/jupyter_server/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/jupyter-server/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/jupyter-server/jupyter_server/blob/main/CONTRIBUTING.rst
- group: commercial
  title: ''
  type: License
  url: https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE
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
overview: 'Jupyter Server publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Checkpoints API, Config API, Contents API, and 5 more. Tagged areas include Compute, Interactive Computing, Kernel, Notebooks, and Portable.


  The Jupyter Server catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Jupyter Server''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 13 more developer resources.'
plans:
- name: Jupyter Server Plans Pricing
  plan_count: 3
  slug: jupyter-server-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Jupyter Server Rate Limits
  slug: jupyter-server-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Jupyter Server API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: jupyter-server-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 62.3
    catalog_earned_first_party: 0.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 64.6
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 65.0
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Kernel
- Notebooks
- Portable
- Workbooks
website: https://jupyter-server.readthedocs.io/
---
