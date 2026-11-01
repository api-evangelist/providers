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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/getcatalyst-io/well-known/getcatalyst-io-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getcatalyst-io-status-security.txt
- group: agent
  href: https://artifacts.apis.io/getcatalyst-io/well-known/getcatalyst-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getcatalyst-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/getcatalyst-io/hosts/getcatalyst-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getcatalyst-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/getcatalyst-io/vendors/getcatalyst-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getcatalyst-io-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.catalyst.io/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.catalyst.io/
- group: auth
  title: ''
  type: Security
  url: https://www.catalyst.io/legal/security
- group: start
  title: ''
  type: Sandbox
  url: https://www.catalyst.io/structure/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.catalyst.io/legal/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://help.catalyst.io/
- group: auth
  href: https://artifacts.apis.io/getcatalyst-io/security/getcatalyst-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getcatalyst-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.catalyst.io
- group: company
  title: ''
  type: Blog
  url: https://www.totango.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.totango.com/platform/catalyst
coverage:
  checked: '2026-10-21'
  detail: The Catalyst website is built with Webflow and serves only HTML without machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.catalyst.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Catalyst provides an intuitive customer success platform that centralizes customer data, offers a clear view of health metrics, and enables scaling of experiences to drive retention and growth. The SaaS solution helps businesses improve engagement, reduce churn, and enhance overall customer satisfaction through data-driven insights and automation.
image: https://cdn.prod.website-files.com/61cb60ab7b41408bfa98cabf/63f627553debba6e57001d51_ctl-share.jpg
layout: provider
modified: '2026-10-21'
name: Catalyst
nav: Providers
network: true
overview: 'Catalyst is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Customer Success, Platform, and Automation.


  Catalyst''s developer surface includes support, sandbox, documentation, engineering blog, pricing, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    conformance: unknown
    mcp: derived
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
  name: Getcatalyst Io Domain Security
  slug: getcatalyst-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: getcatalyst-io
tags:
- Company
- SaaS
- Customer Success
- Platform
- Automation
website: https://www.catalyst.io
---
