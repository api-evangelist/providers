---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: An OAuth-protected Model Context Protocol (MCP) server operated by Cerapedics at mcp.cerapedics.com. The endpoint publishes RFC 9728 protected-resource metadata and RFC 8414 authorization-server metad
  name: Cerapedics MCP Server
  slug: cerapedics-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.cerapedics.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cerapedics-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cerapedics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerapedics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cerapedics-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cerapedics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cerapedics-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerapedics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cerapedics-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.cerapedics.com/news-and-events/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cerapedics.com/rss.xml
- group: operate
  title: ''
  type: Contact
  url: https://www.cerapedics.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cerapedics.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cerapedics.com/terms-of-use
- group: company
  title: ''
  type: Careers
  url: https://www.cerapedics.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cerapedics
- group: company
  title: ''
  type: Twitter
  url: https://x.com/CerapedicsInc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cerapedics_stock/
created: '2026-08-02'
description: Cerapedics is a global, commercial-stage orthobiologics company headquartered in Westminster, Colorado, that develops and commercializes bone repair products built on its proprietary P-15 synthetic small peptide technology — an osteogenic cell-binding peptide discovered in 1996. Its FDA premarket-approved (PMA) products are i-FACTOR Peptide Enhanced Bone Graft, approved in 2015 for single-level anterior cervical discectomy and fusion (ACDF), and PearlMatrix P-15 Peptide Enhanced Bone Graft, approved in 2025 for single-level transforaminal lumbar interbody fusion (TLIF). Cerapedics publishes no public developer program, OpenAPI definition or SDKs; the only machine-readable surface discovered by the API Evangelist enrichment pipeline is an OAuth-protected Model Context Protocol (MCP) server at mcp.cerapedics.com, gated behind the company's Microsoft Entra ID tenant.
image: https://www.cerapedics.com/sites/default/files/styles/large/public/2024-11/cerapedics-logo_0.png
layout: provider
mcp_servers:
- description: ''
  name: Cerapedics MCP Server
  slug: cerapedics-mcp-server
modified: '2026-08-02'
name: Cerapedics
nav: Providers
network: true
overview: 'Cerapedics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Orthopedics, Orthobiologics, and Bone Graft.


  Cerapedics'' developer surface includes authentication, engineering blog, and 16 more developer resources.'
random_paper: 14
scopes:
- name: Cerapedics Scopes
  scope_count: 4
  slug: cerapedics-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cerapedics/refs/heads/main/screenshots/cerapedics-2026-08-07T163308.png
security:
- kind: authentication
  name: Cerapedics Authentication
  slug: cerapedics-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cerapedics Domain Security
  slug: cerapedics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cerapedics
tags:
- Company
- Medical Devices
- Orthopedics
- Orthobiologics
- Bone Graft
- Spine Surgery
- Healthcare
- Life Sciences
- MCP
website: https://www.cerapedics.com/
---
