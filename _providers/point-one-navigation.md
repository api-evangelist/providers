---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Standards-based NTRIP interface to the Point One Polaris RTK corrections network. Clients connect over NTRIP 1.0 or 2.0 to a regional caster, authenticate with Basic auth using a unique per-connection
  name: Polaris RTK Network (NTRIP)
  slug: polaris-ntrip
- description: The native Point One corrections protocol. A Polaris API key is POSTed unauthenticated to https://api.pointonenav.com/api/v1/auth/token and exchanged for a bearer access token valid for 604800 seconds
  name: Polaris Native API (Point One Open)
  slug: polaris-native
- description: The single-endpoint GraphQL API behind the Point One web application, covering device registration and metadata, tags, seat licenses and entitlements, device profiles (True RTK and Virtual RTK correct
  name: Point One Platform GraphQL API
  slug: graphql
artifact_total: 5
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/PointOneNav/polaris/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/point-one-navigation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pointonenav.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pointonenav.com/resources/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pointonenav.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pointonenav.com/docs/graphql-api/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://support.pointonenav.com/connect-to-point-one-rtk
- group: operate
  title: ''
  type: Support
  url: https://support.pointonenav.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.pointonenav.com/
- group: company
  title: ''
  type: Blog
  url: https://pointonenav.com/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PointOneNav
- group: commercial
  title: ''
  type: Pricing
  url: https://pointonenav.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.pointonenav.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pointonenav.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pointonenav.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pointonenav.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://pointonenav.com/changelog/
- group: operate
  title: ''
  type: Contact
  url: https://pointonenav.com/contact/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/point-one-navigation_stock/
- group: docs
  title: ''
  type: GraphQL
  url: graphql/point-one-navigation-graphql-surface.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/point-one-navigation-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/point-one-navigation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/point-one-navigation-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/point-one-navigation-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/point-one-navigation-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/point-one-navigation-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/point-one-navigation-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/point-one-navigation-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/point-one-navigation-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/point-one-navigation-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/point-one-navigation-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/point-one-navigation-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: 'Point One Navigation operates Polaris, a GNSS RTK corrections network delivering 1-3 cm (True RTK) and sub-10 cm (Virtual RTK) positioning across North America, Europe, the UK, Australia, New Zealand, Japan and South Korea, alongside FusionEngine, its GNSS/INS sensor-fusion positioning engine, and the Atlas and Standard Dev Kit hardware platforms. Developers reach the network three ways: a standards-based NTRIP interface that streams RTCM v3.2 MSM4 corrections to any compatible receiver, a native Polaris protocol with an API-key-to-bearer-token exchange, and a Personal Access Token-authenticated GraphQL platform API for device, tag, license, device-profile and reference station management with real-time subscriptions.'
image: https://docs.pointonenav.com/img/point-one-white-logo2.jpg
layout: provider
modified: '2026-08-05'
name: Point One Navigation
nav: Providers
network: true
overview: 'Point One Navigation publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Location, GNSS, Positioning, Geospatial, and RTK.


  Point One Navigation''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 66
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 37.8
  provenance:
    conformance: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Point One Navigation Authentication
  slug: point-one-navigation-authentication
  summary_line: apiKey/http/custom · 4 schemes
- kind: domain-security
  name: Point One Navigation Domain Security
  slug: point-one-navigation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: point-one-navigation
tags:
- Location
- GNSS
- Positioning
- Geospatial
- RTK
- Navigation
- Mapping
- Robotics
- Autonomous Vehicles
- IoT
- Hardware
- GraphQL
website: https://pointonenav.com/
---
