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
  url: security/88rising-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://88rising.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://88rising.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://88rising.com/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/88rising
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/88rising/
- group: learn
  title: ''
  type: Youtube
  url: https://www.youtube.com/@88rising
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/88rising/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/88rising/
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/88rising
coverage:
  checked: '2026-08-06'
  detail: '88rising is a record label and mass media company, not a software vendor — the only publicly reachable API on any of its hosts is the undocumented Strapi v4 CMS backend at api.88rising.com/api that renders its own Angular website (five anonymous read endpoints: /cards, /footer, /privacy-policy, /terms-of-service, /findOneShopify), and every /openapi.json, /swagger.json, /documentation and /.well-known/ probe against that host returned a genuine JSON 404.'
  evidence:
  - status: 404
    url: https://api.88rising.com/openapi.json
  - status: 404
    url: https://api.88rising.com/documentation/v1.0.0/swagger.json
  - status: 404
    url: https://api.88rising.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/88rising
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: '88rising (stylized 88 with a rising arrow) is an American mass media company and record label founded in 2015 by Sean Miyashiro, headquartered in Los Angeles and New York with a division in Shanghai. It describes itself as a hybrid management, record label, video production and marketing company, and is known for building a global platform for Asian and Asian American artists including Rich Brian, NIKI, Joji and Keith Ape. Beyond recorded music it operates the Head in the Clouds festival franchise and the 88 Night Market live and commerce brand. It is a media and entertainment company rather than a software company: it publishes no developer program, no public API documentation and no machine-readable specifications.'
image: https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/88rising_logo.svg/1200px-88rising_logo.svg.png
layout: provider
modified: '2026-08-06'
name: 88rising
nav: Providers
network: true
overview: '88rising is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Entertainment, Music, and Record Label.


  88rising''s developer surface includes YouTube channel and 9 more developer resources.'
random_paper: 8
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
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: 88Rising Domain Security
  slug: 88rising-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 88rising
tags:
- Company
- Media
- Entertainment
- Music
- Record Label
- Live Events
- Content
- Marketing
website: https://88rising.com/
---
