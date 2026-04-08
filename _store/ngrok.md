---
aid: ngrok
url: https://raw.githubusercontent.com/api-evangelist/ngrok/refs/heads/main/apis.yml
apis:
- aid: ngrok:ngrok
  name: Ngrok API
  tags:
  - Compute
  - Demonstration
  - Gateways
  - Platform
  - Proxies
  - Servers
  - Testing
  - Tunnels
  humanURL: https://ngrok.com/docs/api
  properties:
  - url: https://ngrok.com/docs/api
    type: Documentation
  - url: openapi/ngrok-api-openapi.yml
    type: OpenAPI
  - url: json-schema/tunnel.json
    type: JSONSchema
  - url: json-schema/endpoint.json
    type: JSONSchema
  - url: json-schema/https-edge.json
    type: JSONSchema
  - url: json-schema/tcp-edge.json
    type: JSONSchema
  - url: json-schema/tls-edge.json
    type: JSONSchema
  - url: json-schema/reserved-domain.json
    type: JSONSchema
  - url: json-schema/reserved-addr.json
    type: JSONSchema
  - url: json-schema/api-key.json
    type: JSONSchema
  - url: json-schema/ip-policy.json
    type: JSONSchema
  - url: json-schema/tls-certificate.json
    type: JSONSchema
  - url: json-schema/event-subscription.json
    type: JSONSchema
  - url: json-schema/tunnel-session.json
    type: JSONSchema
  - url: json-ld/ngrok-context.jsonld
    type: JSONLD
  description: The ngrok API provides programmatic access to all of ngrok's resources. The API is REST-ish. It follows most of the conventions of a REST API but diverges slightly when the REST model does not fit well. The API listens only on port 443 to help avoid any accidental unencrypted requests. All API access requires an API key.
name: Ngrok
tags:
- Compute
- Demonstration
- Gateways
- Platform
- Proxies
- Servers
- Testing
- Tunnels
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Ngrok is a service that creates secure tunnels to local servers, allowing them to be accessed remotely over the internet. This means that developers can easily test and share their web applications without having to deploy them to a public server. Ngrok provides a unique URL for each tunnel, making it simple to share the application with others for testing or demonstration purposes.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

