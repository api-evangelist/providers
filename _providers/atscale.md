---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-03'
api_count: 11
apis:
- description: API documentation is available but no machine‑readable contract was found.
  name: AtScale API
  slug: atscale-api-2
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Aggregates API from Atscale — 5 operation(s) for aggregates.
  name: Atscale Aggregates API
  slug: atscale-aggregates-api
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Atscale API API from Atscale — 2 operation(s) for atscale api.
  name: Atscale Atscale API
  slug: atscale-atscale-api-api
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Catalogs API from Atscale — 3 operation(s) for catalogs.
  name: Atscale Catalogs API
  slug: atscale-catalogs-api
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Data Warehouses API from Atscale — 1 operation(s) for data warehouses.
  name: Atscale Data Warehouses API
  slug: atscale-data-warehouses-api
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Default API from Atscale — 1 operation(s) for default.
  name: Atscale Default API
  slug: atscale-default-api
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Org API from Atscale — 7 operation(s) for org.
  name: Atscale Org API
  slug: atscale-org-api
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Orgs API from Atscale — 1 operation(s) for orgs.
  name: Atscale Orgs API
  slug: atscale-orgs-api
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Query API from Atscale — 1 operation(s) for query.
  name: Atscale Query API
  slug: atscale-query-api
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Sessiontoken API from Atscale — 1 operation(s) for sessiontoken.
  name: Atscale Sessiontoken API
  slug: atscale-sessiontoken-api
- baseURL: http://atscale-node-01.docker.infra.atscale.com:10500
  baseurl_source: declared
  description: The Soap API from Atscale — 1 operation(s) for soap.
  name: Atscale Soap API
  slug: atscale-soap-api
artifact_total: 20
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/rules/atscale-rules.yml
  title: ''
  type: Spectral
  url: rules/atscale-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/json-ld/atscale-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atscale-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/vocabulary/atscale-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atscale-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/data-model/atscale-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atscale-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/changelog/atscale-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/atscale-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/conformance/atscale-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atscale-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/llms/atscale-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atscale-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/hosts/atscale-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atscale-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/vendors/atscale-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atscale-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/packages/atscale-packages.yml
  title: ''
  type: SDKs
  url: packages/atscale-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/packages/atscale-packages.yml
  title: ''
  type: Packages
  url: packages/atscale-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.atscale.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atscale.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atscale.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.atscale.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.atscale.com/about/team/
- group: operate
  title: ''
  type: ChangeLog
  url: https://documentation.atscale.com/container/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.atscale.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.atscale.com/kb/what-access-is-needed-in-sentry-for-impala-if-udf-schema-override-is-setup-in-atscale
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.atscale.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atscale/refs/heads/main/security/atscale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atscale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atscale.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://help.atscale.com/mcp
  - status: 403
    url: https://equityzen.com/company/atscale
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: AtScale provides a semantic layer platform that enables enterprises to unify data across data warehouses, data lakes, and cloud services, delivering AI‑powered analytics, business intelligence, and data governance. Their solution supports integrations with Snowflake, Databricks, Google BigQuery, Amazon Redshift, Microsoft Azure, and many other platforms, helping organizations to build a trusted analytics foundation for AI and BI workloads.
image: https://www.atscale.com/wp-content/uploads/2021/12/AtScale_Logo_RGB_2C.png
json_schemas:
- name: GetV1AggregatesExportCatalogsCatalogidModelsModelidResponse
  property_count: 6
  slug: atscale-get-v1-aggregates-export-catalogs-catalogid-models-modelid-response
- name: GetV1DataWarehousesDatawarehouseidIdResponse
  property_count: 10
  slug: atscale-get-v1-data-warehouses-datawarehouseid-id-response
- name: PostOrgOrgidResponse
  property_count: 4
  slug: atscale-post-org-orgid-response
- name: PostV1AggregatesImportCatalogsCatalogidModelsModelidResponse
  property_count: 7
  slug: atscale-post-v1-aggregates-import-catalogs-catalogid-models-modelid-response
- name: PostV1V1IdRequest
  property_count: 15
  slug: atscale-post-v1-v1-id-request
- name: PostV1V1IdResponse
  property_count: 9
  slug: atscale-post-v1-v1-id-response
jsonld:
- class_count: 27
  name: Atscale Context
  property_count: 73
  slug: atscale-context
layout: provider
modified: '2026-09-26'
name: Atscale
nav: Providers
network: true
overview: 'Atscale publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Aggregates API, Atscale API, Catalogs API, and 8 more. Tagged areas include Analytics, Business Intelligence, Data Integration, Artificial Intelligence, and Semantic Layer.


  The Atscale catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Atscale''s developer surface includes changelog, support, pricing, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 7
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Atscale API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 3
  slug: atscale-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 26.8
    developer_ergonomics: 35.7
    discoverability: 73.2
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Atscale Domain Security
  slug: atscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atscale
tags:
- Analytics
- Business Intelligence
- Data Integration
- Artificial Intelligence
- Semantic Layer
website: https://www.atscale.com
---
