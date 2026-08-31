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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Trade Desk Agentic Access
  operation_count: 8
  slug: trade-desk-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 2
apis:
- description: The original REST Platform API covering advertisers, campaigns, ad groups, creatives, targeting data, reporting, and audience operations. Documentation is gated behind the TTD Partner Portal. New inte
  name: The Trade Desk Platform API
  slug: trade-desk-platform-api
- description: Server-side and client-side conversion event ingestion (Apache 2.0 Google Tag Manager templates) for capturing high-fidelity attribution signals in a cookie-deprecated environment. Pairs with UID2 for
  name: The Trade Desk Real-Time Conversion Events API
  slug: trade-desk-realtime-conversion-events-api
- description: Unified ID 2.0 is an open-source, deterministic identity framework seeded by The Trade Desk and now governed by the IAB Tech Lab. UID2 resolves hashed email addresses and phone numbers into rotating t
  name: Unified ID 2.0 (UID2)
  slug: trade-desk-uid2-api
- description: OpenSincera (from the May 2024 Sincera acquisition) provides programmatic supply-side transparency data — ad slot quality, page attributes, viewability metadata, supply-path metrics — to help buyers v
  name: OpenSincera API
  slug: trade-desk-opensincera-api
- description: The Advertiser API from The Trade Desk — 1 operation(s) for advertiser.
  name: The Trade Desk Advertiser API
  slug: trade-desk-advertiser-api
- description: The DeletionOptOut API from The Trade Desk — 3 operation(s) for deletionoptout.
  name: The Trade Desk DeletionOptOut API
  slug: trade-desk-deletionoptout-api
- description: The OfflineConversion API from The Trade Desk — 1 operation(s) for offlineconversion.
  name: The Trade Desk OfflineConversion API
  slug: trade-desk-offlineconversion-api
- description: The ThirdParty API from The Trade Desk — 1 operation(s) for thirdparty.
  name: The Trade Desk ThirdParty API
  slug: trade-desk-thirdparty-api
- description: IP-address ingestion endpoints of the TTD Data API — upload first-party or third-party IP-address-based targeting data for use in audience targeting. Discovered 2026-08-13 in the provider-published Sw
  name: The Trade Desk IPAddress Data API
  slug: trade-desk-ipaddress-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TTD Data Advertiser API
  slug: open-trade-desk-advertiser-api
- collection_type: open
  name: TTD Data API
  slug: open-trade-desk-data-api
- collection_type: open
  name: TTD Data Advertiser DeletionOptOut API
  slug: open-trade-desk-deletionoptout-api
- collection_type: open
  name: TTD Data IPAddress API
  slug: open-trade-desk-ipaddress-api
- collection_type: open
  name: TTD Data Advertiser OfflineConversion API
  slug: open-trade-desk-offlineconversion-api
- collection_type: open
  name: TTD Data Advertiser ThirdParty API
  slug: open-trade-desk-thirdparty-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.thetradedesk.com/trust
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.thetradedesk.com
- group: docs
  title: ''
  type: APIReference
  url: https://partner.thetradedesk.com/v3/portal/api/doc/ApiReferencePlatform
- group: operate
  title: ''
  type: Roadmap
  url: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/UpgradeSupport
- group: build
  title: ''
  type: SDKs
  url: packages/trade-desk-packages.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/trade-desk-data-api-swagger.json
- group: docs
  title: ''
  type: GraphQL
  url: https://api.thetradedesk.com/graphql
- group: start
  title: ''
  type: SignUp
  url: https://open.sincera.io/sign_up
- group: operate
  title: ''
  type: Support
  url: https://open.thetradedesk.com/contact-us
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trade-desk-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/trade-desk-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trade-desk-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/trade-desk-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trade-desk-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trade-desk-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/trade-desk-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://www.thetradedesk.com/trust/report-a-vulnerability
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trade-desk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trade-desk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trade-desk-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/UpgradeSupport
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trade-desk-lifecycle.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/trade-desk-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trade-desk-problem-types.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.thetradedesk.com/trust/security
- group: design
  title: ''
  type: Conformance
  url: conformance/trade-desk-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trade-desk-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/trade-desk-tool-crosswalk.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trade-desk-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trade-desk-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/trade-desk-packages.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trade-desk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trade-desk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thetradedesk.com
- group: start
  title: ''
  type: Portal
  url: https://www.thetradedesk.com/us
- group: docs
  title: ''
  type: Documentation
  url: https://open.thetradedesk.com
- group: docs
  title: ''
  type: Documentation
  url: https://partner.thetradedesk.com
- group: start
  title: ''
  type: GettingStarted
  url: https://partner.thetradedesk.com/v3/portal/api/doc/ApiPlatformGetStarted
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/our-platform
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/our-platform/dsp-demand-side-platform
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/openpath
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/our-platform/koa-ai-artificial-intelligence
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/news/introducing-galileo
- group: other
  title: ''
  type: Identity
  url: https://unifiedid.com
- group: other
  title: ''
  type: Identity
  url: https://euid.eu
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheTradeDesk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IABTechLab
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-workflows-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-workflows-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-workflows-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-data-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-databricks-python
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/TheTradeDesk/Platform
- group: company
  title: ''
  type: PressRoom
  url: https://www.thetradedesk.com/us/news
- group: company
  title: ''
  type: Blog
  url: https://www.thetradedesk.com/us/news-insights
- group: company
  title: ''
  type: Newsroom
  url: https://www.thetradedesk.com/us/press-room
- group: company
  title: ''
  type: AboutUs
  url: https://www.thetradedesk.com/us/about-us
- group: company
  title: ''
  type: Careers
  url: https://careers.thetradedesk.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.thetradedesk.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thetradedesk.com/legal/trade-desk-advertising-terms-4-7-26
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thetradedesk.com/legal/website-privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.thetradedesk.com/us/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-trade-desk
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/thetradedesk
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@thetradedesk
created: '2026-05-25'
description: 'The Trade Desk is an independent, omnichannel demand-side platform (DSP) for programmatic advertising, headquartered in Ventura, California. Its cloud-based platform — Kokai (the current flagship, succeeding Solimar) — lets agencies, brands, and trading desks buy and optimize digital ad inventory across connected TV (CTV), audio, mobile, video, native, display, and digital out-of-home. The Trade Desk positions itself as the buy-side counterweight to the walled gardens by championing the open internet through OpenPath (direct publisher integrations that bypass SSPs) and Unified ID 2.0 (UID2), an open-source, deterministic identity framework governed by the IAB Tech Lab. The company also stewards EUID (UID2''s European equivalent), the Galileo first-party data activation framework, and Koa — its in-platform AI used for forecasting, bidding optimization, and audience modeling. Programmatic developers integrate via the TTD Workflows API (REST + GraphQL for campaign, ad group, and
  creative management), the Data API (advertiser/third-party data ingestion, offline conversions, deletion/opt-out), the Real-Time Conversion Events API (RTCE), and the OpenSincera data-quality APIs (acquired May 2024). Official SDKs are published in Python, Go, and Java and are Speakeasy-generated from OpenAPI specs. Most documentation lives behind the Partner Portal (partner.thetradedesk.com) but a public docs surface is exposed at open.thetradedesk.com. The Trade Desk is publicly traded (NASDAQ: TTD).'
graphqls:
- description: 'generated: ''2026-08-13'''
  name: The Trade Desk GraphQL API
  slug: trade-desk-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trade-desk.png
layout: provider
mcp_servers:
- description: The Trade Desk's MCP-based access to Koa Agents, announced in the Platform API release notes on 2026-08-10 and available to select partners in private beta. Rather than exposing one tool per API endpo
  name: Open Agentic Kit (OAK)
  slug: open-agentic-kit-oak
modified: '2026-08-13'
name: The Trade Desk
nav: Providers
network: true
overview: 'The Trade Desk publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Advertiser API, DeletionOptOut API, OfflineConversion API, and 2 more. Tagged areas include Advertising, Programmatic Advertising, Demand-Side Platform, DSP, and AdTech.


  The Trade Desk''s developer surface includes API reference, signup flow, support, changelog, sandbox, authentication, developer portal, and 59 more developer resources.'
plans:
- name: Trade Desk Plans Pricing
  plan_count: 0
  slug: trade-desk-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Trade Desk Rate Limits
  slug: trade-desk-rate-limits
scopes:
- name: Trade Desk Scopes
  scope_count: 91
  slug: trade-desk-scopes
  summary_line: 91 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 25
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trade-desk/refs/heads/main/screenshots/trade-desk-2026-06-20T195532.png
security:
- kind: authentication
  name: Trade Desk Authentication
  slug: trade-desk-authentication
  summary_line: apiKey/oauth2/openIdConnect/http · 7 schemes
- kind: domain-security
  name: Trade Desk Domain Security
  slug: trade-desk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trade Desk Vulnerability Disclosure
  slug: trade-desk-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Trade Desk Trust Center
  slug: trade-desk-trust-center
  summary_line: SSAE18 SOC 2 Type 2, SSAE18 SOC 1, Sarbanes-Oxley (SOX) Section 404, PCI DSS SAQ A (self-attestation)
slug: trade-desk
tags:
- Advertising
- Programmatic Advertising
- Demand-Side Platform
- DSP
- AdTech
- Connected TV
- CTV
- Identity
- Unified ID 2.0
- UID2
- OpenPath
- Kokai
- Koa AI
- Galileo
- Sincera
- Open Internet
- Real-Time Bidding
- Open Measurement
website: https://www.thetradedesk.com
---
