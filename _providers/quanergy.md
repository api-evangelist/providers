---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The QORTEX DTC API is the integration surface of Quanergy's detect-track-classify perception server. A gRPC service on port 17177 (Protocol Buffers 3) covers zone, counter-line, rule, PTZ camera, sett
  name: QORTEX DTC API
  slug: qortex-dtc-api
artifact_total: 4
asyncapis:
- description: ''
  name: Quanergy Qortex Dtc Events
  slug: quanergy-qortex-dtc-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quanergy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quanergy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://quanergy.com/resources/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://downloads.quanergy.com/qortex/Qortex-API-Reference-RevA-120824.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://downloads.quanergy.com/qortex/QPN-96-00131-Quick%20Start%20Card%20%E2%80%93%20Q-Track%20-%20Rev%20A.pdf
- group: operate
  title: ''
  type: Support
  url: https://quanergy.com/about/contact/
- group: company
  title: ''
  type: Blog
  url: https://quanergy.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QuanergySystems
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quanergy.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quanergy.com/terms-of-use/
- group: commercial
  title: ''
  type: TermsOfSale
  url: https://quanergy.com/terms-of-sale/
- group: other
  title: ''
  type: CaseStudies
  url: https://quanergy.com/resources/case-studies/
- group: company
  title: ''
  type: Investors
  url: https://quanergy.com/about/investors/
- group: company
  title: ''
  type: Careers
  url: https://quanergy.com/about/careers/
- group: start
  title: ''
  type: RequestDemo
  url: https://quanergy.com/about/request-a-demo/
- group: company
  title: ''
  type: PartnerProgram
  url: https://quanergy.com/channel-partners/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quanergy/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCczCM_jVyZk-19_iUuQq_9g
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/quanergy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quanergy-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/quanergy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/quanergy-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/quanergy-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quanergy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quanergy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/quanergy-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/quanergy-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quanergy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quanergy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/quanergy-conformance.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/quanergy-qortex-dtc-events.yml
created: '2026-08-05'
description: Quanergy Solutions, Inc. is a San Jose, California company that builds 3D LiDAR sensors and perception software for physical security, crowd management and industrial automation. Its Q-Track, Q-Shield, Q-Vision F540 and M-Series sensors feed QORTEX DTC, an on-premises detect-track-classify server that turns point clouds into anonymous person and vehicle tracks. QORTEX DTC publishes trackable, zone, counter-line and sensor-health streams over configurable TCP ports in protobuf, JSON, XML or NDJSON, and exposes a gRPC API on port 17177 so VMS, PSIM and access-control platforms — Milestone XProtect, Genetec Security Center, Bosch BVMS, Hanwha Wave, Motorola Unity and others — can consume real-time 3D object data.
image: https://quanergy.com/wp-content/uploads/blue-logo-updated-with-300-x-95.png
layout: provider
modified: '2026-08-05'
name: Quanergy
nav: Providers
network: true
overview: 'Quanergy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LiDAR, Sensors, Physical Security, and Perimeter Security.


  The Quanergy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Quanergy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, YouTube channel, CLI, and 24 more developer resources.'
random_paper: 131
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.6
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 39.8
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Quanergy Authentication
  slug: quanergy-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Quanergy Domain Security
  slug: quanergy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quanergy
tags:
- Company
- LiDAR
- Sensors
- Physical Security
- Perimeter Security
- Perception
- Crowd Management
- Industrial Automation
- Internet of Things
- gRPC
- Streaming
- Hardware
website: https://quanergy.com/
---
