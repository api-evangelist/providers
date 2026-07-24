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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 13.5
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: The Smithy Interface Definition Language (IDL) is a specification for defining API models using shapes and traits. Models can be written in the Smithy IDL syntax or the JSON AST representation. Smithy
  name: Smithy IDL
  slug: smithy-idl
- description: The Smithy CLI is a command-line tool for building, validating, diffing, and transforming Smithy models. It can generate JSON AST representations, run model validation, perform backwards-compatibility
  name: Smithy CLI
  slug: smithy-cli
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smithy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smithy.io
- group: docs
  title: ''
  type: Documentation
  url: https://smithy.io/2.0/
- group: docs
  title: ''
  type: Specification
  url: https://smithy.io/2.0/spec/
- group: start
  title: ''
  type: GettingStarted
  url: https://smithy.io/2.0/quickstart.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smithy-lang
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/smithy-lang/smithy
- group: build
  title: ''
  type: Examples
  url: https://github.com/smithy-lang/smithy-examples
- group: other
  title: ''
  type: Awesome List
  url: https://github.com/smithy-lang/awesome-smithy
- group: other
  title: ''
  type: AWS API Models
  url: https://github.com/aws/api-models-aws
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/developer/tag/smithy/
created: '2026-03-25'
description: Smithy is an open source, protocol-agnostic interface definition language (IDL) and toolchain developed at AWS for defining, validating, and generating API clients, servers, and documentation for any programming language. It powers the AWS SDK code generation pipeline and supports protocol-agnostic API modeling with traits, validators, and code generators. Smithy IDL 2.0 is the current stable version.
examples:
- key_count: 4
  name: Smithy Simple Service Example
  slug: smithy-simple-service-example
finops:
- name: Smithy Finops
  service_category: API
  slug: smithy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smithy.png
json_schemas:
- name: Smithy Model (JSON AST)
  property_count: 3
  slug: smithy-model
- name: Smithy Shape
  property_count: 12
  slug: smithy-shape
json_structures:
- name: Smithy Model Structure
  property_count: 0
  slug: smithy-model-structure
jsonld:
- class_count: 26
  name: Smithy Context
  property_count: 0
  slug: smithy-context
layout: provider
modified: '2026-05-02'
name: Smithy
nav: Providers
network: true
overview: 'Smithy publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, IDL, SDKs, API Design, and Interface Definition Language.


  The Smithy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Smithy''s developer surface includes documentation, getting-started guide, code examples, engineering blog, and 7 more developer resources.'
plans:
- name: Smithy Plans Pricing
  plan_count: 3
  slug: smithy-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Smithy Rate Limits
  slug: smithy-rate-limits
rules:
- name: Smithy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: smithy-jsonschema-spectral-rules
- name: Smithy API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: smithy-rules
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 15.1
    developer_ergonomics: 21.7
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 37.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smithy/refs/heads/main/screenshots/smithy-2026-06-20T194054.png
security:
- kind: domain-security
  name: Smithy Domain Security
  slug: smithy-domain-security
  summary_line: TLSv1.3
slug: smithy
tags:
- Code Generation
- IDL
- SDKs
- API Design
- Interface Definition Language
- Toolchain
website: https://smithy.io
---
