---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Phoslabs Io Agentic Access
  operation_count: 7
  slug: phoslabs-io-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- description: 'Hosted, remote Model Context Protocol server. POST https://mcp.phoslabs.io/mcp is Streamable HTTP behind OAuth 2.1: the 401 challenge names RFC 9728 protected-resource metadata, whose authorization se'
  name: Phos Labs MCP Server
  slug: phos-labs-mcp-server
- baseURL: https://phoslabs.io/api/v1
  baseurl_source: declared
  description: The Audit API from Phos Labs — 1 operation(s) for audit.
  name: Phos Labs Audit API
  slug: phoslabs-io-audit-api
- baseURL: https://phoslabs.io/api/v1
  baseurl_source: declared
  description: The Copy API from Phos Labs — 1 operation(s) for copy.
  name: Phos Labs Copy API
  slug: phoslabs-io-copy-api
- baseURL: https://phoslabs.io/api/v1
  baseurl_source: declared
  description: The Detect Biases API from Phos Labs — 1 operation(s) for detect biases.
  name: Phos Labs Detect Biases API
  slug: phoslabs-io-detect-biases-api
- baseURL: https://phoslabs.io/api/v1
  baseurl_source: declared
  description: The Diagnose API from Phos Labs — 1 operation(s) for diagnose.
  name: Phos Labs Diagnose API
  slug: phoslabs-io-diagnose-api
- baseURL: https://phoslabs.io/api/v1
  baseurl_source: declared
  description: The Fix Checkout API from Phos Labs — 1 operation(s) for fix checkout.
  name: Phos Labs Fix Checkout API
  slug: phoslabs-io-fix-checkout-api
- baseURL: https://phoslabs.io/api/v1
  baseurl_source: declared
  description: The Pricing API from Phos Labs — 1 operation(s) for pricing.
  name: Phos Labs Pricing API
  slug: phoslabs-io-pricing-api
- baseURL: https://phoslabs.io/api/v1
  baseurl_source: declared
  description: The Tools API from Phos Labs — 1 operation(s) for tools.
  name: Phos Labs Tools API
  slug: phoslabs-io-tools-api
artifact_total: 20
common:
- group: other
  href: https://artifacts.apis.io/phoslabs-io/capabilities/phoslabs-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/phoslabs-io-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/phoslabs-io/skills/phoslabs-io-diagnose-and-fix-a-funnel.md
  title: ''
  type: AgentSkill
  url: skills/phoslabs-io-diagnose-and-fix-a-funnel.md
- group: agent
  href: https://artifacts.apis.io/phoslabs-io/skills/phoslabs-io-price-and-write-an-offer.md
  title: ''
  type: AgentSkill
  url: skills/phoslabs-io-price-and-write-an-offer.md
- group: company
  title: ''
  type: Website
  url: https://phoslabs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/phoslabs/behavioral-science-api
- group: docs
  title: ''
  type: APIReference
  url: https://phoslabs.io/api/v1/tools
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/phoslabs/behavioral-science-api#quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://phoslabs.io/credits
- group: operate
  title: ''
  type: Support
  url: mailto:support@phoslabs.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phoslabs.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phoslabs.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phoslabs
- group: agent
  href: https://artifacts.apis.io/phoslabs-io/llms/phoslabs-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phoslabs-io-llms.txt
- group: other
  href: https://artifacts.apis.io/phoslabs-io/a2a/phoslabs-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/phoslabs-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/phoslabs-io/well-known/phoslabs-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phoslabs-io-well-known.yml
- group: agent
  href: https://artifacts.apis.io/phoslabs-io/mcp/phoslabs-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/phoslabs-io-mcp.yml
- group: build
  href: https://artifacts.apis.io/phoslabs-io/mcp/phoslabs-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/phoslabs-io-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/phoslabs-io/packages/phoslabs-io-packages.yml
  title: ''
  type: Packages
  url: packages/phoslabs-io-packages.yml
- group: auth
  href: https://artifacts.apis.io/phoslabs-io/authentication/phoslabs-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phoslabs-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/phoslabs-io/scopes/phoslabs-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/phoslabs-io-scopes.yml
- group: design
  href: https://artifacts.apis.io/phoslabs-io/conventions/phoslabs-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/phoslabs-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/phoslabs-io/errors/phoslabs-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/phoslabs-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/phoslabs-io/lifecycle/phoslabs-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/phoslabs-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/phoslabs-io/conformance/phoslabs-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phoslabs-io-conformance.yml
- group: design
  href: https://artifacts.apis.io/phoslabs-io/data-model/phoslabs-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/phoslabs-io-data-model.yml
- group: other
  href: https://artifacts.apis.io/phoslabs-io/overlays/phoslabs-io-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/phoslabs-io-openapi-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/phoslabs-io/rate-limits/phoslabs-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/phoslabs-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/phoslabs-io/plans/phoslabs-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/phoslabs-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/phoslabs-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/phoslabs-io/agentic-access/phoslabs-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/phoslabs-io-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/phoslabs-io/security/phoslabs-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phoslabs-io-domain-security.yml
- group: other
  href: https://artifacts.apis.io/phoslabs-io/regulatory/phoslabs-io-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/phoslabs-io-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/phoslabs-io/regulatory/phoslabs-io-regulatory-posture.yml
  title: ''
  type: Subprocessors
  url: regulatory/phoslabs-io-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/phoslabs-io/regulatory/phoslabs-io-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/phoslabs-io-regulatory-posture.yml
created: '2026-09-19'
description: 'Phos Labs is an independent studio that sells behavioral-science "commerce intelligence" to AI agents: diagnose where a funnel loses customers, redesign a checkout, rewrite offer copy, optimize price framing and detect cognitive biases. The surface is a Bearer-key REST API at phoslabs.io/api/v1 (OpenAPI 3.0.3, 7 operations, an anonymous tool-and-price listing) and a hosted MCP server at mcp.phoslabs.io behind OAuth 2.1 with RFC 8414 / RFC 9728 discovery and dynamic client registration, listed twice in the official MCP registry and described by an A2A-shaped agent card with nine skills. Billing is prepaid credits (1 credit = EUR 0.01) debited per call, with x402 USDC micropayments stated but not verifiable. The same domain also hosts Mind of Granite, a consumer decision-guidance product.'
finops:
- has_sources: true
  method: derived
  name: Phoslabs Io Finops
  primary_unit: pack
  service_category: ''
  slug: phoslabs-io-finops
  template: false
image: https://phoslabs.io/favicon.ico
layout: provider
mcp_servers:
- description: 'Phos Labs ships a hosted, remote MCP server on mcp.phoslabs.io and lists it twice in the official MCP registry: io.phoslabs/commerce-intelligence (4.0.0, streamable-http, remote url https://mcp.phosla'
  name: Phos Labs Commerce Intelligence
  slug: phos-labs-commerce-intelligence
modified: '2026-09-19'
name: Phos Labs
nav: Providers
network: true
overview: 'Phos Labs publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit API, Copy API, Detect Biases API, and 5 more. Tagged areas include Company, Behavioral Science, Conversion Optimization, E-Commerce, and Pricing.


  The Phos Labs catalog on APIs.io includes 1 Spectral governance ruleset.


  Phos Labs'' developer surface includes documentation, API reference, getting-started guide, pricing, support, authentication, and 28 more developer resources.'
plans:
- name: Phoslabs Io Plans Pricing
  plan_count: 3
  slug: phoslabs-io-plans-pricing
- name: Phoslabs Io Price Estimates
  plan_count: 0
  slug: phoslabs-io-price-estimates
random_paper: 17
rate_limits:
- limit_count: 0
  name: Phoslabs Io Rate Limits
  slug: phoslabs-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Phos Labs API Rules
  rule_count: 54
  severity_counts:
    error: 51
    hint: 0
    info: 2
    warn: 1
  slug: phoslabs-io-rules
scopes:
- name: Phoslabs Io Scopes
  scope_count: 1
  slug: phoslabs-io-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 55.4
    developer_ergonomics: 32.7
    discoverability: 68.3
    operational_transparency: 2.6
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/phoslabs-io/phoslabs-io-2026-10-11T112547.png
security:
- kind: authentication
  name: Phoslabs Io Authentication
  slug: phoslabs-io-authentication
  summary_line: http/oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Phoslabs Io Domain Security
  slug: phoslabs-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Diagnose a funnel drop-off and redesign the checkout
  slug: phoslabs-io-diagnose-and-fix-a-funnel
- name: Price an offer and write the copy for it
  slug: phoslabs-io-price-and-write-an-offer
slug: phoslabs-io
tags:
- Company
- Behavioral Science
- Conversion Optimization
- E-Commerce
- Pricing
- Copywriting
- AI Agents
- MCP
- A2A
- Decision Intelligence
- Agentic Commerce
website: https://phoslabs.io/
---
