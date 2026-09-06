---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Public gRPC API for the StellarStation ground-station-as-a-service platform. Lets satellite operators list upcoming available passes, reserve and cancel plans, add and retrieve TLE orbital data, set p
  name: StellarStation API
  slug: stellarstation-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infostellar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.infostellar.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/infostellarinc/stellarstation-api
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/infostellarinc/stellarstation-api#readme
- group: docs
  title: ''
  type: APIReference
  url: https://javadoc.io/doc/com.stellarstation.api/stellarstation-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infostellarinc
- group: other
  title: ''
  type: Product
  url: https://www.stellarstation.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/infostellarinc/stellarstation-api/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/infostellar-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infostellar-lifecycle.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/infostellar-stellarstation.proto
- group: build
  title: ''
  type: Packages
  url: packages/infostellar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/infostellar-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infostellar-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infostellar-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infostellar-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infostellar-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infostellar-problem-types.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/infostellar-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infostellar-llms.txt
created: '2026-07-17'
description: Infostellar is a Tokyo-based space infrastructure company that operates StellarStation, a cloud ground-station-as-a-service (GSaaS) platform. It aggregates partner and operator antennas into a shared global network so satellite operators can discover and reserve upcoming passes, schedule and cancel plans, manage two-line element (TLE) orbital data, and stream live telemetry and commands to and from their spacecraft. StellarStation exposes a public gRPC API (defined with Protocol Buffers) at api.stellarstation.com, with precompiled client stubs published for Java, Python, Go, and Node.js and authentication handled via JWT bearer service-account credentials issued from the StellarStation Console. The API separates a satellite-operator service (StellarStationService) from a ground-station-operator service (GroundStationService), plus supporting definitions for antennas, radios, orbit, monitoring, and transport.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infostellar.png
layout: provider
modified: '2026-07-19'
name: Infostellar
nav: Providers
network: true
overview: 'Infostellar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Satellite, Ground Station, and Aerospace.


  Infostellar''s developer surface includes documentation, API reference, changelog, authentication, and 17 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 26.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infostellar/refs/heads/main/screenshots/infostellar-2026-07-25T222423.png
security:
- kind: authentication
  name: Infostellar Authentication
  slug: infostellar-authentication
  summary_line: jwt-bearer · 1 scheme
- kind: domain-security
  name: Infostellar Domain Security
  slug: infostellar-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: infostellar
tags:
- Company
- Space
- Satellite
- Ground Station
- Aerospace
- Telemetry
- gRPC
- GSaaS
- Orbital
website: https://www.infostellar.net
---
