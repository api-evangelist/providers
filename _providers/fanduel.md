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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fanduel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fanduel-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fanduel
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fanduel
- group: company
  title: ''
  type: Website
  url: https://www.fanduel.com/
- group: other
  title: ''
  type: AffiliatesProgram
  url: https://www.fanduelpartners.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/fanduel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fanduel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fanduel-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://www.fanduel.com/llms.txt
created: '2026-05-08'
description: FanDuel is a major US sports betting and daily fantasy sports operator (FanDuel Sportsbook, FanDuel Casino, FanDuel Fantasy, FanDuel TV). FanDuel does not publish a public developer REST API for its sportsbook, casino, or fantasy products. Internal/private APIs power the apps and a Sportradar/SBTech-derived trading stack but are not available to third-party developers.
finops:
- name: Fanduel Finops
  service_category: Sports Betting / DFS
  slug: fanduel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fanduel.png
layout: provider
modified: '2026-05-08'
name: FanDuel
nav: Providers
network: true
overview: FanDuel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports Betting, Daily Fantasy Sports, Sportsbook, Casino, and Gaming.
plans:
- name: Fanduel Plans Pricing
  plan_count: 1
  slug: fanduel-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Fanduel Rate Limits
  slug: fanduel-rate-limits
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fanduel/refs/heads/main/screenshots/fanduel-2026-06-20T181034.png
security:
- kind: domain-security
  name: Fanduel Domain Security
  slug: fanduel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fanduel Vulnerability Disclosure
  slug: fanduel-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fanduel
tags:
- Sports Betting
- Daily Fantasy Sports
- Sportsbook
- Casino
- Gaming
- Regulated
website: https://www.fanduel.com/
---
