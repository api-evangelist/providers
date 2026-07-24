---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Outbrain Agentic Access
  operation_count: 24
  slug: outbrain-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 10
apis:
- description: Token-based authentication
  name: Outbrain Authentication API
  slug: outbrain-authentication-api
- description: Budget management
  name: Outbrain Budgets API
  slug: outbrain-budgets-api
- description: Campaign management
  name: Outbrain Campaigns API
  slug: outbrain-campaigns-api
- description: Server-side conversion events
  name: Outbrain Conversions API
  slug: outbrain-conversions-api
- description: Impression and click events
  name: Outbrain Events API
  slug: outbrain-events-api
- description: Marketer (customer account) resources
  name: Outbrain Marketers API
  slug: outbrain-marketers-api
- description: Promoted link (ad creative) management
  name: Outbrain PromotedLinks API
  slug: outbrain-promotedlinks-api
- description: Retrieve content recommendations
  name: Outbrain Recommendations API
  slug: outbrain-recommendations-api
- description: Performance reporting
  name: Outbrain Reporting API
  slug: outbrain-reporting-api
- description: Audience and contextual targeting
  name: Outbrain Targeting API
  slug: outbrain-targeting-api
artifact_total: 49
collections:
- collection_type: open
  name: Outbrain Amplify API
  slug: open-outbrain-amplify-api
- collection_type: open
  name: Outbrain Engage API
  slug: open-outbrain-engage-api
- collection_type: open
  name: Teads Advertiser Conversion API
  slug: open-outbrain-teads-conversion-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/outbrain-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/outbrain-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/outbrain-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outbrain-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/outbrain-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.outbrain.com
- group: start
  title: ''
  type: Portal
  url: https://www.teads.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/apis/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/home-page/amplify-api/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/home-page/amplify-api/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://amplifyv01.docs.apiary.io/
- group: docs
  title: ''
  type: Documentation
  url: https://teadsapi.docs.apiary.io/
- group: start
  title: ''
  type: Signup
  url: https://www.outbrain.com/partner-api/
- group: start
  title: ''
  type: Signup
  url: https://developer.outbrain.com/home-page/amplify-api/apply/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/outbrain-javascript-implementation-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/apis/outbrain-js-api-guide/
- group: build
  title: ''
  type: SDKs
  url: https://sdk.outbrain.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.outbrain.com/help/advertisers/amplify-api/
- group: learn
  title: ''
  type: Training
  url: https://academy.teads.com
- group: company
  title: ''
  type: Blog
  url: https://engineering.teads.com
- group: company
  title: ''
  type: Blog
  url: https://blog.outbrain.com
- group: company
  title: ''
  type: Blog
  url: https://www.outbrain.com/blog/
- group: company
  title: ''
  type: Blog
  url: https://www.teads.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://investors.teads.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.outbrain.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.outbrain.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.outbrain.com/help/
- group: operate
  title: ''
  type: Forums
  url: https://groups.google.com/g/outbrain-amplifyapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/outbrain
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teads
- group: build
  title: ''
  type: SDKs
  url: https://github.com/teads/TeadsSDK-iOS
- group: build
  title: ''
  type: SDKs
  url: https://github.com/teads/TeadsSDK-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/teads/TeadsSDK-ReactNative
- group: build
  title: ''
  type: Tools
  url: https://github.com/teads/teads-gtm-template
- group: build
  title: ''
  type: Tools
  url: https://github.com/teads/teads-advertiser-conversion-api-gtm-template
- group: build
  title: ''
  type: Tools
  url: https://github.com/teads/prebid-server-fork
- group: build
  title: ''
  type: Tools
  url: https://github.com/outbrain/go-secretcrypt
- group: build
  title: ''
  type: Tools
  url: https://github.com/outbrain/gracefulshutdown
- group: build
  title: ''
  type: Tools
  url: https://github.com/outbrain/elasticsearch_exporter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/outbrain
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/outbrain
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/teads
- group: commercial
  title: ''
  type: Plans
  url: plans/outbrain-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/outbrain-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/outbrain-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/outbrain-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/outbrain-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: Outbrain Inc. (NASDAQ&#58; OB), which closed its acquisition of Teads in early 2025 and now operates publicly as Teads, is one of the largest open-internet advertising platforms — reaching 2 billion+ consumers per month across 50+ markets, with 20,000+ direct advertisers and 10,000+ premium media properties. The combined company spans open-web native (Outbrain Amplify), premium video, display, and Connected TV (Teads), powered by a Predictive AI engine and an omnichannel data graph. Developer surface area centers on the Amplify API (campaign management + reporting), the Engage API (publisher content recommendations and the JS Widget / Mobile SDK), and a server-side Conversion API for cookieless measurement and optimization.
examples:
- key_count: 2
  name: Outbrain List Campaigns Example
  slug: outbrain-list-campaigns-example
- key_count: 2
  name: Outbrain Realtime Report Example
  slug: outbrain-realtime-report-example
features:
- Outbrain Amplify — open-web native advertising platform with self-service and managed offerings
- Teads — premium video, display, and CTV inventory across 10,000+ media environments in 50+ markets
- Combined open-internet platform reaching 2B+ consumers/month with 20,000+ direct advertisers
- Amplify API for programmatic campaign management — Marketer, Campaign, PromotedLink, Budget, Targeting
- Performance and real-time reporting APIs (10 req/min and 50 req/min per marketer)
- OB-TOKEN-V1 bearer authentication acquired via /login HTTP Basic
- Engage API for publisher-side content recommendations (organic + paid)
- JS Widget for web (WordPress, GAM, mediation guides) and Mobile SDK for iOS / Android / React Native / Flutter
- Conversion API (server-to-server) for cookieless conversion measurement and Predictive AI optimization
- Teads Conversion API GTM server-side template (open source)
- Teads SDKs for iOS, Android, and React Native (open source on github.com/teads)
- Prebid Server fork on github.com/teads for OpenRTB / programmatic integrations
- Predictive AI engine — 1B predictions/sec across 500+ microservices, 18B ad opportunities/day, 8M req/sec
- Omnichannel Graph with audience, contextual, conversion, and purchase signals
- High-impact creative formats via Teads Studio (outstream, InRead, CTV)
- Conversion Bid Strategy for goal-based bidding in Amplify
- Direct IO, PMP deals, and open exchange paths for buy-side integrations
- Headquartered in NYC and managed in the US; combined company trades NASDAQ&#58; OB; brand consolidated as Teads
- Engineering hubs in Paris, Netanya, Montpellier, Ljubljana
finops:
- name: Outbrain Finops
  service_category: Advertising and Marketing
  slug: outbrain-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/outbrain.png
json_schemas:
- name: Outbrain Amplify Campaign
  property_count: 12
  slug: outbrain-campaign
- name: Outbrain Amplify Promoted Link
  property_count: 9
  slug: outbrain-promoted-link
- name: Outbrain Engage Recommendation
  property_count: 8
  slug: outbrain-recommendation
json_structures:
- name: Outbrain Campaign Structure
  property_count: 1
  slug: outbrain-campaign-structure
jsonld:
- class_count: 14
  name: Outbrain Context
  property_count: 8
  slug: outbrain-context
layout: provider
modified: '2026-05-25'
name: Outbrain
nav: Providers
network: true
overview: 'Outbrain publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Budgets API, Campaigns API, and 7 more. Tagged areas include Advertising, Native Advertising, Open Web, CTV, and Connected TV.


  The Outbrain catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Outbrain''s developer surface includes authentication, developer portal, documentation, signup flow, training material, engineering blog, support, and 42 more developer resources.'
plans:
- name: Outbrain Plans Pricing
  plan_count: 4
  slug: outbrain-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Outbrain Rate Limits
  slug: outbrain-rate-limits
rules:
- name: Outbrain API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: outbrain-jsonschema-spectral-rules
- name: Outbrain API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: outbrain-rules
score:
  band: strong
  composite: 61.7
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 64.4
    developer_ergonomics: 50.0
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 61.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/outbrain/refs/heads/main/screenshots/outbrain-2026-06-20T191227.png
security:
- kind: authentication
  name: Outbrain Authentication
  slug: outbrain-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Outbrain Domain Security
  slug: outbrain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Outbrain Vulnerability Disclosure
  slug: outbrain-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Outbrain Trust Center
  slug: outbrain-trust-center
  summary_line: SOC 2, ISO 27001
slug: outbrain
tags:
- Advertising
- Native Advertising
- Open Web
- CTV
- Connected TV
- Video Advertising
- Content Discovery
- Programmatic
- Performance Marketing
- AdTech
- Teads
website: https://www.outbrain.com
---
