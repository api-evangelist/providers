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
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-10-17'
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
artifact_total: 20
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/agentic-access/paidhandshake-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paidhandshake-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/plans/paidhandshake-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/paidhandshake-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/rules/paidhandshake-rules.yml
  title: ''
  type: Spectral
  url: rules/paidhandshake-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/json-ld/paidhandshake-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/paidhandshake-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/vocabulary/paidhandshake-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/paidhandshake-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/data-model/paidhandshake-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paidhandshake-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/conventions/paidhandshake-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/paidhandshake-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/conventions/paidhandshake-conventions.yml
  title: ''
  type: Conventions
  url: conventions/paidhandshake-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/errors/paidhandshake-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paidhandshake-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/conformance/paidhandshake-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paidhandshake-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/llms/paidhandshake-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paidhandshake-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/a2a/paidhandshake-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/paidhandshake-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/mcp/paidhandshake-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/paidhandshake-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/mcp/paidhandshake-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/paidhandshake-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/well-known/paidhandshake-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paidhandshake-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/hosts/paidhandshake-hosts.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/authentication/paidhandshake-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paidhandshake-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paidhandshake/refs/heads/main/security/paidhandshake-domain-security.yml
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


  PaidHandshake Exchange''s developer surface includes API reference, authentication, documentation, getting-started guide, and 22 more developer resources.'
plans:
- name: Paidhandshake Plans Pricing
  plan_count: 1
  slug: paidhandshake-plans-pricing
random_paper: 7
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
  composite: 45.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.0
    catalog_earned_first_party: 8.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 19.7
    contract_quality: 55.3
    developer_ergonomics: 42.3
    discoverability: 66.7
    operational_transparency: 0.0
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Paidhandshake Authentication
  slug: paidhandshake-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paidhandshake Domain Security
  slug: paidhandshake-domain-security
  summary_line: TLSv1.3 · DMARC
slug: paidhandshake
tags:
- Company
- Artificial Intelligence
- Marketplace
- Data
- Automation
website: https://paidhandshake.com
---
