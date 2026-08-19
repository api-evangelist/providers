---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regular-expressions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.regular-expressions.info/
- group: company
  title: ''
  type: Website
  url: https://regex101.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.python.org/3/library/re.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions
- group: docs
  title: ''
  type: Documentation
  url: https://www.pcre.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nicowillis/awesome-regex
- group: docs
  title: ''
  type: Documentation
  url: https://regexlib.com/
- group: docs
  title: ''
  type: Documentation
  url: https://en.wikipedia.org/wiki/Regular_expression
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/regular-expressions/refs/heads/main/json-schema/regular-expressions-pattern-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/regular-expressions/refs/heads/main/json-structure/regular-expressions-pattern-structure.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/regular-expressions/refs/heads/main/json-ld/regular-expressions-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/regular-expressions/refs/heads/main/vocabulary/regular-expressions-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/regular-expressions/refs/heads/main/examples/regular-expressions-email-pattern-example.json
created: '2025-01-01'
description: A sequence of characters that define a search pattern, commonly used for string matching, validation, and text manipulation across programming languages and data processing pipelines. Regular expressions are supported natively in virtually every programming language and are foundational to text processing, log analysis, data validation, and search tooling.
examples:
- key_count: 13
  name: Regular Expressions Email Pattern Example
  slug: regular-expressions-email-pattern-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/regular-expressions.png
json_schemas:
- name: Regular Expression Pattern
  property_count: 13
  slug: regular-expressions-pattern
json_structures:
- name: Regular Expressions Pattern Structure
  property_count: 0
  slug: regular-expressions-pattern-structure
jsonld:
- class_count: 5
  name: Regular Expressions Context
  property_count: 9
  slug: regular-expressions-context
layout: provider
modified: '2026-05-02'
name: Regular Expressions
nav: Providers
network: true
overview: 'Regular Expressions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pattern Matching, Programming, String Manipulation, Text Processing, and Validation.


  The Regular Expressions catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Regular Expressions'' developer surface includes documentation, code examples, and 12 more developer resources.'
random_paper: 81
rules:
- effective_rule_count: 5
  extends: []
  name: Regular Expressions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: regular-expressions-jsonschema-spectral-rules
score:
  band: emerging
  composite: 13.8
  delta: -5.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 12.7
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 5.3
  previous_composite: 18.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/regular-expressions/refs/heads/main/screenshots/regular-expressions-2026-06-20T192758.png
security:
- kind: domain-security
  name: Regular Expressions Domain Security
  slug: regular-expressions-domain-security
  summary_line: TLSv1.3 · HSTS
slug: regular-expressions
tags:
- Pattern Matching
- Programming
- String Manipulation
- Text Processing
- Validation
- Search
- Parsing
website: https://www.regular-expressions.info/
---
