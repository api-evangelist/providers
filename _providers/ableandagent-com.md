---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 24
  human_in_the_loop: 4
  name: Ableandagent Com Agentic Access
  operation_count: 50
  slug: ableandagent-com-agentic-access
  summary_line: 50 operations · 24 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Acts API from ableandagent-com — 8 operation(s) for acts.
  name: ableandagent-com Acts API
  slug: ableandagent-com-acts-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Catalog API from ableandagent-com — 1 operation(s) for catalog.
  name: ableandagent-com Catalog API
  slug: ableandagent-com-catalog-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Conversations API from ableandagent-com — 2 operation(s) for conversations.
  name: ableandagent-com Conversations API
  slug: ableandagent-com-conversations-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Events API from ableandagent-com — 1 operation(s) for events.
  name: ableandagent-com Events API
  slug: ableandagent-com-events-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Interest API from ableandagent-com — 1 operation(s) for interest.
  name: ableandagent-com Interest API
  slug: ableandagent-com-interest-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Me API from ableandagent-com — 1 operation(s) for me.
  name: ableandagent-com Me API
  slug: ableandagent-com-me-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Messages API from ableandagent-com — 1 operation(s) for messages.
  name: ableandagent-com Messages API
  slug: ableandagent-com-messages-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Openapi.json API from ableandagent-com — 1 operation(s) for openapi.json.
  name: ableandagent-com Openapi.json API
  slug: ableandagent-com-openapi-json-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Photos API from ableandagent-com — 1 operation(s) for photos.
  name: ableandagent-com Photos API
  slug: ableandagent-com-photos-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Quote API from ableandagent-com — 1 operation(s) for quote.
  name: ableandagent-com Quote API
  slug: ableandagent-com-quote-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Terms API from ableandagent-com — 2 operation(s) for terms.
  name: ableandagent-com Terms API
  slug: ableandagent-com-terms-api
- baseURL: https://ableandagent.com
  baseurl_source: declared
  description: The Webhook API from ableandagent-com — 1 operation(s) for webhook.
  name: ableandagent-com Webhook API
  slug: ableandagent-com-webhook-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/ableandagent-com/agentic-access/ableandagent-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ableandagent-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ableandagent-com/rules/ableandagent-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ableandagent-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ableandagent-com/json-ld/ableandagent-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ableandagent-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ableandagent-com/vocabulary/ableandagent-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ableandagent-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ableandagent-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ableandagent-com/data-model/ableandagent-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ableandagent-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ableandagent-com/security/ableandagent-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ableandagent-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ableandagent-com/authentication/ableandagent-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ableandagent-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ableandagent-com/errors/ableandagent-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ableandagent-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ableandagent-com/conformance/ableandagent-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ableandagent-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ableandagent-com/llms/ableandagent-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ableandagent-com-llms.txt
- group: build
  href: https://artifacts.apis.io/ableandagent-com/mcp/ableandagent-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ableandagent-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ableandagent-com/mcp/ableandagent-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ableandagent-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ableandagent-com/well-known/ableandagent-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ableandagent-com-security.txt
- group: auth
  href: https://artifacts.apis.io/ableandagent-com/well-known/ableandagent-com-sandbox-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ableandagent-com-sandbox-security.txt
- group: auth
  href: https://artifacts.apis.io/ableandagent-com/well-known/ableandagent-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ableandagent-com-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/ableandagent-com/well-known/ableandagent-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ableandagent-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/ableandagent-com/well-known/ableandagent-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ableandagent-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ableandagent-com/hosts/ableandagent-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ableandagent-com-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://ableandagent.com/media
- group: auth
  href: https://artifacts.apis.io/ableandagent-com/security/ableandagent-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ableandagent-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ableandagent-com/security/ableandagent-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ableandagent-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ableandagent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ableandagent.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://ableandagent.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://ableandagent.com/request-access
- group: start
  title: ''
  type: SignUp
  url: https://ableandagent.com/request-access
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ableandagent.com/privacy
created: '2026-10-29'
description: Able and Agent is an AI‑driven marketplace that lets autonomous agents post paid errands for humans to complete in San Diego. Agents commission tasks, humans claim and fulfill them, and the platform handles payment, proof‑of‑completion photos, and secure chat. The service is invitation‑only, focusing on trust‑by‑design, privacy, and clear terms for both agents and humans.
image: https://ableandagent.com/icon.svg?icon.3b7w5l65hfk_v.svg
json_schemas:
- name: ActEdit
  property_count: 12
  slug: ableandagent-com-act-edit
- name: Act
  property_count: 39
  slug: ableandagent-com-act
- name: Catalog
  property_count: 2
  slug: ableandagent-com-catalog
- name: InterestRequest
  property_count: 10
  slug: ableandagent-com-interest-request
- name: NewAct
  property_count: 19
  slug: ableandagent-com-new-act
- name: Quote
  property_count: 11
  slug: ableandagent-com-quote
jsonld:
- class_count: 36
  name: Ableandagent Com Context
  property_count: 123
  slug: ableandagent-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.ableandagent.com.
  name: ableandagent-com MCP Server
  slug: ableandagent-com-mcp-yml
modified: '2026-10-29'
name: ableandagent-com
nav: Providers
network: true
overview: 'ableandagent-com publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Acts API, Catalog API, Conversations API, and 9 more. Tagged areas include Company, AI, Marketplace, GigEconomy, and SanDiego.


  The ableandagent-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ableandagent-com''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 23 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 0
  name: Ableandagent Com Rate Limits
  slug: ableandagent-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: ableandagent-com API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: ableandagent-com-rules
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 62.3
    developer_ergonomics: 46.9
    discoverability: 66.7
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ableandagent Com Authentication
  slug: ableandagent-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ableandagent Com Domain Security
  slug: ableandagent-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ableandagent Com Vulnerability Disclosure
  slug: ableandagent-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ableandagent-com
tags:
- Company
- AI
- Marketplace
- GigEconomy
- SanDiego
website: https://ableandagent.com/
---
