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
  url: security/hungryroot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hungryroot.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hungryroot.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.hungryroot.com/hc/en-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hungryroot-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hungryroot.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hungryroot.com/privacy/
created: '2026-07-17'
description: Hungryroot is a personalized grocery and meal-planning service that blends meal-kit convenience with grocery-store variety. Its AI-driven personalization engine builds each customer's cart from dietary preferences, health goals, and budget, drawing on a catalog of 50,000+ recipes and curated grocery products that support high-protein, gluten-free, vegan, and other dietary needs. Hungryroot is a direct-to-consumer company backed by Lightspeed Venture Partners; it operates a consumer web and mobile app experience rather than a public developer platform. This profile was surfaced through the venture portfolio graph and enriched by the API Evangelist pipeline, which probed the provider's domain and public discovery surfaces (no public API, OpenAPI, SDKs, well-known catalog, security.txt, or llms.txt were found as of this pass).
image: https://www.hungryroot.com/public/img/favicons/favicon-192.png
layout: provider
modified: '2026-07-19'
name: Hungryroot
nav: Providers
network: true
overview: 'Hungryroot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Grocery, Meal Kit, Food Delivery, and Direct to Consumer.


  Hungryroot''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hungryroot/refs/heads/main/screenshots/hungryroot-2026-07-25T221733.png
security:
- kind: domain-security
  name: Hungryroot Domain Security
  slug: hungryroot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hungryroot
tags:
- Company
- Grocery
- Meal Kit
- Food Delivery
- Direct to Consumer
- Personalization
- E-Commerce
- Consumer
website: https://www.hungryroot.com/
---
