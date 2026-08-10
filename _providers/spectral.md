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
- description: Spectral is a flexible JSON/YAML linter and style guide enforcer with built-in support for OpenAPI (v3.1, v3.0, v2.0), Arazzo v1.0, and AsyncAPI v2.x. It enables teams to define custom rulesets to enf
  name: Spectral
  slug: spectral
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spectral-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spectralcode
- group: company
  title: ''
  type: Website
  url: https://stoplight.io/open-source/spectral
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stoplight.io/docs/spectral
- group: build
  title: ''
  type: GitHub
  url: https://github.com/stoplightio/spectral
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stoplightio
- group: build
  title: ''
  type: NPMPackage
  url: https://www.npmjs.com/package/@stoplight/spectral-cli
- group: commercial
  title: ''
  type: License
  url: https://github.com/stoplightio/spectral/blob/main/LICENSE
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/stoplightio/spectral/releases
- group: other
  title: ''
  type: Contributing
  url: https://github.com/stoplightio/spectral/blob/main/CONTRIBUTING.md
- group: company
  title: ''
  type: Blog
  url: https://blog.stoplight.io/feed
created: '2026-03-25'
description: Spectral is an open-source API style guide enforcer and linter from Stoplight, providing a flexible JSON/YAML linting engine with built-in support for OpenAPI (v3.1, v3.0, v2.0), Arazzo v1.0, and AsyncAPI v2.x. Teams use Spectral to define, share, and enforce API design standards through custom rulesets, integrating into CI/CD pipelines, VS Code, and the Stoplight Platform for real-time style guide feedback.
examples:
- key_count: 3
  name: Spectral Openapi Ruleset Example
  slug: spectral-openapi-ruleset-example
finops:
- name: Spectral Finops
  service_category: API
  slug: spectral-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spectral.png
json_schemas:
- name: Spectral Ruleset
  property_count: 5
  slug: spectral-ruleset
json_structures:
- name: Spectral Ruleset Structure
  property_count: 0
  slug: spectral-ruleset-structure
jsonld:
- class_count: 9
  name: Spectral Context
  property_count: 10
  slug: spectral-context
layout: provider
modified: '2026-05-02'
name: Spectral
nav: Providers
network: true
overview: 'Spectral publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, API Linting, API Style Guide, AsyncAPI, and JSON Schema.


  The Spectral catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spectral''s developer surface includes documentation, GitHub presence, release notes, engineering blog, and 7 more developer resources.'
plans:
- name: Spectral Plans Pricing
  plan_count: 3
  slug: spectral-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Spectral Rate Limits
  slug: spectral-rate-limits
rules:
- name: Spectral API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spectral-jsonschema-spectral-rules
- name: Spectral API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 2
    info: 0
    warn: 2
  slug: spectral-rules
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 27.4
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 37.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spectral/refs/heads/main/screenshots/spectral-2026-06-20T194300.png
security:
- kind: domain-security
  name: Spectral Domain Security
  slug: spectral-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spectral
tags:
- API Design
- API Linting
- API Style Guide
- AsyncAPI
- JSON Schema
- OpenAPI
- Quality Assurance
website: https://stoplight.io/open-source/spectral
---
