---
aid: twirp
name: Twirp
description: Twirp is a simple RPC framework built on Protocol Buffers, created by Twitch, that generates routing and serialization code from Protobuf service definitions for Go and other languages. Similar to gRPC but runs on the standard library's net/http Server without custom HTTP server or transport implementations. Supports both binary Protobuf and JSON serialization, making debugging easy. Uses HTTP POST for all requests with URLs in the format /twirp/[Package].[Service]/[Method]. Protocol version 7 is the current stable version. Licensed under Apache 2.0.
type: Contract
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Protocol Buffers
  - RPC
  - Go
  - SDKs
  - Open Source
  - Protobuf
created: '2026-03-27'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/twirp/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: twirp:twirp-framework
    name: Twirp RPC Framework
    description: 'Twirp is a simple RPC framework with protobuf service definitions. Define your service in a .proto file and Twirp generates servers and clients implementing the Twirp wire protocol. Services are exposed over HTTP using POST requests with paths in the form /twirp/[Package].[Service]/[Method]. Supports both Protobuf binary encoding (Content-Type: application/protobuf) and JSON encoding (Content-Type: application/json). Includes a Go runtime and protoc-gen-twirp code generator plugin.'
    humanURL: https://twitchtv.github.io/twirp/
    baseURL: https://twitchtv.github.io/twirp/
    tags:
      - Protocol Buffers
      - RPC
      - Go
      - Code Generation
    properties:
      - type: Documentation
        url: https://twitchtv.github.io/twirp/docs/intro.html
      - type: Getting Started
        url: https://twitchtv.github.io/twirp/docs/install.html
      - type: GitHub
        url: https://github.com/twitchtv/twirp
      - type: Wire Protocol
        url: https://github.com/twitchtv/twirp/blob/main/PROTOCOL.md
common:
  - type: Website
    url: https://twitchtv.github.io/twirp/
  - type: Documentation
    url: https://twitchtv.github.io/twirp/docs/intro.html
  - type: GitHub Organization
    url: https://github.com/twitchtv
  - type: GitHub Repository
    url: https://github.com/twitchtv/twirp
  - type: Wire Protocol
    url: https://github.com/twitchtv/twirp/blob/main/PROTOCOL.md
  - type: License
    url: https://github.com/twitchtv/twirp/blob/main/LICENSE
  - type: Contributing
    url: https://github.com/twitchtv/twirp/blob/main/CONTRIBUTING.md
  - type: JSONSchema
    url: json-schema/twirp-error-schema.json
  - type: JSONLD
    url: json-ld/twirp-context.jsonld
  - type: Vocabulary
    url: vocabulary/twirp-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
