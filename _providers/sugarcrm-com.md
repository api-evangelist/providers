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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: REST API reference for SugarCRM version 26.2, covering modules, filters, and authentication.
  name: SugarCRM REST API
  slug: sugarcrm-rest-api
- description: 'SugarCRM API as documented publicly: 91 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: SugarCRM API
  slug: sugarcrm-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/sugarcrm-com/rules/sugarcrm-com-rules.yml
  title: ''
  type: Spectral
  url: rules/sugarcrm-com-rules.yml
- group: design
  href: https://artifacts.apis.io/sugarcrm-com/json-ld/sugarcrm-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sugarcrm-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/sugarcrm-com/vocabulary/sugarcrm-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sugarcrm-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sugarcrm-com/data-model/sugarcrm-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sugarcrm-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/sugarcrm-com/changelog/sugarcrm-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sugarcrm-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/sugarcrm-com/conformance/sugarcrm-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sugarcrm-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/sugarcrm-com/well-known/sugarcrm-com-sugarai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sugarcrm-com-sugarai-security.txt
- group: agent
  href: https://artifacts.apis.io/sugarcrm-com/well-known/sugarcrm-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sugarcrm-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/sugarcrm-com/hosts/sugarcrm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sugarcrm-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sugarcrm-com/vendors/sugarcrm-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sugarcrm-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/sugarcrm-com/packages/sugarcrm-com-packages.yml
  title: ''
  type: SDKs
  url: packages/sugarcrm-com-packages.yml
- group: build
  href: https://artifacts.apis.io/sugarcrm-com/packages/sugarcrm-com-packages.yml
  title: ''
  type: Packages
  url: packages/sugarcrm-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.sugarcrm.com/why-sugar/trust/
- group: other
  title: ''
  type: Leadership
  url: https://www.sugarcrm.com/about/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.sugarai.com/documentation/discover/sugar_discover_user_guide/getting_started/
- group: auth
  href: https://artifacts.apis.io/sugarcrm-com/security/sugarcrm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sugarcrm-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sugarcrm.com/
- group: company
  title: ''
  type: Blog
  url: https://sugarai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://sugarai.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sugarai.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sugarai.com/legal/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://support.sugarai.com/documentation/sugar_developer/sugar_developer_guide_26.2/
- group: operate
  title: ''
  type: Support
  url: https://support.sugarai.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sugarcrm
coverage:
  checked: '2026-10-29'
  detail: Public documentation is available but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 404
    url: https://www.sugarcrm.com/api-docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: SugarCRM provides a B2B sales CRM platform that combines AI‑driven precision selling with a suite of solutions such as Sugar Sell, Sugar Serve, Sugar Market and Sugar Predict. The company’s website highlights its leadership in sales force automation for 2026, integration with ERP systems, and a marketplace of apps. It offers documentation, pricing, privacy and terms pages hosted on the SugarAI domain, and a public GitHub organization for open‑source components.
image: https://www.sugarcrm.com/wp-content/uploads/2021/05/sugarcrm-blk-logo.png
json_schemas:
- name: GetForecastmanagerworksheetsTimeperiodidUseridResponse
  property_count: 1
  slug: sugarcrm-com-get-forecastmanagerworksheets-timeperiodid-userid-response
- name: GetForecastsTimeperiodidUseridChartDisplaymanagerResponse
  property_count: 1
  slug: sugarcrm-com-get-forecasts-timeperiodid-userid-chart-displaymanager-response
- name: GetForecastworksheetsRecordResponse
  property_count: 1
  slug: sugarcrm-com-get-forecastworksheets-record-response
- name: GetLeadsIdFreebusyResponse
  property_count: 3
  slug: sugarcrm-com-get-leads-id-freebusy-response
- name: PostRestV10ModuleRecordListRequest
  property_count: 1
  slug: sugarcrm-com-post-rest-v10-module-record-list-request
- name: PostRestV10ModuleRecordListResponse
  property_count: 5
  slug: sugarcrm-com-post-rest-v10-module-record-list-response
jsonld:
- class_count: 9
  name: Sugarcrm Com Context
  property_count: 7
  slug: sugarcrm-com-context
layout: provider
modified: '2026-10-29'
name: SugarCRM
nav: Providers
network: true
overview: 'SugarCRM is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including REST API, and 1 more. Tagged areas include CRM, Sales, B2B, SaaS, and AI.


  The SugarCRM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SugarCRM''s developer surface includes changelog, getting-started guide, engineering blog, pricing, documentation, support, and 18 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: SugarCRM API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: sugarcrm-com-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 35.6
    contract_quality: 20.9
    developer_ergonomics: 35.7
    discoverability: 58.9
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 27
      marker_coverage: 100.0
      total: 27
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sugarcrm Com Domain Security
  slug: sugarcrm-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sugarcrm-com
tags:
- CRM
- Sales
- B2B
- SaaS
- AI
- Integration
website: https://www.sugarcrm.com/
---
