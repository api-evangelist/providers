---
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
- group: company
  title: ''
  type: Website
  url: https://abcmob.com/
- group: operate
  title: ''
  type: Support
  url: https://abcmob.com/contact.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abcmob
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/abc_mob
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/abcmobapp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abcmob-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abcmob-llms.txt
coverage:
  checked: '2026-09-05'
  detail: abcmob.com is a five-page static brochure site selling finished mobile apps to businesses — every contract-discovery path (/openapi.json, /swagger.json, /api-docs, /graphql, /api, /apis.json, /llms.txt, /sitemap.xml and all seven /.well-known/ paths on both abcmob.com and www.abcmob.com) returns the site's 404 HTML page, there is no developer, docs or pricing page in the navigation, and no abcMob organization exists on GitHub, npm or PyPI.
  evidence:
  - status: 200
    url: https://abcmob.com/
  - status: 404
    url: https://abcmob.com/openapi.json
  - status: 404
    url: https://abcmob.com/api-docs
  - status: 404
    url: https://abcmob.com/.well-known/api-catalog
  - status: 404
    url: https://abcmob.com/developers.html
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: abcMob is a mobile business application company founded in 2010 and headquartered in Westminster, California. It builds and sells ready-made and custom native business applications for banking, airlines, HRIS, insurance, restaurants, hotels, tourism, universities, gyms, music, sport clubs, brokerage, oil and gas, real estate, retail, agriculture, survey, TV and places of worship. Its stated approach is to write one codebase that is translated to native code per platform (Objective-C on iOS, Java on Android, C on Windows and Linux) and compiled into full native applications, with an HTML5 web view of the same service, so the look, feel and update cadence stay consistent across devices. The company sells finished client/server applications and cloud hosting to businesses; it publishes no public developer program, API reference, or machine-readable contract of any kind.
image: https://abcmob.com/images/logo.png
layout: provider
modified: '2026-09-05'
name: abcMob
nav: Providers
network: true
overview: 'abcMob is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile, Mobile Applications, Application Development, and Enterprise Software.


  abcMob''s developer surface includes support, YouTube channel, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Abcmob Domain Security
  slug: abcmob-domain-security
  summary_line: TLSv1.3
slug: abcmob
tags:
- Company
- Mobile
- Mobile Applications
- Application Development
- Enterprise Software
- Cross Platform
- Banking
- Hospitality
- United States
website: https://abcmob.com/
---
