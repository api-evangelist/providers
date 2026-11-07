---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Logimu Com Agentic Access
  operation_count: 4
  slug: logimu-com-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://llmlatency.dev
  baseurl_source: declared
  description: The Coding Agents.json API from logimu-com — 1 operation(s) for coding agents.json.
  name: logimu-com Coding Agents.json API
  slug: logimu-com-coding-agents-json-api
- baseURL: https://llmlatency.dev
  baseurl_source: declared
  description: The Deprecations.json API from logimu-com — 1 operation(s) for deprecations.json.
  name: logimu-com Deprecations.json API
  slug: logimu-com-deprecations-json-api
- baseURL: https://llmlatency.dev
  baseurl_source: declared
  description: The Rankings.json API from logimu-com — 1 operation(s) for rankings.json.
  name: logimu-com Rankings.json API
  slug: logimu-com-rankings-json-api
- baseURL: https://llmlatency.dev
  baseurl_source: declared
  description: The Subscribe API from logimu-com — 1 operation(s) for subscribe.
  name: logimu-com Subscribe API
  slug: logimu-com-subscribe-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/logimu-com/agentic-access/logimu-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/logimu-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/logimu-com/plans/logimu-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logimu-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/logimu-com/rules/logimu-com-rules.yml
  title: ''
  type: Spectral
  url: rules/logimu-com-rules.yml
- group: design
  href: https://artifacts.apis.io/logimu-com/errors/logimu-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/logimu-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/logimu-com/conformance/logimu-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/logimu-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/logimu-com/well-known/logimu-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/logimu-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/logimu-com/hosts/logimu-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/logimu-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.logimu.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://api.logimu.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.logimu.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logimu.com/pricing-plans/
- group: start
  title: ''
  type: Login
  url: https://api.logimu.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://api.logimu.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.logimu.com/reference
- group: auth
  href: https://artifacts.apis.io/logimu-com/security/logimu-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logimu-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://logimu.com/
created: '2026-10-30'
description: Logimu provides an Amazon and Walmart product data and search API, enabling developers to retrieve product details, pricing, rankings, seller offers, and search results from both marketplaces. The service supports REST endpoints and an MCP connector, targeting e‑commerce businesses for price monitoring, repricing, product research, brand protection, and analytics. It offers documentation, pricing plans, FAQs, and contact options, positioning itself as a comprehensive solution for integrating marketplace data into AI applications and business workflows.
image: https://www.logimu.com/og/home.png
layout: provider
modified: '2026-10-30'
name: logimu-com
nav: Providers
network: true
overview: 'logimu-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Coding Agents.json API, Deprecations.json API, Rankings.json API, and 1 more. Tagged areas include Company, E-Commerce, Data API, Amazon, and Walmart.


  The logimu-com catalog on APIs.io includes 1 Spectral governance ruleset.


  logimu-com''s developer surface includes support, pricing, documentation, API reference, and 12 more developer resources.'
plans:
- name: Logimu Com Plans Pricing
  plan_count: 1
  slug: logimu-com-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: logimu-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: logimu-com-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 39.2
    developer_ergonomics: 10.7
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/logimu-com/logimu-com-2026-11-03T135029.png
security:
- kind: domain-security
  name: Logimu Com Domain Security
  slug: logimu-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: logimu-com
tags:
- Company
- E-Commerce
- Data API
- Amazon
- Walmart
website: https://logimu.com/
---
