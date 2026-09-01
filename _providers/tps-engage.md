---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Play API from TPS Engage — 1 operation(s) for play.
  name: TPS Engage Play API
  slug: tps-engage-play-api
- description: The Prefetch API from TPS Engage — 1 operation(s) for prefetch.
  name: TPS Engage Prefetch API
  slug: tps-engage-prefetch-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blindspot Pull Play API
  slug: open-tps-engage-play-api
- collection_type: open
  name: Blindspot Pull Play Prefetch API
  slug: open-tps-engage-prefetch-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tps-engage-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tps-engage-blindspot-pull-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tps-engage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seeblindspot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tpsengage.github.io/BlindspotPullApi/
- group: docs
  title: ''
  type: APIReference
  url: https://tpsengage.github.io/BlindspotPullApi/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TPSEngage
- group: operate
  title: ''
  type: Support
  url: https://seeblindspot.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://seeblindspot.com/dooh-pricing-index/
- group: start
  title: ''
  type: SignUp
  url: https://portal.seeblindspot.com/join
- group: start
  title: ''
  type: Login
  url: https://portal.seeblindspot.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seeblindspot.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seeblindspot.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://seeblindspot.com/create-your-first-campaign-in-less-than-5-minutes-step-by-step/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tps-engage-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tps-engage-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tps-engage-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tps-engage-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tps-engage-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tps-engage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tps-engage-rate-limits.yml
- group: build
  title: ''
  type: Examples
  url: examples/tps-engage-examples.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tps-engage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/tps-engage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tps-engage-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/tps-engage-trust-center.yml
created: '2026-07-17'
description: 'TPS Engage, LLC operates Blindspot (seeblindspot.com), a self-serve programmatic digital out-of-home (DOOH) advertising platform: 3,000,000+ digital billboards and screens in 50+ countries bookable by the exact hour, with pay-per-play pricing, no minimums, and an agentic AI media planner (Blinky). The company publishes one public API — the Blindspot Pull API, the device-facing surface screen owners use to pull the creative to play, prefetch media, and log verified proof-of-play — documented with an OpenAPI 3.0 spec on the TPSEngage GitHub org. Originally added to the API Evangelist network as a Techstars portfolio lead, this profile has been enriched from Blindspot''s public surface.'
image: https://seeblindspot.com/wp-content/uploads/APU.COM-_The-One-Times-Square-NYC-Blindspot-1-1.jpg
layout: provider
mcp_servers:
- description: ''
  name: tps-engage-pull-api (candidate)
  slug: tps-engage-pull-api-candidate
modified: '2026-08-13'
name: TPS Engage
nav: Providers
network: true
overview: 'TPS Engage publishes 2 APIs on the [APIs.io](https://apis.io/) network: Play API and Prefetch API. Tagged areas include Company, Advertising, DOOH, Digital Billboards, and Programmatic Advertising.


  TPS Engage''s developer surface includes documentation, API reference, support, pricing, signup flow, getting-started guide, authentication, and 20 more developer resources.'
plans:
- name: Tps Engage Plans Pricing
  plan_count: 0
  slug: tps-engage-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Tps Engage Rate Limits
  slug: tps-engage-rate-limits
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 45.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tps-engage/refs/heads/main/screenshots/tps-engage-2026-08-17T082415.png
security:
- kind: authentication
  name: Tps Engage Authentication
  slug: tps-engage-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tps Engage Domain Security
  slug: tps-engage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tps Engage Vulnerability Disclosure
  slug: tps-engage-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Tps Engage Trust Center
  slug: tps-engage-trust-center
  summary_line: trust center published
slug: tps-engage
tags:
- Company
- Advertising
- DOOH
- Digital Billboards
- Programmatic Advertising
- Media Buying
- Out-of-Home
website: https://seeblindspot.com/
---
