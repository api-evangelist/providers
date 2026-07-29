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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 21
  human_in_the_loop: 4
  name: Jupyterhub Agentic Access
  operation_count: 35
  slug: jupyterhub-agentic-access
  summary_line: 35 operations · 21 acting · 4 human-in-the-loop
api_count: 11
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
artifact_total: 25
collections:
- collection_type: open
  name: JupyterHub REST API
  slug: open-jupyterhub-rest-api
common:
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


  JupyterHub''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Jupyterhub Plans Pricing
  plan_count: 3
  slug: jupyterhub-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Jupyterhub Rate Limits
  slug: jupyterhub-rate-limits
rules:
- name: JupyterHub API Rules
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
  composite: 50.2
  delta: -4.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.6
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- OAuth2
- Python
website: https://jupyter.org/hub
---
