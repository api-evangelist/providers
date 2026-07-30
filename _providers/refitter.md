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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Refitter is a .NET source generator and CLI tool that produces Refit HTTP client interfaces from OpenAPI 2.0 and 3.x specifications. Supports compile-time code generation via MSBuild source generators
  name: Refitter
  slug: refitter
- description: The type-safe REST library for .NET that Refitter generates interfaces for. Refit turns REST APIs into live interfaces by decorating C# interfaces with attributes describing the HTTP endpoints, then g
  name: Refit
  slug: refit
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://refitter.github.io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/christianhelle/refitter
- group: docs
  title: ''
  type: Documentation
  url: https://refitter.github.io
- group: operate
  title: ''
  type: Issues
  url: https://github.com/christianhelle/refitter/issues
- group: build
  title: ''
  type: NuGetPackage
  url: https://www.nuget.org/packages/Refitter
- group: commercial
  title: ''
  type: License
  url: https://github.com/christianhelle/refitter/blob/main/LICENSE
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refitter-settings-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/refitter-output-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/refitter-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/refitter-vocabulary.yml
created: '2026-03-25'
description: Refitter is a .NET tool and source generator that produces Refit HTTP client interfaces from OpenAPI specifications. It runs at compile time as a source generator or as a standalone CLI tool (dotnet-refitter), enabling type-safe API consumption in .NET projects. Refitter reads OpenAPI 2.0 (Swagger) and OpenAPI 3.x specifications and generates strongly-typed C# interface definitions and model classes compatible with the Refit library.
finops:
- name: Refitter Finops
  service_category: API
  slug: refitter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/refitter.png
json_schemas:
- name: Refitter Settings
  property_count: 18
  slug: refitter-settings
json_structures:
- name: Refitter Output Structure
  property_count: 0
  slug: refitter-output-structure
jsonld:
- class_count: 9
  name: Refitter Context
  property_count: 7
  slug: refitter-context
layout: provider
modified: '2026-05-02'
name: Refitter
nav: Providers
network: true
overview: 'Refitter publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, C#, Code Generation, OpenAPI, and Refit.


  The Refitter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Refitter''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Refitter Plans Pricing
  plan_count: 3
  slug: refitter-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Refitter Rate Limits
  slug: refitter-rate-limits
rules:
- name: Refitter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: refitter-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.2
  delta: -4.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 35.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/refitter/refs/heads/main/screenshots/refitter-2026-06-20T192745.png
slug: refitter
tags:
- .NET
- C#
- Code Generation
- OpenAPI
- Refit
- Source Generator
- Type-Safe
website: https://refitter.github.io
---
