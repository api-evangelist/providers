---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer API with broad read and write coverage across the GPX platform — investor data, fund accounting, payments, compliance, and reporting. Used to sync investor and fund data into CRMs (Salesforc
  name: Juniper Square Developer API
  slug: juniper-square-developer-api
artifact_total: 4
common:
- group: build
  href: https://artifacts.apis.io/junipersquare/integrations/junipersquare-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/junipersquare-integration-edges.yml
- group: auth
  href: https://artifacts.apis.io/junipersquare/well-known/junipersquare-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/junipersquare-status-security.txt
- group: agent
  href: https://artifacts.apis.io/junipersquare/well-known/junipersquare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/junipersquare-well-known.yml
- group: other
  href: https://artifacts.apis.io/junipersquare/hosts/junipersquare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/junipersquare-hosts.yml
- group: other
  href: https://artifacts.apis.io/junipersquare/vendors/junipersquare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/junipersquare-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.junipersquare.com/news/kudu
- group: start
  title: ''
  type: GettingStarted
  url: https://www.junipersquare.com/investor-relations/investor-onboarding
- group: company
  title: ''
  type: Website
  url: https://junipersquare.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.junipersquare.com/platform/apis-and-integrations
- group: agent
  href: https://artifacts.apis.io/junipersquare/mcp/junipersquare-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/junipersquare-mcp.yml
- group: auth
  href: https://artifacts.apis.io/junipersquare/security/junipersquare-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/junipersquare-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.junipersquare.com/
- group: auth
  href: https://artifacts.apis.io/junipersquare/security/junipersquare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/junipersquare-domain-security.yml
- group: design
  href: https://artifacts.apis.io/junipersquare/lifecycle/junipersquare-lifecycle.yml
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
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.junipersquare.com/terms-of-use
- group: design
  href: https://artifacts.apis.io/junipersquare/conformance/junipersquare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/junipersquare-conformance.yml
coverage:
  checked: '2026-10-20'
  detail: Juniper Square says its REST APIs and webhooks are built to OpenAPI and its Headless GPX MCP server is live, but neither a reference nor a spec is public; access comes through a 'Book an intro call' developer-led engagement and api.junipersquare.com answers 403 anonymously.
  evidence:
  - status: 200
    url: https://www.junipersquare.com/gpx/apis-and-integrations
  - status: 403
    url: https://api.junipersquare.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Juniper Square is a fund operating system for the private markets, used by 2,300+ general partners across private equity, venture capital, commercial real estate, and private credit to raise capital, run fund administration and fund accounting, and manage the LP experience. Its GPX platform unifies investor data, fund accounting, payments, compliance, and reporting, and exposes them through a developer API (broad read/write coverage delivered as a developer-led engagement), pre-built connectors (HubSpot, Preqin, Outlook, DocuSign, Yardi IM/Voyager, Lob), and Headless GPX — an MCP server that brings the platform to any MCP-compatible AI client (Claude, Copilot, ChatGPT, Gemini) with authentication, permissions, and audit inherited from the customer's existing configuration.
image: https://assets.junipersquare.com/images/_1200x630_crop_center-center_82_none/share.png?v=1779402326
layout: provider
mcp_servers:
- description: Headless GPX brings Juniper Square's GPX fund operating system to any MCP-compatible AI client (Claude, Microsoft Copilot, ChatGPT, Gemini, or a custom client). It gives agents real-time access to fun
  name: Headless GPX
  slug: junipersquare-headless-gpx
modified: '2026-08-08'
name: Juniper Square
nav: Providers
network: true
overview: 'Juniper Square is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Investment Management, Private Markets, Fund Administration, and Fund Accounting.


  Juniper Square''s developer surface includes getting-started guide, engineering blog, documentation, and 19 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 74.1
    operational_transparency: 28.9
  previous_composite: 30.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/junipersquare/junipersquare-2026-07-25T223322.png
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
- AI Agents
website: https://junipersquare.com
---
