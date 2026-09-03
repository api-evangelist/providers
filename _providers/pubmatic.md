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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'PubMatic''s Model Context Protocol (MCP) server — the company''s public agent-facing API surface for programmatic advertising. It exposes four published tools over JSON-RPC 2.0: deal_management (create '
  name: PubMatic MCP Server
  slug: pubmatic-mcp-server
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pubmatic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pubmatic.com
- group: other
  title: ''
  type: Publisher
  url: https://pubmatic.com/products/publisher/
- group: other
  title: ''
  type: Buyer
  url: https://pubmatic.com/products/buyer/
- group: other
  title: ''
  type: CommerceMedia
  url: https://pubmatic.com/products/commerce-media/
- group: other
  title: ''
  type: OpenWrap
  url: https://pubmatic.com/products/openwrap/
- group: other
  title: ''
  type: Connect
  url: https://pubmatic.com/products/connect/
- group: other
  title: ''
  type: Activate
  url: https://pubmatic.com/products/activate/
- group: other
  title: ''
  type: Convert
  url: https://pubmatic.com/products/convert/
- group: other
  title: ''
  type: IdentityHub
  url: https://pubmatic.com/products/identity-hub/
- group: agent
  title: ''
  type: AgenticOS
  url: https://pubmatic.com/products/agentic-os/
- group: build
  title: ''
  type: AuctionPackages
  url: https://pubmatic.com/products/auction-packages/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.pubmatic.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PubMatic
- group: other
  title: ''
  type: OpenWrapRepo
  url: https://github.com/PubMatic/OpenWrap
- group: build
  title: ''
  type: OpenWrapSDKSwift
  url: https://github.com/PubMatic/OpenWrapSDK-Swift-Package
- group: build
  title: ''
  type: OpenWrapSDKFlutter
  url: https://github.com/PubMatic/flutter-openwrap-sdk
- group: build
  title: ''
  type: OpenWrapSamplesIOS
  url: https://github.com/PubMatic/ios-openwrap-sdk-samples
- group: build
  title: ''
  type: OpenWrapSamplesAndroid
  url: https://github.com/PubMatic/android-openwrap-sdk-samples
- group: build
  title: ''
  type: OpenWrapSamplesUnity
  url: https://github.com/PubMatic/unity-openwrap-sdk-samples
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pubmatic-mcp.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/PubMatic/pubmatic-mcp-server
- group: other
  title: ''
  type: SKAdNetworkApp
  url: https://github.com/PubMatic/PubMatic-SKAdNetwork-App
- group: other
  title: ''
  type: SupplyChain
  url: https://pubmatic.com/sellers.json
- group: company
  title: ''
  type: Investors
  url: https://investors.pubmatic.com
- group: company
  title: ''
  type: Newsroom
  url: https://pubmatic.com/news/
- group: company
  title: ''
  type: Blog
  url: https://pubmatic.com/resources/?type=blog
- group: company
  title: ''
  type: BlogRSS
  url: https://pubmatic.com/blog/feed/
- group: company
  title: ''
  type: Careers
  url: https://pubmatic.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://pubmatic.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pubmatic.com/legal/privacy/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/pubmatic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pubmatic
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@PubMatic
- group: docs
  title: ''
  type: Documentation
  url: https://help.pubmatic.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pubmatic.com/legal/website-terms-of-service/
- group: commercial
  title: ''
  type: DeveloperTerms
  url: https://pubmatic.com/legal/developer-terms-use/
- group: start
  title: ''
  type: Login
  url: https://apps.pubmatic.com/login/community
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pubmatic-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/pubmatic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pubmatic-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pubmatic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pubmatic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pubmatic-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pubmatic-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pubmatic-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pubmatic-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pubmatic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pubmatic-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pubmatic-data-model.yml
created: '2026-05-25'
description: 'PubMatic is a Redwood City, California-headquartered independent technology company (NASDAQ: PUBM) operating a supply-side platform (SSP) that powers programmatic advertising for publishers, media buyers, commerce media, and AI agents across CTV, mobile app, online video, display, and audio. Its unified platform combines an SSP for monetization and demand access, the OpenWrap header-bidding wrapper (an open-source Prebid-based wrapper with web, iOS, Android, Flutter, and Unity SDKs), Connect for curation and audience activation, Activate for buyer-side supply-path optimization and direct-to-publisher deals, Convert for commerce/retail media, Identity Hub for identity orchestration, and AgenticOS for agent-driven campaign planning and execution. PubMatic processes trillions of bids per day across global infrastructure, and exposes its programmatic surface primarily via the OpenRTB protocol, prebid integrations, and embedded SDKs rather than a public REST developer portal — making
  this profile a directory of PubMatic''s products, OpenWrap repos, sample apps, and supply-chain endpoints rather than a tier-1 OpenAPI-backed catalog. Its one reachable agent-facing API is the PubMatic MCP Server at https://mcp.pubmatic.com/mcp, whose specifications, integration guides and packaged Agent Skills PubMatic publishes openly at github.com/PubMatic/pubmatic-mcp-server even though the endpoint itself is account-gated; the customer API reference at help.pubmatic.com sits behind an Okta/Auth0 login, and no OpenAPI, AsyncAPI, GraphQL or A2A agent card is served on any PubMatic host.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pubmatic.png
layout: provider
mcp_servers:
- description: ''
  name: PubMatic MCP Server
  slug: pubmatic-mcp-server
modified: '2026-08-13'
name: PubMatic
nav: Providers
network: true
overview: 'PubMatic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, AdTech, Programmatic Advertising, Supply Side Platform, and SSP.


  PubMatic''s developer surface includes engineering blog, YouTube channel, documentation, authentication, changelog, and 46 more developer resources.'
plans:
- name: Pubmatic Plans Pricing
  plan_count: 0
  slug: pubmatic-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Pubmatic Rate Limits
  slug: pubmatic-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pubmatic/refs/heads/main/screenshots/pubmatic-2026-06-20T192244.png
security:
- kind: authentication
  name: Pubmatic Authentication
  slug: pubmatic-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Pubmatic Domain Security
  slug: pubmatic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pubmatic
tags:
- Advertising
- AdTech
- Programmatic Advertising
- Supply Side Platform
- SSP
- Header Bidding
- OpenWrap
- Prebid
- OpenRTB
- Connected TV
- CTV
- Mobile Advertising
- Commerce Media
- Retail Media
- Identity
- Curation
- Auction Packages
- Agentic AI
website: https://pubmatic.com
---
