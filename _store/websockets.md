---
aid: websockets
name: WebSockets
description: WebSockets is a communication protocol providing full-duplex communication channels over a single TCP connection, enabling real-time data exchange between client and server. Standardized by RFC 6455 and the WHATWG Living Standard, it is fundamental to modern web architecture and enables reliable bidirectional communication between systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Full Duplex
  - Networking
  - Real-Time Communication
  - RFC 6455
  - Web Technology
url: https://raw.githubusercontent.com/api-evangelist/websockets/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis: []
common:
  - type: AsyncAPI
    url: asyncapi/websockets.yml
  - type: JSONSchema
    url: json-schema/websocket-handshake-request.json
  - type: JSONSchema
    url: json-schema/websocket-handshake-response.json
  - type: JSONSchema
    url: json-schema/websocket-frame.json
  - type: JSONSchema
    url: json-schema/websocket-message.json
  - type: JSONSchema
    url: json-schema/websocket-close-code.json
  - type: JSONStructure
    url: json-structure/websocket-message-structure.json
  - type: JSONLD
    url: json-ld/websockets-context.jsonld
  - type: Vocabulary
    url: vocabulary/websockets-vocabulary.yml
  - type: Specification
    url: https://www.rfc-editor.org/rfc/rfc6455
  - type: Living Standard
    url: https://websockets.spec.whatwg.org/
  - type: MDN Documentation
    url: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
