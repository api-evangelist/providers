---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Live Model Context Protocol server operated by ServiceUp at api.serviceup.com/mcp, exposing the agentic repair platform to MCP clients. The endpoint is protected by OAuth 2.1 (authorization code + PKC
  name: ServiceUp MCP Server
  slug: serviceup-mcp-server
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/serviceup-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serviceup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.serviceup.com/
- group: start
  title: ''
  type: Login
  url: https://app.serviceup.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.serviceup.com/company/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.serviceup.com/company/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.serviceup.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.serviceup.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ServiceUpAuto
- group: auth
  title: ''
  type: Compliance
  url: https://trust.serviceup.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/serviceup-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/serviceup-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/serviceup-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/serviceup-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/serviceup-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/serviceup-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/serviceup-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/serviceup-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/serviceup-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/serviceup-llms.txt
created: '2026-08-05'
description: ServiceUp is an agentic vehicle repair and maintenance platform for commercial fleets, insurance carriers and repair shops, founded in 2021 and headquartered in Los Gatos, California. The platform centralizes the full repair lifecycle — intake, shop routing, estimate and invoice approval, repair status tracking and payment — across collision, mechanical and preventative maintenance work, and layers AI Repair Agents over it that run in manual, co-pilot or autopilot control modes. ServiceUp integrates with existing fleet management systems, telematics providers and rental management systems, and operates a live, OAuth-2.1-protected Model Context Protocol (MCP) server at api.serviceup.com/mcp for agent access. The company raised a $55M Series B and ranked 77th on the 2025 Inc. 5000 list.
image: https://cdn.prod.website-files.com/65dfc331994523c04b3fbb30/6a3c44c69acc55aa24cf9bb7_7125858b1dfb99cd458a33c165bd452b_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: ServiceUp MCP Server
  slug: serviceup-mcp-server
modified: '2026-08-05'
name: ServiceUp
nav: Providers
network: true
overview: 'ServiceUp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet Management, Vehicle Repair, Automotive, and Insurance.


  ServiceUp''s developer surface includes engineering blog, support, authentication, and 17 more developer resources.'
random_paper: 16
scopes:
- name: Serviceup Scopes
  scope_count: 3
  slug: serviceup-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 28.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/serviceup/refs/heads/main/screenshots/serviceup-2026-09-02T155016.png
security:
- kind: authentication
  name: Serviceup Authentication
  slug: serviceup-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Serviceup Domain Security
  slug: serviceup-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Serviceup Trust Center
  slug: serviceup-trust-center
  summary_line: SOC 2, ISO 27001
slug: serviceup
tags:
- Company
- Fleet Management
- Vehicle Repair
- Automotive
- Insurance
- Maintenance
- Agentic AI
- MCP
- Transportation
website: https://www.serviceup.com/
---
