---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
  score: 22.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Shellrecharge Agentic Access
  operation_count: 8
  slug: shellrecharge-agentic-access
  summary_line: 8 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Locations API from ShellRecharge — 4 operation(s) for locations.
  name: ShellRecharge Locations API
  slug: shellrecharge-locations-api
- description: The Sessions API from ShellRecharge — 4 operation(s) for sessions.
  name: ShellRecharge Sessions API
  slug: shellrecharge-sessions-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ShellRecharge EV Platform Locations API
  slug: open-shellrecharge-locations-api
- collection_type: open
  name: ShellRecharge EV Platform Locations Sessions API
  slug: open-shellrecharge-sessions-api
- collection_type: open
  name: ShellRecharge EV Platform API
  slug: open-shellrecharge
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shellrecharge-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shellrecharge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shellrecharge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shellrecharge-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shellrecharge-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shellrecharge
- group: company
  title: ''
  type: Website
  url: https://shellrecharge.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shell.com/api-catalog
- group: commercial
  title: ''
  type: Plans
  url: plans/shellrecharge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shellrecharge-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shellrecharge-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://developer.shell.com/latest-updates
created: '2026-06-21'
description: ShellRecharge (formerly NewMotion) is Shell's EV charging network and operator platform. Its EV-Platform / Shell Developer APIs let partners and charge point operators manage public charging - retrieving charging locations, starting, stopping, and tracking charge sessions, and exchanging locations, sessions, tariffs, tokens, and CDRs over the OCPI 2.2.1 standard. The APIs are partner-gated and secured with OAuth 2.0 client credentials.
finops:
- name: Shellrecharge Finops
  service_category: Mobility and EV Charging
  slug: shellrecharge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shellrecharge.png
layout: provider
modified: '2026-06-21'
name: ShellRecharge
nav: Providers
network: true
overview: 'ShellRecharge publishes 2 APIs on the [APIs.io](https://apis.io/) network: Locations API and Sessions API. Tagged areas include EV Charging, Electric Vehicles, Mobility, Charge Points, and OCPI.


  ShellRecharge''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Shellrecharge Plans Pricing
  plan_count: 1
  slug: shellrecharge-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Shellrecharge Rate Limits
  slug: shellrecharge-rate-limits
scopes:
- name: Shellrecharge Scopes
  scope_count: 0
  slug: shellrecharge-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 46.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 39.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Shellrecharge Authentication
  slug: shellrecharge-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Shellrecharge Domain Security
  slug: shellrecharge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: shellrecharge
tags:
- EV Charging
- Electric Vehicles
- Mobility
- Charge Points
- OCPI
- Energy
website: https://shellrecharge.com
---
