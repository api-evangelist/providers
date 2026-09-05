---
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Synse Server exposes a uniform HTTP and WebSocket API for reading from and writing to physical and virtual devices through protocol-specific plugins. The same 18 operations are available over both tra
  name: Synse Server API (v3)
  slug: synse-server
- description: The internal gRPC API for bi-directional communication between Synse Server and Synse plugins. The published Protocol Buffers contract defines the V3Plugin service with 12 RPCs — Devices, Health, Meta
  name: Synse Plugin gRPC API (V3Plugin)
  slug: synse-plugin-grpc
artifact_total: 7
asyncapis:
- description: ''
  name: Vapor Io Synse Websocket Events
  slug: vapor-io-synse-websocket-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vapor-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vapor.io/
- group: docs
  title: ''
  type: Documentation
  url: https://synse.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://synse.readthedocs.io/en/latest/server/api.v3/
- group: start
  title: ''
  type: GettingStarted
  url: https://synse.readthedocs.io/en/latest/server/user/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vapor-ware
- group: company
  title: ''
  type: Blog
  url: https://www.vapor.io/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vapor.io/feed/
- group: operate
  title: ''
  type: Support
  url: https://github.com/vapor-ware/synse-server/issues
- group: operate
  title: ''
  type: Contact
  url: https://www.vapor.io/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vapor.io/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vapor.io/legal/privacy-policy/
- group: commercial
  title: ''
  type: License
  url: https://synse.readthedocs.io/en/latest/license/
- group: other
  title: ''
  type: Protobuf
  url: grpc/vapor-io-synse-v3plugin.proto
- group: build
  title: ''
  type: Packages
  url: packages/vapor-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vapor-io-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vapor-io-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vapor-io-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vapor-io-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vapor-io-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vapor-io-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vapor-io-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vapor-io-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vapor-io-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vapor-io-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vapor-io-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vapor-io-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vapor-io-llms.txt
created: '2026-09-02'
description: 'Vapor IO is an Austin, Texas edge computing company that builds and operates the Kinetic Grid, a carrier-neutral network of micro modular data centers offering edge colocation, interconnection, networking and network-delivered AI across dozens of US markets and, through a Cellnex partnership, into Europe. Its public, machine-readable developer surface is the open source Synse platform, published under the vapor-ware GitHub organization: Synse Server, a uniform HTTP and WebSocket API for monitoring and controlling physical and virtual devices (data center equipment, IoT devices, building management systems, edge hardware), and the Synse plugin gRPC API, whose Protocol Buffers contract is published in full. Protocol-specific plugins cover IPMI, SNMP, Modbus over TCP/IP, Intel AMT and Juniper JTI, with Go and Python SDKs, a Go CLI, Helm charts and Docker images. Kinetic Grid Portal telemetry is described as API-accessible but is documented only to customers.'
image: https://www.vapor.io/wp-content/uploads/2021/06/cropped-1-Fav.png
layout: provider
modified: '2026-09-02'
name: Vapor IO
nav: Providers
network: true
overview: 'Vapor IO publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Edge Computing, Data Centers, Colocation, and Infrastructure.


  The Vapor IO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vapor IO''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, sandbox, and 22 more developer resources.'
plans:
- name: Vapor Io Plans Pricing
  plan_count: 0
  slug: vapor-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Vapor Io Rate Limits
  slug: vapor-io-rate-limits
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 70.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 38.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Vapor Io Authentication
  slug: vapor-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Vapor Io Domain Security
  slug: vapor-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: vapor-io
tags:
- Company
- Edge Computing
- Data Centers
- Colocation
- Infrastructure
- Device Management
- Monitoring
- Telemetry
- IoT
- gRPC
- Open Source
- Kubernetes
website: https://www.vapor.io/
---
