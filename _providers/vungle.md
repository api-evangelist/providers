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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: 'Automated access to Vungle/Liftoff campaign performance reports — impressions, clicks, installs, and in-app events — with configurable groupings, metrics, and cohort (look-back window) analysis. HTTP '
  name: Liftoff Reporting API
  slug: liftoff-reporting-api
- description: Closed-beta API to programmatically launch UA expansion campaigns, manage spend and targeting, upload assets, and assemble creatives. Standard REST/JSON at https://cm-api.liftoff.io/v1.
  name: Liftoff Campaign Management API
  slug: liftoff-campaign-management-api
- description: Audience ingestion/validation API for partners working on behalf of multiple clients, at https://analytics.liftoff.io/audiences/v1.
  name: Liftoff Audiences Integration API
  slug: liftoff-audiences-integration-api
- description: Submit GDPR-compliant opt-out requests to remove user data by device ID, at https://analytics.liftoff.io/opt_out/v3.
  name: Liftoff GDPR Opt-Out API
  slug: liftoff-gdpr-opt-out-api
artifact_total: 9
asyncapis:
- description: ''
  name: Vungle S2S Webhooks
  slug: vungle-s2s-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vungle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vungle.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.liftoff.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liftoff.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.liftoff.io/advertiser
- group: auth
  title: ''
  type: Authentication
  url: authentication/vungle-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vungle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vungle-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vungle-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vungle-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vungle-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/vungle-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vungle-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vungle-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vungle-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/vungle-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vungle-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vungle-s2s-webhooks.yml
- group: company
  title: ''
  type: Blog
  url: https://liftoff.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liftoff.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liftoff.io/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vungle
created: '2026-07-17'
description: Vungle is a mobile app monetization and user-acquisition platform, now operated as part of Liftoff (the merged Liftoff + Vungle mobile growth company). Vungle's in-app advertising SDKs help mobile publishers monetize with performance-focused ad formats (video, interactive, and playable ads), while Liftoff's advertiser APIs let growth teams launch and manage user-acquisition campaigns, assemble creatives, ingest audiences, and pull automated performance reporting. The programmatic surface is documented at docs.liftoff.io and includes a Reporting API, a closed-beta Campaign Management API, an Audiences Integration API, a GDPR Opt-Out API, and a server-to-server (S2S) postback integration. All advertiser APIs authenticate with an HTTP Basic API key and secret issued by a Liftoff Account Manager.
image: https://liftoff.ai/wp-content/uploads/2025/01/B-Meta-Image-20240912-122239.jpg
layout: provider
mcp_servers:
- description: ''
  name: vungle-mcp.yml
  slug: vungle-mcpyml
modified: '2026-07-21'
name: Vungle
nav: Providers
network: true
overview: 'Vungle publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Mobile, Monetization, and User Acquisition.


  The Vungle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vungle''s developer surface includes documentation, getting-started guide, authentication, sandbox, engineering blog, and 17 more developer resources.'
random_paper: 45
rate_limits:
- limit_count: 0
  name: Vungle Rate Limits
  slug: vungle-rate-limits
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 22.6
    developer_ergonomics: 63.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 34.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Vungle Authentication
  slug: vungle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vungle Domain Security
  slug: vungle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vungle
tags:
- Company
- Advertising
- Mobile
- Monetization
- User Acquisition
- Ad Tech
- Analytics
- Reporting
website: https://vungle.com
---
