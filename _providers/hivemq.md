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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Hivemq Agentic Access
  operation_count: 30
  slug: hivemq-agentic-access
  summary_line: 30 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: MQTT 3.x and MQTT 5 messaging endpoints exposed over WebSocket for browser and edge clients to publish and subscribe to topics. Used by web dashboards and JavaScript IoT clients to interact with the H
  name: HiveMQ MQTT over WebSocket
  slug: mqtt-websocket
- baseURL: http://127.0.0.1:8888
  baseurl_source: declared
  description: The Data Hub API from HiveMQ — 4 operation(s) for data hub.
  name: HiveMQ Data Hub API
  slug: hivemq-data-hub-api
- baseURL: http://127.0.0.1:8888
  baseurl_source: declared
  description: The Management API from HiveMQ — 9 operation(s) for management.
  name: HiveMQ Management API
  slug: hivemq-management-api
- baseURL: http://127.0.0.1:8888
  baseurl_source: declared
  description: The Mqtt API from HiveMQ — 5 operation(s) for mqtt.
  name: HiveMQ Mqtt API
  slug: hivemq-mqtt-api
artifact_total: 16
asyncapis:
- description: AsyncAPI description of the message-oriented surface of a HiveMQ enterprise MQTT broker. HiveMQ implements MQTT 3.1, MQTT 3.1.1, and MQTT 5 over plain TCP, TLS, WebSocket, and Secure WebSocket listene
  name: HiveMQ MQTT Broker
  slug: hivemq-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HiveMQ REST Data Hub API
  slug: open-hivemq-data-hub-api
- collection_type: open
  name: HiveMQ REST Data Hub Management API
  slug: open-hivemq-management-api
- collection_type: open
  name: HiveMQ REST Data Hub Mqtt API
  slug: open-hivemq-mqtt-api
- collection_type: open
  name: HiveMQ REST API
  slug: open-hivemq
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hivemq-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hivemq-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hivemq-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hivemq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hivemq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hivemq-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hivemq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hivemq.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hivemq.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.hivemq.com/signup
- group: other
  title: ''
  type: Cloud
  url: https://www.hivemq.com/cloud
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hivemq
- group: operate
  title: ''
  type: Community Edition
  url: https://www.hivemq.com/developers/community
- group: company
  title: ''
  type: Blog
  url: https://www.hivemq.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hivemq
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.hivemq.com/llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hivemq.com/developers/
- group: start
  title: ''
  type: SignUp
  url: https://console.hivemq.cloud/
- group: start
  title: ''
  type: Login
  url: https://console.hivemq.cloud/
- group: operate
  title: ''
  type: Support
  url: https://www.hivemq.com/company/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hivemq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hivemq.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hivemq.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hivemq.cloud/
- group: auth
  title: ''
  type: Security
  url: https://www.hivemq.com/solutions/technology/hivemq-security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.hivemq.com/solutions/technology/hivemq-security/
- group: build
  title: ''
  type: Packages
  url: packages/hivemq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hivemq-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hivemq-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hivemq-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hivemq-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hivemq-llms.txt
created: '2026-05-11'
description: HiveMQ is an enterprise MQTT broker and IoT connectivity platform that provides reliable, scalable bidirectional messaging between connected devices and back-end systems using the MQTT protocol. It supports MQTT 3, MQTT 5, MQTT over WebSocket, clustering, multi-cloud deployments, and an extensible enterprise extension framework for security, data routing, and stream processing through HiveMQ Data Hub. HiveMQ exposes a REST API (OpenAPI 3.0) for broker administration, client management, backups, trace recordings, and Data Hub policy management.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hivemq.png
layout: provider
modified: '2026-08-08'
name: HiveMQ
nav: Providers
network: true
overview: 'HiveMQ publishes 4 APIs on the [APIs.io](https://apis.io/) network, including MQTT over WebSocket, Data Hub API, Management API, and 1 more. Tagged areas include MQTT, IoT, Messaging, Message Broker, and Pub-Sub.


  The HiveMQ catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  HiveMQ''s developer surface includes authentication, documentation, pricing, signup flow, GitHub presence, engineering blog, support, and 25 more developer resources.'
random_paper: 20
rules:
- effective_rule_count: 29
  extends:
  - spectral:asyncapi
  name: HiveMQ API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: hivemq-asyncapi-spectral-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 79.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 29.5
    contract_quality: 57.2
    developer_ergonomics: 52.4
    discoverability: 66.7
    governance: 29.5
    operational_transparency: 28.9
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hivemq/refs/heads/main/screenshots/hivemq-2026-07-25T221301.png
security:
- kind: authentication
  name: Hivemq Authentication
  slug: hivemq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hivemq Domain Security
  slug: hivemq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hivemq Vulnerability Disclosure
  slug: hivemq-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Hivemq Trust Center
  slug: hivemq-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: hivemq
tags:
- MQTT
- IoT
- Messaging
- Message Broker
- Pub-Sub
- WebSocket
website: https://www.hivemq.com
---
