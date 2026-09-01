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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 3.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Developer API with broad read and write coverage across the GPX platform — investor data, fund accounting, payments, compliance, and reporting. Used to sync investor and fund data into CRMs (Salesforc
  name: Juniper Square Developer API
  slug: juniper-square-developer-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://junipersquare.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.junipersquare.com/platform/apis-and-integrations
- group: agent
  title: ''
  type: MCPServer
  url: mcp/junipersquare-mcp.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/junipersquare-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.junipersquare.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/junipersquare-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/junipersquare-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.junipersquare.com/
- group: company
  title: ''
  type: Blog
  url: https://www.junipersquare.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/junipersquare
- group: start
  title: ''
  type: Login
  url: https://app.junipersquare.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.junipersquare.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://www.junipersquare.com/platform/apis-and-integrations
- group: operate
  title: ''
  type: Support
  url: https://support.junipersquare.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.junipersquare.com/terms-of-use
- group: design
  title: ''
  type: Conformance
  url: conformance/junipersquare-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/junipersquare-llms.txt
created: '2026-07-17'
description: Juniper Square is a fund operating system for the private markets, used by 2,300+ general partners across private equity, venture capital, commercial real estate, and private credit to raise capital, run fund administration and fund accounting, and manage the LP experience. Its GPX platform unifies investor data, fund accounting, payments, compliance, and reporting, and exposes them through a developer API (broad read/write coverage delivered as a developer-led engagement), pre-built connectors (HubSpot, Preqin, Outlook, DocuSign, Yardi IM/Voyager, Lob), and Headless GPX — an MCP server that brings the platform to any MCP-compatible AI client (Claude, Copilot, ChatGPT, Gemini) with authentication, permissions, and audit inherited from the customer's existing configuration.
image: https://assets.junipersquare.com/images/_1200x630_crop_center-center_82_none/share.png?v=1779402326
layout: provider
mcp_servers:
- description: ''
  name: Headless GPX
  slug: headless-gpx
modified: '2026-08-08'
name: Juniper Square
nav: Providers
network: true
overview: 'Juniper Square publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Investment Management, Private Markets, Fund Administration, and Fund Accounting.


  Juniper Square''s developer surface includes engineering blog, documentation, support, and 14 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/junipersquare/refs/heads/main/screenshots/junipersquare-2026-07-25T223322.png
security:
- kind: domain-security
  name: Junipersquare Domain Security
  slug: junipersquare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Junipersquare Trust Center
  slug: junipersquare-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR
slug: junipersquare
tags:
- Company
- Investment Management
- Private Markets
- Fund Administration
- Fund Accounting
- Commercial Real Estate
- Private Equity
- Investor Relations
- MCP
- Agentic AI
website: https://junipersquare.com
---
