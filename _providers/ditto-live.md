---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Ditto Live Agentic Access
  operation_count: 27
  slug: ditto-live-agentic-access
  summary_line: 27 operations · 20 acting
api_count: 7
apis:
- description: Multi-platform embeddable SDK for peer-to-peer and cloud-synced data storage. Supports Swift, Kotlin, Flutter, React Native, JavaScript, .NET/C#, C++, Rust, Go, and Java. Developers use DQL to create,
  name: Ditto SDK
  slug: sdk
- description: Big Peer HTTP API keys
  name: Ditto API Keys API
  slug: ditto-live-api-keys-api
- description: The Apps API from Ditto — 6 operation(s) for apps.
  name: Ditto Apps API
  slug: ditto-live-apps-api
- description: The BigPeerReplication API from Ditto — 2 operation(s) for bigpeerreplication.
  name: Ditto BigPeerReplication API
  slug: ditto-live-bigpeerreplication-api
- description: Apps' data bridges (CDC)
  name: Ditto Data Bridge API
  slug: ditto-live-data-bridge-api
- description: The Store API from Ditto — 5 operation(s) for store.
  name: Ditto Store API
  slug: ditto-live-store-api
- description: The Sync API from Ditto — 1 operation(s) for sync.
  name: Ditto Sync API
  slug: ditto-live-sync-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ditto HTTP RPC API Keys API
  slug: open-ditto-live-api-keys-api
- collection_type: open
  name: Ditto HTTP RPC API Keys Apps API
  slug: open-ditto-live-apps-api
- collection_type: open
  name: Ditto HTTP RPC API Keys BigPeerReplication API
  slug: open-ditto-live-bigpeerreplication-api
- collection_type: open
  name: Ditto HTTP RPC API Keys Data Bridge API
  slug: open-ditto-live-data-bridge-api
- collection_type: open
  name: Ditto HTTP RPC API Keys Store API
  slug: open-ditto-live-store-api
- collection_type: open
  name: Ditto HTTP RPC API Keys Sync API
  slug: open-ditto-live-sync-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ditto-live-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ditto-live-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ditto-live-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ditto-live-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ditto.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ditto.live
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getditto
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dittolive
- group: other
  title: ''
  type: X
  url: https://twitter.com/dittolive
- group: company
  title: ''
  type: Blog
  url: https://www.ditto.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ditto.com/pricing/cloud-sync
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ditto.live/changelog
- group: start
  title: ''
  type: Portal
  url: https://portal.ditto.live
- group: commercial
  title: ''
  type: Plans
  url: plans/ditto-live-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ditto-live-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ditto-live-finops.yml
created: '2026-06-12'
description: Ditto is a peer-to-peer data sync platform for mobile and edge devices that enables real-time synchronization without requiring a central server, using Bluetooth, WiFi Direct, and LAN transports. The platform ships an embeddable SDK for iOS, Android, Flutter, React Native, JavaScript, .NET/C#, C++, Rust, Go, Java, and Kotlin, and backs it with an optional cloud tier (the "Big Peer") that bridges device meshes to the internet. Developers query and mutate data through DQL (Ditto Query Language) on-device, or via a cloud HTTP API (v5) against per-app endpoints. Ditto targets mission-critical mobile and edge workloads — retail, manufacturing, aviation, healthcare — where connectivity is intermittent or absent.
examples:
- key_count: 2
  name: Ditto Live Store Execute Request Example
  slug: ditto-live-store-execute-request-example
- key_count: 5
  name: Ditto Live Store Execute Response Example
  slug: ditto-live-store-execute-response-example
- key_count: 6
  name: Ditto Live Store Find Request Example
  slug: ditto-live-store-find-request-example
- key_count: 2
  name: Ditto Live Store Find Response Example
  slug: ditto-live-store-find-response-example
- key_count: 1
  name: Ditto Live Store Write Request Example
  slug: ditto-live-store-write-request-example
- key_count: 1
  name: Ditto Live Store Write Response Example
  slug: ditto-live-store-write-response-example
finops:
- name: Ditto Live Finops
  service_category: Database / Sync
  slug: ditto-live-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ditto-live.png
json_schemas:
- name: ApiKey
  property_count: 4
  slug: ditto-live-apikey
- name: App
  property_count: 3
  slug: ditto-live-app
- name: BigPeerReplication
  property_count: 3
  slug: ditto-live-bigpeer-replication
- name: DataBridge
  property_count: 5
  slug: ditto-live-databridge
- name: Document
  property_count: 2
  slug: ditto-live-document
- name: FindRequest
  property_count: 9
  slug: ditto-live-findrequest
- name: FindResponse
  property_count: 2
  slug: ditto-live-findresponse
- name: QueryRequest
  property_count: 2
  slug: ditto-live-queryrequest
- name: QueryResponse
  property_count: 7
  slug: ditto-live-queryresponse
- name: WriteRequest
  property_count: 1
  slug: ditto-live-writerequest
- name: WriteResponse
  property_count: 1
  slug: ditto-live-writeresponse
jsonld:
- class_count: 0
  name: Ditto Live Context
  property_count: 34
  slug: ditto-live-context
layout: provider
modified: '2026-06-12'
name: Ditto
nav: Providers
network: true
overview: 'Ditto publishes 6 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Apps API, BigPeerReplication API, and 3 more. Tagged areas include Developer Tools, Database, Synchronization, Peer-to-Peer, and Edge Computing.


  The Ditto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ditto''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, developer portal, and 10 more developer resources.'
plans:
- name: Ditto Live Plans Pricing
  plan_count: 3
  slug: ditto-live-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Ditto Live Rate Limits
  slug: ditto-live-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ditto API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ditto-live-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.2
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 50.0
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ditto-live/refs/heads/main/screenshots/ditto-live-2026-06-20T180058.png
security:
- kind: authentication
  name: Ditto Live Authentication
  slug: ditto-live-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ditto Live Domain Security
  slug: ditto-live-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ditto Live Trust Center
  slug: ditto-live-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: ditto-live
tags:
- Developer Tools
- Database
- Synchronization
- Peer-to-Peer
- Edge Computing
- Offline-First
- Mobile
website: https://www.ditto.com
---
