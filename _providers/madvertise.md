---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 11.4
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: JSON ad-request endpoint (mobile.mng-ads.com) that returns a single ad (banner, interstitial, native) for a given placement, device User-Agent, SDK version and consent signal. GET or POST.
  name: Madvertise Ad Request API
  slug: madvertise-ad-request-api
- description: OpenRTB 2.5 bid-request endpoint (mobile.mng-ads.com/bidrequest/{placement}) for programmatic in-app demand. POST JSON with x-openrtb-version 2.5; returns bid markup in the adm field, 204 when no bid,
  name: Madvertise OpenRTB Bid Request API
  slug: madvertise-openrtb-bid-request-api
- description: 'Token-authenticated JSON reporting API family covering seller (publisher), buyer (advertiser), DSP and mediation reporting. POST /auth-reporting mints an opaque token passed bare in the Authorization '
  name: Madvertise Reporting API
  slug: madvertise-reporting-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bluestack.app/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bluestack.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bluestack.app/adserving/
- group: company
  title: ''
  type: Blog
  url: https://developers.bluestack.app/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.bluestack.app/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/azerion
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.bluestack.app/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://madvertise.com/en
- group: build
  title: ''
  type: Packages
  url: packages/madvertise-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/madvertise-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/madvertise-error-codes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/madvertise-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/madvertise-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/madvertise-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/madvertise-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/madvertise-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.bluestack.app/releases
- group: auth
  title: ''
  type: DomainSecurity
  url: security/madvertise-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/madvertise-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/madvertise-bluestack-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/madvertise-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/madvertise-tool-crosswalk.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/madvertise-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/madvertise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/madvertise-rate-limits.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bluestack.app/android/
- group: start
  title: ''
  type: Login
  url: https://console.bluestack.app
- group: operate
  title: ''
  type: Support
  url: https://www.azerion.com/azerion-contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.azerion.com/publishers-seller-monetization-terms-and-conditions/
created: '2026-07-17'
description: Madvertise is a mobile advertising and monetization brand now operating within Azerion as the "BlueStack" (Improve Digital InApp) mobile SDK suite and the mng-ads.com ad-serving platform. It lets mobile publishers monetize in-app inventory with banner, interstitial, native, rewarded-video and App Open ad formats through first-party SDKs for Android, iOS, Unity, React Native, Flutter and .NET MAUI, and connects programmatic demand through an OpenRTB 2.5 bid-request API, a JSON ad-request API, VAST video, and a Prebid Server adapter. A separate token-authenticated reporting API family serves sellers, buyers, DSPs and mediation partners with revenue and delivery data. The platform advertises IAB TCF, IAB Open Measurement, GDPR and COPPA compliance. Originally a Munich-founded mobile ad network backed by Point Nine Capital, Madvertise's technology now ships under Azerion / Improve Digital, whose GitHub org also publishes a first-party MCP server for publisher inventory management.
image: https://www.azerion.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Improve Digital Publisher MCP Server (Azerion; targets the sibling 360Yield inventory API)
  slug: improve-digital-publisher-mcp-server-azerion-targets-the-sibling-360yield-inventory-api
modified: '2026-08-12'
name: Madvertise
nav: Providers
network: true
overview: 'Madvertise publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Mobile, and Monetization.


  Madvertise''s developer surface includes documentation, API reference, engineering blog, changelog, authentication, sandbox, getting-started guide, and 22 more developer resources.'
plans:
- name: Madvertise Plans Pricing
  plan_count: 0
  slug: madvertise-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Madvertise Rate Limits
  slug: madvertise-rate-limits
score:
  band: thin
  composite: 33.9
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 33.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/madvertise/refs/heads/main/screenshots/madvertise-2026-07-25T225832.png
security:
- kind: authentication
  name: Madvertise Authentication
  slug: madvertise-authentication
  summary_line: placement-code/app-id/token/oauth2 · 4 schemes
- kind: domain-security
  name: Madvertise Domain Security
  slug: madvertise-domain-security
  summary_line: TLSv1.3
slug: madvertise
tags:
- Company
- Advertising
- AdTech
- Mobile
- Monetization
- Programmatic
- OpenRTB
- SDK
- Publishers
website: https://madvertise.com/en
---
