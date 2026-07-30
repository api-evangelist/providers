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
api_count: 1
apis:
- description: The RAML (RESTful API Modeling Language) specification defines a YAML 1.2-based language for describing HTTP-based APIs. RAML 1.0 introduces a unified type system, annotations, libraries, overlays, ex
  name: RAML Specification
  slug: raml-spec
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raml-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://raml.org
- group: docs
  title: ''
  type: Documentation
  url: https://raml.org/developers/raml-100-tutorial
- group: docs
  title: ''
  type: Specification
  url: https://github.com/raml-org/raml-spec
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/raml-org
- group: operate
  title: ''
  type: Forums
  url: https://forum.raml.org
- group: other
  title: ''
  type: Parser JavaScript
  url: https://github.com/raml-org/raml-js-parser-2
- group: other
  title: ''
  type: Parser PHP
  url: https://github.com/raml-org/raml-php-parser
- group: other
  title: ''
  type: TCK
  url: https://github.com/raml-org/raml-tck
- group: docs
  title: ''
  type: JSONSchemaConverter
  url: https://github.com/raml-org/ramldt2jsonschema
- group: other
  title: ''
  type: WebapiParser
  url: https://github.com/raml-org/webapi-parser
- group: design
  title: ''
  type: JSONLD
  url: json-ld/raml-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/raml-vocabulary.yml
created: '2026-03-25'
description: RAML (RESTful API Modeling Language) is a YAML-based specification language for describing RESTful APIs with first-class support for reusable patterns, traits, resource types, data type annotations, libraries, overlays, and extensions. Developed by MuleSoft and Salesforce, RAML 1.0 is the current stable version. The raml-org GitHub organization maintains the canonical specification and related tooling, all of which are archived and read-only as of February 2024.
examples:
- key_count: 4
  name: Raml Basic Api Example
  slug: raml-basic-api-example
- key_count: 4
  name: Raml Traits Example
  slug: raml-traits-example
finops:
- name: Raml Finops
  service_category: API
  slug: raml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raml.png
json_schemas:
- name: RAML 1.0 Document
  property_count: 13
  slug: raml-document
json_structures:
- name: Raml Document Structure
  property_count: 0
  slug: raml-document-structure
jsonld:
- class_count: 15
  name: Raml Context
  property_count: 18
  slug: raml-context
layout: provider
modified: '2026-05-02'
name: RAML
nav: Providers
network: true
overview: 'RAML publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, Specification Language, Standards, YAML, and REST.


  The RAML catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RAML''s developer surface includes documentation and 12 more developer resources.'
plans:
- name: Raml Plans Pricing
  plan_count: 3
  slug: raml-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Raml Rate Limits
  slug: raml-rate-limits
rules:
- name: RAML API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: raml-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.5
  delta: -5.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 27.4
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 40.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/raml/refs/heads/main/screenshots/raml-2026-06-20T192542.png
security:
- kind: domain-security
  name: Raml Domain Security
  slug: raml-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: raml
tags:
- API Design
- Specification Language
- Standards
- YAML
- REST
- API Modeling
website: https://raml.org
---
