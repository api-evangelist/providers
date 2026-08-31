---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: GraphQL API exposing occupancy and space-utilization insights across sites, buildings, floors, zones, and groups. Available to customers with an active contract; authenticated with OAuth 2.0 client cr
  name: InnerSpace API v2
  slug: innerspace-api-v2
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://innerspace.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.innerspace.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.innerspace.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.innerspace.io/api-reference-v2
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.innerspace.io/master
- group: auth
  title: ''
  type: Authentication
  url: authentication/innerspace-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.innerspace.io
- group: commercial
  title: ''
  type: Pricing
  url: https://innerspace.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://innerspace.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.innerspace.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://innerspace.io/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://innerspace.io/trust
- group: auth
  title: ''
  type: Compliance
  url: https://innerspace.io/trust
- group: auth
  title: ''
  type: Security
  url: https://www.innerspace.io/responsible-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/innerspace-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/innerspace-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/innerspace-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/innerspace-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/innerspace-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/innerspace-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/innerspace-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/innerspace-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/innerspace-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/innerspace-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/innerspace-mcp.yml
created: '2026-07-17'
description: InnerSpace (InnerSpace Technologies Inc.) is a workplace analytics company that measures how physical space is used by leveraging a building's existing Wi-Fi infrastructure rather than dedicated occupancy sensors. Its patented Predictive Hyperbolic Location Fingerprinting (PHLF) technology locates and counts people to within roughly four feet to reveal occupancy, movement, and space-utilization patterns across sites, buildings, floors, and zones. The InnerSpace platform serves hybrid-workplace management, real-estate portfolio optimization, higher-education, and employee-experience use cases for enterprises including Microsoft, KPMG, Indeed, and LinkedIn. A GraphQL API (v2) at api.innerspace.io exposes building, zone, site, floor, group, and insights data to customers with active contracts, authenticated via an OAuth 2.0 client-credentials exchange that returns a session token.
image: https://innerspace.io/hubfs/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: InnerSpace MCP Server
  slug: innerspace-mcp-server
modified: '2026-07-19'
name: InnerSpace
nav: Providers
network: true
overview: 'InnerSpace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workplace Analytics, Occupancy, Space Utilization, and Real-Estate.


  InnerSpace''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, support, and 18 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 33.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/innerspace/refs/heads/main/screenshots/innerspace-2026-07-25T222456.png
security:
- kind: authentication
  name: Innerspace Authentication
  slug: innerspace-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Innerspace Domain Security
  slug: innerspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Innerspace Vulnerability Disclosure
  slug: innerspace-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Innerspace Trust Center
  slug: innerspace-trust-center
  summary_line: SOC 2, ISO 27001
slug: innerspace
tags:
- Company
- Workplace Analytics
- Occupancy
- Space Utilization
- Real-Estate
- Wi-Fi Location
- Building Insights
- GraphQL
- Hybrid Workplace
- PropTech
website: https://innerspace.io
---
