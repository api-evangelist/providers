---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Aisoup Net Agentic Access
  operation_count: 22
  slug: aisoup-net-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 2
apis:
- description: Paid source-linked preflight of one California contractor license. Human reports are sold separately through Stripe Checkout.
  name: California C-10 Contractor Check
  slug: california-c-10-contractor-check
- baseURL: https://api.aisoup.net
  baseurl_source: declared
  description: The Commerce API from aisoup-net — 5 operation(s) for commerce.
  name: aisoup-net Commerce API
  slug: aisoup-net-commerce-api
- baseURL: https://api.aisoup.net
  baseurl_source: declared
  description: The contact API from aisoup-net — 1 operation(s) for contact.
  name: aisoup-net Contact API
  slug: aisoup-net-contact-api
- baseURL: https://api.aisoup.net
  baseurl_source: declared
  description: The Contractor Check API from aisoup-net — 1 operation(s) for contractor check.
  name: aisoup-net Contractor Check API
  slug: aisoup-net-contractor-check-api
- baseURL: https://api.aisoup.net
  baseurl_source: declared
  description: The discovery API from aisoup-net — 1 operation(s) for discovery.
  name: aisoup-net Discovery API
  slug: aisoup-net-discovery-api
- baseURL: https://api.aisoup.net
  baseurl_source: declared
  description: The Evidence Snapshots API from aisoup-net — 2 operation(s) for evidence snapshots.
  name: aisoup-net Evidence Snapshots API
  slug: aisoup-net-evidence-snapshots-api
- baseURL: https://api.aisoup.net
  baseurl_source: declared
  description: The Photo Scout API from aisoup-net — 1 operation(s) for photo scout.
  name: aisoup-net Photo Scout API
  slug: aisoup-net-photo-scout-api
- baseURL: https://api.aisoup.net
  baseurl_source: declared
  description: The status API from aisoup-net — 3 operation(s) for status.
  name: aisoup-net Status API
  slug: aisoup-net-status-api
- baseURL: https://api.aisoup.net
  baseurl_source: declared
  description: The support API from aisoup-net — 3 operation(s) for support.
  name: aisoup-net Support API
  slug: aisoup-net-support-api
- baseURL: https://api.aisoup.net
  baseurl_source: declared
  description: The Web Evidence API from aisoup-net — 4 operation(s) for web evidence.
  name: aisoup-net Web Evidence API
  slug: aisoup-net-web-evidence-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/aisoup-net/agentic-access/aisoup-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aisoup-net-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aisoup-net/rules/aisoup-net-rules.yml
  title: ''
  type: Spectral
  url: rules/aisoup-net-rules.yml
- group: design
  href: https://artifacts.apis.io/aisoup-net/json-ld/aisoup-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aisoup-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/aisoup-net/vocabulary/aisoup-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aisoup-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aisoup-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aisoup-net/data-model/aisoup-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aisoup-net-data-model.yml
- group: design
  href: https://artifacts.apis.io/aisoup-net/errors/aisoup-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aisoup-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aisoup-net/conformance/aisoup-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aisoup-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aisoup-net/llms/aisoup-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aisoup-net-llms.txt
- group: other
  href: https://artifacts.apis.io/aisoup-net/a2a/aisoup-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aisoup-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aisoup-net/mcp/aisoup-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aisoup-net-mcp.yml
- group: other
  href: https://artifacts.apis.io/aisoup-net/hosts/aisoup-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aisoup-net-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aisoup.net/
- group: auth
  href: https://artifacts.apis.io/aisoup-net/security/aisoup-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aisoup-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aisoup.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api.aisoup.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.aisoup.net/openapi.json
created: '2026-10-29'
description: 'AI Soup (legal name Dream Workshop LLC) builds AI agent‑native applications that enable two A4As: Agent for App and App for Agent. It offers a suite of AI‑driven tools including AgenticWiKi for knowledge work, Web Evidence for claim verification, California C‑10 Contractor Check, Niche Discovery, Photo Scout, and Property Scout, each providing specialized agent‑led workflows and infrastructure.'
image: https://aisoup.net/favicon.svg
json_schemas:
- name: ContactMessageRequest
  property_count: 6
  slug: aisoup-net-contact-message-request
- name: StatusSubscriptionRequest
  property_count: 3
  slug: aisoup-net-status-subscription-request
- name: SupportMessageRequest
  property_count: 1
  slug: aisoup-net-support-message-request
- name: SupportTicketCreateRequest
  property_count: 5
  slug: aisoup-net-support-ticket-create-request
jsonld:
- class_count: 56
  name: Aisoup Net Context
  property_count: 186
  slug: aisoup-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.aisoup.net.
  name: aisoup-net MCP Server
  slug: aisoup-net-mcp-yml
modified: '2026-10-29'
name: aisoup-net
nav: Providers
network: true
overview: 'aisoup-net publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Commerce API, Contact API, Contractor Check API, and 7 more. Tagged areas include AI, Agent, Platform, Workflow, and LLM.


  The aisoup-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aisoup-net''s developer surface includes documentation, API reference, and 15 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: aisoup-net API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 4
  slug: aisoup-net-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.7
    developer_ergonomics: 23.1
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 44.4
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aisoup Net Domain Security
  slug: aisoup-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: web-evidence
  slug: aisoup-net-web-evidence
slug: aisoup-net
tags:
- AI
- Agent
- Platform
- Workflow
- LLM
website: https://aisoup.net/
---
