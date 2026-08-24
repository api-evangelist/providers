---
access_model:
  confidence: high
  label: Contact sales for API credentials
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - plans
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.8
  scored_at: '2026-08-24'
api_count: 6
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
- description: Publisher (OFP) revenue and delivery reporting — a measurement/dimension query returning revenue, eCPM, requests, responses, impressions, clicks, CTR, CPC, fill rate and show rate, plus the older toke
  name: Opera Publisher Report API
  slug: opera-publisher-report-api
- description: Demand-side performance reporting for the Opera ADX exchange — daily impressions, requests, fills and revenue over a window of up to 180 consecutive days, authenticated by a token query parameter.
  name: Opera ADX DSP Report API
  slug: opera-dsp-report-api
- description: Resumable large-file upload implementing the TUS 1.0.0 protocol, with API-key or HMAC-SHA256 authentication, 4 GB maximum file size, 256 MB chunk ceiling and 7-day session expiry. The upload host is i
  name: Opera Ads File Upload API
  slug: opera-file-upload-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Opera Ads Open Inventory API
  slug: open-opera-inventory-api
- collection_type: open
  name: Opera Ads Open Inventory Marketing API
  slug: open-opera-marketing-api
- collection_type: open
  name: Opera Ads Open Inventory Report API
  slug: open-opera-report-api
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/opera-tool-crosswalk.yml
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
  type: ErrorCodes
  url: errors/opera-sdk-error-codes.yml
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
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opera-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/opera-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opera-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/opera-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/opera-components.yml
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
  url: https://blogs.opera.com/ads/
- group: operate
  title: ''
  type: Support
  url: https://help.opera.com/en/
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
  type: TermsOfService
  url: https://www.opera.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opera.com/privacy
- group: company
  title: ''
  type: Website
  url: https://opera.com/
created: '2026-07-17'
description: 'Opera is the Norway-based, Nasdaq-listed (OPRA) maker of the Opera, Opera GX, Opera Air, Opera Mini and Opera Neon web browsers, and the operator of the Opera Ads advertising and monetization platform. Opera Ads exposes six documented HTTP APIs: an advertiser Report API for daily campaign performance, a publisher Inventory Management API for apps and placements, a publisher OFP Report API for revenue and delivery, an ADX DSP Report API for exchange performance, a server-to-server Marketing API for conversion postbacks, and a TUS 1.0.0 resumable File Upload API. Around them sit Android and iOS ad SDKs with mediation adapters for AdMob, AppLovin MAX, TopOn, TradPlus and LevelPlay, an OpenRTB/ADX exchange with Prebid.js and Prebid Server adapters, a web JS ad tag, first-party Go OpenRTB and VAST libraries, and the self-serve Opera Ad Manager console. Authentication differs per API — bearer token, token query parameter, X-API-Key or HMAC signature — and every credential is issued
  by contacting Opera Ads.'
image: https://github.com/operaads.png
layout: provider
mcp_servers:
- description: ''
  name: Opera MCP Server
  slug: opera-mcp-server
modified: '2026-08-13'
name: Opera
nav: Providers
network: true
overview: 'Opera publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Inventory API, Marketing API, Report API, and 3 more. Tagged areas include Company, Consumer Technology, Advertising, AdTech, and Browser.


  Opera''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, engineering blog, and 29 more developer resources.'
plans:
- name: Opera Plans Pricing
  plan_count: 0
  slug: opera-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Opera Rate Limits
  slug: opera-rate-limits
score:
  band: strong
  composite: 57.3
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 30.3
    contract_quality: 57.1
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 50.0
  previous_composite: 57.3
  provenance:
    conformance: first-party
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/screenshots/opera-2026-08-17T083429.png
security:
- kind: authentication
  name: Opera Authentication
  slug: opera-authentication
  summary_line: http/apiKey/custom-hmac/unauthenticated · 5 schemes
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
- Mobile SDK
- Header Bidding
- Publisher Monetization
- Reporting
website: https://opera.com/
---
