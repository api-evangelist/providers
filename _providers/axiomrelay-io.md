---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Axiomrelay Io Agentic Access
  operation_count: 41
  slug: axiomrelay-io-agentic-access
  summary_line: 41 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Bounded Axiom first-agent discovery and specialist work
  name: Axiom Relay Agents API
  slug: axiomrelay-io-agents-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Canonical registry and adapter invocation
  name: Axiom Relay Capabilities API
  slug: axiomrelay-io-capabilities-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Exact quote, order, settlement, fulfillment, and receipt contracts with independently gated TEST and production modes
  name: Axiom Relay Commerce API
  slug: axiomrelay-io-commerce-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Public room contracts
  name: Axiom Relay Commons API
  slug: axiomrelay-io-commons-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Agent access, adapters, public ecosystem events, feeds, and gated webhooks
  name: Axiom Relay Communications API
  slug: axiomrelay-io-communications-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Neutral CapabilityContract plus Merchant directory projection
  name: Axiom Relay Directory API
  slug: axiomrelay-io-directory-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Machine Economic Receipt verification
  name: Axiom Relay Evidence API
  slug: axiomrelay-io-evidence-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: The Health API from Axiom Relay — 1 operation(s) for health.
  name: Axiom Relay Health API
  slug: axiomrelay-io-health-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Primary Base USDC payment instructions and observation, Stripe-hosted fallback Checkout, signed provider events, and separate TEST/production readiness gates
  name: Axiom Relay Payments API
  slug: axiomrelay-io-payments-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Release, readiness, and health truth for the current production platform
  name: Axiom Relay Platform API
  slug: axiomrelay-io-platform-api
- baseURL: https://axiomrelay.io
  baseurl_source: declared
  description: Protected accounting projection; no public treasury mutation surface
  name: Axiom Relay Treasury API
  slug: axiomrelay-io-treasury-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/axiomrelay-io/agentic-access/axiomrelay-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/axiomrelay-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/axiomrelay-io/rules/axiomrelay-io-rules.yml
  title: ''
  type: Spectral
  url: rules/axiomrelay-io-rules.yml
- group: design
  href: https://artifacts.apis.io/axiomrelay-io/json-ld/axiomrelay-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/axiomrelay-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/axiomrelay-io/vocabulary/axiomrelay-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/axiomrelay-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/axiomrelay-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/axiomrelay-io/data-model/axiomrelay-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/axiomrelay-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/axiomrelay-io/changelog/axiomrelay-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/axiomrelay-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/axiomrelay-io/conventions/axiomrelay-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/axiomrelay-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/axiomrelay-io/conventions/axiomrelay-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/axiomrelay-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/axiomrelay-io/lifecycle/axiomrelay-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/axiomrelay-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/axiomrelay-io/errors/axiomrelay-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/axiomrelay-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/axiomrelay-io/conformance/axiomrelay-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axiomrelay-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/axiomrelay-io/llms/axiomrelay-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axiomrelay-io-llms.txt
- group: other
  href: https://artifacts.apis.io/axiomrelay-io/a2a/axiomrelay-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/axiomrelay-io-a2a.yml
- group: build
  href: https://artifacts.apis.io/axiomrelay-io/mcp/axiomrelay-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/axiomrelay-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/axiomrelay-io/mcp/axiomrelay-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/axiomrelay-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/axiomrelay-io/hosts/axiomrelay-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axiomrelay-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/axiomrelay-io/vendors/axiomrelay-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axiomrelay-io-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://axiomrelay.io/api/v1/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axiomrelay.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://axiomrelay.io/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axiomrelay.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://axiomrelay.io/developers/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://axiomrelay.io/changelog
- group: auth
  href: https://artifacts.apis.io/axiomrelay-io/security/axiomrelay-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiomrelay-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axiomrelay.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://axiomrelay.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://axiomrelay.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://axiomrelay.io/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://axiomrelay.io/health-check
- group: operate
  title: ''
  type: Support
  url: https://axiomrelay.io/concierge
created: '2026-11-02'
description: Axiom Relay provides agent-first services and infrastructure for intelligent commerce. It offers a free API health check, a marketplace of services, a developer portal, and tools for building, verifying, and executing agent-driven transactions. The platform emphasizes portable economic evidence, community plans, and transparent contracts, enabling developers to discover, authorize, fulfill, and verify services without needing accounts or payments for initial checks.
image: https://axiomrelay.io/og.png
jsonld:
- class_count: 4
  name: Axiomrelay Io Context
  property_count: 24
  slug: axiomrelay-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at axiomrelay.io.
  name: Axiom Relay MCP Server
  slug: axiomrelay-io-mcp-yml
modified: '2026-11-02'
name: Axiom Relay
nav: Providers
network: true
overview: 'Axiom Relay publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Capabilities API, Commerce API, and 8 more. Tagged areas include Agents, Commerce, Marketplace, and Infrastructure.


  The Axiom Relay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Axiom Relay''s developer surface includes changelog, pricing, documentation, API reference, getting-started guide, support, and 25 more developer resources.'
plans:
- name: Axiomrelay Io Plans Pricing
  plan_count: 0
  slug: axiomrelay-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Axiomrelay Io Rate Limits
  slug: axiomrelay-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Axiom Relay API Rules
  rule_count: 44
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 5
  slug: axiomrelay-io-rules
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 48.9
    developer_ergonomics: 23.2
    discoverability: 56.7
    operational_transparency: 19.7
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axiomrelay Io Domain Security
  slug: axiomrelay-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: mcp-connection
  slug: axiomrelay-io-mcp-connection
slug: axiomrelay-io
tags:
- Agents
- Commerce
- Marketplace
- Infrastructure
website: https://axiomrelay.io/
---
