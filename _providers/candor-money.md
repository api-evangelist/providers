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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Candor Money Agentic Access
  operation_count: 1
  slug: candor-money-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.candor.money
  baseurl_source: declared
  description: The Conversations API from Candor Finance — 1 operation(s) for conversations.
  name: Candor Finance Conversations API
  slug: candor-money-conversations-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/candor-money/vocabulary/candor-money-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/candor-money-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/candor-money/data-model/candor-money-data-model.yml
  title: ''
  type: DataModel
  url: data-model/candor-money-data-model.yml
- group: agent
  href: https://artifacts.apis.io/candor-money/agentic-access/candor-money-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/candor-money-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/candor-money/plans/candor-money-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/candor-money-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/candor-money/rules/candor-money-rules.yml
  title: ''
  type: Spectral
  url: rules/candor-money-rules.yml
- group: build
  href: https://artifacts.apis.io/candor-money/cli/candor-money-cli.yml
  title: ''
  type: CLI
  url: cli/candor-money-cli.yml
- group: design
  href: https://artifacts.apis.io/candor-money/errors/candor-money-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/candor-money-problem-types.yml
- group: design
  href: https://artifacts.apis.io/candor-money/conformance/candor-money-conformance.yml
  title: ''
  type: Conformance
  url: conformance/candor-money-conformance.yml
- group: other
  href: https://artifacts.apis.io/candor-money/overlays/candor-money-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/candor-money-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/candor-money/llms/candor-money-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/candor-money-llms.txt
- group: auth
  href: https://artifacts.apis.io/candor-money/well-known/candor-money-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/candor-money-security.txt
- group: auth
  href: https://artifacts.apis.io/candor-money/well-known/candor-money-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/candor-money-app-security.txt
- group: auth
  href: https://artifacts.apis.io/candor-money/well-known/candor-money-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/candor-money-api-security.txt
- group: agent
  href: https://artifacts.apis.io/candor-money/well-known/candor-money-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/candor-money-well-known.yml
- group: other
  href: https://artifacts.apis.io/candor-money/hosts/candor-money-hosts.yml
  title: ''
  type: Hosts
  url: hosts/candor-money-hosts.yml
- group: other
  href: https://artifacts.apis.io/candor-money/vendors/candor-money-vendors.yml
  title: ''
  type: Vendors
  url: vendors/candor-money-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://candor.money/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://candor.money/terms
- group: operate
  title: ''
  type: Support
  url: https://candor.money/support
- group: start
  title: ''
  type: SignUp
  url: https://app.candor.money/signup
- group: auth
  title: ''
  type: Security
  url: https://candor.money/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://candor.money/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/candorsystems
- group: start
  title: ''
  type: GettingStarted
  url: https://candor.money/monarch-alternative
- group: docs
  title: ''
  type: APIReference
  url: https://candor.money/developers
- group: auth
  href: https://artifacts.apis.io/candor-money/security/candor-money-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/candor-money-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/candor-money/security/candor-money-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/candor-money-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://candor.money
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://candor.money/openapi.json
  - status: null
    url: https://api.candor.money/openapi.json
  - status: 401
    url: https://api.candor.money/mcp
  - status: 200
    url: https://candor.money
  reason: partner-login
  state: gated
created: '2026-10-26'
description: Candor Finance provides an AI‑driven personal finance platform that helps users manage spending, bills, investments, and long‑term money goals. The service integrates with real accounts to generate weekly financial plans, offers budgeting tools, and answers hard‑money questions through an AI agent that can suggest actions like saving for a home or optimizing expenses.
image: https://candor.money/og/candor-og-home.png
json_schemas:
- name: ResponseEnvelope
  property_count: 0
  slug: candor-money-response-envelope
layout: provider
modified: '2026-10-26'
name: Candor Finance
nav: Providers
network: true
overview: 'Candor Finance publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Conversations API. Tagged areas include Company, Finance, Artificial Intelligence, Personal Finance, and Budgeting.


  The Candor Finance catalog on APIs.io includes 1 Spectral governance ruleset.


  Candor Finance''s developer surface includes CLI, support, signup flow, getting-started guide, API reference, and 23 more developer resources.'
plans:
- name: Candor Money Plans Pricing
  plan_count: 2
  slug: candor-money-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Candor Finance API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: candor-money-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 47.8
    developer_ergonomics: 19.0
    discoverability: 80.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/candor-money/candor-money-2026-11-03T123120.png
security:
- kind: domain-security
  name: Candor Money Domain Security
  slug: candor-money-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Candor Money Vulnerability Disclosure
  slug: candor-money-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: candor-money
tags:
- Company
- Finance
- Artificial Intelligence
- Personal Finance
- Budgeting
website: https://candor.money
---
