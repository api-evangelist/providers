---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Gaipagents Com Agentic Access
  operation_count: 123
  slug: gaipagents-com-agentic-access
  summary_line: 123 operations · 38 acting
api_count: 1
apis:
- baseURL: https://www.gaipagents.com
  baseurl_source: declared
  description: Conformance of A2A, MCP and OpenAPI declarations and the manifest change log.
  name: gaipagents-com Agent Observatory API
  slug: gaipagents-com-agent-observatory-api
- baseURL: https://www.gaipagents.com
  baseurl_source: declared
  description: Pre-delegation checks, delivery terms, witnessing and citation checks.
  name: gaipagents-com Delivery Assurance API
  slug: gaipagents-com-delivery-assurance-api
- baseURL: https://www.gaipagents.com
  baseurl_source: declared
  description: Agent cards, MCP Server Cards, catalogs, guides and product documents.
  name: gaipagents-com Discovery API
  slug: gaipagents-com-discovery-api
- baseURL: https://www.gaipagents.com
  baseurl_source: declared
  description: Receipts, verification, evidence packs, incident bundles and outcomes.
  name: gaipagents-com Evidence Ledger API
  slug: gaipagents-com-evidence-ledger-api
- baseURL: https://www.gaipagents.com
  baseurl_source: declared
  description: Status, history and other platform resources.
  name: gaipagents-com Platform API
  slug: gaipagents-com-platform-api
- baseURL: https://www.gaipagents.com
  baseurl_source: declared
  description: Supplier snapshots, change watch and failed-call diagnosis.
  name: gaipagents-com Supplier Reliability API
  slug: gaipagents-com-supplier-reliability-api
- baseURL: https://www.gaipagents.com
  baseurl_source: declared
  description: Answers read from GAIP's dated record of what was published, as indexed, each with a receipt.
  name: gaipagents-com The record API
  slug: gaipagents-com-the-record-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/gaipagents-com/agentic-access/gaipagents-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gaipagents-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/gaipagents-com/rules/gaipagents-com-rules.yml
  title: ''
  type: Spectral
  url: rules/gaipagents-com-rules.yml
- group: design
  href: https://artifacts.apis.io/gaipagents-com/json-ld/gaipagents-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gaipagents-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/gaipagents-com/vocabulary/gaipagents-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gaipagents-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gaipagents-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gaipagents-com/data-model/gaipagents-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gaipagents-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/gaipagents-com/changelog/gaipagents-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gaipagents-com-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gaipagents.com/security
- group: design
  href: https://artifacts.apis.io/gaipagents-com/errors/gaipagents-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gaipagents-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gaipagents-com/conformance/gaipagents-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gaipagents-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gaipagents-com/llms/gaipagents-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gaipagents-com-llms.txt
- group: other
  href: https://artifacts.apis.io/gaipagents-com/a2a/gaipagents-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gaipagents-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/gaipagents-com/well-known/gaipagents-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gaipagents-com-security.txt
- group: auth
  href: https://artifacts.apis.io/gaipagents-com/well-known/gaipagents-com-gaipagents-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gaipagents-com-gaipagents-security.txt
- group: agent
  href: https://artifacts.apis.io/gaipagents-com/well-known/gaipagents-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gaipagents-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/gaipagents-com/hosts/gaipagents-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gaipagents-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gaipagents-com/vendors/gaipagents-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gaipagents-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gaipagents.com/v1/free/plans
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.gaipagents.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.gaipagents.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/gaipagents-com/security/gaipagents-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gaipagents-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gaipagents-com/security/gaipagents-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gaipagents-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gaipagents.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.gaipagents.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gaipagents.com/
- group: docs
  title: ''
  type: APIReference
  url: https://gaipagents.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gaipagents.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gaipagents.com/privacy
created: '2026-10-29'
description: GAIP (Governed Agentic Intelligence Platform) provides a public, read‑only API that records and serves dated evidence of AI agents, MCP servers, and online shops. It offers OpenAPI 3.1 specification, MCP and A2A JSON‑RPC endpoints, and a suite of discovery documents (agent‑card, AI catalog, llms.txt). The service is free, requires no authentication, and returns signed receipts for queries, enabling transparent verification of published data. Operated by GAIP, the platform aims to foster trustworthy AI interoperability.
image: https://www.gaipagents.com/erc8004/images/gaip.svg
jsonld:
- class_count: 1
  name: Gaipagents Com Context
  property_count: 3
  slug: gaipagents-com-context
layout: provider
modified: '2026-10-29'
name: gaipagents-com
nav: Providers
network: true
overview: 'gaipagents-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Observatory API, Delivery Assurance API, Discovery API, and 4 more. Tagged areas include Company, AI, Agentic, MCP, and A2A.


  The gaipagents-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  gaipagents-com''s developer surface includes changelog, pricing, getting-started guide, documentation, API reference, and 23 more developer resources.'
plans:
- name: Gaipagents Com Plans Pricing
  plan_count: 0
  slug: gaipagents-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Gaipagents Com Rate Limits
  slug: gaipagents-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: gaipagents-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: gaipagents-com-rules
scopes:
- name: Gaipagents Com Scopes
  scope_count: 0
  slug: gaipagents-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 39.9
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gaipagents Com Authentication
  slug: gaipagents-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Gaipagents Com Domain Security
  slug: gaipagents-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gaipagents Com Vulnerability Disclosure
  slug: gaipagents-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-platform-agent-card
  slug: gaipagents-com-get-platform-agent-card
slug: gaipagents-com
tags:
- Company
- AI
- Agentic
- MCP
- A2A
- OpenAPI
website: https://gaipagents.com/
---
