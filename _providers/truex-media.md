---
access_model:
  confidence: medium
  label: Partner
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://github.com/socialvibe/truex-ads-docs/blob/master/web_service_ad_api.md
  - https://infillion.com/contact/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.9
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: Server-side ad request API. A GET against the versioned endpoint with a placement key, user id, IP and user agent returns a JSON `ad` object (creative id, campaign id, window URL and dimensions, curre
  name: true[X] Web Service Ad API
  slug: truex-media-web-service-ad-api
- description: Publisher performance reporting. A GET against /v1/publisher/performance.json (or .csv) with an api_key and a date range returns revenue and key performance indicators broken out by placement key, day
  name: true[X] Reporting API
  slug: truex-media-reporting-api
- description: Client-side JavaScript integration for publishers embedding true[X] engagement ads on the web. Loads truex.client from static.truex.com, exposes requestAd, loadAdIntoContainer, openAdWindow, trackTrig
  name: true[X] JavaScript Ad API
  slug: truex-media-js-ad-api
artifact_total: 9
asyncapis:
- description: ''
  name: Truex Media Webhooks
  slug: truex-media-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://infillion.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/socialvibe/truex-ads-docs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/socialvibe/truex-ads-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/socialvibe/truex-ads-docs/blob/master/web_service_ad_api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/socialvibe/truex-mobile-integrations/wiki
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/socialvibe
- group: company
  title: ''
  type: Blog
  url: https://infillion.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://infillion.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://infillion.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infillion.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infillion.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://infillion.com/cookie-policy/
- group: build
  title: ''
  type: Packages
  url: packages/truex-media-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/truex-media-packages.yml
- group: design
  title: ''
  type: Components
  url: components/truex-media-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/truex-media-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/truex-media-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truex-media-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truex-media-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/truex-media-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/truex-media-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/truex-media-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truex-media-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/truex-media-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/truex-media-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truex-media-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/truex-media-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/truex-media-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truex-media-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/truex-media-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truex-media-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truex-media-llms.txt
created: '2026-07-17'
description: TrueX (stylized true[X]) is an interactive, opt-in video advertising company now operating as part of Infillion. Its technology delivers "attention-based" ad experiences — Choice Cards and interactive engagement units that let viewers opt in to a single, longer branded interaction in exchange for an ad-free content break — across connected TV (CTV), over-the-top (OTT), mobile, and web. The company originated as SocialVibe (a Redpoint Ventures portfolio company), was acquired by 21st Century Fox, and is now a video advertising product within Infillion alongside MediaMath, InStadium, Gimbal, and Catalina. true[X] publishes two real HTTP APIs from its own truex.com hosts — a Web Service Ad API at get.truex.com/v2 that returns a JSON ad object for server-side ad requests, and a Reporting API at api.truex.com/v1 that returns publisher performance by placement, day and campaign — alongside a signed server-to-server engagement callback. Its primary integration surface remains the TruexAdRenderer
  (TAR) client SDK, published first-party from the "socialvibe" GitHub organization and the @truex npm scope for iOS, tvOS, Android/Fire TV, Roku, Amazon Vega OS, and CTV/HTML5 web. Parent company Infillion also operates Infillion Agent Connector, an MCP-based agent-native media execution layer at mcp.infillion.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truex-media.png
layout: provider
mcp_servers:
- description: Infillion Agent Connector is marketed as an agent-native media execution layer built on the Model Context Protocol, letting AI systems plan, buy and optimize media directly rather than through human w
  name: Infillion Agent Connector
  slug: infillion-agent-connector
modified: '2026-08-12'
name: Truex Media
nav: Providers
network: true
overview: 'Truex Media publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Video Advertising, and Connected TV.


  The Truex Media catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Truex Media''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Truex Media Plans Pricing
  plan_count: 0
  slug: truex-media-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Truex Media Rate Limits
  slug: truex-media-rate-limits
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 46.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truex-media/refs/heads/main/screenshots/truex-media-2026-08-17T082454.png
security:
- kind: authentication
  name: Truex Media Authentication
  slug: truex-media-authentication
  summary_line: apiKey/oauth2/hmac · 4 schemes
- kind: domain-security
  name: Truex Media Domain Security
  slug: truex-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truex-media
tags:
- Company
- Advertising
- AdTech
- Video Advertising
- Connected TV
- Interactive Advertising
- SDK
- Mobile
- Ad Serving
- Reporting
- Attention Measurement
- OTT
website: https://infillion.com
---
