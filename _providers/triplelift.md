---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.4
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Real-time bidding API implementing OpenRTB 2.x and Native Ads 1.2 specifications for demand partners to participate in native, banner, and video ad auctions. Supports bid request and response objects,
  name: TripleLift Exchange (TLX) API
  slug: triplelift-exchange-tlx-api
- description: GraphQL API for publishers and supply partners covering standard and connected TV (CTV) network reporting. A single unversioned endpoint exposes publisherNetworkReport and ctvPublisherNetworkReport pl
  name: TripleLift Reporting API
  slug: triplelift-reporting-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triplelift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://triplelift.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.triplelift.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/triplelift
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triplelift/
- group: company
  title: ''
  type: Blog
  url: https://triplelift.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://triplelift.com/contact-us/
- group: other
  title: ''
  type: X
  url: https://twitter.com/TripleLiftHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/triplelift-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/triplelift-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/triplelift-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.triplelift.com
- group: docs
  title: ''
  type: APIReference
  url: https://supply-docs.triplelift.com/reference/introduction
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://triplelift.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://console.triplelift.com
- group: operate
  title: ''
  type: Support
  url: https://triplelift.com/contact-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.triplelift.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/triplelift-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/triplelift-mcp.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/triplelift-graphql.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/triplelift-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/triplelift-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/triplelift-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/triplelift-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/triplelift-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/triplelift-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/triplelift-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/triplelift-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/triplelift-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/triplelift-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/triplelift-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-06-13'
description: TripleLift is a programmatic advertising exchange and supply-side platform built around native inventory, with a public developer surface in two parts. The TripleLift Exchange (TLX) is an IAB OpenRTB 2.x server-to-server auction endpoint for native, banner, video and connected TV, geo-load balanced across four AWS regions, with user-sync endpoints carrying GDPR TCF, us_privacy and GPP consent signals and SKAdNetwork support for iOS attribution. The TripleLift Reporting API is a GraphQL API for publishers and supply partners covering standard and CTV network reporting, with synchronous cursor-paginated queries and asynchronous CSV export by pre-signed download or email. TripleLift also publishes sellers.json, a component-level status page, a dated Reporting API changelog, and Prebid.js and Prebid Server bid adapters.
finops:
- name: Triplelift Finops
  service_category: ''
  slug: triplelift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/triplelift.png
jsonld:
- class_count: 62
  name: Triplelift Context
  property_count: 0
  slug: triplelift-context
layout: provider
mcp_servers:
- description: Three live Model Context Protocol endpoints were found on TripleLift-controlled hosts. Two are documentation servers provisioned by ReadMe on TripleLift's own docs domains; one is a WordPress MCP serv
  name: TripleLift MCP Servers
  slug: triplelift-mcp-servers
modified: '2026-08-12'
name: TripleLift
nav: Providers
network: true
overview: 'TripleLift publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Programmatic Advertising, Native Advertising, Ad Exchange, OpenRTB, and Header Bidding.


  The TripleLift catalog on APIs.io includes 1 JSON-LD context.


  TripleLift''s developer surface includes documentation, engineering blog, pricing, API reference, support, authentication, changelog, and 25 more developer resources.'
plans:
- name: Triplelift Plans Pricing
  plan_count: 0
  slug: triplelift-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Triplelift Rate Limits
  slug: triplelift-rate-limits
scopes:
- name: Triplelift Scopes
  scope_count: 51
  slug: triplelift-scopes
  summary_line: 51 scopes
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 38.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triplelift/refs/heads/main/screenshots/triplelift-2026-06-20T195728.png
security:
- kind: authentication
  name: Triplelift Authentication
  slug: triplelift-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Triplelift Domain Security
  slug: triplelift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Triplelift Vulnerability Disclosure
  slug: triplelift-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Triplelift Trust Center
  slug: triplelift-trust-center
  summary_line: trust center published
slug: triplelift
tags:
- Programmatic Advertising
- Native Advertising
- Ad Exchange
- OpenRTB
- Header Bidding
- Connected TV
- Supply Side Platform
- Demand-Side Platform
- GraphQL
- Ad Tech
- Publisher Reporting
- Real-Time Bidding
website: https://triplelift.com
---
