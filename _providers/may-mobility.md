---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: A WebSocket streaming API that delivers live May Mobility vehicle data in two modes. Telemetry mode streams JSON messages for a comma-separated list of per-vehicle topics (GPS, POSE, DRIVE_STATUS, RUN
  name: May Mobility Fleet Realtime API
  slug: fleet-realtime-api
- description: A REST API that returns historical May Mobility vehicle data between two Unix timestamps. Telemetry is retrieved per vehicle and topic at /vehicles/{vehicleID}/topics/{topicName} with startTime and en
  name: May Mobility Fleet Batch (REST) API
  slug: fleet-batch-api
artifact_total: 8
asyncapis:
- description: ''
  name: May Mobility Fleet Events
  slug: may-mobility-fleet-events
common:
- group: company
  title: ''
  type: Website
  url: https://maymobility.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.maymobility.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.maymobility.com/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://docs.maymobility.com/docs/fleet-api/types-of-data
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.maymobility.com/docs/fleet-api/connecting-to-fleet-api
- group: company
  title: ''
  type: Blog
  url: https://maymobility.com/posts/type/company-blog/
- group: operate
  title: ''
  type: Support
  url: https://maymobility.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maymobility
- group: commercial
  title: ''
  type: TermsOfService
  url: https://maymobility.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://maymobility.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://maymobility.com/cybersecurity/
- group: auth
  title: ''
  type: TrustCenter
  url: security/may-mobility-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://net.maymobility.com/docs/policies/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/may-mobility-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/may-mobility-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/may-mobility-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/may-mobility-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/may-mobility-fleet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/may-mobility-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/may-mobility-fleet-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/may-mobility-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/may-mobility-fleet-error-catalog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/may-mobility-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.net.maymobility.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/may-mobility-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/may-mobility-fleet-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/may-mobility-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/may-mobility-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/may-mobility-quic-wrapper.proto
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/may-mobility-fleet-events.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/may-mobility-llms.txt
created: '2026-08-01'
description: May Mobility is an American autonomous vehicle technology company headquartered in Ann Arbor, Michigan, founded in 2017 by Edwin Olson, Alisyn Malek and Steve Vozar. It develops and operates self-driving shuttle, microtransit and robotaxi services in partnership with cities, transit agencies, commercial sites and ride-hail networks including Uber and Lyft, using a proprietary Multi-Policy Decision Making (MPDM) autonomy stack. For fleet partners May Mobility publishes a Fleet API at docs.maymobility.com consisting of a Realtime API (WebSocket streaming of vehicle telemetry topics and exterior camera video, the latter as serialized protobuf) and a Batch REST API that returns historical telemetry, LiDAR ROSBAG exports, vehicle shift timings and last-active status. Access is provisioned per account by the Fleet API team and authenticated with AWS Cognito OAuth 2.0 client-credentials tokens. May Mobility also operates its own autonomous system (AS398351) with a public NOC documentation
  site, peering policy, responsible-disclosure program and internal PKI.
image: https://maymobility.com/apple-touch-icon.png
layout: provider
modified: '2026-08-01'
name: May Mobility
nav: Providers
network: true
overview: 'May Mobility publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomous Vehicles, Transportation, Mobility, and Robotaxi.


  The May Mobility catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  May Mobility''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 24 more developer resources.'
random_paper: 6
scopes:
- name: May Mobility Scopes
  scope_count: 0
  slug: may-mobility-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 44.6
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/may-mobility/refs/heads/main/screenshots/may-mobility-2026-08-07T172133.png
security:
- kind: authentication
  name: May Mobility Fleet Authentication
  slug: may-mobility-fleet-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: May Mobility Domain Security
  slug: may-mobility-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: May Mobility Vulnerability Disclosure
  slug: may-mobility-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: May Mobility Trust Center
  slug: may-mobility-trust-center
  summary_line: trust center published
slug: may-mobility
tags:
- Company
- Autonomous Vehicles
- Transportation
- Mobility
- Robotaxi
- Fleet Management
- Telemetry
- Public Transit
- Automotive
- Streaming
website: https://maymobility.com/
---
