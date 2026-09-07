---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-09-06'
api_count: 7
apis:
- description: 'Cross-platform video playback (formerly THEOplayer) for web, Android/Fire TV, iOS/tvOS, Roku, React Native and Flutter, with DRM, ad and analytics connectors. A client-side SDK surface: there is no pu'
  name: Dolby OptiView Player
  slug: optiview-player
- baseURL: https://api.theo.live/v2
  baseurl_source: declared
  description: 'THEOlive API v2 - live streaming channel orchestration: channels, ingests, engines, distributions, ABR ladders, schedulers, custom endpoints, webhooks and per-channel analytics. 57 paths / 82 operatio'
  name: Dolby OptiView Live
  slug: optiview-live
- baseURL: https://api.millicast.com
  baseurl_source: declared
  description: 'Millicast API - sub-second WebRTC streaming at scale: publish/subscribe tokens, streams, transcoders, media assets and distributions, recordings, clipping, geo rules, webhooks and analytics. 98 paths '
  name: Dolby OptiView Real-time Streaming (Millicast)
  slug: real-time-millicast
- baseURL: https://director.millicast.com
  baseurl_source: declared
  description: Millicast Director API - the WebRTC/WHIP/WHEP signalling entry point clients call to obtain publish and subscribe endpoints, plus the DRM proxy and multi-track video configuration. 7 paths / 7 operati
  name: Dolby OptiView Director API (Millicast)
  slug: millicast-director
- baseURL: https://analyticsapi.millicast.com
  baseurl_source: declared
  description: Millicast Advanced Analytics API - viewer records for real-time streams, with a v1 and a v2 records endpoint. 2 paths / 2 operations, authenticated with the account API secret.
  name: Dolby OptiView Advanced Analytics API (Millicast)
  slug: millicast-analytics
- baseURL: https://us.ads.optiview.dolby.com
  baseurl_source: declared
  description: 'OptiView Ads API (THEOads) - server-guided ad insertion: channels, ad breaks, events, marker rules, SCTE marker detection, origins, templates and organization integrations. 28 paths / 55 operations un'
  name: Dolby OptiView Ads
  slug: optiview-ads
- baseURL: https://api.galaxy.dolbyrasp.com
  baseurl_source: declared
  description: 'Just-in-time serverless ad conformance service that transcodes an ad from its master format into a streaming format matching the primary content stream. 9 paths / 12 operations, authenticated with an '
  name: Dolby OptiView Ad Engine
  slug: optiview-ad-engine
artifact_total: 15
asyncapis:
- description: ''
  name: Dolby Webhooks
  slug: dolby-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://optiview.dolby.com
- group: other
  title: ''
  type: ParentCompany
  url: https://www.dolby.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://optiview.dolby.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://optiview.dolby.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://optiview.dolby.com/docs/millicast/api/millicast-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://optiview.dolby.com/docs/theolive/api/full-example/
- group: operate
  title: ''
  type: Support
  url: https://support.dolby.io/hc/en-au
- group: company
  title: ''
  type: Blog
  url: https://optiview.dolby.com/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://optiview.dolby.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/THEOplayer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/millicast
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DolbyIO
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dolbylaboratories
- group: commercial
  title: ''
  type: Pricing
  url: https://optiview.dolby.com/plans/
- group: start
  title: ''
  type: Login
  url: https://portal.theoplayer.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://optiview.dolby.com/policies/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://optiview.dolby.com/policies/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dolbyoptiview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dolby.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://optiview.dolby.com/docs/millicast/changelog/changelog-rest-apis/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dolby-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dolby-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dolby-security.txt
- group: auth
  title: ''
  type: Security
  url: security/dolby-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dolby-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dolby-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/dolby-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dolby-packages.yml
- group: design
  title: ''
  type: Components
  url: components/dolby-components.yml
- group: build
  title: ''
  type: CLI
  url: cli/dolby-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dolby-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dolby-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/dolby-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dolby-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dolby-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dolby-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/dolby-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dolby-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dolby-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dolby-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dolby-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dolby-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dolby-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dolby-finops.yml
created: '2025-03-01'
description: Dolby Laboratories is an audio and video technology company whose developer platform, Dolby OptiView, is the merged surface of the original dolby.io platform, THEO Technologies (THEOplayer, THEOlive, THEOads) and Millicast. It ships publicly documented REST APIs for real-time WebRTC streaming, live channel orchestration, video playback, server-guided ad insertion and just-in-time ad conformance, alongside player SDKs for web, mobile, smart TV, Roku, React Native and Flutter. Dolby is also responsible for Dolby Atmos, Dolby Vision and Dolby Digital.
finops:
- name: Dolby Finops
  service_category: API
  slug: dolby-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dolby.png
layout: provider
mcp_servers:
- description: ''
  name: Dolby MCP Server
  slug: dolby-mcp-server
modified: '2026-09-06'
name: Dolby
nav: Providers
network: true
overview: 'Dolby publishes 6 APIs on the [APIs.io](https://apis.io/) network, including OptiView Live, OptiView Real-time Streaming (Millicast), OptiView Director API (Millicast), and 3 more. Tagged areas include Audio, Video, Streaming, Media, and Real-Time.


  The Dolby catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dolby''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 38 more developer resources.'
plans:
- name: Dolby Plans Pricing
  plan_count: 3
  slug: dolby-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Dolby Rate Limits
  slug: dolby-rate-limits
score:
  band: strong
  composite: 64.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 58.0
    catalog_earned_first_party: 20.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 51.5
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 60.3
    developer_ergonomics: 73.2
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 81.6
  previous_composite: 13.4
  provenance:
    conformance: derived
    contracts:
      callable: 71.4
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dolby/refs/heads/main/screenshots/dolby-2026-06-20T180133.png
security:
- kind: authentication
  name: Dolby Authentication
  slug: dolby-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Dolby Domain Security
  slug: dolby-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dolby Vulnerability Disclosure
  slug: dolby-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: dolby
tags:
- Audio
- Video
- Streaming
- Media
- Real-Time
- WebRTC
- Advertising
- Video Player
- Live Streaming
- Broadcasting
website: https://optiview.dolby.com
---
