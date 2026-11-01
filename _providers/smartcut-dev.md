---
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Cutting optimisation for sheet, linear and roll
  name: SmartCut API
  slug: smartcut-api
- baseURL: https://api.smartcut.dev
  baseurl_source: declared
  description: Cutting optimisation for sheet, linear and roll stock.
  name: SmartCut API V3 Openapi API
  slug: smartcut-api-v3-openapi-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/smartcut-dev/rules/smartcut-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/smartcut-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/smartcut-dev/json-ld/smartcut-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/smartcut-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/smartcut-dev/vocabulary/smartcut-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/smartcut-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/smartcut-dev/conformance/smartcut-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/smartcut-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/smartcut-dev/data-model/smartcut-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/smartcut-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/smartcut-dev/errors/smartcut-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/smartcut-dev-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/smartcut-dev/llms/smartcut-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smartcut-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/smartcut-dev/well-known/smartcut-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smartcut-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/smartcut-dev/hosts/smartcut-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smartcut-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/smartcut-dev/vendors/smartcut-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/smartcut-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smartcut.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smartcut.dev/privacy-policy
- group: auth
  href: https://artifacts.apis.io/smartcut-dev/security/smartcut-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smartcut-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smartcut.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://smartcut.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://smartcut.dev/api-docs/v3
- group: commercial
  title: ''
  type: Pricing
  url: https://smartcut.dev/plans
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.smartcut.dev/mcp
  - status: 403
    url: https://smartcut.dev/mcp
  - status: 200
    url: https://smartcut.dev/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Smartcut.dev is a developer-focused platform that provides tools for creating, managing, and deploying software shortcuts and automation scripts. It offers a suite of APIs enabling integration with CI/CD pipelines, code repositories, and cloud services, allowing developers to streamline repetitive tasks, share reusable code snippets, and accelerate development workflows across teams.
image: https://smartcut.dev/images/sharing.png
json_schemas:
- name: CalculateRequest
  property_count: 8
  slug: smartcut-dev-calculate-request
- name: ModelAnalysisResponse
  property_count: 5
  slug: smartcut-dev-model-analysis-response
- name: ResultResponse
  property_count: 13
  slug: smartcut-dev-result-response
jsonld:
- class_count: 27
  name: Smartcut Dev Context
  property_count: 164
  slug: smartcut-dev-context
layout: provider
modified: '2026-10-31'
name: smartcut-dev
nav: Providers
network: true
overview: 'smartcut-dev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including SmartCut API V3 Openapi API, and 1 more. Tagged areas include Company, Developer Tools, Automation, CI/CD, and APIs.


  The smartcut-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  smartcut-dev''s developer surface includes documentation, API reference, pricing, and 14 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: smartcut-dev API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: smartcut-dev-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 50.7
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Smartcut Dev Domain Security
  slug: smartcut-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: smartcut-dev
tags:
- Company
- Developer Tools
- Automation
- CI/CD
- APIs
website: https://smartcut.dev/
---
