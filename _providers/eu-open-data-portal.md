---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 72
  human_in_the_loop: 0
  name: Eu Open Data Portal Agentic Access
  operation_count: 172
  slug: eu-open-data-portal-agentic-access
  summary_line: 172 operations · 72 acting
api_count: 12
apis:
- baseURL: https://data.europa.eu/api/hub/statistics
  baseurl_source: declared
  description: The hub statistics service exposes portal-wide counts over time — datasets per category, per catalogue, per country, per format and per licence — behind a Swagger 2.0 contract served from a Flask/flas
  name: EU Open Data Portal Statistics API
  slug: eu-open-data-portal-statistics-api
- description: The OpenLink Virtuoso SPARQL endpoint for data.europa.eu. Every harvested dataset is stored in its own named graph alongside DCAT-AP controlled vocabularies, NUTS codes and MQA quality measurements, a
  name: EU Open Data Portal SPARQL API
  slug: eu-open-data-portal-sparql-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: 'The action API utilizes the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification with the following constraints: * `id` reference needs to be a string * `params` are passed as object ma'
  name: EU Open Data Portal Action API
  slug: eu-open-data-portal-action-api-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: 'The action API utilizes the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification with the following constraints: * `id` reference needs to be a string * `params` are passed as object ma'
  name: EU Open Data Portal Actions API
  slug: eu-open-data-portal-actions-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Administration API from EU Open Data Portal — 5 operation(s) for administration.
  name: EU Open Data Portal Administration API
  slug: eu-open-data-portal-administration-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Catalogues API from EU Open Data Portal — 7 operation(s) for catalogues.
  name: EU Open Data Portal Catalogues API
  slug: eu-open-data-portal-catalogues-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Ckan API from EU Open Data Portal — 3 operation(s) for ckan.
  name: EU Open Data Portal Ckan API
  slug: eu-open-data-portal-ckan-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Countries API from EU Open Data Portal — 4 operation(s) for countries.
  name: EU Open Data Portal Countries API
  slug: eu-open-data-portal-countries-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: '**Deprecated !** Will be replaced with the generic DCAT resource API (endpoints will be reused). Any future custom resource definitions must be sub-classed from DCAT Resource.'
  name: EU Open Data Portal Custom Resources API
  slug: eu-open-data-portal-custom-resources-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Data API from EU Open Data Portal — 3 operation(s) for data.
  name: EU Open Data Portal Data API
  slug: eu-open-data-portal-data-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Data Services API from EU Open Data Portal — 1 operation(s) for data services.
  name: EU Open Data Portal Data Services API
  slug: eu-open-data-portal-data-services-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Dataset Series API from EU Open Data Portal — 1 operation(s) for dataset series.
  name: EU Open Data Portal Dataset Series API
  slug: eu-open-data-portal-dataset-series-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: '**Deprecated !** Please use general DCAT Resources API instead'
  name: EU Open Data Portal Datasets API
  slug: eu-open-data-portal-datasets-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: Manage DCAT resources and its sub-classes, except DCAT Catalogues.
  name: EU Open Data Portal DCAT Resources API
  slug: eu-open-data-portal-dcat-resources-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: '**Deprecated !** Will be removed completely in the future'
  name: EU Open Data Portal Distributions API
  slug: eu-open-data-portal-distributions-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Drafts API from EU Open Data Portal — 4 operation(s) for drafts.
  name: EU Open Data Portal Drafts API
  slug: eu-open-data-portal-drafts-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The EditorialContent API from EU Open Data Portal — 3 operation(s) for editorialcontent.
  name: EU Open Data Portal Editorial Content API
  slug: eu-open-data-portal-editorialcontent-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Feeds API from EU Open Data Portal — 3 operation(s) for feeds.
  name: EU Open Data Portal Feeds API
  slug: eu-open-data-portal-feeds-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Gazetteer API from EU Open Data Portal — 1 operation(s) for gazetteer.
  name: EU Open Data Portal Gazetteer API
  slug: eu-open-data-portal-gazetteer-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Generate API from EU Open Data Portal — 1 operation(s) for generate.
  name: EU Open Data Portal Generate API
  slug: eu-open-data-portal-generate-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Global API from EU Open Data Portal — 2 operation(s) for global.
  name: EU Open Data Portal Global API
  slug: eu-open-data-portal-global-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Maintenance API from EU Open Data Portal — 1 operation(s) for maintenance.
  name: EU Open Data Portal Maintenance API
  slug: eu-open-data-portal-maintenance-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Organizations API from EU Open Data Portal — 3 operation(s) for organizations.
  name: EU Open Data Portal Organizations API
  slug: eu-open-data-portal-organizations-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: Create persistent identifiers for data artifacts.
  name: EU Open Data Portal Persistent Identifiers API
  slug: eu-open-data-portal-persistent-identifiers-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Report API from EU Open Data Portal — 2 operation(s) for report.
  name: EU Open Data Portal Report API
  slug: eu-open-data-portal-report-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Reports API from EU Open Data Portal — 1 operation(s) for reports.
  name: EU Open Data Portal Reports API
  slug: eu-open-data-portal-reports-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Resources API from EU Open Data Portal — 1 operation(s) for resources.
  name: EU Open Data Portal Resources API
  slug: eu-open-data-portal-resources-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Search API from EU Open Data Portal — 2 operation(s) for search.
  name: EU Open Data Portal Search API
  slug: eu-open-data-portal-search-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Sitemap API from EU Open Data Portal — 2 operation(s) for sitemap.
  name: EU Open Data Portal Sitemap API
  slug: eu-open-data-portal-sitemap-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Test API from EU Open Data Portal — 1 operation(s) for test.
  name: EU Open Data Portal Test API
  slug: eu-open-data-portal-test-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Translation API from EU Open Data Portal — 1 operation(s) for translation.
  name: EU Open Data Portal Translation API
  slug: eu-open-data-portal-translation-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Validation API from EU Open Data Portal — 1 operation(s) for validation.
  name: EU Open Data Portal Validation API
  slug: eu-open-data-portal-validation-api
- baseURL: https://data.europa.eu/api/hub/search
  baseurl_source: declared
  description: The Vocabularies API from EU Open Data Portal — 5 operation(s) for vocabularies.
  name: EU Open Data Portal Vocabularies API
  slug: eu-open-data-portal-vocabularies-api
artifact_total: 46
common:
- group: other
  href: https://artifacts.apis.io/eu-open-data-portal/capabilities/eu-open-data-portal-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/eu-open-data-portal-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/eu-open-data-portal/overlays/eu-open-data-portal-hub-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/eu-open-data-portal-hub-search-overlay.yaml
- group: other
  href: https://artifacts.apis.io/eu-open-data-portal/overlays/eu-open-data-portal-hub-repo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/eu-open-data-portal-hub-repo-overlay.yaml
- group: other
  href: https://artifacts.apis.io/eu-open-data-portal/overlays/eu-open-data-portal-mqa-metrics-cache-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/eu-open-data-portal-mqa-metrics-cache-overlay.yaml
- group: other
  href: https://artifacts.apis.io/eu-open-data-portal/overlays/eu-open-data-portal-mqa-shacl-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/eu-open-data-portal-mqa-shacl-overlay.yaml
- group: other
  href: https://artifacts.apis.io/eu-open-data-portal/overlays/eu-open-data-portal-mqa-reporter-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/eu-open-data-portal-mqa-reporter-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://data.europa.eu/
- group: start
  title: ''
  type: Portal
  url: https://data.europa.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dataeuropa.gitlab.io/data-provider-manual/api-documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://dataeuropa.gitlab.io/data-provider-manual/
- group: docs
  title: ''
  type: APIReference
  url: https://data.europa.eu/api/hub/search/
- group: start
  title: ''
  type: GettingStarted
  url: https://dataeuropa.gitlab.io/data-provider-manual/api-documentation/
- group: operate
  title: ''
  type: Support
  url: https://data.europa.eu/en/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://data.europa.eu/en/faq
- group: company
  title: ''
  type: Blog
  url: https://data.europa.eu/en/news-events/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.europa.eu/en/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://data.europa.eu/en/legal-notice
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/dataeuropa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/publications-office-of-the-european-union
- group: agent
  href: https://artifacts.apis.io/eu-open-data-portal/agentic-access/eu-open-data-portal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eu-open-data-portal-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/eu-open-data-portal/authentication/eu-open-data-portal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eu-open-data-portal-authentication.yml
- group: design
  href: https://artifacts.apis.io/eu-open-data-portal/conventions/eu-open-data-portal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/eu-open-data-portal-conventions.yml
- group: design
  href: https://artifacts.apis.io/eu-open-data-portal/errors/eu-open-data-portal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eu-open-data-portal-problem-types.yml
- group: design
  href: https://artifacts.apis.io/eu-open-data-portal/lifecycle/eu-open-data-portal-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/eu-open-data-portal-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/eu-open-data-portal/changelog/eu-open-data-portal-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/eu-open-data-portal-changelog.yml
- group: design
  href: https://artifacts.apis.io/eu-open-data-portal/conformance/eu-open-data-portal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eu-open-data-portal-conformance.yml
- group: design
  href: https://artifacts.apis.io/eu-open-data-portal/data-model/eu-open-data-portal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eu-open-data-portal-data-model.yml
- group: build
  href: https://artifacts.apis.io/eu-open-data-portal/packages/eu-open-data-portal-packages.yml
  title: ''
  type: Packages
  url: packages/eu-open-data-portal-packages.yml
- group: design
  href: https://artifacts.apis.io/eu-open-data-portal/vocabulary/eu-open-data-portal-vocabularies.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eu-open-data-portal-vocabularies.yml
- group: agent
  href: https://artifacts.apis.io/eu-open-data-portal/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/eu-open-data-portal/llms/eu-open-data-portal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eu-open-data-portal-llms.txt
- group: commercial
  href: https://artifacts.apis.io/eu-open-data-portal/plans/eu-open-data-portal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eu-open-data-portal-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/eu-open-data-portal/rate-limits/eu-open-data-portal-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eu-open-data-portal-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/eu-open-data-portal/security/eu-open-data-portal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eu-open-data-portal-domain-security.yml
- group: docs
  href: https://artifacts.apis.io/eu-open-data-portal/json-schema/eu-open-data-portal-dataset-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/eu-open-data-portal-dataset-schema.json
- group: design
  href: https://artifacts.apis.io/eu-open-data-portal/json-ld/eu-open-data-portal-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/eu-open-data-portal-context.jsonld
- group: commercial
  href: https://artifacts.apis.io/eu-open-data-portal/finops/eu-open-data-portal-finops.yml
  title: ''
  type: FinOps
  url: finops/eu-open-data-portal-finops.yml
- group: design
  href: https://artifacts.apis.io/eu-open-data-portal/rules/eu-open-data-portal-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/eu-open-data-portal-jsonschema-spectral-rules.yml
created: '2026-04-28'
description: 'data.europa.eu is the official portal for European open data, operated by the Publications Office of the European Union. It federates roughly 1.9 million dataset records from EU institutions, the national open data portals of the member states and international organisations, and republishes them as DCAT-AP metadata. Six machine-readable APIs sit on top of that corpus: a hub-search metadata search service, a hub-repo DCAT-AP registry for publishers, a Virtuoso SPARQL endpoint, and the Metadata Quality Assurance metrics cache, metrics reporter and SHACL validation services. Read access is public and unauthenticated; publishing into a catalogue requires an EU Login account or a service account issued by the portal team.'
finops:
- has_sources: true
  method: derived
  name: Eu Open Data Portal Finops
  primary_unit: ''
  service_category: ''
  slug: eu-open-data-portal-finops
  template: true
image: https://raw.githubusercontent.com/api-evangelist/eu-open-data-portal/main/screenshots/eu-open-data-portal-2026-06-20T180843.png
json_schemas:
- name: EU Open Data Portal Dataset (DCAT-AP)
  property_count: 17
  slug: eu-open-data-portal-dataset
jsonld:
- class_count: 6
  name: Eu Open Data Portal Context
  property_count: 27
  slug: eu-open-data-portal-context
layout: provider
modified: '2026-09-07'
name: EU Open Data Portal
nav: Providers
network: true
overview: 'EU Open Data Portal publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including Statistics API, Action API, Actions API, and 30 more. Tagged areas include Government, Open Data, SPARQL, EU, and Regulatory.


  The EU Open Data Portal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EU Open Data Portal''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, authentication, and 31 more developer resources.'
plans:
- name: Eu Open Data Portal Plans Pricing
  plan_count: 0
  slug: eu-open-data-portal-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Eu Open Data Portal Rate Limits
  slug: eu-open-data-portal-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: EU Open Data Portal — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: eu-open-data-portal-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 59.3
    catalog_earned_first_party: 5.0
    catalog_gap: 55.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 21.1
    contract_governance: 43.2
    contract_quality: 58.8
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 38.7
      total: 31
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/eu-open-data-portal/eu-open-data-portal-2026-06-20T180843.png
security:
- kind: authentication
  name: Eu Open Data Portal Authentication
  slug: eu-open-data-portal-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Eu Open Data Portal Domain Security
  slug: eu-open-data-portal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 4
skills:
- name: eu-open-data-portal-assess-metadata-quality
  slug: eu-open-data-portal-assess-metadata-quality
- name: eu-open-data-portal-publish-dataset
  slug: eu-open-data-portal-publish-dataset
- name: eu-open-data-portal-search-datasets
  slug: eu-open-data-portal-search-datasets
- name: eu-open-data-portal-validate-dcat-ap
  slug: eu-open-data-portal-validate-dcat-ap
slug: eu-open-data-portal
tags:
- Government
- Open Data
- SPARQL
- EU
- Regulatory
- Linked Data
- DCAT-AP
- Data Quality
- Metadata
- Catalog
website: https://data.europa.eu/
---
