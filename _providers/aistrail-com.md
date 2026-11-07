---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Normalized historical AIS vessel positions from public maritime authorities.
  name: AIS Trail API
  slug: ais-trail-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/aistrail-com/plans/aistrail-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aistrail-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aistrail-com/conventions/aistrail-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aistrail-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aistrail-com/authentication/aistrail-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aistrail-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/aistrail-com/conformance/aistrail-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aistrail-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/aistrail-com/hosts/aistrail-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aistrail-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aistrail-com/vendors/aistrail-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aistrail-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.aistrail.com/login
- group: auth
  href: https://artifacts.apis.io/aistrail-com/security/aistrail-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aistrail-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aistrail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aistrail.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.aistrail.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://aistrail.com/docs/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://aistrail.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aistrail.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aistrail.com/legal/privacy/
created: '2026-11-01'
description: AIS Trail provides a unified API delivering historical and real-time Automatic Identification System (AIS) data for vessels worldwide. The service offers clean, standardized, and query‑ready ship movement information, supporting use cases such as live tracking, route analysis, and maritime analytics. Users can access vessel positions, historical routes, and source metadata through a consistent RESTful interface, enabling integration into logistics, compliance, and marine research applications.
image: https://aistrail.com/assets/img/og-aistrail.png
layout: provider
modified: '2026-11-01'
name: AIS Trail
nav: Providers
network: true
overview: 'AIS Trail is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Maritime, AIS, Data, and Real-Time.


  AIS Trail''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 10 more developer resources.'
plans:
- name: Aistrail Com Plans Pricing
  plan_count: 4
  slug: aistrail-com-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 33.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aistrail Com Authentication
  slug: aistrail-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aistrail Com Domain Security
  slug: aistrail-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aistrail-com
tags:
- Company
- Maritime
- AIS
- Data
- Real-Time
website: https://aistrail.com/
---
