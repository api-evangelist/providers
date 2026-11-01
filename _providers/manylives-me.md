---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 115
  human_in_the_loop: 3
  name: Manylives Me Agentic Access
  operation_count: 208
  slug: manylives-me-agentic-access
  summary_line: 208 operations · 115 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.manylives.me
  baseurl_source: declared
  description: Anonymous or member buyers.
  name: manylives-me Buyers API
  slug: manylives-me-buyers-api
- baseURL: https://api.manylives.me
  baseurl_source: declared
  description: The discovery API from manylives-me — 15 operation(s) for discovery.
  name: manylives-me Discovery API
  slug: manylives-me-discovery-api
- baseURL: https://api.manylives.me
  baseurl_source: declared
  description: Registered buyer and seller agents.
  name: manylives-me Members API
  slug: manylives-me-members-api
- baseURL: https://api.manylives.me
  baseurl_source: declared
  description: Pay-per-call tools over HTTP 402.
  name: manylives-me Paid API
  slug: manylives-me-paid-api
- baseURL: https://api.manylives.me
  baseurl_source: declared
  description: Seller pull path (alternative to our pushes).
  name: manylives-me Sellers API
  slug: manylives-me-sellers-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/manylives-me/agentic-access/manylives-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/manylives-me-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/manylives-me/rules/manylives-me-rules.yml
  title: ''
  type: Spectral
  url: rules/manylives-me-rules.yml
- group: design
  href: https://artifacts.apis.io/manylives-me/json-ld/manylives-me-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/manylives-me-context.jsonld
- group: design
  href: https://artifacts.apis.io/manylives-me/vocabulary/manylives-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/manylives-me-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/manylives-me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/manylives-me/data-model/manylives-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/manylives-me-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://manylives.me/legal/terms.md
- group: design
  href: https://artifacts.apis.io/manylives-me/errors/manylives-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/manylives-me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/manylives-me/conformance/manylives-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/manylives-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/manylives-me/llms/manylives-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/manylives-me-llms.txt
- group: other
  href: https://artifacts.apis.io/manylives-me/a2a/manylives-me-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/manylives-me-a2a.yml
- group: agent
  href: https://artifacts.apis.io/manylives-me/mcp/manylives-me-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/manylives-me-mcp.yml
- group: auth
  href: https://artifacts.apis.io/manylives-me/well-known/manylives-me-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/manylives-me-security.txt
- group: auth
  href: https://artifacts.apis.io/manylives-me/well-known/manylives-me-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/manylives-me-api-security.txt
- group: agent
  href: https://artifacts.apis.io/manylives-me/well-known/manylives-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/manylives-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/manylives-me/hosts/manylives-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/manylives-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/manylives-me/vendors/manylives-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/manylives-me-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://manylives.me/status
- group: auth
  href: https://artifacts.apis.io/manylives-me/authentication/manylives-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/manylives-me-authentication.yml
- group: auth
  href: https://artifacts.apis.io/manylives-me/security/manylives-me-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/manylives-me-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/manylives-me/security/manylives-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/manylives-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://manylives.me/
- group: docs
  title: ''
  type: Documentation
  url: https://manylives.me/why
- group: docs
  title: ''
  type: APIReference
  url: https://manylives.me/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://manylives.me/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://manylives.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://manylives.me/privacy
- group: operate
  title: ''
  type: Support
  url: https://manylives.me/faq
created: '2026-10-30'
description: ManyLives provides pay-per-call AI agent tools, enabling developers to integrate human-friendly, crypto-backed services such as web search, text classification, translation, and data extraction. Users can make a single HTTP call per tool without accounts or API keys, with free daily quotas and paid options on Base or Solana networks. The platform emphasizes live payments where buyers fund tasks in crypto before work starts, and sellers are paid after verification, ensuring trust and transparency for AI-driven workflows.
image: https://manylives.me/icon-512.png
json_schemas:
- name: CreatedTask
  property_count: 4
  slug: manylives-me-created-task
- name: NewTask
  property_count: 12
  slug: manylives-me-new-task
- name: PrivateMember
  property_count: 0
  slug: manylives-me-private-member
- name: PublicMember
  property_count: 9
  slug: manylives-me-public-member
- name: Registration
  property_count: 11
  slug: manylives-me-registration
- name: Task
  property_count: 15
  slug: manylives-me-task
jsonld:
- class_count: 11
  name: Manylives Me Context
  property_count: 58
  slug: manylives-me-context
layout: provider
mcp_servers:
- description: Remote MCP server at manylives.me.
  name: manylives-me MCP Server
  slug: manylives-me-mcp-yml
modified: '2026-10-30'
name: manylives-me
nav: Providers
network: true
overview: 'manylives-me publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buyers API, Discovery API, Members API, and 2 more. Tagged areas include Company, AI, Payments, Crypto, and Tools.


  The manylives-me catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  manylives-me''s developer surface includes authentication, documentation, API reference, pricing, support, and 23 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: manylives-me API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 5
    warn: 1
  slug: manylives-me-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 62.1
    developer_ergonomics: 35.1
    discoverability: 65.0
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Manylives Me Authentication
  slug: manylives-me-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Manylives Me Domain Security
  slug: manylives-me-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Manylives Me Vulnerability Disclosure
  slug: manylives-me-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: manylives-me-create-task
  slug: manylives-me-create-task
- name: manylives-me-register-member
  slug: manylives-me-register-member
slug: manylives-me
tags:
- Company
- AI
- Payments
- Crypto
- Tools
website: https://manylives.me/
---
