---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.sayweee.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.weee.com/en — a different registrable domain (sayweee.com -> weee.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/weee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sayweee.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.sayweee.com/
- group: operate
  title: ''
  type: Support
  url: https://www.sayweee.com/en/help
- group: start
  title: ''
  type: Login
  url: https://www.sayweee.com/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sayweee.com/en/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sayweee.com/en/about/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weee-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/weee-well-known.yml
created: '2026-07-17'
description: Weee! is America's largest online Asian grocery store and delivery platform, operating as a direct-to-consumer online supermarket serving major metropolitan areas across the United States. It curates and fulfills inventory through regional distribution centers and cold-chain logistics, bringing together products and ingredients commonly found in Chinese, Japanese, Korean, Vietnamese, Thai, Filipino, and Indian supermarkets. The storefront spans fresh produce, frozen meats, seafood, pantry staples, snacks, sauces, hot pot ingredients, beverages, and household essentials, accepts EBT/SNAP in eligible cities, and runs a multilingual experience (English, Chinese, Korean, Japanese, Vietnamese, Thai). Weee is backed by Lightspeed Venture Partners and the SoftBank Vision Fund. As of this profile Weee publishes no public developer API; this record captures its public web identity and AI-indexing (llms.txt) surface.
image: https://www.sayweee.com/favicons/apple-touch-icon.png
layout: provider
modified: '2026-07-21'
name: Weee
nav: Providers
network: true
overview: 'Weee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Grocery, E-Commerce, Food and Beverage, and Delivery.


  Weee''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weee/refs/heads/main/screenshots/weee-2026-09-02T170553.png
security:
- kind: domain-security
  name: Weee Domain Security
  slug: weee-domain-security
  summary_line: TLSv1.3 · DMARC
slug: weee
tags:
- Company
- Grocery
- E-Commerce
- Food and Beverage
- Delivery
- Retail
- Marketplace
- Asian Groceries
website: https://www.sayweee.com/
---
