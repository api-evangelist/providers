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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dsw-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dswinc
- group: company
  title: ''
  type: Website
  url: https://www.dsw.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dsw-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/dsw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dsw-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://www.dsw.com/customer-service/general-questions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dsw.com/legal/web-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dsw.com/legal/privacy-policy
coverage:
  checked: '2026-09-06'
  detail: DSW is a footwear retailer with no developer program at all — developer.dsw.com does not resolve, the only DSW-operated API host (api.dsw.com, the private storefront backend named in the dsw.com homepage window.__env block) returns a hard 404 for every spec and /.well-known/ path and an Akamai 403 on its routed services, and supplier integration is handled over EDI through the Designer Brands vendor portal rather than a partner API.
  evidence:
  - status: 404
    url: https://api.dsw.com/openapi.json
  - status: 404
    url: https://api.dsw.com/.well-known/api-catalog
  - status: 404
    url: https://www.dsw.com/.well-known/security.txt
  - status: 404
    url: https://designerbrands.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-04-28'
description: 'DSW (Designer Shoe Warehouse) is the footwear and accessories retail banner of Designer Brands Inc. (NYSE: DBI), selling athletic shoes, sneakers, boots, sandals and accessories through roughly 500 US stores, the dsw.com storefront, a mobile app, and the DSW VIP Rewards loyalty program. DSW publishes no public API, SDK, developer portal or machine-readable contract: dsw.com is a client-side Angular application served by a private first-party backend at api.dsw.com, and supplier-side integration runs over EDI through the Designer Brands vendor portal rather than a partner API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dsw.png
layout: provider
modified: '2026-09-06'
name: Dsw
nav: Providers
network: true
overview: 'Dsw is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, E-Commerce, Footwear, Apparel, and Consumer.


  Dsw''s developer surface includes support and 8 more developer resources.'
plans:
- name: Dsw Plans Pricing
  plan_count: 0
  slug: dsw-plans-pricing
press:
- date: '2026-05-25'
  title: DSW Successfully Incorporates AI into Customer Experience
  url: https://www.nice.com/blog/dsw-successfully-incorporates-ai-into-customer-experience
- date: '2026-05-25'
  title: Designer Brands Debuts "Warehouse Reimagined" for ...
  url: https://www.prnewswire.com/news-releases/designer-brands-debuts-warehouse-reimagined-for-enhanced-immersive-retail-store-experience-301542851.html
- date: '2026-05-25'
  title: Epsilon to Launch “Front Row Connection,” For DSW
  url: https://www.epsilon.com/us/about-us/pressroom/epsilon-to-launch-front-row-connection-for-dsw
- date: '2026-05-25'
  title: DSW is in the news! Our latest launch
  url: https://www.instagram.com/p/DWOd4XyjVfL/
- date: '2026-05-25'
  title: DSW partners with Marketing Evolution on AI-powered ...
  url: https://www.marketingdive.com/news/dsw-partners-with-marketing-evolution-on-ai-powered-personalization-strateg/517594/
random_paper: 19
rate_limits:
- limit_count: 0
  name: Dsw Rate Limits
  slug: dsw-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/dsw/refs/heads/main/screenshots/dsw-2026-06-20T180312.png
security:
- kind: domain-security
  name: Dsw Domain Security
  slug: dsw-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dsw
tags:
- Retail
- E-Commerce
- Footwear
- Apparel
- Consumer
- Loyalty
- Omnichannel
website: https://www.dsw.com
---
