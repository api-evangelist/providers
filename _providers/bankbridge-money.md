---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'BankBridge API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: BankBridge API
  slug: bankbridge-money-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/bankbridge-money/plans/bankbridge-money-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bankbridge-money-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bankbridge-money/rules/bankbridge-money-rules.yml
  title: ''
  type: Spectral
  url: rules/bankbridge-money-rules.yml
- group: design
  href: https://artifacts.apis.io/bankbridge-money/json-ld/bankbridge-money-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bankbridge-money-context.jsonld
- group: design
  href: https://artifacts.apis.io/bankbridge-money/vocabulary/bankbridge-money-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bankbridge-money-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bankbridge-money/data-model/bankbridge-money-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bankbridge-money-data-model.yml
- group: build
  href: https://artifacts.apis.io/bankbridge-money/cli/bankbridge-money-cli.yml
  title: ''
  type: CLI
  url: cli/bankbridge-money-cli.yml
- group: auth
  href: https://artifacts.apis.io/bankbridge-money/authentication/bankbridge-money-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bankbridge-money-authentication.yml
- group: design
  href: https://artifacts.apis.io/bankbridge-money/conformance/bankbridge-money-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bankbridge-money-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bankbridge-money/llms/bankbridge-money-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bankbridge-money-llms.txt
- group: agent
  href: https://artifacts.apis.io/bankbridge-money/well-known/bankbridge-money-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bankbridge-money-well-known.yml
- group: other
  href: https://artifacts.apis.io/bankbridge-money/hosts/bankbridge-money-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankbridge-money-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bankbridge.money/terms
- group: auth
  title: ''
  type: Security
  url: https://bankbridge.money/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bankbridge.money/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://bankbridge.money/press
- group: start
  title: ''
  type: Login
  url: https://bankbridge.money/login
- group: docs
  title: ''
  type: Documentation
  url: https://bankbridge.money/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://bankbridge.money/changelog
- group: auth
  href: https://artifacts.apis.io/bankbridge-money/security/bankbridge-money-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bankbridge-money-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bankbridge-money/security/bankbridge-money-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankbridge-money-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bankbridge.money
coverage:
  checked: '2026-10-29'
  detail: The provider's documentation pages are public markdown but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://bankbridge.money/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: BankBridge provides a hosted MCP (Machine-Readable Consumer Protocol) server that gives AI assistants like Claude, ChatGPT, and Cursor read‑only access to users’ bank accounts. For a fee of $5 per month per connected bank (or $50 per year), users can link their bank once and let AI agents query spending, cash‑flow, subscriptions, and rent information without exposing credentials. The service emphasizes privacy, regulatory compliance, and secure, read‑only connections, positioning itself as a bridge between financial data and generative AI tools.
image: https://bankbridge.money/og-image.png
json_schemas:
- name: PostApiMcpRequest
  property_count: 3
  slug: bankbridge-money-post-api-mcp-request
- name: PostV1ResponsesRequest
  property_count: 8
  slug: bankbridge-money-post-v1-responses-request
jsonld:
- class_count: 2
  name: Bankbridge Money Context
  property_count: 6
  slug: bankbridge-money-context
layout: provider
modified: '2026-10-29'
name: BankBridge
nav: Providers
network: true
overview: 'BankBridge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Artificial Intelligence, MCP, and Banking.


  The BankBridge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BankBridge''s developer surface includes CLI, authentication, documentation, changelog, and 17 more developer resources.'
plans:
- name: Bankbridge Money Plans Pricing
  plan_count: 2
  slug: bankbridge-money-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: BankBridge API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: bankbridge-money-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 38.2
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 23.8
    discoverability: 65.2
    operational_transparency: 13.2
  previous_composite: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bankbridge-money/bankbridge-money-2026-11-03T121530.png
security:
- kind: authentication
  name: Bankbridge Money Authentication
  slug: bankbridge-money-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bankbridge Money Domain Security
  slug: bankbridge-money-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bankbridge Money Vulnerability Disclosure
  slug: bankbridge-money-vulnerability-disclosure
  summary_line: no policy recorded
slug: bankbridge-money
tags:
- Company
- Finance
- Artificial Intelligence
- MCP
- Banking
website: https://bankbridge.money
---
