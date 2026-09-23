---
access_model:
  confidence: medium
  label: Documented, account-manager mediated
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://wiki.pokkt.com/api-guide
  - https://wiki.pokkt.com/dsp-integration-guide/pokkt-dsp.md
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-23'
api_count: 6
apis:
- description: Supply-side ad request API. A single GET to /api/AdServer returns one or more ad objects for a full-screen interstitial or banner placement, as a JSON array (response_format=0) or as HTML markup (resp
  name: POKKT Ad Server API
  slug: ad-server-api
- description: Video ad request API for supply-side platforms. The same /api/AdServer endpoint called with response_format=1 responds with a VAST XML tag rather than a JSON ad object, adding video-specific parameter
  name: POKKT VAST Video API
  slug: vast-video-api
- description: Demand-side bidding endpoint. Exchanges POST an OpenRTB bid request object as application/json to /api/rtb/<appid> with an x-openrtb-version header; POKKT answers HTTP 204 with no body for a no-bid or
  name: POKKT DSP OpenRTB API
  slug: dsp-openrtb-api
- description: Hosted rewarded-video surface for mobile web. The publisher opens /videoWap with its appId, a format selector and a URL-encoded `encodedparams` bag carrying custom session data such as a session id or
  name: POKKT Mobile Web Video API
  slug: mobile-web-video-api
- description: Server-to-server rewarded-video confirmation callback. When a user completes a rewarded video, POKKT issues a GET to a publisher-hosted URL configured in the app settings page, carrying app_id, unique
  name: POKKT Gratification API
  slug: gratification-api
- description: 'The GraphQL API behind the POKKT campaign-management console, live at api.pokkt.com/graphql and referenced directly by the console''s own JavaScript bundle. Authentication-gated: an anonymous introspec'
  name: POKKT Console GraphQL API
  slug: console-graphql-api
artifact_total: 11
asyncapis:
- description: ''
  name: Pokkt Webhooks
  slug: pokkt-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://pokkt.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wiki.pokkt.com
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.pokkt.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pokkt.com
- group: docs
  title: ''
  type: APIReference
  url: https://wiki.pokkt.com/api-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://wiki.pokkt.com/pokkt-sdk
- group: start
  title: ''
  type: Login
  url: https://pokkt.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anymindgroup.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AnyMindGroup
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/llms/pokkt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pokkt-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/packages/pokkt-packages.yml
  title: ''
  type: Packages
  url: packages/pokkt-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/packages/pokkt-packages.yml
  title: ''
  type: SDKs
  url: packages/pokkt-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/authentication/pokkt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pokkt-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/conventions/pokkt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pokkt-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/errors/pokkt-error-responses.yml
  title: ''
  type: ErrorCatalog
  url: errors/pokkt-error-responses.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/conformance/pokkt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pokkt-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/asyncapi/pokkt-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pokkt-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/components/pokkt-components.yml
  title: ''
  type: Components
  url: components/pokkt-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/lifecycle/pokkt-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pokkt-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/plans/pokkt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pokkt-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/rate-limits/pokkt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pokkt-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/security/pokkt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pokkt-domain-security.yml
created: '2026-07-17'
description: 'Pokkt is a mobile-first advertising and app monetization platform, part of AnyMind Group, serving app publishers and game developers with SDK-based ad monetization (rewarded video, interstitial, and video advertising) and serving advertisers with performance campaigns, remarketing, and connected-TV (CTV) inventory across India, Southeast Asia, and MENA. Its public API surface is entirely ad-tech: a supply-side Ad Server API at vdo.pokkt.com serving JSON, HTML and VAST responses, a mobile-web rewarded video surface, a server-to-server rewarded-video gratification callback, and a demand-side OpenRTB 2.5/2.6 bid endpoint with global, APAC and US regional hosts. Pokkt publishes an llms.txt-indexed developer wiki and an IAB Tech Lab sellers.json, but no OpenAPI, no OAuth, and no public pricing; the console GraphQL API at api.pokkt.com is authentication-gated and its client SDKs have not been republished since October 2021.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pokkt.png
layout: provider
modified: '2026-08-12'
name: Pokkt
nav: Providers
network: true
overview: 'Pokkt publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Monetization, Mobile, and Video Advertising.


  The Pokkt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pokkt''s developer surface includes documentation, API reference, getting-started guide, authentication, and 18 more developer resources.'
plans:
- name: Pokkt Plans Pricing
  plan_count: 0
  slug: pokkt-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Pokkt Rate Limits
  slug: pokkt-rate-limits
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 81.5
    operational_transparency: 10.5
  previous_composite: 36.9
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/pokkt/refs/heads/main/screenshots/pokkt-2026-09-02T151638.png
security:
- kind: authentication
  name: Pokkt Authentication
  slug: pokkt-authentication
  summary_line: apiKey/custom-hash-signature/undocumented-header · 4 schemes
- kind: domain-security
  name: Pokkt Domain Security
  slug: pokkt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pokkt
tags:
- Company
- Advertising
- Monetization
- Mobile
- Video Advertising
- AdTech
- Remarketing
- OpenRTB
- Programmatic Advertising
- Rewarded Video
- Mobile SDK
- Ad Serving
- Connected TV
- Supply Side Platform
- DSP
website: https://pokkt.com
---
