---
aid: fluentd
url: https://raw.githubusercontent.com/api-evangelist/fluentd/refs/heads/main/apis.yml
apis:
- aid: fluentd:fluentd-plugin-api
  name: Fluentd Plugin API
  description: The Fluentd Plugin API allows developers to write custom input, output, filter, parser, formatter, and buffer plugins in Ruby. Plugins are distributed as RubyGems and integrate with Fluentd's plugin management system to extend data collection and processing pipelines.
  humanURL: https://docs.fluentd.org/plugin-development
  tags:
  - Open Source
  - Plugin Development
  - Ruby
  properties:
  - type: Documentation
    url: https://docs.fluentd.org/plugin-development
  - type: Reference
    url: https://docs.fluentd.org/plugin-development/api-plugin-base
- aid: fluentd:fluentd-forward-protocol
  name: Fluentd Forward Protocol
  description: The Fluentd Forward Protocol is a binary protocol used to transport event streams between Fluentd nodes and compatible agents over TCP. It supports multiple transport modes including Message, Forward, PackedForward, and CompressedPackedForward, and includes authentication and heartbeat mechanisms.
  humanURL: https://github.com/fluent/fluentd/wiki/Forward-Protocol-Specification-v1
  tags:
  - Logging
  - Networking
  - Protocol
  properties:
  - type: Documentation
    url: https://github.com/fluent/fluentd/wiki/Forward-Protocol-Specification-v1
  - type: Reference
    url: https://docs.fluentd.org/input/forward
  - type: AsyncAPI
    url: asyncapi/fluentd-forward-protocol-asyncapi.yml
- aid: fluentd:fluentd-http-input
  name: Fluentd HTTP Input API
  description: The Fluentd HTTP Input plugin exposes an HTTP endpoint that accepts log records posted as JSON or form-encoded data. It allows applications to send events to Fluentd over standard HTTP, making it accessible from any language or platform that can make HTTP requests.
  humanURL: https://docs.fluentd.org/input/http
  tags:
  - HTTP
  - Input
  - Logging
  properties:
  - type: Documentation
    url: https://docs.fluentd.org/input/http
  - type: OpenAPI
    url: openapi/fluentd-http-input-openapi.yml
name: Fluentd
tags:
- Data Collection
- Logging
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Open source data collector for unified logging layer that allows you to unify data collection and consumption for better use and understanding of data.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

