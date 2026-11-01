---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/adjoe/llms/adjoe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adjoe-llms.txt
- group: other
  href: https://artifacts.apis.io/adjoe/hosts/adjoe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adjoe-hosts.yml
- group: other
  href: https://artifacts.apis.io/adjoe/vendors/adjoe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adjoe-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adjoe.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adjoe.io/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adjoeio
- group: start
  title: ''
  type: GettingStarted
  url: https://test-docs.adjoe.zone/rewarded-solutions/sdks/4.x/studio/best-practices/setup/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adjoe.io/
- group: auth
  href: https://artifacts.apis.io/adjoe/security/adjoe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adjoe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adjoe.io/
- group: company
  title: ''
  type: Blog
  url: https://adjoe.io/blog/
coverage:
  checked: '2026-10-28'
  detail: Docs site renders HTML via Docusaurus and does not expose a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.adjoe.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: adjoe is a fast-growing adtech company that provides advertising, monetization, loyalty, and playtime solutions for mobile apps. It helps advertisers, publishers, and brands reach their app growth and revenue goals through innovative ad technologies and data-driven insights.
image: https://adjoe.io/wp-content/uploads/2025/05/adjoe.io-eng-1.png?wsr
layout: provider
modified: '2026-10-28'
name: adjoe (playtime rewards)
nav: Providers
network: true
overview: 'adjoe (playtime rewards) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Monetization, Loyalty, Mobile Gaming, and SDK.


  adjoe (playtime rewards)''s developer surface includes getting-started guide, documentation, engineering blog, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adjoe Domain Security
  slug: adjoe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adjoe
tags:
- Advertising
- Monetization
- Loyalty
- Mobile Gaming
- SDK
- Supply‑Side Platform
- Ad Exchange
website: https://adjoe.io/
---
