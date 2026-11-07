---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Proof signing API that provides cryptographic receipts for agent calls. Offers a free tier with 500 proofs/month.
  name: ArkForge Trust Layer API
  slug: arkforge-trust-layer-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/arkforge-tech/rate-limits/arkforge-tech-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arkforge-tech-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/arkforge-tech/plans/arkforge-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arkforge-tech-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/arkforge-tech/changelog/arkforge-tech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/arkforge-tech-changelog.yml
- group: start
  href: https://artifacts.apis.io/arkforge-tech/sandbox/arkforge-tech-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/arkforge-tech-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/arkforge-tech/authentication/arkforge-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arkforge-tech-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://arkforge.tech/en/status.html
- group: design
  href: https://artifacts.apis.io/arkforge-tech/lifecycle/arkforge-tech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/arkforge-tech-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/arkforge-tech/errors/arkforge-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arkforge-tech-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/arkforge-tech/llms/arkforge-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arkforge-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/arkforge-tech/mcp/arkforge-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arkforge-tech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/arkforge-tech/well-known/arkforge-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arkforge-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/arkforge-tech/hosts/arkforge-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arkforge-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/arkforge-tech/vendors/arkforge-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arkforge-tech-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.arkforge.tech/
- group: auth
  href: https://artifacts.apis.io/arkforge-tech/security/arkforge-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arkforge-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arkforge.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://arkforge.tech/en/trust-layer.html
- group: docs
  title: ''
  type: APIReference
  url: https://arkforge.tech/en/eu-ai-act-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://arkforge.tech/en/signup.html
- group: operate
  title: ''
  type: Support
  url: https://arkforge.tech/en/support.html
- group: company
  title: ''
  type: Blog
  url: https://arkforge.tech/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ark-forge
- group: commercial
  title: ''
  type: Pricing
  url: https://arkforge.tech/en/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arkforge.tech/en/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arkforge.tech/en/privacy.html
coverage:
  checked: '2026-11-02'
  detail: Provider documentation describes API endpoints but no machine-readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is available.
  evidence:
  - status: 404
    url: https://trust.arkforge.tech/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ArkForge builds verifiable infrastructure for AI agents. Its Trust Layer is a certifying proxy that fingerprints, signs, and timestamps every agent transaction, generating cryptographic proofs anchored by RFC 3161 timestamps and Sigstore Rekor entries. The mission is to ensure autonomous AI agents' economic actions are independently verifiable, offering proof specifications (JSON, HTTP headers, HTML) and free and paid plans. ArkForge is a French company focused on trust and auditability for the AI economy.
image: https://arkforge.tech/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.arkforge.tech requiring an API key.
  name: ArkForge MCP Server
  slug: arkforge-tech-mcp-yml
modified: '2026-11-01'
name: ArkForge
nav: Providers
network: true
overview: 'ArkForge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Trust, Verification, Infrastructure, and Security.


  ArkForge''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Arkforge Tech Plans Pricing
  plan_count: 3
  slug: arkforge-tech-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Arkforge Tech Rate Limits
  slug: arkforge-tech-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 36.9
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 40.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arkforge Tech Authentication
  slug: arkforge-tech-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arkforge Tech Domain Security
  slug: arkforge-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arkforge-tech
tags:
- Artificial Intelligence
- Trust
- Verification
- Infrastructure
- Security
website: https://arkforge.tech/
---
