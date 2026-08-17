---
access_model:
  confidence: high
  label: Enterprise contract
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.magnite.com/contact-us/
  - plans/magnite-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 349
  human_in_the_loop: 1
  name: Magnite Agentic Access
  operation_count: 668
  slug: magnite-agentic-access
  summary_line: 668 operations · 349 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'The SpringServe ad server REST API — the machine-readable core of Magnite Streaming. Two versions run concurrently: v0 (289 operations, 173 paths) and v1 (379 operations, 295 paths, 139 component sche'
  name: SpringServe UI API
  slug: springserve-ui-api
artifact_total: 9
collections:
- collection_type: open
  name: SpringServe UI API (V0)
  slug: open-magnite-springserve-v0
- collection_type: open
  name: SpringServe UI API
  slug: open-magnite-springserve-v1
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/magnite-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magnite-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magnite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.magnite.com
- group: company
  title: ''
  type: AboutUs
  url: https://www.magnite.com/about-us/
- group: other
  title: ''
  type: Sellers
  url: https://www.magnite.com/sellers/
- group: other
  title: ''
  type: Buyers
  url: https://www.magnite.com/buyers/
- group: other
  title: ''
  type: MagniteStreaming
  url: https://www.magnite.com/solutions/magnite-streaming/
- group: other
  title: ''
  type: SpringServe
  url: https://www.springserve.com
- group: other
  title: ''
  type: ClearLine
  url: https://www.magnite.com/solutions/clearline/
- group: other
  title: ''
  type: DVPlus
  url: https://www.magnite.com/solutions/dv/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.magnite.com/help
- group: docs
  title: ''
  type: Documentation
  url: https://help.magnite.com/help/developer-documentation
- group: other
  title: ''
  type: StreamingPublicAPI
  url: https://help.magnite.com/help/api-documentation-test
- group: docs
  title: ''
  type: SpringServeAPIDocs
  url: https://springserve.atlassian.net/wiki/spaces/SSD/pages/1573617663/API+-+Getting+Started
- group: other
  title: ''
  type: SpringServeReportingAPI
  url: https://springserve.atlassian.net/wiki/spaces/SSD/pages/1588035603/Reporting+API
- group: start
  title: ''
  type: SDKQuickStart
  url: https://help.magnite.com/help/sdk-quick-start-guide
- group: build
  title: ''
  type: iOSSDK
  url: https://help.magnite.com/help/in-app-sdk-integration-guide-ios
- group: build
  title: ''
  type: AndroidSDK
  url: https://help.magnite.com/help/in-app-sdk-integration-guide-android
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/SpringServe/springserve-python
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/springserve/
- group: company
  title: ''
  type: Blog
  url: https://www.magnite.com/blog/
- group: company
  title: ''
  type: Press
  url: https://www.magnite.com/press/
- group: other
  title: ''
  type: Glossary
  url: https://www.magnite.com/glossary/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.magnite.com
- group: company
  title: ''
  type: Careers
  url: https://www.magnite.com/careers/
- group: build
  title: ''
  type: SpringServeGitHub
  url: https://github.com/SpringServe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/magnite
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/magniteinc
- group: other
  title: ''
  type: NASDAQ
  url: https://www.nasdaq.com/market-activity/stocks/mgni
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Magnite_Inc
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/magnite-springserve-v1-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/magnite-springserve-v0-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/magnite-springserve-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/magnite-springserve-v0-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/magnite-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/magnite-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/magnite-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/magnite-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/magnite-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/magnite-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/magnite-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.magnite.com/trust-center/
- group: auth
  title: ''
  type: TrustCenter
  url: security/magnite-trust-center.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/magnite-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/magnite-plans-pricing.yml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/magnite-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/magnite-llms.txt
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/magnite-well-known.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.springserve.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://springserve.atlassian.net/wiki/spaces/SSD/pages/1573617663/API+-+Getting+Started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.magnite.com/help/developer-documentation
- group: operate
  title: ''
  type: Support
  url: https://www.magnite.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.magnite.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.magnite.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://console.springserve.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.magnite.com/legal/magnite-website-privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.magnite.com/legal/purchase-requisition-terms-and-conditions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magniteinc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpringServe
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rubicon-project
created: '2026-05-25'
description: 'Magnite, Inc. (NASDAQ: MGNI) is the world''s largest independent sell-side advertising platform, headquartered in New York with major operations in Los Angeles. Formed in 2020 from the merger of Rubicon Project and Telaria, and expanded through the acquisitions of SpotX (2021), SpringServe (2021), and Streamr.ai (2025), Magnite operates an omnichannel SSP spanning Connected TV (CTV), online video, display, audio, and mobile in-app. Its flagship offering is the Magnite Streaming platform — a next-generation CTV/OTT solution that unifies the SpringServe ad server with Magnite''s Streaming SSP — alongside DV+ for display/video web and mobile, ClearLine for agency self-service direct buying of premium video, and Magnite Access for first- and third-party data activation. Magnite connects publishers including Disney Advertising, Paramount, Roku, Samsung, LG Ad Solutions, and Warner Bros. Discovery to virtually all major DSPs, and Jounce Media''s March 2025 Supply Path Benchmarking
  Report verified Magnite reaches 99% of US streaming supply on a dollar-weighted basis. The company exposes developer surfaces through the SpringServe REST API, the Magnite Streaming Public API, the Magnite Seller Platform / CTV Platform Public APIs, an OpenRTB v2.5 bidder integration, and iOS/Android in-app SDKs. The SpringServe UI API publishes a real, anonymously reachable OpenAPI 3.1.2 contract in two concurrent versions (v0, 289 operations; v1, 379 operations) from the Swagger UI at https://api.springserve.com/api-docs, with the callable base at https://console.springserve.com. The Magnite Streaming and Seller Platform reference material on help.magnite.com remains gated behind an authenticated partner login. In Q1 2026 Magnite reported $164.4M revenue with CTV crossing 51% of contribution ex-TAC for the first time.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magnite.png
layout: provider
modified: '2026-08-13'
name: Magnite
nav: Providers
network: true
overview: 'Magnite publishes 1 API on the [APIs.io](https://apis.io/) network: SpringServe UI API. Tagged areas include Advertising, Programmatic Advertising, Sell-Side Platform, SSP, and Connected TV.


  Magnite''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, pricing, and 55 more developer resources.'
plans:
- name: Magnite Plans Pricing
  plan_count: 0
  slug: magnite-plans-pricing
random_paper: 145
rate_limits:
- limit_count: 3
  name: Magnite Rate Limits
  slug: magnite-rate-limits
score:
  band: developing
  composite: 53.5
  delta: 34.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.4
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 19.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/magnite/refs/heads/main/screenshots/magnite-2026-07-25T225900.png
security:
- kind: authentication
  name: Magnite Authentication
  slug: magnite-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Magnite Domain Security
  slug: magnite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Magnite Trust Center
  slug: magnite-trust-center
  summary_line: SOC 2 Type I, JICDAQ, ISO 27001
slug: magnite
tags:
- Advertising
- Programmatic Advertising
- Sell-Side Platform
- SSP
- Connected TV
- CTV
- OTT
- Streaming
- Display Advertising
- Video Advertising
- OpenRTB
- Header Bidding
- Ad Tech
- Publisher Monetization
- Demand-Side Integration
- Ad Server
- Deal Curation
- Reporting API
- Agent Readiness
- OpenAPI
website: https://www.magnite.com
---
