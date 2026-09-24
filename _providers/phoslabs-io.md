---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Phoslabs Io Agentic Access
  operation_count: 7
  slug: phoslabs-io-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- baseURL: https://phoslabs.io/api/v1
  baseurl_source: declared
  description: Bearer-key JSON REST API on phoslabs.io. The provider-published OpenAPI 3.0.3 (verbatim in openapi/) declares seven operations — six metered POST tools (audit 0 credits, diagnose 10, fixCheckout 30, c
  name: Behavioral Science API
  slug: behavioral-science-api
- description: 'Hosted, remote Model Context Protocol server. POST https://mcp.phoslabs.io/mcp is Streamable HTTP behind OAuth 2.1: the 401 challenge names RFC 9728 protected-resource metadata, whose authorization se'
  name: Phos Labs MCP Server
  slug: phos-labs-mcp-server
artifact_total: 9
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/llms/phoslabs-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phoslabs-io-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/a2a/phoslabs-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/phoslabs-io-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/well-known/phoslabs-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phoslabs-io-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/mcp/phoslabs-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/phoslabs-io-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/mcp/phoslabs-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/phoslabs-io-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/packages/phoslabs-io-packages.yml
  title: ''
  type: Packages
  url: packages/phoslabs-io-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/authentication/phoslabs-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phoslabs-io-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/scopes/phoslabs-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/phoslabs-io-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/conventions/phoslabs-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/phoslabs-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/errors/phoslabs-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/phoslabs-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/lifecycle/phoslabs-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/phoslabs-io-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/conformance/phoslabs-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phoslabs-io-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/data-model/phoslabs-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/phoslabs-io-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/overlays/phoslabs-io-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/phoslabs-io-openapi-overlay.yaml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/rate-limits/phoslabs-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/phoslabs-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/plans/phoslabs-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/phoslabs-io-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/agentic-access/phoslabs-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/phoslabs-io-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/security/phoslabs-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phoslabs-io-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/regulatory/phoslabs-io-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/phoslabs-io-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/regulatory/phoslabs-io-regulatory-posture.yml
  title: ''
  type: Subprocessors
  url: regulatory/phoslabs-io-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phoslabs-io/refs/heads/main/regulatory/phoslabs-io-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/phoslabs-io-regulatory-posture.yml
created: '2026-09-19'
description: 'Phos Labs is an independent studio that sells behavioral-science "commerce intelligence" to AI agents: diagnose where a funnel loses customers, redesign a checkout, rewrite offer copy, optimize price framing and detect cognitive biases. The surface is a Bearer-key REST API at phoslabs.io/api/v1 (OpenAPI 3.0.3, 7 operations, an anonymous tool-and-price listing) and a hosted MCP server at mcp.phoslabs.io behind OAuth 2.1 with RFC 8414 / RFC 9728 discovery and dynamic client registration, listed twice in the official MCP registry and described by an A2A-shaped agent card with nine skills. Billing is prepaid credits (1 credit = EUR 0.01) debited per call, with x402 USDC micropayments stated but not verifiable. The same domain also hosts Mind of Granite, a consumer decision-guidance product.'
image: https://phoslabs.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Phos Labs Commerce Intelligence
  slug: phos-labs-commerce-intelligence
modified: '2026-09-19'
name: Phos Labs
nav: Providers
network: true
overview: 'Phos Labs publishes 1 API on the [APIs.io](https://apis.io/) network: Behavioral Science API. Tagged areas include Company, Behavioral Science, Conversion Optimization, E-Commerce, and Pricing.


  Phos Labs'' developer surface includes documentation, API reference, getting-started guide, pricing, support, authentication, and 25 more developer resources.'
plans:
- name: Phoslabs Io Plans Pricing
  plan_count: 4
  slug: phoslabs-io-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Phoslabs Io Rate Limits
  slug: phoslabs-io-rate-limits
scopes:
- name: Phoslabs Io Scopes
  scope_count: 1
  slug: phoslabs-io-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 47.0
    discoverability: 68.5
    operational_transparency: 5.3
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Phoslabs Io Authentication
  slug: phoslabs-io-authentication
  summary_line: http/oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Phoslabs Io Domain Security
  slug: phoslabs-io-domain-security
  summary_line: TLSv1.3 · DMARC
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
