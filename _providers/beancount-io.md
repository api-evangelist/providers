---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Beancount Io Agentic Access
  operation_count: 6
  slug: beancount-io-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://beancount.io
  baseurl_source: declared
  description: Ledger file and BQL operations
  name: Beancount.io Ledger API
  slug: beancount-io-ledger-api
- baseURL: https://beancount.io
  baseurl_source: declared
  description: Model Context Protocol - tool calling for ledgers
  name: Beancount.io MCP API
  slug: beancount-io-mcp-api
- baseURL: https://beancount.io
  baseurl_source: declared
  description: Beancount.io GraphQL API - blog, docs, and ledger queries
  name: Beancount.io Graph QL API
  slug: beancount-io-graph-ql-api
artifact_total: 15
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beancount.io/terms-of-service
- group: agent
  href: https://artifacts.apis.io/beancount-io/agentic-access/beancount-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beancount-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/beancount-io/plans/beancount-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beancount-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/beancount-io/rules/beancount-io-rules.yml
  title: ''
  type: Spectral
  url: rules/beancount-io-rules.yml
- group: design
  href: https://artifacts.apis.io/beancount-io/json-ld/beancount-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beancount-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/beancount-io/vocabulary/beancount-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beancount-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/beancount-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/beancount-io/data-model/beancount-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beancount-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/beancount-io/changelog/beancount-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/beancount-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/beancount-io/errors/beancount-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beancount-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/beancount-io/conformance/beancount-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beancount-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beancount-io/llms/beancount-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beancount-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/beancount-io/well-known/beancount-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beancount-io-security.txt
- group: agent
  href: https://artifacts.apis.io/beancount-io/well-known/beancount-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beancount-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/beancount-io/hosts/beancount-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beancount-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/beancount-io/vendors/beancount-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beancount-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/beancount-io/packages/beancount-io-packages.yml
  title: ''
  type: SDKs
  url: packages/beancount-io-packages.yml
- group: build
  href: https://artifacts.apis.io/beancount-io/packages/beancount-io-packages.yml
  title: ''
  type: Packages
  url: packages/beancount-io-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://beancount.io/sign-up/?next=%2Fledger%2F&utm_source=beancount.io&utm_medium=cta&utm_campaign=nav_signup
- group: auth
  title: ''
  type: Security
  url: https://beancount.io/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://beancount.io/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.v3.beancount.io</code
- group: auth
  href: https://artifacts.apis.io/beancount-io/scopes/beancount-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/beancount-io-scopes.yml
- group: auth
  href: https://artifacts.apis.io/beancount-io/authentication/beancount-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beancount-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/beancount-io/security/beancount-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beancount-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/beancount-io/security/beancount-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beancount-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beancount.io/
- group: docs
  title: ''
  type: Documentation
  url: https://beancount.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://beancount.io/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://beancount.io/docs/introduction-to-beancount
- group: commercial
  title: ''
  type: Pricing
  url: https://beancount.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beancount.io/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://beancount.io/blog
created: '2026-11-02'
description: Beancount.io provides hosted plain‑text accounting powered by Git and AI. It offers bookkeeping, bank sync, smart import of statements, AI‑driven insights, and customizable reporting. Designed for couples, freelancers, professionals, and small businesses, the platform delivers an auditable, version‑controlled ledger with collaborative features and open‑source tooling.
image: https://opengraph-image.blockeden.xyz/og/beancount-io/v1/card.webp?title=Beancount.io%20%E2%80%94%20Hosted%20Plain-Text%20Accounting%20with%20Git%20%26%20AI
json_schemas:
- name: Error
  property_count: 4
  slug: beancount-io-error
- name: MCPManifest
  property_count: 5
  slug: beancount-io-mcpmanifest
jsonld:
- class_count: 3
  name: Beancount Io Context
  property_count: 10
  slug: beancount-io-context
layout: provider
modified: '2026-11-02'
name: Beancount.io
nav: Providers
network: true
overview: 'Beancount.io publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Ledger API, MCP API, and Graph QL API. Tagged areas include Accounting, Finance, Software-as-a-Service, Open Source, and Collaboration.


  The Beancount.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Beancount.io''s developer surface includes changelog, signup flow, authentication, documentation, API reference, getting-started guide, pricing, and 26 more developer resources.'
plans:
- name: Beancount Io Plans Pricing
  plan_count: 5
  slug: beancount-io-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Beancount.io API Rules
  rule_count: 66
  severity_counts:
    error: 64
    hint: 0
    info: 1
    warn: 1
  slug: beancount-io-rules
scopes:
- name: Beancount Io Scopes
  scope_count: 3
  slug: beancount-io-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 62.9
    developer_ergonomics: 41.1
    discoverability: 66.1
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Beancount Io Authentication
  slug: beancount-io-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Beancount Io Domain Security
  slug: beancount-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Beancount Io Vulnerability Disclosure
  slug: beancount-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: beancount-io-graphql-query
  slug: beancount-io-graphql-query
- name: beancount-io-mcp-invoke
  slug: beancount-io-mcp-invoke
slug: beancount-io
tags:
- Accounting
- Finance
- Software-as-a-Service
- Open Source
- Collaboration
website: https://beancount.io/
---
