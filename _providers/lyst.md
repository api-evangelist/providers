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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: http://www.lyst.com
- group: company
  title: ''
  type: Blog
  url: https://making.lyst.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lyst
- group: operate
  title: ''
  type: Support
  url: https://help.lyst.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.lyst.com/account/register/
- group: company
  title: ''
  type: Partners
  url: https://www.lyst.com/partners/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lyst-domain-security.yml
created: '2026-07-17'
description: 'Lyst is a global fashion aggregation and shopping platform that consolidates products from more than 27,000 brands and retailers, connecting roughly 160 million annual shoppers with clothing, shoes, bags, accessories and jewelry across a single personalized, AI-driven catalog. Rather than a public developer API, Lyst exposes a partner surface: brands and retailers integrate via product-feed synchronization and a Stripe-powered "Lyst Shop" checkout, with API access granted privately during a two-week partner onboarding. Backed by Accel and Balderton Capital, Lyst also runs an engineering organization (making.lyst.com, github.com/lyst) best known for the open-source LightFM recommendation library.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lyst.png
layout: provider
modified: '2026-07-20'
name: LYST
nav: Providers
network: true
overview: 'LYST is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fashion, E-Commerce, and Shopping.


  LYST''s developer surface includes engineering blog, support, signup flow, and 4 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lyst/refs/heads/main/screenshots/lyst-2026-07-25T225759.png
security:
- kind: domain-security
  name: Lyst Domain Security
  slug: lyst-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lyst
tags:
- Company
- Consumer
- Fashion
- E-Commerce
- Shopping
- Marketplace
- Retail
- Recommendations
website: http://www.lyst.com
---
