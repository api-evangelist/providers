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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-03'
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
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/smithy-lang/smithy/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/smithy-lang/smithy/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/smithy-lang/smithy/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/smithy-lang/smithy/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/smithy-lang/smithy/blob/main/LICENSE
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
overview: 'Smithy publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, IDL, SDK, API Design, and Interface Definition Language.


  The Smithy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Smithy''s developer surface includes documentation, getting-started guide, code examples, engineering blog, and 12 more developer resources.'
plans:
- name: Smithy Plans Pricing
  plan_count: 3
  slug: smithy-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Smithy Rate Limits
  slug: smithy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Smithy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: smithy-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Smithy API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: smithy-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 61.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 17.3
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 27.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- SDK
- API Design
- Interface Definition Language
- Toolchain
website: https://smithy.io
---
