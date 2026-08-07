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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Vacuum is the world's fastest OpenAPI linter written in Go. It processes API specifications at lightning speed with full Spectral ruleset compatibility, interactive dashboards, HTML reports, and Langu
  name: Vacuum
  slug: vacuum
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vacuum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quobix.com/vacuum
- group: docs
  title: ''
  type: Documentation
  url: https://quobix.com/vacuum/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daveshanley
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/daveshanley/vacuum
- group: build
  title: ''
  type: NPM Package
  url: https://www.npmjs.com/package/@quobix/vacuum
- group: other
  title: ''
  type: Docker Image
  url: https://hub.docker.com/r/dshanley/vacuum
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/UAcUF78MQN
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/json-schema/vacuum-ruleset-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/json-schema/vacuum-report-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/vocabulary/vacuum-vocabulary.yml
created: '2026-03-25'
description: Vacuum is the world's fastest and most versatile OpenAPI linter and toolkit, built in Go for validating and linting API specifications at scale. It is 100% compatible with Spectral rulesets and supports OpenAPI 3.0, 3.1, and 3.2.
examples:
- key_count: 2
  name: Vacuum Ruleset Example
  slug: vacuum-ruleset-example
finops:
- name: Vacuum Finops
  service_category: API
  slug: vacuum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vacuum.png
json_schemas:
- name: Vacuum Report
  property_count: 3
  slug: vacuum-report
- name: Vacuum Ruleset
  property_count: 3
  slug: vacuum-ruleset
json_structures:
- name: Vacuum Ruleset Structure
  property_count: 0
  slug: vacuum-ruleset-structure
jsonld:
- class_count: 17
  name: Vacuum Context
  property_count: 0
  slug: vacuum-context
layout: provider
modified: '2026-05-03'
name: Vacuum
nav: Providers
network: true
overview: 'Vacuum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, Documentation, Linting, OpenAPI, and Spectral.


  The Vacuum catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vacuum''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Vacuum Plans Pricing
  plan_count: 3
  slug: vacuum-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 5
  name: Vacuum Rate Limits
  slug: vacuum-rate-limits
rules:
- name: Vacuum API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: vacuum-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 31.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/screenshots/vacuum-2026-06-20T200740.png
security:
- kind: domain-security
  name: Vacuum Domain Security
  slug: vacuum-domain-security
  summary_line: TLSv1.3
slug: vacuum
tags:
- API Design
- Documentation
- Linting
- OpenAPI
- Spectral
- Developer Tools
- Go
website: https://quobix.com/vacuum
---
