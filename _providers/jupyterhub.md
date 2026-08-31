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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 21
  human_in_the_loop: 4
  name: Jupyterhub Agentic Access
  operation_count: 35
  slug: jupyterhub-agentic-access
  summary_line: 35 operations · 21 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: User activity reporting.
  name: JupyterHub Activity API
  slug: jupyterhub-activity-api
- description: Administrative operations.
  name: JupyterHub Admin API
  slug: jupyterhub-admin-api
- description: Token and cookie verification.
  name: JupyterHub Authorizations API
  slug: jupyterhub-authorizations-api
- description: Hub identity and information.
  name: JupyterHub General API
  slug: jupyterhub-general-api
- description: User group management.
  name: JupyterHub Groups API
  slug: jupyterhub-groups-api
- description: OAuth2 authorization endpoints.
  name: JupyterHub OAuth2 API
  slug: jupyterhub-oauth2-api
- description: Configurable HTTP proxy management.
  name: JupyterHub Proxy API
  slug: jupyterhub-proxy-api
- description: Single-user server lifecycle.
  name: JupyterHub Servers API
  slug: jupyterhub-servers-api
- description: Hub-managed services.
  name: JupyterHub Services API
  slug: jupyterhub-services-api
- description: API token management for users.
  name: JupyterHub Tokens API
  slug: jupyterhub-tokens-api
- description: User account management.
  name: JupyterHub Users API
  slug: jupyterhub-users-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: JupyterHub REST Activity API
  slug: open-jupyterhub-activity-api
- collection_type: open
  name: JupyterHub REST Activity Admin API
  slug: open-jupyterhub-admin-api
- collection_type: open
  name: JupyterHub REST Activity Authorizations API
  slug: open-jupyterhub-authorizations-api
- collection_type: open
  name: JupyterHub REST Activity General API
  slug: open-jupyterhub-general-api
- collection_type: open
  name: JupyterHub REST Activity Groups API
  slug: open-jupyterhub-groups-api
- collection_type: open
  name: JupyterHub REST Activity OAuth2 API
  slug: open-jupyterhub-oauth2-api
- collection_type: open
  name: JupyterHub REST Activity Proxy API
  slug: open-jupyterhub-proxy-api
- collection_type: open
  name: JupyterHub REST API
  slug: open-jupyterhub-rest-api
- collection_type: open
  name: JupyterHub REST Activity Servers API
  slug: open-jupyterhub-servers-api
- collection_type: open
  name: JupyterHub REST Activity Services API
  slug: open-jupyterhub-services-api
- collection_type: open
  name: JupyterHub REST Activity Tokens API
  slug: open-jupyterhub-tokens-api
- collection_type: open
  name: JupyterHub REST Activity Users API
  slug: open-jupyterhub-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/jupyterhub-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jupyterhub/jupyterhub/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/jupyterhub/jupyterhub/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/jupyterhub/jupyterhub/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/jupyterhub/jupyterhub/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jupyterhub-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jupyterhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupyterhub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jupyterhub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jupyterhub-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/project-jupyter
- group: company
  title: ''
  type: Website
  url: https://jupyter.org/hub
- group: docs
  title: ''
  type: Documentation
  url: https://jupyterhub.readthedocs.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://jupyterhub.readthedocs.io/en/stable/tutorial/quickstart.html
- group: other
  title: ''
  type: Installation
  url: https://jupyterhub.readthedocs.io/en/stable/installation-guide.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jupyterhub
- group: other
  title: ''
  type: Repository
  url: https://github.com/jupyterhub/jupyterhub
- group: operate
  title: ''
  type: Community
  url: https://discourse.jupyter.org/c/jupyterhub
- group: commercial
  title: ''
  type: License
  url: https://github.com/jupyterhub/jupyterhub/blob/main/COPYING.md
- group: company
  title: ''
  type: Blog
  url: https://blog.jupyter.org/feed
created: '2024-01-01'
description: JupyterHub is a multi-user server for Jupyter notebooks. It manages authentication, spawns and proxies multiple instances of the single-user Jupyter notebook server, and exposes a REST API for managing users, groups, services, tokens, and the proxy.
finops:
- name: Jupyterhub Finops
  service_category: API
  slug: jupyterhub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupyterhub.png
json_schemas:
- name: JupyterHub Group
  property_count: 4
  slug: jupyterhub-group
- name: JupyterHub Server
  property_count: 10
  slug: jupyterhub-server
- name: JupyterHub User
  property_count: 9
  slug: jupyterhub-user
jsonld:
- class_count: 9
  name: Jupyterhub Context
  property_count: 0
  slug: jupyterhub-context
layout: provider
modified: '2026-05-19'
name: JupyterHub
nav: Providers
network: true
overview: 'JupyterHub publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Admin API, Authorizations API, and 8 more. Tagged areas include Authentication, Data Science, Education, Hub, and Multi-User.


  The JupyterHub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JupyterHub''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 16 more developer resources.'
plans:
- name: Jupyterhub Plans Pricing
  plan_count: 3
  slug: jupyterhub-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Jupyterhub Rate Limits
  slug: jupyterhub-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: JupyterHub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: jupyterhub-jsonschema-spectral-rules
scopes:
- name: Jupyterhub Scopes
  scope_count: 9
  slug: jupyterhub-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 3.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 64.3
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 75.0
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jupyterhub/refs/heads/main/screenshots/jupyterhub-2026-06-20T183841.png
security:
- kind: authentication
  name: Jupyterhub Authentication
  slug: jupyterhub-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Jupyterhub Domain Security
  slug: jupyterhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jupyterhub Vulnerability Disclosure
  slug: jupyterhub-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jupyterhub
tags:
- Authentication
- Data Science
- Education
- Hub
- Multi-User
- Notebooks
- Python
website: https://jupyter.org/hub
---
