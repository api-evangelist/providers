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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 5.8
  scored_at: '2026-07-27'
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
random_paper: 62
rules:
- name: WebSockets API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 4
  slug: websockets-asyncapi-spectral-rules
- name: WebSockets API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: websockets-jsonschema-spectral-rules
score:
  band: emerging
  composite: 26.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 37.7
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 78.9
    operational_transparency: 5.3
  previous_composite: 26.3
  schema_version: 0.5
  scored_at: '2026-07-27'
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
