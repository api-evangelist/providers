---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 12
asyncapis:
- description: AsyncAPI specification describing WebSocket communication patterns as defined by RFC 6455. WebSockets provide full-duplex communication channels over a single TCP connection, enabling real-time bidire
  name: WebSocket Communication API
  slug: websockets
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/websockets
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/websockets.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/websocket-handshake-request.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/websocket-handshake-response.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/websocket-frame.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/websocket-message.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/websocket-close-code.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/websocket-message-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/websockets-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/websockets-vocabulary.yml
- group: docs
  title: ''
  type: Specification
  url: https://www.rfc-editor.org/rfc/rfc6455
- group: other
  title: ''
  type: Living Standard
  url: https://websockets.spec.whatwg.org/
- group: docs
  title: ''
  type: MDN Documentation
  url: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
created: '2025-01-01'
description: WebSockets is a communication protocol providing full-duplex communication channels over a single TCP connection, enabling real-time data exchange between client and server. Standardized by RFC 6455 and the WHATWG Living Standard, it is fundamental to modern web architecture and enables reliable bidirectional communication between systems.
examples:
- key_count: 5
  name: Websocket Close Example
  slug: websocket-close-example
- key_count: 5
  name: Websocket Handshake Example
  slug: websocket-handshake-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/websockets.png
json_schemas:
- name: WebSocket Close Status Code
  property_count: 2
  slug: websocket-close-code
- name: WebSocket Frame
  property_count: 10
  slug: websocket-frame
- name: WebSocket Handshake Request
  property_count: 4
  slug: websocket-handshake-request
- name: WebSocket Handshake Response
  property_count: 3
  slug: websocket-handshake-response
- name: WebSocket Message
  property_count: 6
  slug: websocket-message
json_structures:
- name: Websocket Message Structure
  property_count: 0
  slug: websocket-message-structure
jsonld:
- class_count: 0
  name: Websockets Context
  property_count: 18
  slug: websockets-context
layout: provider
modified: '2026-05-03'
name: WebSockets
nav: Providers
network: true
overview: 'WebSockets is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Full Duplex, Networking, Real-Time Communication, RFC 6455, and Web Technology.


  The WebSockets catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.'
random_paper: 11
rules:
- effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: WebSockets API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 4
  slug: websockets-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: WebSockets API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: websockets-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 70.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 51.9
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 21.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/websockets/refs/heads/main/screenshots/websockets-2026-06-20T201337.png
slug: websockets
tags:
- Full Duplex
- Networking
- Real-Time Communication
- RFC 6455
- Web Technology
---
