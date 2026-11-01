---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Useagentbank Agentic Access
  operation_count: 3
  slug: useagentbank-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://protocol.useagentbank.com
  baseurl_source: declared
  description: The Payouts API from AgentBank — 3 operation(s) for payouts.
  name: AgentBank Payouts API
  slug: useagentbank-payouts-api
artifact_total: 10
asyncapis:
- description: ''
  name: Useagentbank Webhooks
  slug: useagentbank-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/useagentbank/agentic-access/useagentbank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/useagentbank-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/useagentbank/rules/useagentbank-rules.yml
  title: ''
  type: Spectral
  url: rules/useagentbank-rules.yml
- group: design
  href: https://artifacts.apis.io/useagentbank/json-ld/useagentbank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/useagentbank-context.jsonld
- group: design
  href: https://artifacts.apis.io/useagentbank/vocabulary/useagentbank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/useagentbank-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/useagentbank/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/useagentbank/asyncapi/useagentbank-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/useagentbank-webhooks.yml
- group: design
  href: https://artifacts.apis.io/useagentbank/data-model/useagentbank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/useagentbank-data-model.yml
- group: operate
  href: https://artifacts.apis.io/useagentbank/changelog/useagentbank-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/useagentbank-changelog.yml
- group: design
  href: https://artifacts.apis.io/useagentbank/conventions/useagentbank-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/useagentbank-conventions.yml
- group: design
  href: https://artifacts.apis.io/useagentbank/conventions/useagentbank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/useagentbank-conventions.yml
- group: auth
  href: https://artifacts.apis.io/useagentbank/authentication/useagentbank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/useagentbank-authentication.yml
- group: design
  href: https://artifacts.apis.io/useagentbank/errors/useagentbank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/useagentbank-problem-types.yml
- group: design
  href: https://artifacts.apis.io/useagentbank/conformance/useagentbank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/useagentbank-conformance.yml
- group: agent
  href: https://artifacts.apis.io/useagentbank/llms/useagentbank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/useagentbank-llms.txt
- group: other
  href: https://artifacts.apis.io/useagentbank/a2a/useagentbank-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/useagentbank-a2a.yml
- group: agent
  href: https://artifacts.apis.io/useagentbank/well-known/useagentbank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/useagentbank-well-known.yml
- group: other
  href: https://artifacts.apis.io/useagentbank/hosts/useagentbank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/useagentbank-hosts.yml
- group: other
  href: https://artifacts.apis.io/useagentbank/vendors/useagentbank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/useagentbank-vendors.yml
- group: build
  href: https://artifacts.apis.io/useagentbank/packages/useagentbank-packages.yml
  title: ''
  type: SDKs
  url: packages/useagentbank-packages.yml
- group: build
  href: https://artifacts.apis.io/useagentbank/packages/useagentbank-packages.yml
  title: ''
  type: Packages
  url: packages/useagentbank-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://useagentbank.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.useagentbank.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.useagentbank.com/reference/mcp-overview
- group: auth
  href: https://artifacts.apis.io/useagentbank/security/useagentbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/useagentbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://useagentbank.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useagentbank.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useagentbank.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useagentbank.com/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.useagentbank.com/getting-started/quickstart.md
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://docs.useagentbank.com/mcp
  - status: 200
    url: https://useagentbank.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: AgentBank provides crypto‑backed banking services tailored for AI agents, enabling them to collect, hold, convert, and move money across the real‑world financial system. Through its Model Context Protocol (MCP) API, agents can initiate payments to bank accounts, QR codes, and crypto wallets, with human owners approving transactions and enforcing spending limits. The platform supports cross‑border stablecoin payments, compliance with financial regulations, and offers developer tools for seamless integration.
image: https://useagentbank.com/opengraph-image.jpg?opengraph-image.38-a9x557i8hq.jpg
json_schemas:
- name: PublicX402ExactSourceStart
  property_count: 5
  slug: useagentbank-public-x402-exact-source-start
- name: PublicX402FundingSubmitted
  property_count: 4
  slug: useagentbank-public-x402-funding-submitted
jsonld:
- class_count: 7
  name: Useagentbank Context
  property_count: 15
  slug: useagentbank-context
layout: provider
modified: '2026-10-20'
name: AgentBank
nav: Providers
network: true
overview: 'AgentBank publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Payouts API. Tagged areas include Company, Finance, AI, Banking, and Crypto.


  The AgentBank catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  AgentBank''s developer surface includes changelog, authentication, API reference, documentation, getting-started guide, and 24 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AgentBank API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: useagentbank-rules
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 65.8
    developer_ergonomics: 49.4
    discoverability: 66.1
    operational_transparency: 34.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 18.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Useagentbank Authentication
  slug: useagentbank-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Useagentbank Domain Security
  slug: useagentbank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: useagentbank-payout-flow
  slug: useagentbank-payout-flow
slug: useagentbank
tags:
- Company
- Finance
- AI
- Banking
- Crypto
- Payments
website: https://useagentbank.com
---
