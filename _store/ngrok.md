---
aid: ngrok
name: ngrok
description: ngrok is a unified application delivery network for developers, providing secure tunnels, ingress-as-a-service, API gateway, and AI gateway capabilities. It enables developers to expose local services on the public internet, manage edge ingress, and route traffic to AI providers without redeploying applications. ngrok provides a unique URL for each tunnel, traffic policy controls, and a comprehensive REST API for programmatic management of all resources.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Gateway
  - API Gateway
  - Compute
  - Developer Tools
  - Gateways
  - Ingress
  - Platform
  - Proxies
  - Servers
  - Tunnels
url: https://raw.githubusercontent.com/api-evangelist/ngrok/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ngrok:ngrok
    name: ngrok API
    description: The ngrok API provides programmatic access to all of ngrok's resources. The API is REST-ish, follows most REST conventions, and listens only on port 443 to avoid accidental unencrypted requests. All API access requires an API key. Resources include endpoints, tunnels, edges (HTTPS, TCP, TLS), backends, reserved domains and addresses, IP policies and restrictions, TLS and SSH certificates, event subscriptions, API keys, and credentials.
    humanURL: https://ngrok.com/docs/api
    baseURL: https://api.ngrok.com
    tags:
      - API Gateway
      - Compute
      - Demonstration
      - Gateways
      - Platform
      - Proxies
      - Servers
      - Testing
      - Tunnels
    properties:
      - type: Documentation
        url: https://ngrok.com/docs/api
      - type: APIReference
        url: https://ngrok.com/docs/api
      - type: OpenAPI
        url: openapi/ngrok-api-openapi.yml
      - type: JSONLD
        url: json-ld/ngrok-context.jsonld
      - type: JSONSchema
        url: json-schema/tunnel.json
      - type: JSONSchema
        url: json-schema/endpoint.json
      - type: JSONSchema
        url: json-schema/https-edge.json
      - type: JSONSchema
        url: json-schema/tcp-edge.json
      - type: JSONSchema
        url: json-schema/tls-edge.json
      - type: JSONSchema
        url: json-schema/reserved-domain.json
      - type: JSONSchema
        url: json-schema/reserved-addr.json
      - type: JSONSchema
        url: json-schema/api-key.json
      - type: JSONSchema
        url: json-schema/ip-policy.json
      - type: JSONSchema
        url: json-schema/tls-certificate.json
      - type: JSONSchema
        url: json-schema/event-subscription.json
      - type: JSONSchema
        url: json-schema/tunnel-session.json
      - type: GitHubRepository
        url: https://github.com/ngrok/ngrok-openapi
        title: ngrok-openapi
common:
  - type: Website
    url: https://ngrok.com
  - type: Documentation
    url: https://ngrok.com/docs
  - type: APIReference
    url: https://ngrok.com/docs/api
  - type: GettingStarted
    url: https://ngrok.com/docs/getting-started
  - type: Blog
    url: https://ngrok.com/blog
  - type: ChangeLog
    url: https://ngrok.com/docs/changelog
  - type: Pricing
    url: https://ngrok.com/pricing
  - type: Support
    url: https://ngrok.com/support
  - type: StatusPage
    url: https://status.ngrok.com
  - type: GitHubOrganization
    url: https://github.com/ngrok
  - type: SDK
    url: https://github.com/ngrok/ngrok-go
    title: Go SDK
  - type: SDK
    url: https://github.com/ngrok/ngrok-rust
    title: Rust SDK
  - type: SDK
    url: https://github.com/ngrok/ngrok-javascript
    title: JavaScript SDK
  - type: SDK
    url: https://github.com/ngrok/ngrok-python
    title: Python SDK
  - type: Terraform
    url: https://registry.terraform.io/providers/ngrok/ngrok/latest
    title: Terraform Provider
  - type: KubernetesOperator
    url: https://github.com/ngrok/ngrok-operator
    title: Kubernetes Operator
  - type: X
    url: https://x.com/ngrokHQ
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
