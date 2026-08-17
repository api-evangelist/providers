---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Farmos Agentic Access
  operation_count: 100
  slug: farmos-agentic-access
  summary_line: 100 operations · 57 acting
api_count: 6
apis:
- description: Physical or logical farm assets (land, animals, equipment, plants, etc.)
  name: farmOS Assets API
  slug: farmos-assets-api
- description: Farm activity records (activities, observations, inputs, harvests, etc.)
  name: farmOS Logs API
  slug: farmos-logs-api
- description: Farm planning records
  name: farmOS Plans API
  slug: farmos-plans-api
- description: Measurement quantities associated with logs
  name: farmOS Quantities API
  slug: farmos-quantities-api
- description: Server metadata and available resource types
  name: farmOS Server Info API
  slug: farmos-server-info-api
- description: Taxonomy term resources (categories, types, units)
  name: farmOS Taxonomy API
  slug: farmos-taxonomy-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'farmOS JSON: Assets API'
  slug: open-farmos-assets-api
- collection_type: open
  name: 'farmOS JSON: Assets Logs API'
  slug: open-farmos-logs-api
- collection_type: open
  name: 'farmOS JSON: Assets Plans API'
  slug: open-farmos-plans-api
- collection_type: open
  name: 'farmOS JSON: Assets Quantities API'
  slug: open-farmos-quantities-api
- collection_type: open
  name: 'farmOS JSON: Assets Server Info API'
  slug: open-farmos-server-info-api
- collection_type: open
  name: 'farmOS JSON: Assets Taxonomy API'
  slug: open-farmos-taxonomy-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/farmOS/farmOS/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/farmOS/farmOS/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/farmOS/farmOS/blob/4.x/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/farmOS/.github/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/farmOS/farmOS/blob/4.x/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/farmos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/farmos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/farmos-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/farmos-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://farmos.org/
- group: docs
  title: ''
  type: Documentation
  url: https://farmos.org/development/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/farmOS
- group: company
  title: ''
  type: Blog
  url: https://farmos.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://farmier.com/pricing/
- group: other
  title: ''
  type: X
  url: https://twitter.com/farmOSorg
- group: operate
  title: ''
  type: Forums
  url: https://farmos.discourse.group/
- group: other
  title: ''
  type: OpenCollective
  url: https://opencollective.com/farmos
- group: build
  title: ''
  type: JavaScriptSDK
  url: https://github.com/farmOS/farmOS.js
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/farmOS/farmOS.py
- group: commercial
  title: ''
  type: Plans
  url: plans/farmos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/farmos-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/farmos-finops.yml
created: '2026-06-13'
description: Open-source farm management and record-keeping system with a JSON:API-based REST API for managing assets, logs, plans, and farm records. Supports self-hosted deployments and managed hosting via Farmier. Authentication uses OAuth2 with Authorization Code, Password Credentials, and Client Credentials grant types.
examples:
- key_count: 4
  name: Farmos Create Animal Asset Example
  slug: farmos-create-animal-asset-example
- key_count: 4
  name: Farmos Create Harvest Log Example
  slug: farmos-create-harvest-log-example
- key_count: 4
  name: Farmos List Assets With Filter Example
  slug: farmos-list-assets-with-filter-example
finops:
- name: Farmos Finops
  service_category: ''
  slug: farmos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farmos.png
json_schemas:
- name: farmOS Asset
  property_count: 3
  slug: farmos-asset
- name: farmOS Log
  property_count: 3
  slug: farmos-log
- name: farmOS Quantity
  property_count: 1
  slug: farmos-quantity
jsonld:
- class_count: 41
  name: Farmos Context
  property_count: 30
  slug: farmos-context
layout: provider
modified: '2026-06-13'
name: farmOS
nav: Providers
network: true
overview: 'farmOS publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Logs API, Plans API, and 3 more. Tagged areas include Agriculture, Farm Management, Open Source, JSON:API, and Record Keeping.


  The farmOS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  farmOS''s developer surface includes authentication, documentation, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Farmos Plans Pricing
  plan_count: 4
  slug: farmos-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 0
  name: Farmos Rate Limits
  slug: farmos-rate-limits
rules:
- name: farmOS API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: farmos-jsonschema-spectral-rules
scopes:
- name: Farmos Scopes
  scope_count: 3
  slug: farmos-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.9
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/farmos/refs/heads/main/screenshots/farmos-2026-06-20T181044.png
security:
- kind: authentication
  name: Farmos Authentication
  slug: farmos-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Farmos Domain Security
  slug: farmos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: farmos
tags:
- Agriculture
- Farm Management
- Open Source
- JSON:API
- Record Keeping
- Self-Hosted
- Drupal
website: https://farmos.org/
---
