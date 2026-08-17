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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 65.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 37
  human_in_the_loop: 1
  name: Outbrain Agentic Access
  operation_count: 105
  slug: outbrain-agentic-access
  summary_line: 105 operations · 37 acting · 1 human-in-the-loop
api_count: 13
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
- description: The complete Outbrain Amplify API surface — 77 operations across marketers, budgets, campaigns, promoted links and promoted-link sequences, audience segments, conversion events, user and invitation ma
  name: Outbrain Amplify API
  slug: outbrain-amplify-api
- description: Asynchronous analytics reporting for the Teads platform. A POST triggers a report that is computed in the background; a GET polls its status and returns a download URL for the finished CSV, JSON or XL
  name: Teads Report API
  slug: outbrain-teads-report-api
- description: Contextual sponsored-recommendation API for chatbot and LLM publishers, backing the Teads Conversational AI Ads SDK (public beta since 2025-11-12). Takes a partner key plus one of contentUrl / bundleU
  name: Teads In-Chat API
  slug: outbrain-teads-in-chat-api
artifact_total: 76
collections:
- collection_type: postman
  name: Outbrain Amplify Authentication API
  slug: postman-outbrain-authentication-api
- collection_type: postman
  name: Outbrain Amplify Authentication Budgets API
  slug: postman-outbrain-budgets-api
- collection_type: postman
  name: Outbrain Amplify Authentication Campaigns API
  slug: postman-outbrain-campaigns-api
- collection_type: postman
  name: Outbrain Amplify Authentication Conversions API
  slug: postman-outbrain-conversions-api
- collection_type: postman
  name: Outbrain Amplify Authentication Events API
  slug: postman-outbrain-events-api
- collection_type: postman
  name: Outbrain Amplify Authentication Marketers API
  slug: postman-outbrain-marketers-api
- collection_type: postman
  name: Outbrain Amplify Authentication PromotedLinks API
  slug: postman-outbrain-promotedlinks-api
- collection_type: postman
  name: Outbrain Amplify Authentication Recommendations API
  slug: postman-outbrain-recommendations-api
- collection_type: postman
  name: Outbrain Amplify Authentication Reporting API
  slug: postman-outbrain-reporting-api
- collection_type: postman
  name: Outbrain Amplify Authentication Targeting API
  slug: postman-outbrain-targeting-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Outbrain Amplify API
  slug: open-outbrain-amplify-api-full
- collection_type: open
  name: Outbrain Amplify API
  slug: open-outbrain-amplify-api
- collection_type: open
  name: Outbrain Amplify Authentication API
  slug: open-outbrain-authentication-api
- collection_type: open
  name: Outbrain Amplify Authentication Budgets API
  slug: open-outbrain-budgets-api
- collection_type: open
  name: Outbrain Amplify Authentication Campaigns API
  slug: open-outbrain-campaigns-api
- collection_type: open
  name: Outbrain Amplify Authentication Conversions API
  slug: open-outbrain-conversions-api
- collection_type: open
  name: Outbrain Engage API
  slug: open-outbrain-engage-api
- collection_type: open
  name: Outbrain Amplify Authentication Events API
  slug: open-outbrain-events-api
- collection_type: open
  name: Outbrain Amplify Authentication Marketers API
  slug: open-outbrain-marketers-api
- collection_type: open
  name: Outbrain Amplify Authentication PromotedLinks API
  slug: open-outbrain-promotedlinks-api
- collection_type: open
  name: Outbrain Amplify Authentication Recommendations API
  slug: open-outbrain-recommendations-api
- collection_type: open
  name: Outbrain Amplify Authentication Reporting API
  slug: open-outbrain-reporting-api
- collection_type: open
  name: Outbrain Amplify Authentication Targeting API
  slug: open-outbrain-targeting-api
- collection_type: open
  name: Teads Advertiser Conversion API
  slug: open-outbrain-teads-conversion-api
- collection_type: open
  name: Teads Report API
  slug: open-outbrain-teads-report-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/outbrain/overview
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
- group: build
  title: ''
  type: Packages
  url: packages/outbrain-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/outbrain-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/outbrain-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/outbrain-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.outbrain.com/security/bug-bounty/
- group: auth
  title: ''
  type: Compliance
  url: https://www.outbrain.com/security/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/outbrain-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/outbrain-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/outbrain-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/outbrain-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/outbrain-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/outbrain-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/outbrain-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/outbrain-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://amplifyv01.docs.apiary.io/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/outbrain-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/outbrain-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/outbrain-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/outbrain-amplify-api-full-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/outbrain-teads-report-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.teads.com
- group: docs
  title: ''
  type: APIReference
  url: https://amplifyv01.docs.apiary.io/
- group: docs
  title: ''
  type: APIReference
  url: https://teadsapi.docs.apiary.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.teads.com/docs/category/start-here
- group: operate
  title: ''
  type: Support
  url: https://support.teads.com
- group: operate
  title: ''
  type: Support
  url: https://groups.google.com/g/outbrain-amplifyapi
- group: start
  title: ''
  type: SignUp
  url: https://www.outbrain.com/partner-api/
- group: start
  title: ''
  type: Login
  url: https://my.outbrain.com/create-token
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teads.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teads.com/privacy-policy/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/teads/TeadsSDK-iOS
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/teads/TeadsSDK-android
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
mcp_servers:
- description: ''
  name: outbrain-mcp.yml
  slug: outbrain-mcpyml
modified: '2026-08-13'
name: Outbrain
nav: Providers
network: true
overview: 'Outbrain publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Budgets API, Campaigns API, and 9 more. Tagged areas include Advertising, Native Advertising, Open Web, CTV, and Connected TV.


  The Outbrain catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Outbrain''s developer surface includes authentication, developer portal, documentation, signup flow, training material, engineering blog, support, and 76 more developer resources.'
plans:
- name: Outbrain Plans Pricing
  plan_count: 4
  slug: outbrain-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 7
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
  band: exemplar
  composite: 83.5
  delta: 18.4
  facets:
    commercial_clarity: 89.5
    contract_quality: 74.6
    developer_ergonomics: 93.5
    discoverability: 92.6
    governance: 89.6
    operational_transparency: 63.2
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
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
website: https://developers.teads.com
---
