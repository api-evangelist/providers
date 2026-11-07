---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Connect your AI via the Dropyour MCP server, enabling creation, publishing, updating and managing drops through a Streamable HTTP endpoint.
  name: Dropyour MCP
  slug: dropyour-mcp
- description: 'Dropyour API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: Dropyour API
  slug: dropyour-io-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/dropyour-io/plans/dropyour-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dropyour-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dropyour-io/rules/dropyour-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dropyour-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dropyour-io/json-ld/dropyour-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dropyour-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/dropyour-io/vocabulary/dropyour-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dropyour-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dropyour-io/data-model/dropyour-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dropyour-io-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://dropyour.io/en/docs/security
- group: design
  href: https://artifacts.apis.io/dropyour-io/conformance/dropyour-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dropyour-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dropyour-io/llms/dropyour-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dropyour-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/dropyour-io/mcp/dropyour-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dropyour-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dropyour-io/well-known/dropyour-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dropyour-io-security.txt
- group: agent
  href: https://artifacts.apis.io/dropyour-io/well-known/dropyour-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dropyour-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dropyour-io/hosts/dropyour-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dropyour-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dropyour-io/vendors/dropyour-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dropyour-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dropyour-io/security/dropyour-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dropyour-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dropyour-io/security/dropyour-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dropyour-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dropyour.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dropyour.io/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dropyour.io/en/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dropyour.io/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dropyour.io/en/privacy
created: '2026-11-06'
description: Dropyour provides a platform to publish AI‑generated applications online without requiring an account. Users receive a permanent address for their app, can connect, maintain, prove ownership, and transfer it. The service emphasizes simplicity, privacy, and seamless integration via its MCP, offering documentation, pricing, and security details publicly.
json_schemas:
- name: GetApiDropsIdExportResponse
  property_count: 1
  slug: dropyour-io-get-api-drops-id-export-response
- name: GetApiV1PublicationsIdResponse
  property_count: 1
  slug: dropyour-io-get-api-v1-publications-id-response
- name: PostApiV1PublicationsIdApprobationRequest
  property_count: 1
  slug: dropyour-io-post-api-v1-publications-id-approbation-request
- name: PostApiV1PublicationsRequest
  property_count: 4
  slug: dropyour-io-post-api-v1-publications-request
- name: PostApiV1PublicationsResponse
  property_count: 2
  slug: dropyour-io-post-api-v1-publications-response
jsonld:
- class_count: 5
  name: Dropyour Io Context
  property_count: 9
  slug: dropyour-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.dropyour.io.
  name: Dropyour MCP Server
  slug: dropyour-io-mcp-yml
modified: '2026-11-06'
name: Dropyour
nav: Providers
network: true
overview: 'Dropyour is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Publishing, and Platform.


  The Dropyour catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dropyour''s developer surface includes documentation, API reference, and 18 more developer resources.'
plans:
- name: Dropyour Io Plans Pricing
  plan_count: 4
  slug: dropyour-io-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Dropyour API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: dropyour-io-rules
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 22.6
    developer_ergonomics: 16.7
    discoverability: 45.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dropyour Io Domain Security
  slug: dropyour-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dropyour Io Vulnerability Disclosure
  slug: dropyour-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dropyour-io
tags:
- Company
- Artificial Intelligence
- Publishing
- Platform
website: https://dropyour.io/
---
