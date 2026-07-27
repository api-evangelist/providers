---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 78.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Smartnews Agentic Access
  operation_count: 46
  slug: smartnews-agentic-access
  summary_line: 46 operations · 21 acting · 1 human-in-the-loop
api_count: 15
apis:
- description: The ad API from SmartNews — 3 operation(s) for ad.
  name: SmartNews ad API
  slug: smartnews-ad-api
- description: The ad-group API from SmartNews — 4 operation(s) for ad-group.
  name: SmartNews ad-group API
  slug: smartnews-ad-group-api
- description: The article category API from SmartNews — 1 operation(s) for article category.
  name: SmartNews article category API
  slug: smartnews-article-category-api
- description: The campaign API from SmartNews — 2 operation(s) for campaign.
  name: SmartNews campaign API
  slug: smartnews-campaign-api
- description: The catalog API from SmartNews — 4 operation(s) for catalog.
  name: SmartNews catalog API
  slug: smartnews-catalog-api
- description: The channel alias label API from SmartNews — 1 operation(s) for channel alias label.
  name: SmartNews channel alias label API
  slug: smartnews-channel-alias-label-api
- description: The custom-audience API from SmartNews — 4 operation(s) for custom-audience.
  name: SmartNews custom-audience API
  slug: smartnews-custom-audience-api
- description: The developer-app API from SmartNews — 1 operation(s) for developer-app.
  name: SmartNews developer-app API
  slug: smartnews-developer-app-api
- description: The insights API from SmartNews — 2 operation(s) for insights.
  name: SmartNews insights API
  slug: smartnews-insights-api
- description: The interests API from SmartNews — 1 operation(s) for interests.
  name: SmartNews interests API
  slug: smartnews-interests-api
- description: The locations API from SmartNews — 1 operation(s) for locations.
  name: SmartNews locations API
  slug: smartnews-locations-api
- description: The media-file API from SmartNews — 1 operation(s) for media-file.
  name: SmartNews media-file API
  slug: smartnews-media-file-api
- description: The oauth API from SmartNews — 2 operation(s) for oauth.
  name: SmartNews oauth API
  slug: smartnews-oauth-api
- description: The pixel API from SmartNews — 2 operation(s) for pixel.
  name: SmartNews pixel API
  slug: smartnews-pixel-api
- description: The smart view article keyword API from SmartNews — 1 operation(s) for smart view article keyword.
  name: SmartNews smart view article keyword API
  slug: smartnews-smart-view-article-keyword-api
artifact_total: 21
common:
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smartnews-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: https://www.smartnews.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/smartnews-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/smartnews-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smartnews-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartnews-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartnews-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartnews-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartnews.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ads.smartnews.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://ads.smartnews.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://ads.smartnews.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://help-ads.smartnews.com/en/item-4207/
- group: operate
  title: ''
  type: Support
  url: https://help-ads.smartnews.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ads.smartnews.com/developers/tos-en.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smartnews
- group: start
  title: ''
  type: SignUp
  url: https://ads.smartnews.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/smartnews-marketing-openapi.json
- group: design
  title: ''
  type: Conventions
  url: conventions/smartnews-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/smartnews-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smartnews-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/smartnews-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/smartnews-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/smartnews-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/smartnews-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/smartnews-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smartnews-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: SmartNews is a news-discovery company whose consumer app ranks and delivers news to tens of millions of readers in Japan and the United States. For developers it operates the SmartNews Ads platform and publishes the SmartNews Marketing API (v3) — a REST API for programmatically managing advertising campaigns, ad groups, ads, media files, custom audiences, conversion pixels, and Business Manager product catalogs, plus an Insights API for performance reporting. The API uses OAuth 2.0 bearer (JWT) access tokens and is documented with a public OpenAPI 3.0 reference and an official API-spec repository.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartnews.png
layout: provider
mcp_servers:
- description: ''
  name: smartnews-mcp.yml
  slug: smartnews-mcpyml
modified: '2026-07-21'
name: SmartNews
nav: Providers
network: true
overview: 'SmartNews publishes 15 APIs on the [APIs.io](https://apis.io/) network, including ad API, ad-group API, article category API, and 12 more. Tagged areas include Company, Consumer, News, Advertising, and AdTech.


  SmartNews'' developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, changelog, and 21 more developer resources.'
random_paper: 44
rate_limits:
- limit_count: 2
  name: Smartnews Rate Limits
  slug: smartnews-rate-limits
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 60.8
    developer_ergonomics: 65.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 49.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Smartnews Authentication
  slug: smartnews-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smartnews Domain Security
  slug: smartnews-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Smartnews Vulnerability Disclosure
  slug: smartnews-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: smartnews
tags:
- Company
- Consumer
- News
- Advertising
- AdTech
- Marketing
- Media
- Campaign Management
website: https://www.smartnews.com
---
