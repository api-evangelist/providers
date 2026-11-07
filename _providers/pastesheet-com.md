---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: PasteSheet provides a REST API that turns Google Sheets into live JSON endpoints, with pagination, filtering, and rate‑limit controls.
  name: PasteSheet API
  slug: pastesheet-api
- description: 'pastesheet-com API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: pastesheet-com API
  slug: pastesheet-com-api
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/pastesheet-com/rate-limits/pastesheet-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pastesheet-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pastesheet-com/plans/pastesheet-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pastesheet-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pastesheet-com/rules/pastesheet-com-rules.yml
  title: ''
  type: Spectral
  url: rules/pastesheet-com-rules.yml
- group: design
  href: https://artifacts.apis.io/pastesheet-com/vocabulary/pastesheet-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pastesheet-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pastesheet-com/conventions/pastesheet-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pastesheet-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/pastesheet-com/authentication/pastesheet-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pastesheet-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/pastesheet-com/conformance/pastesheet-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pastesheet-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pastesheet-com/llms/pastesheet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pastesheet-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/pastesheet-com/well-known/pastesheet-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pastesheet-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/pastesheet-com/hosts/pastesheet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pastesheet-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pastesheet-com/vendors/pastesheet-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pastesheet-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pastesheet.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pastesheet.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://pastesheet.com/pricing
- group: start
  title: ''
  type: Login
  url: https://pastesheet.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://pastesheet.com/guides
- group: auth
  href: https://artifacts.apis.io/pastesheet-com/security/pastesheet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pastesheet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pastesheet.com/
coverage:
  checked: '2026-10-31'
  detail: Documentation is provided as markdown pages but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract is published.
  evidence:
  - status: 200
    url: https://pastesheet.com/guides/google-sheets-rest-api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: PasteSheet provides a service that turns Google Sheets into a live, cached JSON API. Users can expose public or private spreadsheets via a simple endpoint, with built-in pagination, filtering, and rate‑limit controls. The platform also offers an MCP (Machine‑Control‑Protocol) for AI agents to interact with sheet data directly, supporting use cases in web apps, no‑code tools, and AI agents. It includes free tier access, paid plans for higher limits, and comprehensive documentation for developers.
image: https://pastesheet.com/pastesheet.png
layout: provider
modified: '2026-10-30'
name: pastesheet-com
nav: Providers
network: true
overview: 'pastesheet-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Google Sheets, No-Code, and Artificial Intelligence.


  The pastesheet-com catalog on APIs.io includes 1 Spectral governance ruleset.


  pastesheet-com''s developer surface includes authentication, pricing, documentation, and 15 more developer resources.'
plans:
- name: Pastesheet Com Plans Pricing
  plan_count: 4
  slug: pastesheet-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Pastesheet Com Rate Limits
  slug: pastesheet-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: pastesheet-com API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: pastesheet-com-rules
scopes:
- name: Pastesheet Com Scopes
  scope_count: 0
  slug: pastesheet-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.8
    catalog_earned_first_party: 24.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 9.9
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 31.6
  previous_composite: 37.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pastesheet-com/pastesheet-com-2026-11-03T140953.png
security:
- kind: authentication
  name: Pastesheet Com Authentication
  slug: pastesheet-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pastesheet Com Domain Security
  slug: pastesheet-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pastesheet-com
tags:
- Company
- Google Sheets
- No-Code
- Artificial Intelligence
website: https://pastesheet.com/
---
