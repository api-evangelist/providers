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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
  score: 7.7
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: Refitter is a .NET source generator and CLI tool that produces Refit HTTP client interfaces from OpenAPI 2.0 and 3.x specifications. Supports compile-time code generation via MSBuild source generators
  name: Refitter
  slug: refitter
- description: The type-safe REST library for .NET that Refitter generates interfaces for. Refit turns REST APIs into live interfaces by decorating C# interfaces with attributes describing the HTTP endpoints, then g
  name: Refit
  slug: refit
artifact_total: 12
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
  type: APIReference
  url: https://refitter.github.io/api/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://refitter.github.io/articles/cli-tool.html
- group: operate
  title: ''
  type: Support
  url: https://github.com/christianhelle/refitter/discussions
- group: build
  title: ''
  type: Packages
  url: packages/refitter-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/refitter-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/refitter-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/refitter-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/refitter-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://refitter.github.io/articles/breaking-changes-v2-0-0.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/refitter-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/christianhelle/refitter/security/policy
- group: design
  title: ''
  type: Conformance
  url: conformance/refitter-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/refitter-llms.txt
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refitter-refitter-file-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refitter-format-mappings-schema.json
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
- name: Refitter Format Mappings
  property_count: 0
  slug: refitter-format-mappings
- name: Refitter Refitter File
  property_count: 52
  slug: refitter-refitter-file
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
modified: '2026-08-06'
name: Refitter
nav: Providers
network: true
overview: 'Refitter publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, C#, Code Generation, OpenAPI, and Refit.


  The Refitter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Refitter''s developer surface includes documentation, API reference, getting-started guide, support, CLI, changelog, and 20 more developer resources.'
plans:
- name: Refitter Plans Pricing
  plan_count: 3
  slug: refitter-plans-pricing
random_paper: 57
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
  composite: 38.3
  delta: -8.9
  facets:
    commercial_clarity: 15.8
    contract_quality: 12.9
    developer_ergonomics: 50.0
    discoverability: 66.7
    governance: 81.3
    operational_transparency: 42.1
  previous_composite: 47.2
  provenance:
    conformance: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/refitter/refs/heads/main/screenshots/refitter-2026-06-20T192745.png
security:
- kind: vulnerability-disclosure
  name: Refitter Vulnerability Disclosure
  slug: refitter-vulnerability-disclosure
  summary_line: disclosure policy published
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
