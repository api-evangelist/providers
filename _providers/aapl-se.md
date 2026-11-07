---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Aapl.se är Sveriges ledande Apple-nyhetssajt sedan 2008. Vi aggregerar ~40 källor och sammanfattar på svenska med AI.
  name: Aapl.se API
  slug: aapl-se-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/aapl-se/conventions/aapl-se-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aapl-se-conventions.yml
- group: design
  href: https://artifacts.apis.io/aapl-se/conventions/aapl-se-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aapl-se-conventions.yml
- group: design
  href: https://artifacts.apis.io/aapl-se/conformance/aapl-se-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aapl-se-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aapl-se/llms/aapl-se-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aapl-se-llms.txt
- group: other
  href: https://artifacts.apis.io/aapl-se/hosts/aapl-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aapl-se-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aapl-se/security/aapl-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aapl-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aapl.se/
- group: docs
  title: ''
  type: Documentation
  url: https://aapl.se/api-docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aapl.se/api-docs
- group: operate
  title: ''
  type: Support
  url: https://aapl.se/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aapl.se/privacy
created: '2026-10-31'
description: Apple Nyheter Sverige is a Swedish news portal delivering Apple-related news, reviews, and rumors since 2008. It provides daily updates on iPhone, iPad, Mac, and Apple Watch, offering test results, product comparisons, and community discussions. The site aims to keep Swedish-speaking Apple enthusiasts informed with timely articles and multimedia content.
image: https://aapl.se/apple-touch-icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at aapl.se over HTTP; 12 tools listed.
  name: Apple Nyheter Sverige MCP Server
  slug: aapl-se
modified: '2026-10-31'
name: Apple Nyheter Sverige
nav: Providers
network: true
overview: 'Apple Nyheter Sverige is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News, Apple, Sweden, Technology, and Reviews.


  Apple Nyheter Sverige''s developer surface includes documentation, support, and 9 more developer resources.'
plans:
- name: Aapl Se Plans Pricing
  plan_count: 0
  slug: aapl-se-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Aapl Se Rate Limits
  slug: aapl-se-rate-limits
scopes:
- name: Aapl Se Scopes
  scope_count: 0
  slug: aapl-se-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 17.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aapl Se Authentication
  slug: aapl-se-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aapl Se Domain Security
  slug: aapl-se-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aapl-se
tags:
- News
- Apple
- Sweden
- Technology
- Reviews
website: https://aapl.se/
---
