---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heirloom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.heirloomcarbon.com/
- group: company
  title: ''
  type: Blog
  url: https://www.heirloomcarbon.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.heirloomcarbon.com/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.heirloomcarbon.com/remove-co2
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heirloomcarbon.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heirloomcarbon.com/privacy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/heirloom-stock
coverage:
  checked: '2026-08-22'
  detail: Heirloom Carbon Technologies is an industrial direct air capture company that sells permanent CO2 removal credits through a Webflow storefront; its 46-URL sitemap contains no developer, docs or API page, no api./docs./developer./app./portal. subdomain resolves in DNS, and every /openapi.json, /llms.txt, /graphql and /.well-known/* path 404s on both www and apex.
  evidence:
  - status: 200
    url: https://www.heirloomcarbon.com/sitemap.xml
  - status: 404
    url: https://www.heirloomcarbon.com/openapi.json
  - status: 404
    url: https://www.heirloomcarbon.com/llms.txt
  - status: 404
    url: https://www.heirloomcarbon.com/.well-known/agent-card.json
  - status: 404
    url: https://heirloomcarbon.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: Heirloom Carbon Technologies, Inc. is a San Francisco Bay Area direct air capture (DAC) company that removes carbon dioxide from the atmosphere by accelerating the natural mineralization of limestone. Heirloom spreads calcium oxide on vertical trays where it re-absorbs atmospheric CO2 in days rather than years, then uses electric kilns to release the captured CO2 for permanent geologic or in-concrete storage. The company opened the first commercial DAC facility in the United States, sells permanent carbon removal credits to individuals, businesses and enterprises, and has signed offtake agreements with Microsoft, Frontier, United's Sustainable Flight Fund and CarbonCure. It is an industrial climate-technology company; it does not operate a public developer program or API.
image: https://cdn.prod.website-files.com/639c8f646dc35afd81aeebc2/651aee726de0080273ee5ad9_Heirloom_SocialShare.jpg
layout: provider
modified: '2026-08-22'
name: Heirloom
nav: Providers
network: true
overview: 'Heirloom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Carbon Removal, Direct Air Capture, Climate Technology, and Carbon Credits.


  Heirloom''s developer surface includes engineering blog, support, pricing, and 5 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heirloom/refs/heads/main/screenshots/heirloom-2026-09-02T145716.png
security:
- kind: domain-security
  name: Heirloom Domain Security
  slug: heirloom-domain-security
  summary_line: TLSv1.3 · HSTS
slug: heirloom
tags:
- Company
- Carbon Removal
- Direct Air Capture
- Climate Technology
- Carbon Credits
- Sustainability
- Energy
- Climate
website: https://www.heirloomcarbon.com/
---
