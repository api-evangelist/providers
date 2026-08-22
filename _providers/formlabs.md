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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Formlabs Agentic Access
  operation_count: 16
  slug: formlabs-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 6
apis:
- description: 'Local-network REST API served by the PreFormServer application for automating job preparation (import, auto-orient, auto-support, auto-layout, hollow, label), scene management, print-time estimation, '
  name: Formlabs Local API (PreFormServer)
  slug: formlabs-local-api
- description: The Consumables API from Formlabs — 2 operation(s) for consumables.
  name: Formlabs Consumables API
  slug: formlabs-consumables-api
- description: The Events API from Formlabs — 1 operation(s) for events.
  name: Formlabs Events API
  slug: formlabs-events-api
- description: The Groups API from Formlabs — 5 operation(s) for groups.
  name: Formlabs Groups API
  slug: formlabs-groups-api
- description: The Printers API from Formlabs — 2 operation(s) for printers.
  name: Formlabs Printers API
  slug: formlabs-printers-api
- description: The Prints API from Formlabs — 2 operation(s) for prints.
  name: Formlabs Prints API
  slug: formlabs-prints-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Formlabs Web Consumables API
  slug: open-formlabs-consumables-api
- collection_type: open
  name: Formlabs Web Consumables Events API
  slug: open-formlabs-events-api
- collection_type: open
  name: Formlabs Web Consumables Groups API
  slug: open-formlabs-groups-api
- collection_type: open
  name: Formlabs Web Consumables Printers API
  slug: open-formlabs-printers-api
- collection_type: open
  name: Formlabs Web Consumables Prints API
  slug: open-formlabs-prints-api
- collection_type: open
  name: Formlabs Web API
  slug: open-formlabs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/formlabs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formlabs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formlabs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/formlabs-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Formlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/formlabs
- group: company
  title: ''
  type: Website
  url: https://formlabs.com
- group: other
  title: ''
  type: DeveloperPlatform
  url: https://formlabs.com/materials/developer-platform/
- group: docs
  title: ''
  type: Documentation
  url: https://support.formlabs.com/s/topic/Developer-Portal
- group: commercial
  title: ''
  type: Plans
  url: plans/formlabs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/formlabs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/formlabs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://formlabs.com/blog/
created: '2026-06-20'
description: Formlabs designs and manufactures desktop and industrial 3D printers (SLA and SLS), materials, and software (PreForm, Dashboard). Its developer platform exposes the Formlabs Web API (Dashboard Developer API) for remote monitoring and management of Internet-connected printers, prints, consumables, events, and printer groups, plus a Local API (PreFormServer) for local-network job preparation and printer control.
finops:
- name: Formlabs Finops
  service_category: Manufacturing and Hardware
  slug: formlabs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/formlabs.png
layout: provider
modified: '2026-06-20'
name: Formlabs
nav: Providers
network: true
overview: 'Formlabs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Consumables API, Events API, Groups API, and 2 more. Tagged areas include 3D Printing, Additive Manufacturing, SLA, SLS, and Hardware.


  Formlabs'' developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Formlabs Plans Pricing
  plan_count: 2
  slug: formlabs-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Formlabs Rate Limits
  slug: formlabs-rate-limits
scopes:
- name: Formlabs Scopes
  scope_count: 1
  slug: formlabs-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 34.5
  delta: 0.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 57.6
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/formlabs/refs/heads/main/screenshots/formlabs-2026-06-20T181439.png
security:
- kind: authentication
  name: Formlabs Authentication
  slug: formlabs-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Formlabs Domain Security
  slug: formlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: formlabs
tags:
- 3D Printing
- Additive Manufacturing
- SLA
- SLS
- Hardware
- Dashboard
website: https://formlabs.com
---
