---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 37
  human_in_the_loop: 1
  name: Outbrain Agentic Access
  operation_count: 105
  slug: outbrain-agentic-access
  summary_line: 105 operations · 37 acting · 1 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Token-based authentication
  name: Outbrain Authentication API
  slug: outbrain-authentication-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Budget management
  name: Outbrain Budgets API
  slug: outbrain-budgets-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Campaign management
  name: Outbrain Campaigns API
  slug: outbrain-campaigns-api
- baseURL: https://r.teads.tv
  baseurl_source: declared
  description: Server-side conversion events
  name: Outbrain Conversions API
  slug: outbrain-conversions-api
- baseURL: https://odb.outbrain.com
  baseurl_source: declared
  description: Impression and click events
  name: Outbrain Events API
  slug: outbrain-events-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Marketer (customer account) resources
  name: Outbrain Marketers API
  slug: outbrain-marketers-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Promoted link (ad creative) management
  name: Outbrain PromotedLinks API
  slug: outbrain-promotedlinks-api
- baseURL: https://odb.outbrain.com
  baseurl_source: declared
  description: Retrieve content recommendations
  name: Outbrain Recommendations API
  slug: outbrain-recommendations-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Performance reporting
  name: Outbrain Reporting API
  slug: outbrain-reporting-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Audience and contextual targeting
  name: Outbrain Targeting API
  slug: outbrain-targeting-api
- description: Contextual sponsored-recommendation API for chatbot and LLM publishers, backing the Teads Conversational AI Ads SDK (public beta since 2025-11-12). Takes a partner key plus one of contentUrl / bundleU
  name: Teads In-Chat API
  slug: outbrain-teads-in-chat-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Token Obtaining a token should be your 1st step toward using Amplify API. You need to include it in all further requests using the HTTP Header OB-TOKEN-V1. In order to protect your privacy, the tokens
  name: Outbrain Authentications API
  slug: outbrain-authentications-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Metadata about the available currencies
  name: Outbrain Currencies API
  slug: outbrain-currencies-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: GeoLocations are representatives of Outbrain Geographic Locations. GeoLocations are being used for campaigns to be targeted (or excluded) by geography. The GeoLocation object has the following attribu
  name: Outbrain Geo Locations API
  slug: outbrain-geo-locations-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'IAB category Targeting gives you the abillity to select your preferred IAB categories in your campaign setup. The IAB category Targeting object has the following attributes: Property Type Semantic Exa'
  name: Outbrain IAB category Targeting API
  slug: outbrain-iab-category-targeting-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Interest Targeting gives you the abillity to select your preferred interests categories in your campaign setup. Then, using our powerful interest insights and predictive technology, we’ll match you wi
  name: Outbrain Interest Targeting API
  slug: outbrain-interest-targeting-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: The Meta Data section represents the various values (Enumarations) that can be provided as part of the different API end-points
  name: Outbrain Meta Data API
  slug: outbrain-meta-data-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'Multiple Conversions gives the ability to track any of the actions a user takes after clicking through to your content. You can track everything from top of funnel (page landings and time on site) to '
  name: Outbrain Multiple Conversions API
  slug: outbrain-multiple-conversions-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'There are a multitude of reporting endpoints that allow you to retrieve metrics at various levels of granularity. Note: All performance reports have a 10-30 minutes delay, therefore performance metric'
  name: Outbrain Performance Reporting API
  slug: outbrain-performance-reporting-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'Sequences comes in 2 formats: - Carousel - multi-promotedLink format that features CTA buttons, brand logo, and more. You can use Carousel to tell your brand story, showcase multiple products, and bui'
  name: Outbrain Promoted Links Sequences API
  slug: outbrain-promotedlinkssequences-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: A Section is a specific content within the publisher's site such as sports, business etc.
  name: Outbrain Sections API
  slug: outbrain-sections-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'Segments give the ability to segment customers based on their actions, and retarget them with new or existing campaigns. This translates into your campaigns reaching a highly engaged audience that is '
  name: Outbrain Segments API
  slug: outbrain-segments-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: User represents a single person's access to Outbrain services and to the site my.outbrain.com. A User is permitted to one or more Marketer accounts, each marketer with a role that specifies the user p
  name: Outbrain Users API
  slug: outbrain-users-api
artifact_total: 85
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
  type: X-MCPServerCandidate
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
modified: '2026-08-13'
name: Outbrain
nav: Providers
network: true
overview: 'Outbrain publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Budgets API, Campaigns API, and 19 more. Tagged areas include Advertising, Native Advertising, Open Web, CTV, and Connected TV.


  The Outbrain catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Outbrain''s developer surface includes authentication, developer portal, documentation, signup flow, training material, engineering blog, support, and 76 more developer resources.'
plans:
- name: Outbrain Plans Pricing
  plan_count: 4
  slug: outbrain-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 7
  name: Outbrain Rate Limits
  slug: outbrain-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Outbrain API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: outbrain-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: Outbrain API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: outbrain-rules
score:
  band: exemplar
  composite: 71.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 91.5
    catalog_earned_first_party: 24.0
    catalog_gap: 23.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 33.3
    contract_quality: 70.5
    developer_ergonomics: 83.9
    discoverability: 68.5
    governance: 33.3
    operational_transparency: 63.2
  previous_composite: 72.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
website: https://developers.teads.com
---
