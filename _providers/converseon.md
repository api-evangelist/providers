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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/converseon/hosts/converseon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/converseon-hosts.yml
- group: other
  href: https://artifacts.apis.io/converseon/vendors/converseon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/converseon-vendors.yml
- group: auth
  href: https://artifacts.apis.io/converseon/security/converseon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/converseon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://converseon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://converseon.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://converseon.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://converseon.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://converseon.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://converseon.com/support
- group: company
  title: ''
  type: Blog
  url: https://converseon.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://converseon.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://converseon.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://converseon.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://converseon.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/converseon/workspace
coverage:
  checked: '2026-10-10'
  detail: API reference page returns only HTML with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://converseon.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Converseon provides AI‑powered natural language processing solutions that help enterprises extract actionable insights from unstructured data such as social media, news, and voice‑of‑customer content. Their platform offers trusted model governance, customizable and pre‑built models, and a suite of analytics tools to improve data quality, enable predictive intelligence, and support market research workflows. Converseon serves sectors including finance, consumer goods, and public relations, delivering scalable, secure, and compliant AI services.
layout: provider
modified: '2026-10-10'
name: Converseon
nav: Providers
network: true
overview: 'Converseon publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Natural Language Processing, Analytics, and Enterprise.


  Converseon''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 23.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/converseon/converseon-2026-11-03T125300.png
security:
- kind: domain-security
  name: Converseon Domain Security
  slug: converseon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: converseon
tags:
- Company
- Artificial Intelligence
- Natural Language Processing
- Analytics
- Enterprise
website: https://converseon.com/
---
