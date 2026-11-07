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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SMS, voice and messaging API documented at the developer docs.
  name: Yunpian SMS API
  slug: yunpian-sms-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/yunpian/hosts/yunpian-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yunpian-hosts.yml
- group: build
  href: https://artifacts.apis.io/yunpian/packages/yunpian-packages.yml
  title: ''
  type: SDKs
  url: packages/yunpian-packages.yml
- group: build
  href: https://artifacts.apis.io/yunpian/packages/yunpian-packages.yml
  title: ''
  type: Packages
  url: packages/yunpian-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.yunpian.com/solution/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yunpian
- group: auth
  href: https://artifacts.apis.io/yunpian/security/yunpian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yunpian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yunpian.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.yunpian.com/dev-doc
- group: company
  title: ''
  type: Blog
  url: https://www.yunpian.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yunpian.com/price
- group: company
  title: ''
  type: About
  url: https://www.yunpian.com/about
coverage:
  checked: '2026-10-27'
  detail: Developer documentation at https://www.yunpian.com/dev-doc is a JavaScript‑rendered single‑page app with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.yunpian.com/dev-doc
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Yunpian (杭州云片网络科技有限公司) provides cloud communication services, offering SMS, voice, and WhatsApp messaging APIs for developers worldwide. Their platform supports domestic and international SMS, super SMS with multimedia, 5G smart messaging, and enterprise solutions like YCloud. They emphasize security with certifications such as ISO27001 and CMMI3, and provide extensive SDKs, documentation, and support for rapid integration.
layout: provider
modified: '2026-10-27'
name: Yunpian
nav: Providers
network: true
overview: 'Yunpian is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SMS, Cloud Communications, API Platform, and China.


  Yunpian''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 53.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 12.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/yunpian/yunpian-2026-11-03T150427.png
security:
- kind: domain-security
  name: Yunpian Domain Security
  slug: yunpian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yunpian
tags:
- Company
- SMS
- Cloud Communications
- API Platform
- China
website: https://www.yunpian.com/
---
