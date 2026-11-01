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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Russian construction companies and house projects catalog for AI agents
  name: MCP Market Russia API
  slug: mcp-market-russia-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/mcp-market-ru/plans/mcp-market-ru-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mcp-market-ru-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/mcp-market-ru/security/mcp-market-ru-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mcp-market-ru-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/mcp-market-ru/conformance/mcp-market-ru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mcp-market-ru-conformance.yml
- group: auth
  href: https://artifacts.apis.io/mcp-market-ru/well-known/mcp-market-ru-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mcp-market-ru-security.txt
- group: agent
  href: https://artifacts.apis.io/mcp-market-ru/well-known/mcp-market-ru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mcp-market-ru-well-known.yml
- group: other
  href: https://artifacts.apis.io/mcp-market-ru/hosts/mcp-market-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcp-market-ru-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcp-market.ru/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://mcp-market.ru/pricing
- group: start
  title: ''
  type: Login
  url: https://mcp-market.ru/login
- group: start
  title: ''
  type: GettingStarted
  url: https://mcp-market.ru/quickstart
- group: auth
  href: https://artifacts.apis.io/mcp-market-ru/security/mcp-market-ru-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mcp-market-ru-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mcp-market-ru/security/mcp-market-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcp-market-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcp-market.ru/
created: '2026-10-30'
description: MCP Market RU is a Russian marketplace platform that aggregates various digital services and products, providing a centralized API for developers to integrate listings, pricing, and transaction capabilities. The company focuses on enabling seamless e‑commerce experiences through standardized RESTful endpoints, comprehensive documentation, and support for multiple authentication methods. It aims to foster a vibrant ecosystem for third‑party developers and partners, offering tools for catalog management, order processing, and analytics.
layout: provider
modified: '2026-10-30'
name: mcp-market-ru
nav: Providers
network: true
overview: 'mcp-market-ru is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, E-commerce, API, and Russia.


  mcp-market-ru''s developer surface includes pricing, getting-started guide, and 11 more developer resources.'
plans:
- name: Mcp Market Ru Plans Pricing
  plan_count: 4
  slug: mcp-market-ru-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 62.5
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mcp Market Ru Domain Security
  slug: mcp-market-ru-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Mcp Market Ru Vulnerability Disclosure
  slug: mcp-market-ru-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mcp-market-ru
tags:
- Company
- Marketplace
- E-commerce
- API
- Russia
website: https://mcp-market.ru/
---
