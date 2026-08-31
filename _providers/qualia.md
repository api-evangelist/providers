---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Qualia API is a read-write GraphQL API over the Qualia title, escrow and closing platform. It lets partner organizations place title orders into Qualia Core or Connect (or route them to third-part
  name: Qualia API
  slug: qualia-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qualia-mcp.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qualia-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.qualia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.qualia.com/qualia-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.qualia.com/api-u
- group: operate
  title: ''
  type: Support
  url: https://help.qualia.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.qualia.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.qualia.com/rss/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qualialabs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qualia.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://connect.qualia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qualia.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qualia.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qualia.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.qualia.com/api-terms/
- group: auth
  title: ''
  type: Security
  url: https://www.qualia.com/.well-known/security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.qualia.com/trust/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qualia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/qualia-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qualia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qualia-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qualia-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qualia-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qualia-llms.txt
created: '2026-08-02'
description: Qualia (Qualia Labs, Inc.) is a digital real estate closing platform whose cloud-based title, escrow and settlement software brings title agents, lenders, real estate agents and consumers onto one secure system of record. Its product family spans Core (title and escrow production), Connect (the secure closing portal for lenders, agents and consumers), Shield (wire-fraud detection, identity verification and insured wire transfers), Marketplace (vendor and title-search ordering), Assure (underwriter management), Atlas (enterprise title and escrow), Clear (an agentic AI system for title production) and Resware (customizable title production). The Qualia API, launched in August 2022, is a read-write GraphQL interface at api.qualia.com/graphql that lets proptech companies, lenders and enterprise title operations place and track title orders, exchange messages and documents, and pull order, accounting and contact data for custom reporting and executive dashboards. Access is organized
  by capability gates granted per organization and authenticated with HTTP Basic credentials.
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/company-logos/qualia.png
layout: provider
mcp_servers:
- description: ''
  name: Qualia MCP Server
  slug: qualia-mcp-server
modified: '2026-08-02'
name: Qualia
nav: Providers
network: true
overview: 'Qualia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, Title Insurance, Escrow, and Mortgage.


  Qualia''s developer surface includes getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 35.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Qualia Authentication
  slug: qualia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qualia Domain Security
  slug: qualia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qualia Vulnerability Disclosure
  slug: qualia-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Qualia Trust Center
  slug: qualia-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ALTA Best Practices Pillar 3
slug: qualia
tags:
- Company
- Real-Estate
- Title Insurance
- Escrow
- Mortgage
- Closing
- Settlement Services
- PropTech
- Financial-Services
- GraphQL
website: https://www.qualia.com/
---
