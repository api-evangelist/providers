---
agent_readiness:
  band: agent-ready
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-30'
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
- description: 'With the App Partner Connection API, you can: - View details about an app partner connection - Create a partner connection for an app (This is the API equivalent of connecting a partner in the dashboa'
  name: AppLike Group App Partner Connection API
  slug: applike-app-partner-connection-api
- description: The Appevents API from AppLike Group — 1 operation(s) for appevents.
  name: AppLike Group Appevents API
  slug: applike-appevents-api
- description: 'With the App API, you can: - View your list of apps - Create an app'
  name: AppLike Group Apps API
  slug: applike-apps-api
- description: 'Bidding operates as a distributed transaction. The sequential flow is as follows: 1. you upload a bid 2. we store it in justtrack -> status: pending 3. we try to apply it on partner side <br/> a. if s'
  name: AppLike Group Bids API
  slug: applike-bids-api
- description: The Campaigns API from AppLike Group — 2 operation(s) for campaigns.
  name: AppLike Group Campaigns API
  slug: applike-campaigns-api
- description: 'In justtrack, you integrate your app with the advertising partners that run your campaigns. Depending on the integrated partner, we exchange data for at least one of the following features: * `attribu'
  name: AppLike Group Partner Configurations API
  slug: applike-partner-configurations-api
- description: The Partners API from AppLike Group — 1 operation(s) for partners.
  name: AppLike Group Partners API
  slug: applike-partners-api
artifact_total: 24
asyncapis:
- description: ''
  name: Applike Webhooks
  slug: applike-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/applike-capability-edges.yml
- group: auth
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
  title: ''
  type: Compliance
  url: conformance/applike-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/applike-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/applike-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/applike-justtrack-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/applike-adjoe-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/applike-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/applike-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/applike-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/applike-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/applike-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/applike-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/applike-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/applike-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/applike-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/applike-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/applike-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/applike-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/applike-trust-center.yml
- group: design
  title: ''
  type: Components
  url: components/applike-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/applike-justtrack-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/applike-justtrack-app-events-overlay.yaml
created: '2026-08-06'
description: 'AppLike Group is a Hamburg, Germany-based company builder in the mobile app economy, founded in 2015 by Jonas Thiemann and Carlo Szelinsky and backed by Bertelsmann. The group operates four independent businesses that cover the mobile app value chain: adjoe (rewarded user acquisition, the Playtime engagement ad format, the Arcade loyalty layer and a programmatic ads platform), justtrack (mobile attribution, user-acquisition automation, cohort and monetization analytics), JustDice (app-discovery products for mobile gamers) and Sunday (mobile game development and publishing). Two of the four brands publish public developer surfaces: justtrack ships OpenAPI 3.1 contracts for its Management and AppEvent APIs plus documented Reporting, Revenue Events and Raw Data Export interfaces, and adjoe publishes SSP reporting APIs and a server-to-server rewarded-payout callback alongside Android, iOS, Unity, Flutter, React Native and Cordova SDKs.'
image: https://applike-group.com/wp-content/uploads/2025/04/Applike-Group-881x1024.png
layout: provider
modified: '2026-08-06'
name: AppLike Group
nav: Providers
network: true
overview: 'AppLike Group publishes 7 APIs on the [APIs.io](https://apis.io/) network, including App Partner Connection API, Appevents API, Apps API, and 4 more. Tagged areas include mobile-attribution, user-acquisition, adtech, mobile-advertising, and app-monetization.


  The AppLike Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AppLike Group''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 31 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 1
  name: Applike Rate Limits
  slug: applike-rate-limits
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 61.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 71.1
  previous_composite: 59.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/applike/refs/heads/main/screenshots/applike-2026-08-07T161506.png
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
slug: applike
tags:
- mobile-attribution
- user-acquisition
- adtech
- mobile-advertising
- app-monetization
- rewarded-advertising
- mobile-sdk
- mobile-analytics
- marketing-attribution
- mobile-games
- event-tracking
- company
website: https://applike-group.com/
---
