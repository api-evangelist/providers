---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Twirp is a simple RPC framework with protobuf service definitions. Define your service in a .proto file and Twirp generates servers and clients implementing the Twirp wire protocol. Services are expos
  name: Twirp RPC Framework
  slug: twirp-framework
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://twitchtv.github.io/twirp/
- group: docs
  title: ''
  type: Documentation
  url: https://twitchtv.github.io/twirp/docs/intro.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twitchtv
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/twitchtv/twirp
- group: other
  title: ''
  type: Wire Protocol
  url: https://github.com/twitchtv/twirp/blob/main/PROTOCOL.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/twitchtv/twirp/blob/main/LICENSE
- group: other
  title: ''
  type: Contributing
  url: https://github.com/twitchtv/twirp/blob/main/CONTRIBUTING.md
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/twirp-error-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/twirp-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/twirp-vocabulary.yml
created: '2026-03-27'
description: Twirp is a simple RPC framework built on Protocol Buffers, created by Twitch, that generates routing and serialization code from Protobuf service definitions for Go and other languages. Similar to gRPC but runs on the standard library's net/http Server without custom HTTP server or transport implementations. Supports both binary Protobuf and JSON serialization, making debugging easy. Uses HTTP POST for all requests with URLs in the format /twirp/[Package].[Service]/[Method]. Protocol version 7 is the current stable version. Licensed under Apache 2.0.
finops:
- name: Twirp Finops
  service_category: API
  slug: twirp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/twirp.png
json_schemas:
- name: Twirp Error
  property_count: 3
  slug: twirp-error
json_structures:
- name: Twirp Error Structure
  property_count: 0
  slug: twirp-error-structure
jsonld:
- class_count: 0
  name: Twirp Context
  property_count: 5
  slug: twirp-context
layout: provider
modified: '2026-05-03'
name: Twirp
nav: Providers
network: true
overview: 'Twirp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Protocol Buffers, RPC, Go, SDKs, and Open Source.


  The Twirp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Twirp''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Twirp Plans Pricing
  plan_count: 3
  slug: twirp-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 5
  name: Twirp Rate Limits
  slug: twirp-rate-limits
rules:
- name: Twirp API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: twirp-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 31.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twirp/refs/heads/main/screenshots/twirp-2026-06-20T195851.png
slug: twirp
tags:
- Protocol Buffers
- RPC
- Go
- SDKs
- Open Source
- Protobuf
website: https://twitchtv.github.io/twirp/
---
