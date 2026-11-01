---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Gold, silver and copper spot prices, with delayed futures settlement prices and gold conversion across 31 currencies using exchangerate.dev FX.
  name: Gold API
  slug: gold-api
artifact_total: 6
asyncapis:
- description: ''
  name: Goldprice Dev Webhooks
  slug: goldprice-dev-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/goldprice-dev/plans/goldprice-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goldprice-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/goldprice-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/goldprice-dev/asyncapi/goldprice-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/goldprice-dev-webhooks.yml
- group: build
  href: https://artifacts.apis.io/goldprice-dev/cli/goldprice-dev-cli.yml
  title: ''
  type: CLI
  url: cli/goldprice-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/goldprice-dev/conventions/goldprice-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/goldprice-dev-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://goldprice.dev/terms
- group: design
  href: https://artifacts.apis.io/goldprice-dev/conformance/goldprice-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goldprice-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/goldprice-dev/llms/goldprice-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goldprice-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/goldprice-dev/well-known/goldprice-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/goldprice-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/goldprice-dev/well-known/goldprice-dev-narwhalapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/goldprice-dev-narwhalapi-security.txt
- group: auth
  href: https://artifacts.apis.io/goldprice-dev/well-known/goldprice-dev-exchangerate-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/goldprice-dev-exchangerate-security.txt
- group: agent
  href: https://artifacts.apis.io/goldprice-dev/well-known/goldprice-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/goldprice-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/goldprice-dev/hosts/goldprice-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goldprice-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/goldprice-dev/vendors/goldprice-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/goldprice-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/goldprice-dev/packages/goldprice-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/goldprice-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/goldprice-dev/packages/goldprice-dev-packages.yml
  title: ''
  type: Packages
  url: packages/goldprice-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goldprice.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goldprice.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://goldprice.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://goldprice.dev/login
- group: docs
  title: ''
  type: Documentation
  url: https://goldprice.dev/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://goldprice.dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://goldprice.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://narwhalapi.com/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://narwhalapi.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/goldprice-dev/security/goldprice-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/goldprice-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/goldprice-dev/security/goldprice-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goldprice-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goldprice.dev/
created: '2026-10-30'
description: Goldprice.dev provides a free and paid JSON API delivering live gold (XAU), silver (XAG), and copper (HG) spot prices, plus futures settlement data, in 31 currencies. The service includes timestamps, source attribution, and an MCP stdio bridge on every plan, catering to developers, fintech engineers, and quantitative traders.
image: https://goldprice.dev/og.jpg
layout: provider
modified: '2026-10-30'
name: goldprice-dev
nav: Providers
network: true
overview: 'goldprice-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Finance, Commodities, and Data.


  The goldprice-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  goldprice-dev''s developer surface includes CLI, pricing, documentation, changelog, engineering blog, getting-started guide, API reference, and 21 more developer resources.'
plans:
- name: Goldprice Dev Plans Pricing
  plan_count: 4
  slug: goldprice-dev-plans-pricing
random_paper: 21
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 16.4
    contract_quality: 39.0
    developer_ergonomics: 51.7
    discoverability: 66.1
    operational_transparency: 34.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Goldprice Dev Domain Security
  slug: goldprice-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Goldprice Dev Vulnerability Disclosure
  slug: goldprice-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: goldprice-dev-noops
  slug: goldprice-dev-noops-skill
slug: goldprice-dev
tags:
- Company
- API
- Finance
- Commodities
- Data
website: https://goldprice.dev/
---
