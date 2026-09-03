---
access_model:
  confidence: high
  label: Requires approval
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.stotles.com/pricing
  - https://www.stotles.com/integrations
  - https://api.stotles.com/v1/openapi.json
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Hosted, remote Model Context Protocol server exposing Stotles public sector market data to AI chat tools and agents. Streamable-HTTP transport at api.stotles.com/mcp, authenticated with the same x-api
  name: Stotles MCP Server
  slug: stotles-mcp-server
- baseURL: https://api.stotles.com/v1
  baseurl_source: declared
  description: Public sector buyers and their procurement activity.
  name: Stotles Buyers API
  slug: stotles-buyers-api
- baseURL: https://api.stotles.com/v1
  baseurl_source: declared
  description: Framework agreements and dynamic purchasing systems.
  name: Stotles Frameworks API
  slug: stotles-frameworks-api
- baseURL: https://api.stotles.com/v1
  baseurl_source: declared
  description: Public sector procurement notices.
  name: Stotles Notices API
  slug: stotles-notices-api
- baseURL: https://api.stotles.com/v1
  baseurl_source: declared
  description: Suppliers bidding for and winning public sector contracts.
  name: Stotles Suppliers API
  slug: stotles-suppliers-api
artifact_total: 12
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/stotles-public-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.stotles.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.stotles.com/
- group: operate
  title: ''
  type: Support
  url: https://help.stotles.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.stotles.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://app.stotles.com/get-started
- group: start
  title: ''
  type: SignUp
  url: https://app.stotles.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.stotles.com/users/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stotles.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.stotles.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stotles.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stotles.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.eu.vanta.com/stotles.com/trust/xpcnkioxgcvk0i3qd7fm
- group: auth
  title: ''
  type: Compliance
  url: https://app.eu.vanta.com/stotles.com/trust/xpcnkioxgcvk0i3qd7fm
- group: design
  title: ''
  type: Conformance
  url: conformance/stotles-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stotles-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stotles-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.stotles.com/llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/stotles-trust-center.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stotles
- group: build
  title: ''
  type: Packages
  url: packages/stotles-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stotles-plans-pricing.yml
created: '2026-07-17'
description: 'Stotles is a B2G (business-to-government) public sector procurement and sales intelligence platform for the UK and Ireland. It aggregates procurement notices, contract awards, framework agreements, buyer spend history, and verified decision-maker contacts from public sources such as Find a Tender, Contracts Finder, Digital Marketplace, TED, and Public Contracts Scotland, then layers tender discovery, market intelligence, AI-assisted bid qualification (Bid Studio), account targeting (Sales Studio), and pipeline management on top so suppliers can find, qualify, and win government contracts. Delivered as a SaaS web application at app.stotles.com, and — since 2026 — as a programmable surface: the Stotles Public API is a documented OpenAPI 3.1.0 REST service at api.stotles.com/v1 covering notices, buyers, suppliers and framework agreements, alongside a hosted Model Context Protocol server at api.stotles.com/mcp that brings the same market data into AI chat tools and agents. Both
  authenticate with a static x-api-key header; keys are issued by a Customer Success Manager rather than self-serve, and MCP access is in beta behind a waitlist.'
image: https://cdn.prod.website-files.com/67caf809eabcc3eb572f7bc7/68149b136c8bcfe66f0b8b2f_SEO%20Image%20-%20Homepage.jpg
layout: provider
mcp_servers:
- description: ''
  name: Stotles MCP server
  slug: stotles-mcp-server
- description: ''
  name: Stotles MCP Server
  slug: stotles-mcp-server-2
modified: '2026-08-14'
name: Stotles
nav: Providers
network: true
overview: 'Stotles publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Buyers API, Frameworks API, Notices API, and 1 more. Tagged areas include Company, Procurement, Public Sector, Government, and Tenders.


  Stotles'' developer surface includes documentation, support, getting-started guide, signup flow, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Stotles Plans Pricing
  plan_count: 11
  slug: stotles-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Stotles Rate Limits
  slug: stotles-rate-limits
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 57.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stotles/refs/heads/main/screenshots/stotles-2026-08-17T082131.png
security:
- kind: authentication
  name: Stotles Authentication
  slug: stotles-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stotles Domain Security
  slug: stotles-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stotles Trust Center
  slug: stotles-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: stotles
tags:
- Company
- Procurement
- Public Sector
- Government
- Tenders
- Sales Intelligence
- B2G
- Market Intelligence
- OpenAPI
- MCP
- agent-native
- Contract Awards
- Framework Agreements
- CPV
- United Kingdom
- Ireland
- GovTech
website: https://www.stotles.com
---
