---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Alphayou Net Agentic Access
  operation_count: 13
  slug: alphayou-net-agentic-access
  summary_line: 13 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.alphayou.net
  baseurl_source: declared
  description: The AlphaYou API from alphayou-net — 13 operation(s) for alphayou.
  name: alphayou-net Alpha You API
  slug: alphayou-net-alphayou-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/alphayou-net/agentic-access/alphayou-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alphayou-net-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/alphayou-net/plans/alphayou-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alphayou-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/alphayou-net/rules/alphayou-net-rules.yml
  title: ''
  type: Spectral
  url: rules/alphayou-net-rules.yml
- group: design
  href: https://artifacts.apis.io/alphayou-net/vocabulary/alphayou-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alphayou-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/alphayou-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/alphayou-net/errors/alphayou-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alphayou-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alphayou-net/conformance/alphayou-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alphayou-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alphayou-net/llms/alphayou-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alphayou-net-llms.txt
- group: other
  href: https://artifacts.apis.io/alphayou-net/hosts/alphayou-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphayou-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/alphayou-net/vendors/alphayou-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphayou-net-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://alphayou.net/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.alphayou.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.alphayou.net/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://alphayou.net/news
- group: other
  title: ''
  type: Leadership
  url: https://alphayou.net/ticker/team
- group: company
  title: ''
  type: Blog
  url: https://app.alphayou.net/blog
- group: docs
  title: ''
  type: APIReference
  url: https://alphayou.net/developers
- group: auth
  href: https://artifacts.apis.io/alphayou-net/authentication/alphayou-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alphayou-net-authentication.yml
- group: auth
  href: https://artifacts.apis.io/alphayou-net/security/alphayou-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphayou-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alphayou.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://alphayou.net/pricing
created: '2026-10-29'
description: AlphaYou provides US stock research and Hyperliquid trading tools, offering smart money alerts, insider tracking, and market analytics. The platform aggregates data on stocks, influencers, politicians, and institutional investors, delivering actionable insights for traders and investors. Users can set up custom alerts, explore detailed stock reports, and follow top traders to inform their strategies.
image: https://alphayou.net/opengraph-image
layout: provider
modified: '2026-10-29'
name: alphayou-net
nav: Providers
network: true
overview: 'alphayou-net publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Alpha You API. Tagged areas include Finance, StockResearch, TradingTools, MarketAnalytics, and Alerts.


  The alphayou-net catalog on APIs.io includes 1 Spectral governance ruleset.


  alphayou-net''s developer surface includes engineering blog, API reference, authentication, pricing, and 17 more developer resources.'
plans:
- name: Alphayou Net Plans Pricing
  plan_count: 3
  slug: alphayou-net-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: alphayou-net API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: alphayou-net-rules
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 22.0
    contract_quality: 51.6
    developer_ergonomics: 23.2
    discoverability: 69.6
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alphayou Net Authentication
  slug: alphayou-net-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Alphayou Net Domain Security
  slug: alphayou-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: getting-started
  slug: alphayou-net-getting_started
slug: alphayou-net
tags:
- Finance
- StockResearch
- TradingTools
- MarketAnalytics
- Alerts
website: https://alphayou.net/
---
