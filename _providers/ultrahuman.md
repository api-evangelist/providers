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
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Ultrahuman Agentic Access
  operation_count: 5
  slug: ultrahuman-agentic-access
  summary_line: 5 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: UltraSignal is Ultrahuman's wearable developer platform for building custom algorithms on raw Ring AIR sensor streams - photoplethysmography (PPG), temperature, and accelerometer data. Access is appli
  name: UltraSignal Sensor Platform API
  slug: ultrahuman-ultrasignal-api
- baseURL: https://partner.ultrahuman.com
  baseurl_source: declared
  description: Ring and CGM daily metrics for consented users.
  name: Ultrahuman Metrics API
  slug: ultrahuman-metrics-api
- baseURL: https://partner.ultrahuman.com
  baseurl_source: declared
  description: Basic authorized-user profile information.
  name: Ultrahuman User API
  slug: ultrahuman-user-api
- baseURL: https://partner.ultrahuman.com
  baseurl_source: declared
  description: OAuth 2.0 authorization, token exchange, and revocation.
  name: Ultrahuman O Auth API
  slug: ultrahuman-oauth-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ultrahuman Partner (UltraSignal) Metrics API
  slug: open-ultrahuman-metrics-api
- collection_type: open
  name: Ultrahuman Partner (UltraSignal) Metrics OAuth API
  slug: open-ultrahuman-oauth-api
- collection_type: open
  name: Ultrahuman Partner (UltraSignal) Metrics User API
  slug: open-ultrahuman-user-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ultrahuman/refs/heads/main/agentic-access/ultrahuman-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ultrahuman-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ultrahuman/refs/heads/main/security/ultrahuman-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ultrahuman-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ultrahuman/refs/heads/main/security/ultrahuman-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ultrahuman-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ultrahuman/refs/heads/main/security/ultrahuman-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ultrahuman-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ultrahuman/refs/heads/main/authentication/ultrahuman-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ultrahuman-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ultrahuman.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ultrahuman
- group: docs
  title: ''
  type: Documentation
  url: https://vision.ultrahuman.com/developer-docs
- group: start
  title: ''
  type: SignUp
  url: https://partnerships.ultrahuman.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ultrahuman/refs/heads/main/plans/ultrahuman-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ultrahuman-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ultrahuman/refs/heads/main/rate-limits/ultrahuman-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ultrahuman-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ultrahuman/refs/heads/main/finops/ultrahuman-finops.yml
  title: ''
  type: FinOps
  url: finops/ultrahuman-finops.yml
created: '2026-07-03'
description: Ultrahuman makes the Ring AIR and Ring Pro smart rings and the M1 continuous glucose monitor (CGM), a subscription-free metabolic-health wearable ecosystem. Its Partner (UltraSignal) API lets approved partners read user-consented health metrics - sleep, HRV, resting heart rate, skin temperature, SpO2, movement/recovery indexes, VO2 max, and (with the M1 patch) continuous glucose - over an OAuth 2.0-secured REST API. A separate UltraSignal developer program offers raw sensor streams (PPG, temperature, accelerometer) from the Ring AIR via a loaned developer kit. API access is not self-serve - partners apply and are onboarded with client credentials; end users authorize data sharing from the Ultrahuman app.
finops:
- name: Ultrahuman Finops
  service_category: Health and Wearables
  slug: ultrahuman-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ultrahuman.png
layout: provider
modified: '2026-07-03'
name: Ultrahuman
nav: Providers
network: true
overview: 'Ultrahuman publishes 3 APIs on the [APIs.io](https://apis.io/) network: Metrics API, User API, and O Auth API. Tagged areas include Wearables, Smart Ring, Health, Metabolic Health, and Sleep.


  Ultrahuman''s developer surface includes authentication, documentation, signup flow, and 9 more developer resources.'
plans:
- name: Ultrahuman Plans Pricing
  plan_count: 4
  slug: ultrahuman-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Ultrahuman Rate Limits
  slug: ultrahuman-rate-limits
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 54.0
    developer_ergonomics: 29.8
    discoverability: 68.5
    operational_transparency: 31.6
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/ultrahuman/refs/heads/main/screenshots/ultrahuman-2026-09-02T164801.png
security:
- kind: authentication
  name: Ultrahuman Authentication
  slug: ultrahuman-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ultrahuman Domain Security
  slug: ultrahuman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ultrahuman Vulnerability Disclosure
  slug: ultrahuman-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ultrahuman Trust Center
  slug: ultrahuman-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: ultrahuman
tags:
- Wearables
- Smart Ring
- Health
- Metabolic Health
- Sleep
- HRV
- Recovery
- CGM
- Glucose
- Digital Health
website: https://www.ultrahuman.com
---
