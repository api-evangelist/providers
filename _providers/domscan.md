---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST domain-intelligence API (40+ endpoints under /v1) for availability, DNS, WHOIS/RDAP, SSL/TLS, email auth, valuation, security, and OSINT, with API-key authentication.
  name: DomScan API
  slug: domscan-api
artifact_total: 9
asyncapis:
- description: ''
  name: Domscan Webhooks
  slug: domscan-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://domscan.net
- group: auth
  title: ''
  type: DomainSecurity
  url: security/domscan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/domscan-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/domscan-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/domscan-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/domscan-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/domscan-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/domscan-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/domscan-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/domscan-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/domscan-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/domscan-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/domscan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/domscan-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/domscan-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/domscan-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/domscan-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/domscan-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/domscan-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/domscan-openapi-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://domscan.net/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://domscan.net/quickstart
- group: company
  title: ''
  type: Blog
  url: https://domscan.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://domscan.net/pricing
- group: start
  title: ''
  type: SignUp
  url: https://domscan.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domscan.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domscan.net/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/estevecastells
created: '2026-07-12'
description: Domain intelligence API for domain availability, DNS, WHOIS/RDAP, valuation, security checks, email posture, social handle checks, and monitoring workflows. Offers REST API, machine-readable contracts, a hosted MCP server, and llms.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/domscan.png
layout: provider
mcp_servers:
- description: ''
  name: DomScan MCP Server
  slug: domscan-mcp-server
- description: Official hosted remote MCP server exposing 136 domain-intelligence tools (domain search, DNS, web intelligence, security, identity, monitoring, and workflow recipes) over Streamable HTTP. Works with C
  name: DomScan MCP Server
  slug: domscan-mcp-server-2
modified: '2026-09-03'
name: DomScan
nav: Providers
network: true
overview: 'DomScan publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Domains, DNS, WHOIS, rdap, and SSL/TLS.


  The DomScan catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DomScan''s developer surface includes authentication, changelog, CLI, API reference, getting-started guide, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Domscan Plans Pricing
  plan_count: 4
  slug: domscan-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Domscan Rate Limits
  slug: domscan-rate-limits
scopes:
- name: Domscan Scopes
  scope_count: 1
  slug: domscan-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 40.6
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 60.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 15.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/screenshots/domscan-2026-07-25T212249.png
security:
- kind: authentication
  name: Domscan Authentication
  slug: domscan-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Domscan Domain Security
  slug: domscan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: domscan
tags:
- Domains
- DNS
- WHOIS
- rdap
- SSL/TLS
- Email Security
- domain-valuation
- Brand Protection
- OSINT
- Threat Intelligence
- MCP
- agent-native
website: https://domscan.net
---
