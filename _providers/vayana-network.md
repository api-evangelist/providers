---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://s.api.one.vayana.com
  baseurl_source: declared
  description: 'Vayana Atlas is Vayana''s API marketplace for trade and compliance. The published OpenAPI 3.1 contract covers 65 operations across four suites: a Verification Suite (PAN, detailed PAN, PAN-GST link, GS'
  name: Vayana Atlas API
  slug: vayana-network-atlas
- description: The Enriched API Service ("Flynn") is Vayana GSP's higher-level API suite over the three GSTN peers — the GST Returns portal, the NIC E-Way Bill portal and the IRP e-invoicing portal. "Basic" routes a
  name: Vayana Enriched API Service (EAS)
  slug: vayana-network-enriched-api-service
- description: Vayana GSP's Pass-Through API Service is the thin, last-mile gateway to the GSTN and NIC ecosystems for integrators who want to speak the government contracts directly. The caller populates the govern
  name: Vayana GSP Pass-Through API Service (PAS)
  slug: vayana-network-gsp-pass-through
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.vayana.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atlas.vayana.com/developer-landing-page/
- group: docs
  title: ''
  type: Documentation
  url: https://s.docs.atlas.vayana.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.enriched-api.vayana.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.enriched-api.vayana.com/1s0-getting-started/
- group: start
  title: ''
  type: SignUp
  url: https://docs.enriched-api.vayana.com/1s1-onboarding/
- group: operate
  title: ''
  type: Support
  url: https://www.vayana.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.vayana.com/blogs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vayana.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vayana
- group: auth
  title: ''
  type: Authentication
  url: authentication/vayana-network-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vayana-network-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vayana-network-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vayana-network-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/vayana-network-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vayana-network-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/vayana-network-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vayana-network-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vayana-network-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vayana-network-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/vayana-network-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vayana-network-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vayana-network-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vayana-network-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vayana-network-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-02'
description: 'Vayana (legal entity Vay Network Services Pvt. Ltd., founded 2016, headquartered in Pune, India) operates India''s trade credit infrastructure network, connecting buyers, sellers, banks and NBFCs across supply chains, and is a GSTN-authorized GST Suvidha Provider (GSP). Its developer surface spans three published programs: Vayana Atlas, an API marketplace for trade and compliance covering identity/business verification (PAN, GSTIN, Aadhaar, MCA, Udyam, EPF, bank account, vehicle, voter ID) alongside GST e-invoicing and E-Way Bill operations; the Enriched API Service (EAS), a higher-level wrapper adding bulk processing, PDF generation and long-running task handling over the GSTN, NIC E-Way Bill and IRP e-invoicing peers; and Vayana GSP Pass-Through API Service (PAS), a thin encrypted gateway to the same government ecosystems. Authentication across all three runs through Vayana''s own SSO service (internally "theodore"), and sensitive values are RSA/AES encrypted in transit above
  TLS.'
image: https://www.vayana.com/wp-content/uploads/2022/11/vayana-logo-1.svg
layout: provider
mcp_servers:
- description: ''
  name: Vayana Network MCP Server
  slug: vayana-network-mcp-server
modified: '2026-09-02'
name: Vayana Network
nav: Providers
network: true
overview: 'Vayana Network publishes 1 API on the [APIs.io](https://apis.io/) network: Vayana Atlas API. Tagged areas include Company, Trade Finance, Supply Chain Finance, Tax Compliance, and E-Invoicing.


  Vayana Network''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Vayana Network Plans Pricing
  plan_count: 0
  slug: vayana-network-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Vayana Network Rate Limits
  slug: vayana-network-rate-limits
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 48.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Vayana Network Authentication
  slug: vayana-network-authentication
  summary_line: http/apiKey · 6 schemes
- kind: domain-security
  name: Vayana Network Domain Security
  slug: vayana-network-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vayana-network
tags:
- Company
- Trade Finance
- Supply Chain Finance
- Tax Compliance
- E-Invoicing
- GST
- Identity Verification
- KYC
- India
- Embedded Finance
- Government
- Logistics
website: https://www.vayana.com/
---
