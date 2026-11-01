---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Paidhandshake Agentic Access
  operation_count: 25
  slug: paidhandshake-agentic-access
  summary_line: 25 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The Capabilities API from PaidHandshake Exchange — 1 operation(s) for capabilities.
  name: PaidHandshake Exchange Capabilities API
  slug: paidhandshake-capabilities-api
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The Checkout API from PaidHandshake Exchange — 1 operation(s) for checkout.
  name: PaidHandshake Exchange Checkout API
  slug: paidhandshake-checkout-api
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The Inventory API from PaidHandshake Exchange — 1 operation(s) for inventory.
  name: PaidHandshake Exchange Inventory API
  slug: paidhandshake-inventory-api
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The Machine API from PaidHandshake Exchange — 12 operation(s) for machine.
  name: PaidHandshake Exchange Machine API
  slug: paidhandshake-machine-api
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The Proof API from PaidHandshake Exchange — 1 operation(s) for proof.
  name: PaidHandshake Exchange Proof API
  slug: paidhandshake-proof-api
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The Quote API from PaidHandshake Exchange — 1 operation(s) for quote.
  name: PaidHandshake Exchange Quote API
  slug: paidhandshake-quote-api
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The Sample API from PaidHandshake Exchange — 1 operation(s) for sample.
  name: PaidHandshake Exchange Sample API
  slug: paidhandshake-sample-api
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The Search API from PaidHandshake Exchange — 2 operation(s) for search.
  name: PaidHandshake Exchange Search API
  slug: paidhandshake-search-api
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The .well Known API from PaidHandshake Exchange — 1 operation(s) for .well known.
  name: PaidHandshake Exchange .well Known API
  slug: paidhandshake-well-known-api
- baseURL: https://paidhandshake.com
  baseurl_source: spec
  description: The X402 API from PaidHandshake Exchange — 3 operation(s) for x402.
  name: PaidHandshake Exchange X402 API
  slug: paidhandshake-x402-api
artifact_total: 22
common:
- group: other
  href: https://artifacts.apis.io/paidhandshake/capabilities/paidhandshake-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/paidhandshake-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/paidhandshake/agentic-access/paidhandshake-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paidhandshake-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/paidhandshake/plans/paidhandshake-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/paidhandshake-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/paidhandshake/rules/paidhandshake-rules.yml
  title: ''
  type: Spectral
  url: rules/paidhandshake-rules.yml
- group: design
  href: https://artifacts.apis.io/paidhandshake/json-ld/paidhandshake-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/paidhandshake-context.jsonld
- group: design
  href: https://artifacts.apis.io/paidhandshake/vocabulary/paidhandshake-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/paidhandshake-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/paidhandshake/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/paidhandshake/data-model/paidhandshake-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paidhandshake-data-model.yml
- group: design
  href: https://artifacts.apis.io/paidhandshake/conventions/paidhandshake-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/paidhandshake-conventions.yml
- group: design
  href: https://artifacts.apis.io/paidhandshake/conventions/paidhandshake-conventions.yml
  title: ''
  type: Conventions
  url: conventions/paidhandshake-conventions.yml
- group: design
  href: https://artifacts.apis.io/paidhandshake/errors/paidhandshake-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paidhandshake-problem-types.yml
- group: design
  href: https://artifacts.apis.io/paidhandshake/conformance/paidhandshake-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paidhandshake-conformance.yml
- group: agent
  href: https://artifacts.apis.io/paidhandshake/llms/paidhandshake-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paidhandshake-llms.txt
- group: other
  href: https://artifacts.apis.io/paidhandshake/a2a/paidhandshake-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/paidhandshake-a2a.yml
- group: build
  href: https://artifacts.apis.io/paidhandshake/mcp/paidhandshake-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/paidhandshake-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/paidhandshake/mcp/paidhandshake-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/paidhandshake-mcp.yml
- group: agent
  href: https://artifacts.apis.io/paidhandshake/well-known/paidhandshake-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paidhandshake-well-known.yml
- group: other
  href: https://artifacts.apis.io/paidhandshake/hosts/paidhandshake-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paidhandshake-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://paidhandshake.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://paidhandshake.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/paidhandshake/authentication/paidhandshake-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paidhandshake-authentication.yml
- group: auth
  href: https://artifacts.apis.io/paidhandshake/security/paidhandshake-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paidhandshake-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paidhandshake.com
- group: docs
  title: ''
  type: Documentation
  url: https://paidhandshake.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paidhandshake.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paidhandshake.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://paidhandshake.com/discover
created: '2026-10-08'
description: PaidHandshake Exchange is a live AI‑enabled marketplace that connects autonomous agents, human workers, and data sources to fulfill commercial intelligence, procurement, and research requests. The platform offers a searchable catalog of verified buyer intent, supplier pricing, RFPs, grants, and local service opportunities. Users can submit queries via API or web UI, receive price quotes, and authorize micro‑transactions for data delivery. It supports MCP tools, A2A integration, and provides OpenAPI 3.1 specifications for programmatic access. Operated by Tech‑World LLC, the service aims to automate market intelligence gathering for AI agents and businesses.
finops:
- has_sources: true
  method: derived
  name: Paidhandshake Finops
  primary_unit: seat
  service_category: ''
  slug: paidhandshake-finops
  template: false
image: https://paidhandshake.com/assets/og-paidhandshake.jpg
json_schemas:
- name: MachineJobRequest
  property_count: 5
  slug: paidhandshake-machine-job-request
- name: MachineQuoteRequest
  property_count: 4
  slug: paidhandshake-machine-quote-request
- name: RecurringWatchRequest
  property_count: 6
  slug: paidhandshake-recurring-watch-request
jsonld:
- class_count: 10
  name: Paidhandshake Context
  property_count: 48
  slug: paidhandshake-context
layout: provider
mcp_servers:
- description: Remote MCP server at paidhandshake.com.
  name: PaidHandshake Exchange MCP Server
  slug: paidhandshake-mcp-yml
modified: '2026-10-08'
name: PaidHandshake Exchange
nav: Providers
network: true
overview: 'PaidHandshake Exchange publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Capabilities API, Checkout API, Inventory API, and 7 more. Tagged areas include Company, Artificial Intelligence, Marketplace, Data, and Automation.


  The PaidHandshake Exchange catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PaidHandshake Exchange''s developer surface includes API reference, authentication, documentation, getting-started guide, and 23 more developer resources.'
plans:
- name: Paidhandshake Plans Pricing
  plan_count: 1
  slug: paidhandshake-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: PaidHandshake Exchange API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: paidhandshake-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 68.0
    catalog_earned_first_party: 8.0
    catalog_gap: 47.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 55.3
    developer_ergonomics: 42.3
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Paidhandshake Authentication
  slug: paidhandshake-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paidhandshake Domain Security
  slug: paidhandshake-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: paidhandshake-search-unlock-checkout
  slug: paidhandshake-search-unlock-checkout
slug: paidhandshake
tags:
- Company
- Artificial Intelligence
- Marketplace
- Data
- Automation
website: https://paidhandshake.com
---
