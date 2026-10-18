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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Vacuum is the world's fastest OpenAPI linter written in Go. It processes API specifications at lightning speed with full Spectral ruleset compatibility, interactive dashboards, HTML reports, and Langu
  name: Vacuum
  slug: vacuum
artifact_total: 11
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/plans/vacuum-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vacuum-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/rate-limits/vacuum-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vacuum-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/finops/vacuum-finops.yml
  title: ''
  type: FinOps
  url: finops/vacuum-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://quobix.com/articles/
- group: company
  title: ''
  type: BlogRSS
  url: https://quobix.com/articles/index.xml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/daveshanley/vacuum/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/daveshanley/vacuum/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/daveshanley/vacuum/blob/main/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/security/vacuum-domain-security.yml
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
- has_sources: false
  method: generated
  name: Vacuum Finops
  primary_unit: ''
  service_category: API
  slug: vacuum-finops
  template: true
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
modified: '2026-10-06'
name: Vacuum
nav: Providers
network: true
overview: 'Vacuum is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, Documentation, Linting, OpenAPI, and Spectral.


  The Vacuum catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vacuum''s developer surface includes engineering blog, documentation, and 17 more developer resources.'
plans:
- name: Vacuum Plans Pricing
  plan_count: 3
  slug: vacuum-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Vacuum Rate Limits
  slug: vacuum-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Vacuum — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: vacuum-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 7.9
    contract_governance: 23.5
    contract_quality: 10.7
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 22.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
