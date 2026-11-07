---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/qlikview-com/plans/qlikview-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qlikview-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/qlikview-com/authentication/qlikview-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qlikview-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/qlikview-com/llms/qlikview-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qlikview-com-llms.txt
- group: other
  href: https://artifacts.apis.io/qlikview-com/hosts/qlikview-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qlikview-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/qlikview-com/vendors/qlikview-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qlikview-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/qlikview-com/packages/qlikview-com-packages.yml
  title: ''
  type: SDKs
  url: packages/qlikview-com-packages.yml
- group: build
  href: https://artifacts.apis.io/qlikview-com/packages/qlikview-com-packages.yml
  title: ''
  type: Packages
  url: packages/qlikview-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.qlik.com/us/company/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/terms-of-use
- group: operate
  title: ''
  type: Roadmap
  url: https://www.qlik.com/us/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/company/trust/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qlik.com/us/di/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.qlik.com/us/company/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.qlik.com/us/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.qlik.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.qlik.com/en-US/onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://help.qlik.com/
- group: auth
  href: https://artifacts.apis.io/qlikview-com/security/qlikview-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qlikview-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.qlikview.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.qlikview.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Qlik provides analytics and data integration solutions that enable enterprises to turn data into trusted, AI‑ready insights. Its portfolio includes Qlik Cloud Analytics (SaaS) and Qlik Sense (on‑premises) for data visualization, real‑time data movement, and AI‑driven analytics. The company serves organizations across industries such as financial services, government, healthcare, and manufacturing.
image: https://www.qlik.com/qlik-og-default.png
layout: provider
modified: '2026-10-25'
name: Qlik
nav: Providers
network: true
overview: 'Qlik is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Business Intelligence, Data Integration, Cloud Analytics, and Enterprise Software.


  Qlik''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Qlikview Com Plans Pricing
  plan_count: 4
  slug: qlikview-com-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 56.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/qlikview-com/qlikview-com-2026-11-03T141752.png
security:
- kind: authentication
  name: Qlikview Com Authentication
  slug: qlikview-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Qlikview Com Domain Security
  slug: qlikview-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qlikview-com
tags:
- Analytics
- Business Intelligence
- Data Integration
- Cloud Analytics
- Enterprise Software
website: http://www.qlikview.com
---
