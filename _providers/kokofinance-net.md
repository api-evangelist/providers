---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Kokofinance Net Agentic Access
  operation_count: 39
  slug: kokofinance-net-agentic-access
  summary_line: 39 operations · 20 acting
api_count: 1
apis:
- description: Stripe billing — checkout sessions and customer portal.
  name: kokofinance-net Billing API
  slug: kokofinance-net-billing-api
- description: Credit card catalog — browse, search, and get detailed card information with structured fields.
  name: kokofinance-net Cards API
  slug: kokofinance-net-cards-api
- description: Developer account management — dashboard, API keys, organization settings.
  name: kokofinance-net Developers API
  slug: kokofinance-net-developers-api
- description: Computational endpoints — compare cards, get recommendations, calculate value, renewal analysis, merchant optimization.
  name: kokofinance-net Intelligence API
  slug: kokofinance-net-intelligence-api
- description: The International API from kokofinance-net — 4 operation(s) for international.
  name: kokofinance-net International API
  slug: kokofinance-net-international-api
- description: System health, API status, and usage tracking.
  name: kokofinance-net Platform API
  slug: kokofinance-net-platform-api
- description: User portfolio management — analyze your cards, manage point balances, get redemption strategies.
  name: kokofinance-net Portfolio API
  slug: kokofinance-net-portfolio-api
- description: Static reference data — points programs, benefit categories, program valuations.
  name: kokofinance-net Reference API
  slug: kokofinance-net-reference-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/kokofinance-net/agentic-access/kokofinance-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kokofinance-net-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/kokofinance-net/rate-limits/kokofinance-net-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kokofinance-net-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kokofinance-net/plans/kokofinance-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kokofinance-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/kokofinance-net/rules/kokofinance-net-rules.yml
  title: ''
  type: Spectral
  url: rules/kokofinance-net-rules.yml
- group: design
  href: https://artifacts.apis.io/kokofinance-net/json-ld/kokofinance-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kokofinance-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/kokofinance-net/vocabulary/kokofinance-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kokofinance-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/kokofinance-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/kokofinance-net/data-model/kokofinance-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kokofinance-net-data-model.yml
- group: design
  href: https://artifacts.apis.io/kokofinance-net/conventions/kokofinance-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kokofinance-net-conventions.yml
- group: design
  href: https://artifacts.apis.io/kokofinance-net/lifecycle/kokofinance-net-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kokofinance-net-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/kokofinance-net/errors/kokofinance-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kokofinance-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kokofinance-net/conformance/kokofinance-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kokofinance-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kokofinance-net/well-known/kokofinance-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kokofinance-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/kokofinance-net/hosts/kokofinance-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kokofinance-net-hosts.yml
- group: build
  href: https://artifacts.apis.io/kokofinance-net/packages/kokofinance-net-packages.yml
  title: ''
  type: SDKs
  url: packages/kokofinance-net-packages.yml
- group: build
  href: https://artifacts.apis.io/kokofinance-net/packages/kokofinance-net-packages.yml
  title: ''
  type: Packages
  url: packages/kokofinance-net-packages.yml
- group: auth
  href: https://artifacts.apis.io/kokofinance-net/authentication/kokofinance-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kokofinance-net-authentication.yml
- group: auth
  href: https://artifacts.apis.io/kokofinance-net/security/kokofinance-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kokofinance-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kokofinance.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kokofinance.net/dashboard.html
- group: docs
  title: ''
  type: Documentation
  url: https://kokofinance.net/developers.html
- group: docs
  title: ''
  type: APIReference
  url: https://kokofinance.net/docs/rest-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://kokofinance.net/developers.html
- group: operate
  title: ''
  type: Support
  url: https://kokofinance.net/contact.html
- group: commercial
  title: ''
  type: Pricing
  url: https://kokofinance.net/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://kokofinance.net/dashboard.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kokofinance.net/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kokofinance.net/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KokoFinance
created: '2026-10-30'
description: Koko Finance provides a credit card intelligence platform offering portfolio analysis, recommendations, renewal value assessment, merchant-level advice, and detailed card term extraction (APR, penalties) with change tracking over time. The service is available via a REST API and an MCP server, with tiered evaluation options and the ability to ship card intelligence in a day.
image: https://kokofinance.net/images/koko-og-image.png
json_schemas:
- name: V1CardSearchRequest
  property_count: 6
  slug: kokofinance-net-v1-card-search-request
- name: V1CardValueRequest
  property_count: 7
  slug: kokofinance-net-v1-card-value-request
- name: V1PlaybookRequest
  property_count: 3
  slug: kokofinance-net-v1-playbook-request
- name: V1PortfolioAnalyzeRequest
  property_count: 3
  slug: kokofinance-net-v1-portfolio-analyze-request
- name: V1RecommendRequest
  property_count: 4
  slug: kokofinance-net-v1-recommend-request
- name: V1RenewalCheckRequest
  property_count: 7
  slug: kokofinance-net-v1-renewal-check-request
jsonld:
- class_count: 41
  name: Kokofinance Net Context
  property_count: 102
  slug: kokofinance-net-context
layout: provider
modified: '2026-10-30'
name: kokofinance-net
nav: Providers
network: true
overview: 'kokofinance-net publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Cards API, Developers API, and 5 more. Tagged areas include Company, Fintech, Credit Cards, and MCP.


  The kokofinance-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  kokofinance-net''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Kokofinance Net Plans Pricing
  plan_count: 3
  slug: kokofinance-net-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Kokofinance Net Rate Limits
  slug: kokofinance-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: kokofinance-net API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: kokofinance-net-rules
scopes:
- name: Kokofinance Net Scopes
  scope_count: 0
  slug: kokofinance-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 72.8
    catalog_earned_first_party: 20.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 42.3
    discoverability: 48.2
    operational_transparency: 23.7
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kokofinance-net/kokofinance-net-2026-11-03T134504.png
security:
- kind: authentication
  name: Kokofinance Net Authentication
  slug: kokofinance-net-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kokofinance Net Domain Security
  slug: kokofinance-net-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: kokofinance-net-intelligence
  slug: kokofinance-net-intelligence
slug: kokofinance-net
tags:
- Company
- Fintech
- Credit Cards
- MCP
website: https://kokofinance.net/
---
