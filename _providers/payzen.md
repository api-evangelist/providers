---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
asyncapis:
- description: ''
  name: Payzen Webhooks
  slug: payzen-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payzen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payzen.com/
- group: company
  title: ''
  type: Blog
  url: https://payzen.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://payzen.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://payzen.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payzen.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payzen-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/payzen-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/payzen-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payzen-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payzen-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/payzen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/payzen-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: PayZen's own status page monitors business services literally named "API" and "Webhooks", but the only place that integration surface is listed is Epic's Showroom marketplace, which is a login-gated React application; payzen.com has no developer section, api.payzen.com and developer.payzen.com do not resolve in DNS, and docs.payzen.com 302s into a staging app host rather than documentation.
  evidence:
  - status: 200
    url: https://status.payzen.com/
  - status: 404
    url: https://payzen.com/docs
  - status: 200
    url: https://showroom.epic.com/Search?q=PayZen
  - status: 302
    url: https://docs.payzen.com/docs/
  reason: marketplace-only
  state: gated
created: '2026-08-26'
description: 'PayZen is a San Francisco-based healthcare fintech that provides AI-powered patient financing — "Care Now, Pay Later" — for hospitals, health systems and large physician groups. Its platform underwrites each patient''s ability to pay and issues interest-free, fee-free monthly payment plans and a white-labelable Care Card, with the provider paid up front. PayZen markets pre-built integrations with Epic, Cerner and other major EHR systems and is listed on Epic''s Showroom (formerly App Orchard) marketplace, but it publishes no public developer portal, API reference or machine-readable contract: the integration surface is delivered to contracted health systems through the EHR marketplace and an implementation engagement. PayZen LLC is a licensed lender (NMLS 2591891), is SOC 2 Type II certified and operates a Vanta trust portal.'
image: https://payzen.com/wp-content/uploads/2023/10/cropped-cropped-payzen-favicon-3-192x192.png
layout: provider
modified: '2026-08-26'
name: PayZen
nav: Providers
network: true
overview: 'PayZen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Healthcare, Patient Financing, and Revenue Cycle Management.


  The PayZen catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PayZen''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Payzen Plans Pricing
  plan_count: 0
  slug: payzen-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Payzen Rate Limits
  slug: payzen-rate-limits
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 25.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payzen/refs/heads/main/screenshots/payzen-2026-09-02T150923.png
security:
- kind: domain-security
  name: Payzen Domain Security
  slug: payzen-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Payzen Trust Center
  slug: payzen-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: payzen
tags:
- Company
- Payments
- Healthcare
- Patient Financing
- Revenue Cycle Management
- Lending
- Fintech
- Electronic Health Records
website: https://payzen.com/
---
