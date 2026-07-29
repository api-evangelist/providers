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
- acting_count: 13
  human_in_the_loop: 3
  name: Jupyter Hub Agentic Access
  operation_count: 23
  slug: jupyter-hub-agentic-access
  summary_line: 23 operations · 13 acting · 3 human-in-the-loop
api_count: 5
apis:
- description: Group membership.
  name: JupyterHub Groups API
  slug: jupyter-hub-groups-api
- description: Hub-level metadata and shutdown.
  name: JupyterHub Hub API
  slug: jupyter-hub-hub-api
- description: Hub-managed and external services.
  name: JupyterHub Services API
  slug: jupyter-hub-services-api
- description: API token management.
  name: JupyterHub Tokens API
  slug: jupyter-hub-tokens-api
- description: User accounts and their servers.
  name: JupyterHub Users API
  slug: jupyter-hub-users-api
artifact_total: 16
collections:
- collection_type: open
  name: JupyterHub REST API
  slug: open-jupyter-hub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jupyter-hub-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jupyter-hub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupyter-hub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jupyter-hub-authentication.yml
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jupyterhub
- group: operate
  title: ''
  type: Community
  url: https://discourse.jupyter.org/c/jupyterhub
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jupyter-hub-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://blog.jupyter.org/feed
created: '2024-01-01'
description: JupyterHub is a multi-user server for Jupyter notebooks. It manages and proxies multiple instances of the single-user Jupyter notebook server, providing authentication and spawning for multiple users.
finops:
- name: Jupyter Hub Finops
  service_category: API
  slug: jupyter-hub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupyter-hub.png
json_schemas:
- name: JupyterHub User
  property_count: 9
  slug: jupyter-hub-user
jsonld:
- class_count: 12
  name: Jupyter Hub Context
  property_count: 0
  slug: jupyter-hub-context
layout: provider
modified: '2026-05-19'
name: JupyterHub
nav: Providers
network: true
overview: 'JupyterHub publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Groups API, Hub API, Services API, and 2 more. Tagged areas include Data Science, Education, Jupyter, Multi-User, and Notebooks.


  The JupyterHub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JupyterHub''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Jupyter Hub Plans Pricing
  plan_count: 3
  slug: jupyter-hub-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 5
  name: Jupyter Hub Rate Limits
  slug: jupyter-hub-rate-limits
rules:
- name: JupyterHub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: jupyter-hub-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.4
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jupyter-hub/refs/heads/main/screenshots/jupyter-hub-2026-06-20T183837.png
security:
- kind: authentication
  name: Jupyter Hub Authentication
  slug: jupyter-hub-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jupyter Hub Domain Security
  slug: jupyter-hub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jupyter Hub Vulnerability Disclosure
  slug: jupyter-hub-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jupyter-hub
tags:
- Data Science
- Education
- Jupyter
- Multi-User
- Notebooks
website: https://jupyter.org/hub
---
