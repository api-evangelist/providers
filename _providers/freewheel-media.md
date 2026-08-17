---
access_model:
  confidence: high
  label: Enterprise / contract only
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://www.freewheel.com/pricing
  - https://api-docs.freewheel.tv/demand/docs/demand-api-authentication
  - https://www.freewheel.com/legal/master-services-agreement
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 111
  human_in_the_loop: 0
  name: Freewheel Media Agentic Access
  operation_count: 171
  slug: freewheel-media-agentic-access
  summary_line: 171 operations · 111 acting
api_count: 5
apis:
- description: The REST API behind FreeWheel's Advertiser Suite / Beeswax DSP ("Buzz"). It exposes the full buy-side object model — accounts, advertisers, campaigns, line items, creatives and creative assets, target
  name: FreeWheel Advertiser (Buzz) API
  slug: freewheel-media-advertiser-buzz-api
- description: Audience and segment management for FreeWheel demand partners. Lists data providers by ad-industry category, searches and filters third-party segments, and creates, retrieves and modifies audience def
  name: FreeWheel Demand Audience Management API
  slug: freewheel-media-demand-audience-management-api
- description: 'Deal synchronization for FreeWheel demand partners. Retrieves programmatic deals available to a buyer seat (filterable by seller status, start/end date and last-updated timestamp), retrieves a single '
  name: FreeWheel Demand Deal Sync API
  slug: freewheel-media-demand-deal-sync-api
- description: Creative management for FreeWheel demand partners. Creates, retrieves and updates creatives (ads) on an account, lists the underlying creatives of a composite ad, and assigns or removes creatives from
  name: FreeWheel Demand Creative Management API
  slug: freewheel-media-demand-creative-management-api
- description: FreeWheel's sell-side APIs for publishers and programmers running on MRM — advertiser and agency management, insertion orders and campaigns, placement operations, forecasting, analytics and reporting.
  name: FreeWheel Publisher (MRM) API
  slug: freewheel-media-publisher-api
artifact_total: 15
collections:
- collection_type: open
  name: buzz
  slug: open-freewheel-media-advertiser-buzz-openapi-original
- collection_type: open
  name: audience-management-api
  slug: open-freewheel-media-demand-audience-management-openapi-original
- collection_type: open
  name: Demand Creative Management API V1
  slug: open-freewheel-media-demand-creative-management-openapi-original
- collection_type: open
  name: Deal Sync API
  slug: open-freewheel-media-demand-deal-sync-openapi-original
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freewheel-media-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freewheel-media-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freewheel-media-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.freewheel.com
- group: start
  title: ''
  type: Portal
  url: https://partners.freewheel.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freewheel
- group: operate
  title: ''
  type: Support
  url: https://www.freewheel.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.freewheel.com/insights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.freewheel.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.freewheel.com/legal/master-services-agreement
- group: start
  title: ''
  type: Login
  url: https://mrm.freewheel.tv/system/account/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freewheel-media-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.freewheel.tv/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.freewheel.tv/advertiser/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.freewheel.tv/advertiser/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.freewheel.tv/advertiser/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/freewheel-media-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/freewheel-media-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/freewheel-media-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/freewheel-media-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freewheel-media-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/freewheel-media-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/freewheel-media-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/freewheel-media-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/freewheel-media-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/freewheel-media-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/freewheel-media-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/freewheel-media-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/freewheel-media-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: FreeWheel, a Comcast company, is an advertising technology platform for the streaming and premium video television marketplace. It gives advertisers, agencies, and media buyers direct connections to premium streaming TV inventory while helping publishers and programmers monetize their video content across linear and digital channels. Its product suites include the Advertiser Suite (media buying, planning, and campaign management via Strata), the Publisher Suite (ad decisioning, forecasting, and yield optimization for sellers), and a Marketplace connecting supply and demand. FreeWheel's platform emphasizes AI-driven optimization, real-time insights, identity, and cross-screen measurement for the converged TV ecosystem. Programmatic and operational access is delivered to partners through gated Publisher (MRM) and Marketer (SFX/Strata) platforms rather than a public self-service developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freewheel-media.png
layout: provider
mcp_servers:
- description: ''
  name: freewheel-media-mcp.yml
  slug: freewheel-media-mcpyml
modified: '2026-08-12'
name: FreeWheel Media
nav: Providers
network: true
overview: 'FreeWheel Media publishes 4 APIs on the [APIs.io](https://apis.io/) network, including FreeWheel Advertiser (Buzz) API, FreeWheel Demand Audience Management API, FreeWheel Demand Deal Sync API, and 1 more. Tagged areas include Company, Advertising, AdTech, Streaming TV, and Video Advertising.


  FreeWheel Media''s developer surface includes authentication, developer portal, support, engineering blog, documentation, API reference, getting-started guide, and 23 more developer resources.'
plans:
- name: Freewheel Media Plans Pricing
  plan_count: 0
  slug: freewheel-media-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Freewheel Media Rate Limits
  slug: freewheel-media-rate-limits
score:
  band: developing
  composite: 50.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 48.3
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 42.1
  previous_composite: 50.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freewheel-media/refs/heads/main/screenshots/freewheel-media-2026-07-25T215145.png
security:
- kind: authentication
  name: Freewheel Media Authentication
  slug: freewheel-media-authentication
  summary_line: oauth2/http/apiKey · 4 schemes
- kind: domain-security
  name: Freewheel Media Domain Security
  slug: freewheel-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freewheel-media
tags:
- Company
- Advertising
- AdTech
- Streaming TV
- Video Advertising
- Programmatic
- Media
- Publisher Monetization
- Comcast
website: https://www.freewheel.com
---
