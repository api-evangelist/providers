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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-17'
api_count: 7
apis:
- description: Data platform API for sustainable finance, providing ESG, SDG, stewardship and compliance data.
  name: Datia API
  slug: datia-api-2
- baseURL: https://eco.datia.app
  baseurl_source: declared
  description: The Instruments API from Datia — 1 operation(s) for instruments.
  name: Datia Instruments API
  slug: datia-instruments-api
- baseURL: https://eco.datia.app
  baseurl_source: declared
  description: The Portfolios API from Datia — 2 operation(s) for portfolios.
  name: Datia Portfolios API
  slug: datia-portfolios-api
- baseURL: https://eco.datia.app
  baseurl_source: declared
  description: The Reports API from Datia — 1 operation(s) for reports.
  name: Datia Reports API
  slug: datia-reports-api
- baseURL: https://eco.datia.app
  baseurl_source: declared
  description: The Sustainable Investments API from Datia — 2 operation(s) for sustainable investments.
  name: Datia Sustainable Investments API
  slug: datia-sustainable-investments-api
- baseURL: https://eco.datia.app
  baseurl_source: declared
  description: The Taxonomy API from Datia — 1 operation(s) for taxonomy.
  name: Datia Taxonomy API
  slug: datia-taxonomy-api
- baseURL: https://eco.datia.app
  baseurl_source: declared
  description: The Temperature Score API from Datia — 1 operation(s) for temperature score.
  name: Datia Temperature Score API
  slug: datia-temperature-score-api
artifact_total: 18
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/plans/datia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datia-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/rules/datia-rules.yml
  title: ''
  type: Spectral
  url: rules/datia-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/json-ld/datia-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datia-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/vocabulary/datia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datia-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/data-model/datia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datia-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/authentication/datia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datia-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/conformance/datia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datia-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/llms/datia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datia-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/hosts/datia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/vendors/datia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datia-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.datia.app/team
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datia.app/docs/quickstart/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datia.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.datia.app/llms-full.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datia/refs/heads/main/security/datia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datia.app/
- group: company
  title: ''
  type: Blog
  url: https://www.datia.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datia.app/pricing
coverage:
  checked: '2026-10-15'
  detail: Docs site is a JavaScript-rendered Next.js app with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.datia.app
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Datia provides a data platform for sustainable finance, offering solutions for ESG, SDGs, stewardship, temperature scoring, and compliance with EU regulations such as SFDR and MiFID II. Their platform enables asset managers, asset owners, wealth advisors, and tech platforms to source data, perform portfolio calculations, and generate ready‑to‑share reports, streamlining sustainable investment processes. Datia is now part of Connect Earth, building a Sustainable Finance OS to help the industry meet ESG goals and regulatory requirements.
json_schemas:
- name: GetPortfoliosResponse
  property_count: 2
  slug: datia-get-portfolios-response
- name: PostInstrumentsInstrumentidResponse
  property_count: 5
  slug: datia-post-instruments-instrumentid-response
- name: PostReportsRequest
  property_count: 6
  slug: datia-post-reports-request
- name: PostSustainableInvestmentsInsightsResponse
  property_count: 1
  slug: datia-post-sustainable-investments-insights-response
- name: PostTaxonomyInsightsResponse
  property_count: 1
  slug: datia-post-taxonomy-insights-response
- name: PostTemperatureScoreInsightsResponse
  property_count: 2
  slug: datia-post-temperature-score-insights-response
jsonld:
- class_count: 15
  name: Datia Context
  property_count: 20
  slug: datia-context
layout: provider
modified: '2026-10-15'
name: Datia
nav: Providers
network: true
overview: 'Datia is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Instruments API, Portfolios API, Reports API, and 4 more. Tagged areas include Sustainable Finance, ESG, Data Platform, and Finance.


  The Datia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Datia''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Datia Plans Pricing
  plan_count: 4
  slug: datia-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Datia API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: datia-rules
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 28.2
    developer_ergonomics: 42.9
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Datia Authentication
  slug: datia-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Datia Domain Security
  slug: datia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datia
tags:
- Sustainable Finance
- ESG
- Data Platform
- Finance
website: https://www.datia.app/
---
