---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://skyselect.com/
- group: other
  title: ''
  type: Product
  url: https://www.skyselect.com/product
- group: commercial
  title: ''
  type: Pricing
  url: https://www.skyselect.com/plans
- group: company
  title: ''
  type: Blog
  url: https://www.skyselect.com/insights
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.skyselect.com/
- group: start
  title: ''
  type: Login
  url: https://app.skyselect.com/db/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skyselect.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skyselect.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/skyselect-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skyselect-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skyselect-well-known.yml
created: '2026-07-17'
description: SkySelect is an AI-powered aircraft parts procurement platform for airlines, MROs (maintenance, repair and overhaul providers), and aircraft lessors. Founded in 2017 and headquartered in San Francisco, it operates an eProcurement-as-a-Service platform that automates sourcing, purchasing, and order tracking for aviation materials. Rather than a listings-based marketplace, buyers submit a demand list and SkySelect's specialised procurement AI automatically issues RFQs to a global network of 3,000+ verified suppliers, having processed more than US$6 billion in transactions. The platform exposes an integration API (inventory sync, RFQ reception, and quote submission) gated behind account login; partners such as Rotabull connect via API Key and Secret credentials generated in Developer Settings. SkySelect is backed by Initialized Capital and raised US$9M in 2026.
image: https://www.skyselect.com/_next/static/images/logo-749bfeaf511d1231670624e18b0090df.svg
layout: provider
modified: '2026-07-21'
name: SkySelect
nav: Providers
network: true
overview: 'SkySelect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplaces, Aviation, Procurement, and Supply Chain.


  SkySelect''s developer surface includes pricing, engineering blog, authentication, and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skyselect/refs/heads/main/screenshots/skyselect-2026-09-02T160032.png
security:
- kind: authentication
  name: Skyselect Authentication
  slug: skyselect-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Skyselect Domain Security
  slug: skyselect-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: skyselect
tags:
- Company
- Marketplaces
- Aviation
- Procurement
- Supply Chain
- Aircraft Parts
- Artificial Intelligence
- MRO
website: https://skyselect.com/
---
