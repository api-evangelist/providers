---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/prizepicks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prizepicks-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myprizepicks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prize-picks
- group: company
  title: ''
  type: Website
  url: https://prizepicks.com/
- group: other
  title: ''
  type: AffiliatesProgram
  url: https://prizepicks.com/promotions
- group: commercial
  title: ''
  type: Plans
  url: plans/prizepicks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prizepicks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prizepicks-finops.yml
created: '2026-05-08'
description: PrizePicks is a US daily-fantasy/pick-em sports operator focused on player-prop projections (more/less). PrizePicks does not publish a public developer REST API. Internal/private endpoints power the web and mobile apps but are not documented or licensed for third-party use.
finops:
- name: Prizepicks Finops
  service_category: Daily Fantasy Sports
  slug: prizepicks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prizepicks.png
layout: provider
modified: '2026-05-08'
name: PrizePicks
nav: Providers
network: true
overview: PrizePicks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Daily Fantasy Sports, Player Props, Pick-em, Gaming, and Regulated.
plans:
- name: Prizepicks Plans Pricing
  plan_count: 1
  slug: prizepicks-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 1
  name: Prizepicks Rate Limits
  slug: prizepicks-rate-limits
score:
  band: emerging
  composite: 14.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 14.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Prizepicks Domain Security
  slug: prizepicks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prizepicks Vulnerability Disclosure
  slug: prizepicks-vulnerability-disclosure
  summary_line: Hackerone
slug: prizepicks
tags:
- Daily Fantasy Sports
- Player Props
- Pick-em
- Gaming
- Regulated
website: https://prizepicks.com/
---
