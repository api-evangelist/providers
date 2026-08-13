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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: Publisher app and placement (inventory) management.
  name: Opera Inventory API
  slug: opera-inventory-api
- description: Server-to-server conversion event reporting.
  name: Opera Marketing API
  slug: opera-marketing-api
- description: Advertiser reporting on campaign performance.
  name: Opera Report API
  slug: opera-report-api
artifact_total: 7
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/opera-ads-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opera-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opera-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://security.opera.com/policy/
- group: build
  title: ''
  type: Packages
  url: packages/opera-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/opera-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opera-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opera-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/opera-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/opera-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/opera-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opera-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opera-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opera-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/opera-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.adx.opera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.adx.opera.com/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.adx.opera.com/advertiser/report-api
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.adx.opera.com/publisher/onboarding/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/operaads
- group: company
  title: ''
  type: Blog
  url: https://blogs.opera.com/
- group: start
  title: ''
  type: SignUp
  url: https://admanager.opera.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opera.com/ads
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opera.com/privacy
- group: company
  title: ''
  type: Website
  url: https://opera.com/
created: '2026-07-17'
description: Opera is the Norway-based maker of the Opera, Opera GX, and Opera Mini web browsers and operator of the Opera Ads advertising and monetization platform. Opera Ads exposes a public Open API for advertisers (daily campaign reporting and server-to-server conversion events) and for publishers (app and placement inventory management), alongside Android/iOS ad SDKs, an OpenRTB/ADX exchange, first-party Go client and protocol libraries, and a self-serve Opera Ad Manager. API authentication is via a bearer token issued by Opera Ads.
image: https://github.com/operaads.png
layout: provider
mcp_servers:
- description: ''
  name: opera-mcp.yml
  slug: opera-mcpyml
modified: '2026-07-20'
name: Opera
nav: Providers
network: true
overview: 'Opera publishes 3 APIs on the [APIs.io](https://apis.io/) network: Inventory API, Marketing API, and Report API. Tagged areas include Company, Consumer Technology, Advertising, AdTech, and Browser.


  Opera''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, and 20 more developer resources.'
random_paper: 55
score:
  band: developing
  composite: 46.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 60.4
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 46.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/screenshots/opera-2026-08-07T190703.png
security:
- kind: authentication
  name: Opera Authentication
  slug: opera-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opera Domain Security
  slug: opera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opera Vulnerability Disclosure
  slug: opera-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: opera
tags:
- Company
- Consumer Technology
- Advertising
- AdTech
- Browser
- Monetization
- OpenRTB
- Marketing
website: https://opera.com/
---
