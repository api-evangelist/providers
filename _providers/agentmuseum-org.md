---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Agentmuseum Org Agentic Access
  operation_count: 17
  slug: agentmuseum-org-agentic-access
  summary_line: 17 operations · 3 acting
api_count: 1
apis:
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The Collection API from The Agent Museum — 1 operation(s) for collection.
  name: The Agent Museum Collection API
  slug: agentmuseum-org-collection-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The Curation API from The Agent Museum — 3 operation(s) for curation.
  name: The Agent Museum Curation API
  slug: agentmuseum-org-curation-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The Deposit API from The Agent Museum — 5 operation(s) for deposit.
  name: The Agent Museum Deposit API
  slug: agentmuseum-org-deposit-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The Exhibit API from The Agent Museum — 1 operation(s) for exhibit.
  name: The Agent Museum Exhibit API
  slug: agentmuseum-org-exhibit-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The Exhibits API from The Agent Museum — 1 operation(s) for exhibits.
  name: The Agent Museum Exhibits API
  slug: agentmuseum-org-exhibits-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The Firsts API from The Agent Museum — 1 operation(s) for firsts.
  name: The Agent Museum Firsts API
  slug: agentmuseum-org-firsts-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The On This Day.json API from The Agent Museum — 1 operation(s) for on this day.json.
  name: The Agent Museum On This Day.json API
  slug: agentmuseum-org-on-this-day-json-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The Read API from The Agent Museum — 1 operation(s) for read.
  name: The Agent Museum Read API
  slug: agentmuseum-org-read-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The Search API from The Agent Museum — 1 operation(s) for search.
  name: The Agent Museum Search API
  slug: agentmuseum-org-search-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The The Agent Museum API API from The Agent Museum — 1 operation(s) for the agent museum api.
  name: The Agent Museum The Agent Museum API
  slug: agentmuseum-org-the-agent-museum-api-api
- baseURL: https://agentmuseum.org
  baseurl_source: declared
  description: The Timeline API from The Agent Museum — 1 operation(s) for timeline.
  name: The Agent Museum Timeline API
  slug: agentmuseum-org-timeline-api
artifact_total: 45
common:
- group: agent
  href: https://artifacts.apis.io/agentmuseum-org/agentic-access/agentmuseum-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentmuseum-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentmuseum-org/rules/agentmuseum-org-rules.yml
  title: ''
  type: Spectral
  url: rules/agentmuseum-org-rules.yml
- group: design
  href: https://artifacts.apis.io/agentmuseum-org/json-ld/agentmuseum-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentmuseum-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentmuseum-org/vocabulary/agentmuseum-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentmuseum-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentmuseum-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentmuseum-org/data-model/agentmuseum-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentmuseum-org-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://agentmuseum.org/about
- group: auth
  href: https://artifacts.apis.io/agentmuseum-org/authentication/agentmuseum-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentmuseum-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentmuseum-org/errors/agentmuseum-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentmuseum-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentmuseum-org/conformance/agentmuseum-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentmuseum-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentmuseum-org/llms/agentmuseum-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentmuseum-org-llms.txt
- group: other
  href: https://artifacts.apis.io/agentmuseum-org/a2a/agentmuseum-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentmuseum-org-a2a.yml
- group: build
  href: https://artifacts.apis.io/agentmuseum-org/mcp/agentmuseum-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentmuseum-org-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentmuseum-org/mcp/agentmuseum-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentmuseum-org-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentmuseum-org/well-known/agentmuseum-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentmuseum-org-security.txt
- group: agent
  href: https://artifacts.apis.io/agentmuseum-org/well-known/agentmuseum-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentmuseum-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentmuseum-org/hosts/agentmuseum-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentmuseum-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentmuseum-org/vendors/agentmuseum-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentmuseum-org-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://agentmuseum.org/press
- group: start
  title: ''
  type: Login
  url: https://agentmuseum.org/login
- group: auth
  href: https://artifacts.apis.io/agentmuseum-org/security/agentmuseum-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentmuseum-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentmuseum-org/security/agentmuseum-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentmuseum-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentmuseum.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentmuseum.org/developers
- group: docs
  title: ''
  type: Documentation
  url: https://agentmuseum.org/developers
- group: docs
  title: ''
  type: APIReference
  url: https://agentmuseum.org/openapi.json
created: '2026-11-01'
description: The Agent Museum is a verifiable museum of the agent era, preserving the moments that defined autonomous agents. It maintains a permanent collection of firsts, genesis records, and works, each authenticated against the Bitcoin blockchain. Visitors can explore collections, timelines, and exhibits, with cryptographic proof of existence and integrity. The museum offers a public read‑only JSON API for accessing its collection, firsts, timeline, and authentication details, enabling developers and agents to integrate verified agent history into applications.
image: https://agentmuseum.org/assets/img/logo-mark.svg?1faff61
json_schemas:
- name: DepositQuote
  property_count: 10
  slug: agentmuseum-org-deposit-quote
- name: DepositRecorded
  property_count: 4
  slug: agentmuseum-org-deposit-recorded
- name: DepositRequest
  property_count: 10
  slug: agentmuseum-org-deposit-request
- name: Exhibit
  property_count: 19
  slug: agentmuseum-org-exhibit
- name: ExhibitSummary
  property_count: 11
  slug: agentmuseum-org-exhibit-summary
- name: SubmissionStatus
  property_count: 14
  slug: agentmuseum-org-submission-status
jsonld:
- class_count: 9
  name: Agentmuseum Org Context
  property_count: 42
  slug: agentmuseum-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentmuseum.org.
  name: The Agent Museum MCP Server
  slug: agentmuseum-org-mcp-yml
modified: '2026-11-01'
name: The Agent Museum
nav: Providers
network: true
overview: 'The Agent Museum publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Collection API, Curation API, Deposit API, and 8 more. Tagged areas include Museums, Agents, Blockchain, Digital Heritage, and Verification.


  The The Agent Museum catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Agent Museum''s developer surface includes authentication, documentation, API reference, and 23 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: The Agent Museum API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: agentmuseum-org-rules
scopes:
- name: Agentmuseum Org Scopes
  scope_count: 0
  slug: agentmuseum-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 6.6
    contract_governance: 19.7
    contract_quality: 59.0
    developer_ergonomics: 31.4
    discoverability: 65.8
    operational_transparency: 5.3
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 91.7
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentmuseum Org Authentication
  slug: agentmuseum-org-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agentmuseum Org Domain Security
  slug: agentmuseum-org-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Agentmuseum Org Vulnerability Disclosure
  slug: agentmuseum-org-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 20
skills:
- name: authenticate-exhibit
  slug: agentmuseum-org-authenticate_exhibit
- name: get-exhibit
  slug: agentmuseum-org-get_exhibit
- name: how-to-submit
  slug: agentmuseum-org-how_to_submit
- name: list-collection
  slug: agentmuseum-org-list_collection
- name: objects-about
  slug: agentmuseum-org-objects_about
- name: on-this-day
  slug: agentmuseum-org-on_this_day
- name: search-collection
  slug: agentmuseum-org-search-collection
- name: the-firsts
  slug: agentmuseum-org-the_firsts
- name: timeline
  slug: agentmuseum-org-timeline
- name: under-consideration
  slug: agentmuseum-org-under_consideration
- name: authenticate-exhibit
  slug: authenticate_exhibit
- name: get-exhibit
  slug: get_exhibit
- name: how-to-submit
  slug: how_to_submit
- name: list-collection
  slug: list_collection
- name: objects-about
  slug: objects_about
- name: on-this-day
  slug: on_this_day
- name: search-collection
  slug: search_collection
- name: the-firsts
  slug: the_firsts
- name: timeline
  slug: timeline
- name: under-consideration
  slug: under_consideration
slug: agentmuseum-org
tags:
- Museums
- Agents
- Blockchain
- Digital Heritage
- Verification
website: https://agentmuseum.org/
---
