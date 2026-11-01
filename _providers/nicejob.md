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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Guides | Where businesses in growth-mode come to learn from experts, explore small business strategies, and gain insight from fellow entrepreneurs.
  name: NiceJob API
  slug: nicejob-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/nicejob/llms/nicejob-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nicejob-llms.txt
- group: auth
  href: https://artifacts.apis.io/nicejob/well-known/nicejob-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nicejob-help-security.txt
- group: agent
  href: https://artifacts.apis.io/nicejob/well-known/nicejob-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nicejob-well-known.yml
- group: other
  href: https://artifacts.apis.io/nicejob/hosts/nicejob-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nicejob-hosts.yml
- group: other
  href: https://artifacts.apis.io/nicejob/vendors/nicejob-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nicejob-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.nicejob.com/en/
- group: company
  title: ''
  type: Newsroom
  url: https://get.nicejob.com/resources/tag/news
- group: auth
  href: https://artifacts.apis.io/nicejob/security/nicejob-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nicejob-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nicejob.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nicejob.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://nicejob.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nicejob.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nicejob.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nicejob.com/privacy
coverage:
  checked: '2026-10-28'
  detail: No machine‑readable API spec is published; only human‑readable guides are available.
  evidence:
  - status: 200
    url: https://get.nicejob.com/resources/tag/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: NiceJob provides an AI‑powered reputation marketing platform for service‑based businesses. Its software helps businesses collect and manage customer reviews, automate responses, and improve online visibility across search engines and AI assistants. The platform includes tools for review solicitation, widgets for website display, analytics, and integrations with common business software.
image: https://get.nicejob.com/hubfs/og-home.png
layout: provider
modified: '2026-10-28'
name: NiceJob
nav: Providers
network: true
overview: 'NiceJob is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Reputation Marketing, AI, SaaS, Service Business, and Customer Reviews.


  NiceJob''s developer surface includes support, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Nicejob Plans Pricing
  plan_count: 0
  slug: nicejob-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Nicejob Rate Limits
  slug: nicejob-rate-limits
scopes:
- name: Nicejob Scopes
  scope_count: 0
  slug: nicejob-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nicejob Authentication
  slug: nicejob-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nicejob Domain Security
  slug: nicejob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nicejob
tags:
- Reputation Marketing
- AI
- SaaS
- Service Business
- Customer Reviews
website: https://nicejob.com/
---
