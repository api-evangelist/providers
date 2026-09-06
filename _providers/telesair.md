---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telesair-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.telesair.com/
- group: company
  title: ''
  type: About
  url: https://www.telesair.com/about-1
- group: operate
  title: ''
  type: Support
  url: https://www.telesair.com/contact-7
- group: company
  title: ''
  type: Blog
  url: https://www.telesair.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telesair.com/privacy
- group: operate
  title: ''
  type: FAQ
  url: https://www.telesair.com/faqs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/telesair-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telesair-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/telesair-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telesair-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/telesair-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/telesair-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/telesair-rate-limits.yml
coverage:
  checked: '2026-08-30'
  detail: Telesair is a medical device manufacturer whose product is the Bonhawa high-flow respiratory humidifier, sold as bedside hardware to US hospitals through an exclusive Tri-anim distribution agreement; its entire web presence is an 11-page Wix marketing site with no developer section, and the only machine-readable surface on the domain is Wix's own platform-provided Site Visitor Assistant MCP endpoint, which returns business details and site search rather than any Telesair product API.
  evidence:
  - status: 200
    url: https://www.telesair.com/pages-sitemap.xml
  - status: 400
    url: https://www.telesair.com/openapi.json
  - status: 404
    url: https://www.telesair.com/api-docs
  - status: 200
    url: https://www.telesair.com/_api/mcp
  - status: 200
    url: https://www.telesair.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: 'Telesair, Inc. is a Southern California MedTech company, founded in 2020 and headquartered in Irvine, California, that builds respiratory care hardware for patients with respiratory insufficiency. Its flagship product is Bonhawa, a purpose-built High Flow Oxygen Therapy (HFOT) respiratory humidifier that delivers warmed and humidified respiratory gases to spontaneously breathing pediatric and adult patients (10 kg and up) across a 2-80 L/min flow range, with separate pediatric and adult modes, a streamlined disinfection process and a touchscreen interface. Bonhawa holds both FDA 510(k) clearance (October 2023) and the CE Mark under the European Medical Device Regulation (August 2023), and is distributed to US hospitals under an exclusive agreement with Tri-anim Health Services. Telesair also supplies AVEA disposable expiratory filters. Telesair is a medical device manufacturer rather than a software vendor: it publishes no developer portal, no API reference and no machine-readable
  API contract. Its only machine-readable agent surface is the Wix platform''s Site Visitor Assistant MCP endpoint and an llms.txt served from its own marketing host.'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Telesair serves a live, unauthenticated remote MCP endpoint from its own marketing host at https://www.telesair.com/_api/mcp. It is the Wix platform's "Site Visitor Assistant" server, provisioned by W
  name: Telesair Site Visitor Assistant (Wix Site MCP)
  slug: telesair-site-visitor-assistant-wix-site-mcp
modified: '2026-08-30'
name: Telesair
nav: Providers
network: true
overview: 'Telesair is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Respiratory Care, and MedTech.


  Telesair''s developer surface includes support, engineering blog, FAQ, authentication, and 10 more developer resources.'
plans:
- name: Telesair Plans Pricing
  plan_count: 0
  slug: telesair-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Telesair Rate Limits
  slug: telesair-rate-limits
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telesair/refs/heads/main/screenshots/telesair-2026-09-02T162737.png
security:
- kind: authentication
  name: Telesair Authentication
  slug: telesair-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Telesair Domain Security
  slug: telesair-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telesair
tags:
- Company
- Medical Devices
- Healthcare
- Respiratory Care
- MedTech
- Hardware
- Oxygen Therapy
- Hospital
website: https://www.telesair.com/
---
