---
aid: falco
url: https://raw.githubusercontent.com/api-evangelist/falco/refs/heads/main/apis.yml
apis:
- aid: falco:falco-http-api
  name: Falco HTTP API
  description: REST API served by the Falco web server providing health checks, version information, and rules management endpoints for the Falco runtime security engine.
  humanURL: https://falco.org/docs/
  tags:
  - Health Check
  - Runtime Security
  - Security
  properties:
  - type: Documentation
    url: https://falco.org/docs/
  - type: Reference
    url: https://falco.org/docs/reference/
  - type: OpenAPI
    url: openapi/falco-openapi.yml
  - type: JSONSchema
    url: json-schema/falco-alert-output.json
  - type: JSONSchema
    url: json-schema/falco-rules.json
  - type: GitHubRepository
    url: https://github.com/falcosecurity/falco
- aid: falco:falco-plugin-api
  name: Falco Plugin API
  description: The Falco Plugin API provides a C ABI interface for developing plugins that extend Falco with new event sources and field extractors. Plugins are shared libraries that implement the plugin API and can be loaded at runtime to add support for new data sources such as cloud audit logs, container activity, and custom event streams.
  humanURL: https://falco.org/docs/reference/plugins/plugin-api-reference/
  tags:
  - Developer Tools
  - Event Sources
  - Plugin
  properties:
  - type: Documentation
    url: https://falco.org/docs/developer-guide/
  - type: Reference
    url: https://falco.org/docs/reference/plugins/plugin-api-reference/
  - type: GitHubRepository
    url: https://github.com/falcosecurity/plugin-sdk-go
- aid: falco:falco-grpc-api
  name: Falco gRPC API
  description: The Falco gRPC API provided a streaming interface for consuming Falco alert outputs and querying version information from a running Falco instance. The embedded gRPC server and gRPC Output have been deprecated in Falco 0.43.0 and will be removed in a future release.
  humanURL: https://falco.org/docs/developer-guide/grpc/
  tags:
  - Deprecated
  - gRPC
  - Security
  properties:
  - type: Documentation
    url: https://falco.org/docs/developer-guide/grpc/
  - type: Deprecation Notice
    url: https://falco.org/blog/falco-0-43-0/
  - type: GitHubRepository
    url: https://github.com/falcosecurity/falco
name: Falco
tags:
- Cloud Native
- eBPF
- Runtime Security
- Security
- Threat Detection
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Falco is a cloud-native runtime security tool that detects unexpected application behavior and alerts on threats at runtime using eBPF. It is a CNCF graduated project that continuously monitors Linux kernel syscalls and compares them against configurable security rules to detect intrusions, privilege escalation, and other suspicious behaviors.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

