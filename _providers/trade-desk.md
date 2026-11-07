---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
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
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
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
- baseURL: https://usw-data.adsrvr.org
  baseurl_source: declared
  description: The Advertiser API from The Trade Desk — 1 operation(s) for advertiser.
  name: The Trade Desk Advertiser API
  slug: trade-desk-advertiser-api
- baseURL: https://usw-data.adsrvr.org
  baseurl_source: declared
  description: The DeletionOptOut API from The Trade Desk — 3 operation(s) for deletionoptout.
  name: The Trade Desk DeletionOptOut API
  slug: trade-desk-deletionoptout-api
- baseURL: https://offlineattrib.adsrvr.org
  baseurl_source: declared
  description: The OfflineConversion API from The Trade Desk — 1 operation(s) for offlineconversion.
  name: The Trade Desk OfflineConversion API
  slug: trade-desk-offlineconversion-api
- description: The Trade Desk Real-Time Conversions API (formerly the Real-Time Conversion Events API) allows advertisers to send conversion events server-side in real time, enabling more accurate attribution, cross
  name: The Trade Desk Real-Time Conversions API
  slug: the-trade-desk-real-time-conversions-api
- description: The Trade Desk Reporting API provides programmatic access to campaign performance data including impressions, clicks, conversions, spend, win rates, viewability, effective CPM, completion rates, and 2
  name: The Trade Desk Reporting API
  slug: the-trade-desk-reporting-api
- baseURL: https://api.thetradedesk.com/v3
  baseurl_source: declared
  description: The IP Address API from The Trade Desk — 2 operation(s) for ip address.
  name: The Trade Desk IP Address API
  slug: trade-desk-ip-address-api
- baseURL: https://api.thetradedesk.com/v3
  baseurl_source: declared
  description: The Third Party API from The Trade Desk — 1 operation(s) for third party.
  name: The Trade Desk Third Party API
  slug: trade-desk-third-party-api
artifact_total: 33
collections:
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
- group: other
  href: https://artifacts.apis.io/trade-desk/capabilities/trade-desk-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trade-desk-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/trade-desk/overlays/trade-desk-ipaddress-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trade-desk-ipaddress-api-overlay.yaml
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
  href: https://artifacts.apis.io/trade-desk/packages/trade-desk-packages.yml
  title: ''
  type: SDKs
  url: packages/trade-desk-packages.yml
- group: docs
  href: https://artifacts.apis.io/trade-desk/openapi/_original/trade-desk-data-api-swagger.json
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
  href: https://artifacts.apis.io/trade-desk/rate-limits/trade-desk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trade-desk-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/trade-desk/plans/trade-desk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trade-desk-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/trade-desk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trade-desk/data-model/trade-desk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trade-desk-data-model.yml
- group: design
  href: https://artifacts.apis.io/trade-desk/components/trade-desk-components.yml
  title: ''
  type: Components
  url: components/trade-desk-components.yml
- group: operate
  href: https://artifacts.apis.io/trade-desk/changelog/trade-desk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/trade-desk-changelog.yml
- group: design
  href: https://artifacts.apis.io/trade-desk/conventions/trade-desk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trade-desk-conventions.yml
- group: start
  href: https://artifacts.apis.io/trade-desk/sandbox/trade-desk-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/trade-desk-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://www.thetradedesk.com/trust/report-a-vulnerability
- group: auth
  href: https://artifacts.apis.io/trade-desk/security/trade-desk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trade-desk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/trade-desk/authentication/trade-desk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trade-desk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/trade-desk/scopes/trade-desk-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/trade-desk-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/UpgradeSupport
- group: design
  href: https://artifacts.apis.io/trade-desk/lifecycle/trade-desk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trade-desk-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/trade-desk/errors/trade-desk-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/trade-desk-error-codes.yml
- group: design
  href: https://artifacts.apis.io/trade-desk/errors/trade-desk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trade-desk-problem-types.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.thetradedesk.com/trust/security
- group: design
  href: https://artifacts.apis.io/trade-desk/conformance/trade-desk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trade-desk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trade-desk/llms/trade-desk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trade-desk-llms.txt
- group: build
  href: https://artifacts.apis.io/trade-desk/mcp/trade-desk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/trade-desk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/trade-desk/mcp/trade-desk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trade-desk-mcp.yml
- group: agent
  href: https://artifacts.apis.io/trade-desk/well-known/trade-desk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trade-desk-well-known.yml
- group: build
  href: https://artifacts.apis.io/trade-desk/packages/trade-desk-packages.yml
  title: ''
  type: Packages
  url: packages/trade-desk-packages.yml
- group: agent
  href: https://artifacts.apis.io/trade-desk/agentic-access/trade-desk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trade-desk-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/trade-desk/security/trade-desk-domain-security.yml
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
finops:
- has_sources: true
  method: derived
  name: Trade Desk Finops
  primary_unit: ''
  service_category: ''
  slug: trade-desk-finops
  template: true
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
overview: 'The Trade Desk publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Advertiser API, DeletionOptOut API, OfflineConversion API, and 8 more. Tagged areas include Advertising, Programmatic Advertising, DSP, AdTech, and Connected TV.


  The The Trade Desk catalog on APIs.io includes 1 Spectral governance ruleset.


  The Trade Desk''s developer surface includes API reference, signup flow, support, changelog, sandbox, authentication, developer portal, and 61 more developer resources.'
plans:
- name: Trade Desk Plans Pricing
  plan_count: 0
  slug: trade-desk-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Trade Desk Rate Limits
  slug: trade-desk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: The Trade Desk API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: trade-desk-rules
scopes:
- name: Trade Desk Scopes
  scope_count: 91
  slug: trade-desk-scopes
  summary_line: 91 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 44.2
    developer_ergonomics: 80.4
    discoverability: 75.8
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 56.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trade-desk/trade-desk-2026-06-20T195532.png
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
skill_count: 4
skills:
- name: Connect an agent to The Trade Desk Open Agentic Kit (OAK)
  slug: trade-desk-connect-open-agentic-kit
- name: Handle a data subject deletion or opt-out request at The Trade Desk
  slug: trade-desk-handle-deletion-optout
- name: Onboard a first-party audience segment to The Trade Desk
  slug: trade-desk-onboard-first-party-audience
- name: Send offline conversions to The Trade Desk
  slug: trade-desk-send-offline-conversions
slug: trade-desk
tags:
- Advertising
- Programmatic Advertising
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
