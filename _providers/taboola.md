---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Taboola Agentic Access
  operation_count: 60
  slug: taboola-agentic-access
  summary_line: 60 operations · 22 acting
api_count: 16
apis:
- description: The Accounts API from Taboola — 3 operation(s) for accounts.
  name: Taboola Accounts API
  slug: taboola-accounts-api
- description: The Audience Targeting API from Taboola — 1 operation(s) for audience targeting.
  name: Taboola Audience Targeting API
  slug: taboola-audience-targeting-api
- description: Bulk create, update, and delete items across campaigns.
  name: Taboola Bulk Items API
  slug: taboola-bulk-items-api
- description: Bulk update or create campaigns across accounts on the network.
  name: Taboola Bulk Operations API
  slug: taboola-bulk-operations-api
- description: Standard ad items (creatives) belonging to a campaign.
  name: Taboola Campaign Items API
  slug: taboola-campaign-items-api
- description: Create, retrieve, update, duplicate, and delete advertising campaigns.
  name: Taboola Campaigns API
  slug: taboola-campaigns-api
- description: The Combined Audiences API from Taboola — 2 operation(s) for combined audiences.
  name: Taboola Combined Audiences API
  slug: taboola-combined-audiences-api
- description: The Conversion Rules API from Taboola — 4 operation(s) for conversion rules.
  name: Taboola Conversion Rules API
  slug: taboola-conversion-rules-api
- description: The Custom Audiences API from Taboola — 1 operation(s) for custom audiences.
  name: Taboola Custom Audiences API
  slug: taboola-custom-audiences-api
- description: The Dictionary API from Taboola — 16 operation(s) for dictionary.
  name: Taboola Dictionary API
  slug: taboola-dictionary-api
- description: The First Party Audiences API from Taboola — 3 operation(s) for first party audiences.
  name: Taboola First Party Audiences API
  slug: taboola-first-party-audiences-api
- description: The Lookalike Audiences API from Taboola — 1 operation(s) for lookalike audiences.
  name: Taboola Lookalike Audiences API
  slug: taboola-lookalike-audiences-api
- description: The Marketplace Audiences API from Taboola — 1 operation(s) for marketplace audiences.
  name: Taboola Marketplace Audiences API
  slug: taboola-marketplace-audiences-api
- description: Estimate reach for campaign targeting before launching.
  name: Taboola Reach Estimator API
  slug: taboola-reach-estimator-api
- description: The Reports API from Taboola — 3 operation(s) for reports.
  name: Taboola Reports API
  slug: taboola-reports-api
- description: Performance video items (motion ads).
  name: Taboola Video Items API
  slug: taboola-video-items-api
artifact_total: 72
collections:
- collection_type: postman
  name: Taboola Backstage Accounts API
  slug: postman-taboola-accounts-api
- collection_type: postman
  name: Taboola Backstage Accounts Audience Targeting API
  slug: postman-taboola-audience-targeting-api
- collection_type: postman
  name: Taboola Backstage Accounts Bulk Items API
  slug: postman-taboola-bulk-items-api
- collection_type: postman
  name: Taboola Backstage Accounts Bulk Operations API
  slug: postman-taboola-bulk-operations-api
- collection_type: postman
  name: Taboola Backstage Accounts Campaign Items API
  slug: postman-taboola-campaign-items-api
- collection_type: postman
  name: Taboola Backstage Accounts Campaigns API
  slug: postman-taboola-campaigns-api
- collection_type: postman
  name: Taboola Backstage Accounts Combined Audiences API
  slug: postman-taboola-combined-audiences-api
- collection_type: postman
  name: Taboola Backstage Accounts Conversion Rules API
  slug: postman-taboola-conversion-rules-api
- collection_type: postman
  name: Taboola Backstage Accounts Custom Audiences API
  slug: postman-taboola-custom-audiences-api
- collection_type: postman
  name: Taboola Backstage Accounts Dictionary API
  slug: postman-taboola-dictionary-api
- collection_type: postman
  name: Taboola Backstage Accounts First Party Audiences API
  slug: postman-taboola-first-party-audiences-api
- collection_type: postman
  name: Taboola Backstage Accounts Lookalike Audiences API
  slug: postman-taboola-lookalike-audiences-api
- collection_type: postman
  name: Taboola Backstage Accounts Marketplace Audiences API
  slug: postman-taboola-marketplace-audiences-api
- collection_type: postman
  name: Taboola Backstage Accounts Reach Estimator API
  slug: postman-taboola-reach-estimator-api
- collection_type: postman
  name: Taboola Backstage Accounts Reports API
  slug: postman-taboola-reports-api
- collection_type: postman
  name: Taboola Backstage Accounts Video Items API
  slug: postman-taboola-video-items-api
- collection_type: open
  name: Taboola Backstage Accounts API
  slug: open-taboola-backstage-accounts-api
- collection_type: open
  name: Taboola Backstage Audiences API
  slug: open-taboola-backstage-audiences-api
- collection_type: open
  name: Taboola Backstage Campaigns API
  slug: open-taboola-backstage-campaigns-api
- collection_type: open
  name: Taboola Backstage Conversions API
  slug: open-taboola-backstage-conversions-api
- collection_type: open
  name: Taboola Backstage Dictionary API
  slug: open-taboola-backstage-dictionary-api
- collection_type: open
  name: Taboola Backstage Campaign Items API
  slug: open-taboola-backstage-items-api
- collection_type: open
  name: Taboola Backstage Reports API
  slug: open-taboola-backstage-reports-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/taboola/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taboola-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/taboola-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taboola-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taboola-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.taboola.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.taboola.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.taboola.com/backstage-api/reference
- group: docs
  title: ''
  type: Documentation
  url: https://developers.taboola.com/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: https://developers.taboola.com/backstage-api/reference/authentication-basics
- group: auth
  title: ''
  type: Authentication
  url: https://developers.taboola.com/backstage-api/reference/client-credentials-flow
- group: auth
  title: ''
  type: Authentication
  url: https://developers.taboola.com/backstage-api/reference/getting-an-access-token
- group: auth
  title: ''
  type: Authentication
  url: https://backstage.taboola.com/backstage/oauth/token
- group: other
  title: ''
  type: BaseURL
  url: https://backstage.taboola.com/backstage/api/1.0
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taboola
- group: build
  title: ''
  type: SDKs
  url: https://github.com/taboola/backstage-api-java-client
- group: build
  title: ''
  type: Tools
  url: https://github.com/taboola/realize-mcp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/taboola/taboola-spm-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/taboola/taboola-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/taboola/taboola-flutter-example
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/taboola/ios-sdk-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/taboola/android-sdk-examples-4x
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/taboola/react-native-examples-3x
- group: build
  title: ''
  type: SDKs
  url: https://github.com/taboola/ios-adx
- group: build
  title: ''
  type: Tools
  url: https://github.com/taboola/Prebid.js
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.taboola.com/legal-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.taboola.com/policies/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.taboola.com/
- group: operate
  title: ''
  type: Support
  url: https://help.taboola.com/
- group: company
  title: ''
  type: Blog
  url: https://www.taboola.com/blog
- group: company
  title: ''
  type: News
  url: https://www.taboola.com/press
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.taboola.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taboola
- group: company
  title: ''
  type: X-Twitter
  url: https://x.com/taboola
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/taboola
- group: start
  title: ''
  type: Login
  url: https://realize.taboola.com/
- group: start
  title: ''
  type: Portal
  url: https://www.taboola.com/products/realize
- group: start
  title: ''
  type: Portal
  url: https://www.taboola.com/abby
- group: start
  title: ''
  type: Portal
  url: https://www.taboola.com/products/genai-ad-maker
- group: start
  title: ''
  type: Portal
  url: https://www.taboola.com/products/deeperdive
- group: start
  title: ''
  type: Portal
  url: https://www.taboola.com/products/connexity
- group: start
  title: ''
  type: Portal
  url: https://www.taboola.com/products/skimlinks
- group: start
  title: ''
  type: Portal
  url: https://www.taboola.com/products/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://developers.taboola.com/taboolasdk/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.taboola.com/dynamic-creative/docs/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/taboola-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taboola-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/taboola-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: 'Taboola (NASDAQ: TBLA) is a New-York-headquartered native and discovery advertising company founded in 2007 by Adam Singolda. Its Realize performance marketing platform serves recommendation widgets across major publishers (a 30-year exclusive partnership with Yahoo since 2022) and offers advertisers programmatic access via the Backstage API for campaign management, audience targeting, conversion tracking, and reporting. The company also operates Connexity (commerce media), Skimlinks (publisher monetization), and DeeperDive (content discovery), and recently shipped Abby (AI ad assistant), the GenAI Ad Maker, and an official Realize MCP server for AI-driven campaign management.'
features:
- Realize performance advertising platform with native, display, carousel, video, and app-promotion formats
- Backstage API — OAuth 2.0 client credentials, base URL https://backstage.taboola.com/backstage/api/1.0
- Campaign CRUD plus duplicate, bulk update, and network-wide campaign list endpoints
- Campaign reach estimator for impression forecasting before launch
- Campaign item (creative) and performance video item (motion ad) management
- First-party, lookalike, marketplace, custom, combined, and contextual audience targeting
- Country, region, city, postal-code, US DMA, platform, OS, browser, language, and publisher targeting
- Conversion rules (event-based and URL-based) with click-through and view-through look-back windows
- Reports API with day/week/month and campaign/site/country/platform/ad breakdowns plus top-content and real-time
- Dictionary endpoints for reference data needed by campaign targeting
- Network-account model for agencies/DSPs managing many advertisers
- Bid strategies including Fixed CPC, SmartBid (Enhanced CPC), Maximize Conversions, and Target CPA
- Mobile SDKs for iOS, Android, Flutter, React Native
- Java client SDK (backstage-api-java-client)
- Official MCP server (realize-mcp) wrapping the Backstage/Realize API with OAuth 2.1 SSO support
- Conversion tracking via Taboola pixel or server-to-server integration
- Dynamic Creative for personalized ads (GTM, JS API, S2S flows)
- Abby AI ad assistant and GenAI Ad Maker for creative automation
- DeeperDive content discovery, Newsroom analytics, Connexity commerce media, and Skimlinks affiliate monetization
- Yahoo native exclusive integration (30-year agreement signed 2022)
- Prebid.js header-bidding integration
finops:
- name: Taboola Finops
  service_category: Marketing and Advertising
  slug: taboola-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taboola.png
json_schemas:
- name: Taboola Campaign
  property_count: 26
  slug: taboola-campaign
- name: Taboola Conversion Rule
  property_count: 14
  slug: taboola-conversion-rule
- name: Taboola Campaign Item
  property_count: 12
  slug: taboola-item
jsonld:
- class_count: 33
  name: Taboola Context
  property_count: 4
  slug: taboola-context
layout: provider
modified: '2026-05-25'
name: Taboola
nav: Providers
network: true
overview: 'Taboola publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Audience Targeting API, Bulk Items API, and 13 more. Tagged areas include Advertising, Native Advertising, Discovery, Performance Marketing, and AdTech.


  The Taboola catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Taboola''s developer surface includes authentication, developer portal, documentation, tooling, code examples, support, engineering blog, and 41 more developer resources.'
plans:
- name: Taboola Plans Pricing
  plan_count: 2
  slug: taboola-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Taboola Rate Limits
  slug: taboola-rate-limits
rules:
- name: Taboola API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: taboola-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.6
  delta: -2.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.5
    developer_ergonomics: 54.3
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taboola/refs/heads/main/screenshots/taboola-2026-06-20T194849.png
security:
- kind: authentication
  name: Taboola Authentication
  slug: taboola-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Taboola Domain Security
  slug: taboola-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Taboola Vulnerability Disclosure
  slug: taboola-vulnerability-disclosure
  summary_line: disclosure policy published
slug: taboola
tags:
- Advertising
- Native Advertising
- Discovery
- Performance Marketing
- AdTech
- Realize
- Backstage
- Recommendation
- Publisher
- Programmatic
website: https://www.taboola.com
---
