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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
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
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Shellrecharge Agentic Access
  operation_count: 8
  slug: shellrecharge-agentic-access
  summary_line: 8 operations · 2 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The Locations API from ShellRecharge — 4 operation(s) for locations.
  name: ShellRecharge Locations API
  slug: shellrecharge-locations-api
- description: The Sessions API from ShellRecharge — 4 operation(s) for sessions.
  name: ShellRecharge Sessions API
  slug: shellrecharge-sessions-api
artifact_total: 10
collections:
- collection_type: open
  name: ShellRecharge EV Platform API
  slug: open-shellrecharge
common:
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


  ShellRecharge''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Shellrecharge Plans Pricing
  plan_count: 1
  slug: shellrecharge-plans-pricing
random_paper: 9
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
  composite: 34.5
  delta: 3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 49.6
    developer_ergonomics: 21.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.3
  schema_version: 0.5
  scored_at: '2026-07-27'
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
