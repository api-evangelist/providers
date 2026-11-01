---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 15
  human_in_the_loop: 3
  name: Bubblio Dev Agentic Access
  operation_count: 27
  slug: bubblio-dev-agentic-access
  summary_line: 27 operations · 15 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.bubblio.dev
  baseurl_source: declared
  description: Managed agent keys — minted by the platform's server for its signed-in users.
  name: bubblio-dev Agent Keys API
  slug: bubblio-dev-agent-keys-api
- baseURL: https://api.bubblio.dev
  baseurl_source: declared
  description: The phone-first consent pages' API (bubblio.dev/a/{id} and /approvals).
  name: bubblio-dev Approvals API
  slug: bubblio-dev-approvals-api
- baseURL: https://api.bubblio.dev
  baseurl_source: declared
  description: Credential-free discovery — directory, manifests, llms.txt signposts.
  name: bubblio-dev Discovery API
  slug: bubblio-dev-discovery-api
- baseURL: https://api.bubblio.dev
  baseurl_source: declared
  description: 'The MCP endpoints. Minimal, hand-rolled, STATELESS Streamable-HTTP servers: POST one JSON-RPC 2.0 message per request, receive one `application/json` response (legal per the MCP spec — no SSE, no sess'
  name: bubblio-dev MCP API
  slug: bubblio-dev-mcp-api
- baseURL: https://api.bubblio.dev
  baseurl_source: declared
  description: Signed platform → Bubblio pushes (late results, payment-link settlements).
  name: bubblio-dev Platform Push API
  slug: bubblio-dev-platform-push-api
- baseURL: https://api.bubblio.dev
  baseurl_source: declared
  description: The code-declared action registry sync (shapes only, never policy).
  name: bubblio-dev Platform Sync API
  slug: bubblio-dev-platform-sync-api
artifact_total: 23
asyncapis:
- description: ''
  name: Bubblio Dev Webhooks
  slug: bubblio-dev-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/bubblio-dev/agentic-access/bubblio-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bubblio-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bubblio-dev/rules/bubblio-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/bubblio-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/bubblio-dev/json-ld/bubblio-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bubblio-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/bubblio-dev/vocabulary/bubblio-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bubblio-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bubblio-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bubblio-dev/asyncapi/bubblio-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bubblio-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bubblio-dev/data-model/bubblio-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bubblio-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bubblio-dev/changelog/bubblio-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bubblio-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/bubblio-dev/authentication/bubblio-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bubblio-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/bubblio-dev/errors/bubblio-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bubblio-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bubblio-dev/conformance/bubblio-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bubblio-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bubblio-dev/llms/bubblio-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bubblio-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/bubblio-dev/mcp/bubblio-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bubblio-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bubblio-dev/mcp/bubblio-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bubblio-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/bubblio-dev/hosts/bubblio-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bubblio-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/bubblio-dev/vendors/bubblio-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bubblio-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bubblio.dev/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://bubblio.dev/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bubblio.dev/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://bubblio.dev/docs/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://bubblio.dev/docs/api
- group: auth
  href: https://artifacts.apis.io/bubblio-dev/security/bubblio-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bubblio-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bubblio.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://bubblio.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://bubblio.dev/blog
- group: start
  title: ''
  type: SignUp
  url: https://bubblio.dev/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://bubblio.dev/docs
created: '2026-10-29'
description: Bubblio provides an AI‑agent gateway that lets agents discover, negotiate, and pay for services on your platform with human‑approved consent. It includes a public directory, passkey‑based consent flow, exact‑once Stripe payments, tiered free and pro plans, and a machine‑readable llms.txt summary. The API hub is reachable at https://api.bubblio.dev/agent/hub/mcp, and the platform emphasizes transparent pricing and honest accounting.
image: https://bubblio.dev/opengraph-image.png?321b57904a27d711
json_schemas:
- name: AgentKeyInfo
  property_count: 7
  slug: bubblio-dev-agent-key-info
- name: DoorId
  property_count: 0
  slug: bubblio-dev-door-id
- name: JsonRpcRequest
  property_count: 4
  slug: bubblio-dev-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: bubblio-dev-json-rpc-response
- name: PaymentSummary
  property_count: 4
  slug: bubblio-dev-payment-summary
- name: QuoteId
  property_count: 0
  slug: bubblio-dev-quote-id
jsonld:
- class_count: 9
  name: Bubblio Dev Context
  property_count: 49
  slug: bubblio-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.bubblio.dev.
  name: bubblio-dev MCP Server
  slug: bubblio-dev-mcp-yml
modified: '2026-10-29'
name: bubblio-dev
nav: Providers
network: true
overview: 'bubblio-dev publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Keys API, Approvals API, Discovery API, and 3 more. Tagged areas include AI, Payments, Automation, Platform, and Agents.


  The bubblio-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  bubblio-dev''s developer surface includes changelog, authentication, API reference, documentation, engineering blog, signup flow, getting-started guide, and 20 more developer resources.'
plans:
- name: Bubblio Dev Plans Pricing
  plan_count: 0
  slug: bubblio-dev-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Bubblio Dev Rate Limits
  slug: bubblio-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: bubblio-dev API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 2
  slug: bubblio-dev-rules
scopes:
- name: Bubblio Dev Scopes
  scope_count: 0
  slug: bubblio-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 69.7
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bubblio Dev Authentication
  slug: bubblio-dev-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Bubblio Dev Domain Security
  slug: bubblio-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: discover-doors
  slug: bubblio-dev-discover-doors
slug: bubblio-dev
tags:
- AI
- Payments
- Automation
- Platform
- Agents
website: https://bubblio.dev/
---
