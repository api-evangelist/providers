---
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
  score: 8.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/zerothreat/plans/zerothreat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zerothreat-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/zerothreat/authentication/zerothreat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zerothreat-authentication.yml
- group: agent
  href: https://artifacts.apis.io/zerothreat/llms/zerothreat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zerothreat-llms.txt
- group: other
  href: https://artifacts.apis.io/zerothreat/hosts/zerothreat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zerothreat-hosts.yml
- group: other
  href: https://artifacts.apis.io/zerothreat/vendors/zerothreat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zerothreat-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zerothreat.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zerothreat.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://zerothreat.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://zerothreat.ai/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zerothreat.ai/solutions/developers
- group: company
  title: ''
  type: Blog
  url: https://zerothreat.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://zerothreat.ai/blog/zerothreat-web-and-api-security-testing-with-zero-configuration
- group: docs
  title: ''
  type: Documentation
  url: https://help.zerothreat.ai/
- group: auth
  href: https://artifacts.apis.io/zerothreat/security/zerothreat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zerothreat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zerothreat.ai/
coverage:
  checked: '2026-10-21'
  detail: Documentation pages return 404 or are JavaScript rendered, no machine-readable spec found.
  evidence:
  - status: 404
    url: https://zerothreat.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: ZeroThreat offers an AI‑driven automated penetration testing platform that continuously tests modern web applications and APIs. It provides end‑to‑end coverage—including authentication flows, business logic, and API attack patterns—and delivers exploit‑validated proof and audit‑ready reports for enterprise security teams, DevOps pipelines, SaaS providers, developers, MSSPs, and startups.
image: https://s3.ap-south-1.amazonaws.com/images.zerothreat.ai/automated_penetration_testing_platform_for_web_app_and_api_9649304105.svg
layout: provider
modified: '2026-10-21'
name: ZeroThreat
nav: Providers
network: true
overview: 'ZeroThreat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pentesting, Web Application Security, API Security, DevOps, and Enterprise Security.


  ZeroThreat''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
plans:
- name: Zerothreat Plans Pricing
  plan_count: 3
  slug: zerothreat-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zerothreat Authentication
  slug: zerothreat-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zerothreat Domain Security
  slug: zerothreat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zerothreat
tags:
- Pentesting
- Web Application Security
- API Security
- DevOps
- Enterprise Security
- Compliance
website: https://zerothreat.ai/
---
