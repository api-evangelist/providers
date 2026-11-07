---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Reporting API exposing the metrics behind the justtrack dashboard — acquisition tables, cohort analysis and event drill-down — as POST endpoints under /reporting/v2 (v1 also documented). Requests carr
  name: justtrack Reporting API
  slug: justtrack-reporting-api
- description: Server-to-server revenue postback sink. Monetization partners and customers send real-time revenue events as GET requests with query parameters to https://sink.justtrack.io/monetization/v0/{provider}/
  name: justtrack Revenue Events API
  slug: justtrack-revenue-events-api
- description: Publisher-facing reporting API returning daily aggregated Playtime revenue, eCPM, offerwall shows, SDK bootups, first impressions, coin sums and view counts, groupable by up to eighteen dimensions. Tw
  name: adjoe SSP Revenue API
  slug: adjoe-ssp-revenue-api
- description: Per-user ad data report download for Playtime publishers. A single GET /v3/ssp-api/user-ad-data-report/sdk/{sdkHash} endpoint returns a text/csv report for a given date, answering 202 with a JSON body
  name: adjoe User Ad Data Report API
  slug: adjoe-user-ad-data-report-api
- baseURL: https://api.justtrack.io
  baseurl_source: declared
  description: 'With the App Partner Connection API, you can: - View details about an app partner connection - Create a partner connection for an app (This is the API equivalent of connecting a partner in the dashboa'
  name: AppLike Group App Partner Connection API
  slug: applike-app-partner-connection-api
- baseURL: https://api.justtrack.io
  baseurl_source: declared
  description: 'With the App API, you can: - View your list of apps - Create an app'
  name: AppLike Group Apps API
  slug: applike-apps-api
- baseURL: https://api.justtrack.io
  baseurl_source: declared
  description: 'Bidding operates as a distributed transaction. The sequential flow is as follows: 1. you upload a bid 2. we store it in justtrack -> status: pending 3. we try to apply it on partner side <br/> a. if s'
  name: AppLike Group Bids API
  slug: applike-bids-api
- baseURL: https://api.justtrack.io
  baseurl_source: declared
  description: The Campaigns API from AppLike Group — 2 operation(s) for campaigns.
  name: AppLike Group Campaigns API
  slug: applike-campaigns-api
- baseURL: https://api.justtrack.io
  baseurl_source: declared
  description: 'In justtrack, you integrate your app with the advertising partners that run your campaigns. Depending on the integrated partner, we exchange data for at least one of the following features: * `attribu'
  name: AppLike Group Partner Configurations API
  slug: applike-partner-configurations-api
- baseURL: https://api.justtrack.io
  baseurl_source: declared
  description: The Partners API from AppLike Group — 1 operation(s) for partners.
  name: AppLike Group Partners API
  slug: applike-partners-api
- baseURL: https://api.justtrack.io
  baseurl_source: declared
  description: The App Events API from AppLike Group — 1 operation(s) for app events.
  name: AppLike Group App Events API
  slug: applike-app-events-api
artifact_total: 32
asyncapis:
- description: ''
  name: Applike Webhooks
  slug: applike-webhooks
collections:
- collection_type: open
  name: Management App Partner Connection API
  slug: open-applike-app-partner-connection-api
- collection_type: open
  name: AppEvent Appevents API
  slug: open-applike-appevents-api
- collection_type: open
  name: Management Apps API
  slug: open-applike-apps-api
- collection_type: open
  name: Management Bids API
  slug: open-applike-bids-api
- collection_type: open
  name: Management Campaigns API
  slug: open-applike-campaigns-api
- collection_type: open
  name: Management Partner Configurations API
  slug: open-applike-partner-configurations-api
- collection_type: open
  name: Management Partners API
  slug: open-applike-partners-api
common:
- group: commercial
  href: https://artifacts.apis.io/applike/plans/applike-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/applike-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/applike/capabilities/applike-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/applike-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/applike/security/applike-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applike-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://applike-group.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.justtrack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.justtrack.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.justtrack.io/api/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.justtrack.io/sdk/setup/
- group: operate
  title: ''
  type: Support
  url: https://justtrack.io/contact/
- group: company
  title: ''
  type: Blog
  url: https://adjoe.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/justtrackio
- group: commercial
  title: ''
  type: Pricing
  url: https://justtrack.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://dashboard.justtrack.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://justtrack.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://justtrack.io/privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.justtrack.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.justtrack.io/sdk/more/changelog/
- group: auth
  href: https://artifacts.apis.io/applike/conformance/applike-conformance.yml
  title: ''
  type: Compliance
  url: conformance/applike-conformance.yml
- group: build
  href: https://artifacts.apis.io/applike/packages/applike-packages.yml
  title: ''
  type: Packages
  url: packages/applike-packages.yml
- group: build
  href: https://artifacts.apis.io/applike/packages/applike-packages.yml
  title: ''
  type: SDKs
  url: packages/applike-packages.yml
- group: agent
  href: https://artifacts.apis.io/applike/llms/applike-justtrack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applike-justtrack-llms.txt
- group: agent
  href: https://artifacts.apis.io/applike/llms/applike-adjoe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applike-adjoe-llms.txt
- group: agent
  href: https://artifacts.apis.io/applike/well-known/applike-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applike-well-known.yml
- group: auth
  href: https://artifacts.apis.io/applike/authentication/applike-authentication.yml
  title: ''
  type: Authentication
  url: authentication/applike-authentication.yml
- group: design
  href: https://artifacts.apis.io/applike/conventions/applike-conventions.yml
  title: ''
  type: Conventions
  url: conventions/applike-conventions.yml
- group: design
  href: https://artifacts.apis.io/applike/conventions/applike-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/applike-conventions.yml
- group: operate
  href: https://artifacts.apis.io/applike/rate-limits/applike-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/applike-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/applike/errors/applike-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/applike-problem-types.yml
- group: design
  href: https://artifacts.apis.io/applike/lifecycle/applike-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/applike-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/applike/lifecycle/applike-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/applike-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/applike/conformance/applike-conformance.yml
  title: ''
  type: Conformance
  url: conformance/applike-conformance.yml
- group: design
  href: https://artifacts.apis.io/applike/data-model/applike-data-model.yml
  title: ''
  type: DataModel
  url: data-model/applike-data-model.yml
- group: design
  href: https://artifacts.apis.io/applike/asyncapi/applike-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/applike-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/applike/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/applike/changelog/applike-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/applike-changelog.yml
- group: auth
  href: https://artifacts.apis.io/applike/security/applike-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/applike-trust-center.yml
- group: design
  href: https://artifacts.apis.io/applike/components/applike-components.yml
  title: ''
  type: Components
  url: components/applike-components.yml
- group: other
  href: https://artifacts.apis.io/applike/overlays/applike-justtrack-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/applike-justtrack-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/applike/overlays/applike-justtrack-app-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/applike-justtrack-app-events-overlay.yaml
created: '2026-08-06'
description: 'AppLike Group is a Hamburg, Germany-based company builder in the mobile app economy, founded in 2015 by Jonas Thiemann and Carlo Szelinsky and backed by Bertelsmann. The group operates four independent businesses that cover the mobile app value chain: adjoe (rewarded user acquisition, the Playtime engagement ad format, the Arcade loyalty layer and a programmatic ads platform), justtrack (mobile attribution, user-acquisition automation, cohort and monetization analytics), JustDice (app-discovery products for mobile gamers) and Sunday (mobile game development and publishing). Two of the four brands publish public developer surfaces: justtrack ships OpenAPI 3.1 contracts for its Management and AppEvent APIs plus documented Reporting, Revenue Events and Raw Data Export interfaces, and adjoe publishes SSP reporting APIs and a server-to-server rewarded-payout callback alongside Android, iOS, Unity, Flutter, React Native and Cordova SDKs.'
finops:
- has_sources: true
  method: derived
  name: Applike Finops
  primary_unit: up to 10k mau
  service_category: ''
  slug: applike-finops
  template: false
image: https://applike-group.com/wp-content/uploads/2025/04/Applike-Group-881x1024.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.justtrack.io over HTTP.
  name: AppLike Group MCP Server
  slug: applike
modified: '2026-08-06'
name: AppLike Group
nav: Providers
network: true
overview: 'AppLike Group publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including App Partner Connection API, Apps API, Bids API, and 8 more. Tagged areas include Mobile Attribution, User Acquisition, AdTech, Mobile Advertising, and App Monetization.


  The AppLike Group catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AppLike Group''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 32 more developer resources.'
plans:
- name: Applike Plans Pricing
  plan_count: 12
  slug: applike-plans-pricing
- name: Applike Price Estimates
  plan_count: 0
  slug: applike-price-estimates
random_paper: 22
rate_limits:
- limit_count: 1
  name: Applike Rate Limits
  slug: applike-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: AppLike Group API Rules
  rule_count: 54
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 3
  slug: applike-rules
score:
  band: exemplar
  composite: 69.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 57.8
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 69.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/applike/applike-2026-08-07T161506.png
security:
- kind: authentication
  name: Applike Authentication
  slug: applike-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Applike Domain Security
  slug: applike-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Applike Trust Center
  slug: applike-trust-center
  summary_line: trust center published
skill_count: 4
skills:
- name: applike-ingest-app-events
  slug: applike-ingest-app-events
- name: applike-manage-campaign-bids
  slug: applike-manage-campaign-bids
- name: applike-onboard-app-and-partner
  slug: applike-onboard-app-and-partner
- name: applike-pull-adjoe-publisher-revenue
  slug: applike-pull-adjoe-publisher-revenue
slug: applike
tags:
- Mobile Attribution
- User Acquisition
- AdTech
- Mobile Advertising
- App Monetization
- rewarded-advertising
- Mobile SDK
- Mobile Analytics
- Marketing Attribution
- Mobile Games
- Event Tracking
- Company
website: https://applike-group.com/
---
