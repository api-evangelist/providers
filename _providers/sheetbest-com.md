---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.sheetbest.com
  baseurl_source: declared
  description: 'sheetbest-com API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: sheetbest-com API
  slug: sheetbest-com-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/sheetbest-com/plans/sheetbest-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sheetbest-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sheetbest-com/rules/sheetbest-com-rules.yml
  title: ''
  type: Spectral
  url: rules/sheetbest-com-rules.yml
- group: design
  href: https://artifacts.apis.io/sheetbest-com/json-ld/sheetbest-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sheetbest-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/sheetbest-com/vocabulary/sheetbest-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sheetbest-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sheetbest-com/data-model/sheetbest-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sheetbest-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/sheetbest-com/conventions/sheetbest-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sheetbest-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sheetbest-com/authentication/sheetbest-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sheetbest-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/sheetbest-com/conformance/sheetbest-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sheetbest-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sheetbest-com/llms/sheetbest-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sheetbest-com-llms.txt
- group: other
  href: https://artifacts.apis.io/sheetbest-com/hosts/sheetbest-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sheetbest-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sheetbest-com/vendors/sheetbest-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sheetbest-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://sheetbest.com/login/?from=home&lang=en
- group: auth
  href: https://artifacts.apis.io/sheetbest-com/security/sheetbest-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sheetbest-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sheetbest.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sheetbest.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sheetbest.com/docs/getting-started/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://sheetbest.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://sheetbest.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sheetbest.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sheetbest.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sheetbest/
coverage:
  checked: '2026-10-31'
  detail: Documentation is public but no OpenAPI or other machine-readable contract was found despite probing known locations.
  evidence:
  - status: 404
    url: https://api.sheetbest.com/openapi.json
  - status: 404
    url: https://api.sheetbest.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Sheetbest.com provides a powerful API that enables developers to integrate spreadsheet data into their applications seamlessly. The platform offers endpoints for reading, writing, and managing spreadsheet rows, columns, and cells, supporting both JSON and CSV formats. It is designed for automation, data synchronization, and building data-driven services without manual spreadsheet handling. With robust documentation, authentication via API keys, and rate limiting, Sheetbest empowers businesses to streamline data workflows and enhance productivity across various use cases.
image: https://sheetbest.com/social/opengraph-image.png
json_schemas:
- name: GetDrivesConnectionidResponse
  property_count: 3
  slug: sheetbest-com-get-drives-connectionid-response
- name: PutSheetsApiidRequest
  property_count: 1
  slug: sheetbest-com-put-sheets-apiid-request
jsonld:
- class_count: 2
  name: Sheetbest Com Context
  property_count: 4
  slug: sheetbest-com-context
layout: provider
modified: '2026-10-31'
name: sheetbest-com
nav: Providers
network: true
overview: 'sheetbest-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spreadsheets, Data Integration, and Automation.


  The sheetbest-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sheetbest-com''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Sheetbest Com Plans Pricing
  plan_count: 5
  slug: sheetbest-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: sheetbest-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: sheetbest-com-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 21.8
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 39.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sheetbest-com/sheetbest-com-2026-11-03T143114.png
security:
- kind: authentication
  name: Sheetbest Com Authentication
  slug: sheetbest-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sheetbest Com Domain Security
  slug: sheetbest-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sheetbest-com
tags:
- Company
- Spreadsheets
- Data Integration
- Automation
website: https://sheetbest.com/
---
