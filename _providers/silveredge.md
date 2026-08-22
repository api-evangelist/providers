---
access_model:
  confidence: medium
  label: Partner
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://docs.prebid.org/dev-docs/bidders/silverpush.html
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Silverpush's first-party programmatic bid endpoint, registered upstream in the Prebid ecosystem under the bidder code "silverpush" and maintained from prebid@silverpush.co. It speaks OpenRTB over HTTP
  name: Silverpush Prebid Bidder (Chocolate Ad Exchange)
  slug: silverpush-prebid-bidder-chocolate-ad-exchange
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://silverpush.co
- group: start
  title: ''
  type: Portal
  url: https://chocolateplatform.com/
- group: docs
  title: ''
  type: Documentation
  url: https://chocolateplatform.com/download-sdk
- group: docs
  title: ''
  type: APIReference
  url: https://docs.prebid.org/dev-docs/bidders/silverpush.html
- group: operate
  title: ''
  type: Support
  url: https://silverpush.co/contact/
- group: company
  title: ''
  type: Blog
  url: https://silverpush.co/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SilverPush
- group: start
  title: ''
  type: SignUp
  url: https://chocolateplatform.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://silverpush.co/terms-services/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://silverpush.co/privacy-policy/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/silveredge-prebid-bidder-params.json
- group: build
  title: ''
  type: Packages
  url: packages/silveredge-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/silveredge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/silveredge-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/silveredge-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/silveredge-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/silveredge-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silveredge-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/silveredge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/silveredge-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silveredge-llms.txt
created: '2026-07-17'
description: 'Silveredge is SilverEdge Technologies, the operating entity behind the Silverpush brand — an AI-powered contextual intelligence and video advertising company backed by 500 Global, whose corporate site is silverpush.co. Silverpush sells Mirrors, a contextual intelligence suite for brand-safe video advertising across YouTube, CTV, TikTok, Meta and the open web, and Parallels, a moment-marketing platform. It also operates Chocolate Platform (chocolateplatform.com), the mobile video SSP it acquired with Vdopia, which is publicly branded "Chocolate Platform by SilverPush". Its machine-readable API surface is programmatic rather than REST: Silverpush maintains a first-party OpenRTB bid endpoint registered upstream in Prebid Server and Prebid.js under the bidder code "silverpush", with a published JSON Schema for its bid parameters and a maintainer address of prebid@silverpush.co. Chocolate also documents a first-party mobile mediation SDK for Android, iOS, Unity, Xamarin, Cordova
  and Cocos2d-x, with public sample apps on GitHub — though every distribution channel that surface advertises now fails to resolve. There is no public REST API, OpenAPI, developer portal, MCP server, agent card or /.well-known discovery surface on any host this company controls.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/silveredge.png
json_schemas:
- name: Silverpush OpenRTB Bidder Adapter
  property_count: 2
  slug: silveredge-prebid-bidder-params
layout: provider
modified: '2026-08-12'
name: Silveredge
nav: Providers
network: true
overview: 'Silveredge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Contextual Intelligence, and Artificial Intelligence.


  Silveredge''s developer surface includes developer portal, documentation, API reference, support, engineering blog, signup flow, authentication, and 14 more developer resources.'
plans:
- name: Silveredge Plans Pricing
  plan_count: 0
  slug: silveredge-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Silveredge Rate Limits
  slug: silveredge-rate-limits
score:
  band: thin
  composite: 28.2
  delta: -1.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 8.5
    developer_ergonomics: 45.2
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 30.0
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Silveredge Authentication
  slug: silveredge-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Silveredge Domain Security
  slug: silveredge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: silveredge
tags:
- Company
- Advertising
- AdTech
- Contextual Intelligence
- Artificial Intelligence
- Video Advertising
- Marketing
- Programmatic Advertising
- OpenRTB
- Prebid
- Supply Side Platform
- CTV
- Mobile Advertising
- Brand Safety
website: https://silverpush.co
---
