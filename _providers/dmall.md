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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dmall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dmall.com
created: '2026-07-17'
description: DMall (多点数智, Dmall Inc.) is an Asia-Pacific retail digitalization service provider that pairs consulting with technology to deliver an all-in-one digital retail operating system for supermarkets, grocery chains, and other retailers. Its cloud-native SaaS platform (Dmall OS) spans supply chain, point-of-sale, store operations, membership, e-commerce, and O2O fulfillment, helping traditional retailers modernize into data-driven omnichannel businesses. The company is backed by IDG Capital among other investors. DMall does not currently publish a public developer portal, open-platform documentation, or machine-readable API specifications; this profile captures its public web identity and domain security posture while awaiting a documented API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dmall.png
layout: provider
modified: '2026-07-18'
name: DMall
nav: Providers
network: true
overview: DMall is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, E-Commerce, and Software-as-a-Service.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dmall/refs/heads/main/screenshots/dmall-2026-07-25T212157.png
security:
- kind: domain-security
  name: Dmall Domain Security
  slug: dmall-domain-security
  summary_line: TLSv1.2 · DMARC
slug: dmall
tags:
- Company
- Consumer
- Retail
- E-Commerce
- Software-as-a-Service
- Digital Retail
- Supply Chain
- China
website: https://www.dmall.com
---
