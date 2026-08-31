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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Nected Agentic Access
  operation_count: 12
  slug: nected-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- description: The Dev API from Nected — 7 operation(s) for dev.
  name: Nected Dev API
  slug: nected-dev-api
- description: The Nected API from Nected — 2 operation(s) for nected.
  name: Nected Nected API
  slug: nected-nected-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nected Dev API
  slug: open-nected-dev-api
- collection_type: open
  name: Dev Nected API
  slug: open-nected-nected-api
- collection_type: open
  name: Nected API
  slug: open-nected
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nected-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nected-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nected-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nected
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nected-ai
- group: company
  title: ''
  type: Website
  url: https://www.nected.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nected.ai
- group: company
  title: ''
  type: Blog
  url: https://www.nected.ai/blog
created: '2026-03-27'
description: Nected is a low-code workflow automation and decision engine platform for building business rules and automated processes. The API supports triggering rules and workflows, managing global variables, listing entities, retrieving audit logs, and checking usage.
finops:
- name: Nected Finops
  service_category: API
  slug: nected-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nected.png
layout: provider
modified: '2026-05-19'
name: Nected
nav: Providers
network: true
overview: 'Nected publishes 2 APIs on the [APIs.io](https://apis.io/) network: Dev API and Nected API. Tagged areas include Low-Code, Workflow-Automation, Decision Engine, and Business Rules.


  Nected''s developer surface includes authentication, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Nected Plans Pricing
  plan_count: 3
  slug: nected-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Nected Rate Limits
  slug: nected-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nected/refs/heads/main/screenshots/nected-2026-06-20T190119.png
security:
- kind: authentication
  name: Nected Authentication
  slug: nected-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nected Domain Security
  slug: nected-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nected
tags:
- Low-Code
- Workflow-Automation
- Decision Engine
- Business Rules
website: https://www.nected.ai
---
