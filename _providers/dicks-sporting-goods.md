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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dicks-sporting-goods-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dickssportinggoods
- group: company
  title: ''
  type: Website
  url: https://www.dickssportinggoods.com
- group: build
  title: ''
  type: Packages
  url: packages/dicks-sporting-goods-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dicks-sporting-goods-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/dickssportinggoods
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dickssportinggoods.com/s/policy/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dickssportinggoods.com/s/policy/terms-of-use
coverage:
  checked: '2026-09-06'
  detail: 'DICK''S ships software only as end-user storefront and app experiences: there is no developer portal, no API reference and no SDK anywhere, api. and developer.dickssportinggoods.com do not resolve in DNS, and the storefront returns the identical Angular app shell with HTTP 200 for /openapi.json, /llms.txt, /apis.json and a negative-control path that cannot exist — so every apparent hit is a soft 404.'
  evidence:
  - status: 200
    url: https://www.dickssportinggoods.com/.well-known/dicks-sporting-goods-negative-control-7f3ab91c.json
  - status: 200
    url: https://www.dickssportinggoods.com/openapi.json
  - status: 200
    url: https://www.dickssportinggoods.com/llms.txt
  - status: 0
    url: https://api.dickssportinggoods.com/openapi.json
  - status: 0
    url: https://developer.dickssportinggoods.com/openapi.json
  - status: 403
    url: https://www.dickssportinggoods.com/s/policy/privacy-policy
  - status: 200
    url: https://bugcrowd.com/engagements/dickssportinggoods
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: 'DICK''S Sporting Goods is a Fortune 500 omni-channel sporting goods retailer selling sports equipment, apparel, footwear and accessories across the DICK''S, House of Sport, Golf Galaxy, Public Lands and Going Going Gone banners. It publishes no developer portal, no API reference and no machine-readable contract: the storefront is an Angular single-page app that answers HTTP 200 with the same shell for every path, and neither api. nor developer.dickssportinggoods.com resolves in DNS. Its B2B integration surface is X12 EDI over AS2/SFTP through third-party trading networks, with vendor guidelines handed out as PDFs. The company does run a named Vulnerability Disclosure Program on Bugcrowd.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dicks-sporting-goods.png
layout: provider
modified: '2026-09-06'
name: Dick's Sporting Goods
nav: Providers
network: true
overview: Dick's Sporting Goods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Sporting Goods, Fortune 500, E-Commerce, and Omnichannel Commerce.
press:
- date: '2026-05-25'
  title: DICK'S Sporting Goods Partners with Adobe to Transform ...
  url: https://www.businesswire.com/news/home/20260421672910/en/DICKS-Sporting-Goods-Partners-with-Adobe-to-Transform-the-Athlete-Experience-with-AI
- date: '2026-05-25'
  title: AI Impact on Retail Traffic with Loni Stark
  url: https://www.linkedin.com/posts/schwab-network_adobes-loni-stark-breaks-down-how-ai-is-activity-7452401605628301312-SoaA
- date: '2026-05-25'
  title: DICK'S Sporting Goods thinks AI should help you buy ...
  url: https://www.reddit.com/r/ArtificialInteligence/comments/1tkxwhj/dicks_sporting_goods_thinks_ai_should_help_you/
- date: '2026-05-25'
  title: What 10 retail executives have to say about AI
  url: https://www.retaildive.com/news/retail-executives-artificial-intelligence-nrf/809654/
- date: '2026-05-25'
  title: How DICK'S Sporting Goods uses AI to elevate team skills
  url: https://eightfold.ai/blog/how-dicks-sporting-goods-uses-ai-to-elevate-team-skills-in-a-changing-workplace/
random_paper: 5
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    operational_transparency: 13.2
  previous_composite: 11.7
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/dicks-sporting-goods/refs/heads/main/screenshots/dicks-sporting-goods-2026-06-20T180011.png
security:
- kind: domain-security
  name: Dicks Sporting Goods Domain Security
  slug: dicks-sporting-goods-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dicks Sporting Goods Vulnerability Disclosure
  slug: dicks-sporting-goods-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: dicks-sporting-goods
tags:
- Retail
- Sporting Goods
- Fortune 500
- E-Commerce
- Omnichannel Commerce
- Consumer Goods
website: https://www.dickssportinggoods.com
---
