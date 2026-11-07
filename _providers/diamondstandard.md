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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides investment and trading functionalities for tokenized diamonds as described on the Regulated Offering page.
  name: Diamondstandard API
  slug: diamondstandard-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/diamondstandard/llms/diamondstandard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diamondstandard-llms.txt
- group: other
  href: https://artifacts.apis.io/diamondstandard/hosts/diamondstandard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diamondstandard-hosts.yml
- group: other
  href: https://artifacts.apis.io/diamondstandard/vendors/diamondstandard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diamondstandard-vendors.yml
- group: auth
  href: https://artifacts.apis.io/diamondstandard/security/diamondstandard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diamondstandard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.diamondstandard.co
- group: docs
  title: ''
  type: Documentation
  url: https://www.diamondstandard.co
- group: company
  title: ''
  type: About
  url: https://www.diamondstandard.co/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.diamondstandard.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.diamondstandard.co/regulated-offering
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diamondstandard.co/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.diamondstandard.co/contact-us
coverage:
  checked: '2026-10-23'
  detail: Main website renders content via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://www.diamondstandard.co
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Diamondstandard is a fintech company that tokenizes natural diamonds, offering investable diamond commodities through blockchain-backed tokens. It provides a suite of investment products for institutional and retail investors, enabling diversification into the $1.2 trillion diamond market. The platform includes a regulated offering, a spot trading venue, and educational resources on diamond investing, with a mission to make diamonds an accessible, liquid asset class.
image: https://www.diamondstandard.co/thumbnails/home.png
layout: provider
modified: '2026-10-23'
name: Diamondstandard
nav: Providers
network: true
overview: 'Diamondstandard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investment, Blockchain, and Commodities.


  Diamondstandard''s developer surface includes documentation, engineering blog, pricing, support, and 7 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 13.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/diamondstandard/diamondstandard-2026-11-03T130701.png
security:
- kind: domain-security
  name: Diamondstandard Domain Security
  slug: diamondstandard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diamondstandard
tags:
- Company
- Fintech
- Investment
- Blockchain
- Commodities
website: https://www.diamondstandard.co
---
