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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Boostly provides a SMS marketing platform for restaurants via its API.
  name: Boostly API
  slug: boostly-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/boostly/vendors/boostly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boostly-vendors.yml
- group: operate
  href: https://artifacts.apis.io/boostly/changelog/boostly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/boostly-changelog.yml
- group: agent
  href: https://artifacts.apis.io/boostly/well-known/boostly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boostly-well-known.yml
- group: other
  href: https://artifacts.apis.io/boostly/hosts/boostly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boostly-hosts.yml
- group: start
  title: ''
  type: Login
  url: http://app.boostly.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.boostly.com/articles/whats-new
- group: auth
  href: https://artifacts.apis.io/boostly/security/boostly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boostly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boostly.com/
- group: company
  title: ''
  type: Blog
  url: https://www.boostly.com/blog
- group: other
  title: ''
  type: Podcast
  url: https://www.boostly.com/podcast
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boostly.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boostly.com/privacy-policy
coverage:
  checked: '2026-10-02'
  detail: API documentation pages return HTML shells and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: network_error
    url: https://api.boostly.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Boostly provides a SMS marketing platform for restaurants, enabling them to attract new diners, boost orders, manage reviews, and measure ROI through text message campaigns. The service offers tools for targeted ads, loyalty programs, and detailed analytics, helping restaurant owners increase revenue and customer engagement.
image: https://framerusercontent.com/assets/oyTJV04Z2m5EklFWks7BT9ZKWQ.png
layout: provider
modified: '2026-10-02'
name: Boostly
nav: Providers
network: true
overview: 'Boostly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SMS Marketing, Restaurant, Customer Engagement, and Analytics.


  Boostly''s developer surface includes changelog, engineering blog, and 10 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/boostly/boostly-2026-11-03T122246.png
security:
- kind: domain-security
  name: Boostly Domain Security
  slug: boostly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boostly
tags:
- Company
- SMS Marketing
- Restaurant
- Customer Engagement
- Analytics
website: https://www.boostly.com/
---
