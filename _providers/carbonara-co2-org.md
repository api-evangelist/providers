---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Carbonara Co2 Org Agentic Access
  operation_count: 8
  slug: carbonara-co2-org-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- baseURL: https://sootcase.org
  baseurl_source: declared
  description: The Calculate API from Carbonara CO2 — 2 operation(s) for calculate.
  name: Carbonara CO2 Calculate API
  slug: carbonara-co2-org-calculate-api
- baseURL: https://sootcase.org
  baseurl_source: declared
  description: The Factors API from Carbonara CO2 — 1 operation(s) for factors.
  name: Carbonara CO2 Factors API
  slug: carbonara-co2-org-factors-api
- baseURL: https://sootcase.org
  baseurl_source: declared
  description: The Healthz API from Carbonara CO2 — 1 operation(s) for healthz.
  name: Carbonara CO2 Healthz API
  slug: carbonara-co2-org-healthz-api
- baseURL: https://sootcase.org
  baseurl_source: declared
  description: The Places API from Carbonara CO2 — 1 operation(s) for places.
  name: Carbonara CO2 Places API
  slug: carbonara-co2-org-places-api
- baseURL: https://sootcase.org
  baseurl_source: declared
  description: The Recommend API from Carbonara CO2 — 1 operation(s) for recommend.
  name: Carbonara CO2 Recommend API
  slug: carbonara-co2-org-recommend-api
- baseURL: https://sootcase.org
  baseurl_source: declared
  description: The Report API from Carbonara CO2 — 1 operation(s) for report.
  name: Carbonara CO2 Report API
  slug: carbonara-co2-org-report-api
- baseURL: https://sootcase.org
  baseurl_source: declared
  description: The Scenario API from Carbonara CO2 — 1 operation(s) for scenario.
  name: Carbonara CO2 Scenario API
  slug: carbonara-co2-org-scenario-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/carbonara-co2-org/agentic-access/carbonara-co2-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carbonara-co2-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/carbonara-co2-org/rules/carbonara-co2-org-rules.yml
  title: ''
  type: Spectral
  url: rules/carbonara-co2-org-rules.yml
- group: design
  href: https://artifacts.apis.io/carbonara-co2-org/json-ld/carbonara-co2-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carbonara-co2-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/carbonara-co2-org/vocabulary/carbonara-co2-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carbonara-co2-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/carbonara-co2-org/data-model/carbonara-co2-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carbonara-co2-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/carbonara-co2-org/errors/carbonara-co2-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carbonara-co2-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carbonara-co2-org/conformance/carbonara-co2-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carbonara-co2-org-conformance.yml
- group: other
  href: https://artifacts.apis.io/carbonara-co2-org/hosts/carbonara-co2-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbonara-co2-org-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sootcase.org/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://sootcase.org/guides
- group: auth
  href: https://artifacts.apis.io/carbonara-co2-org/security/carbonara-co2-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbonara-co2-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbonara-co2.org/
created: '2026-11-03'
description: Carbonara CO2 provides an open-source platform for developers to assess and reduce the carbon emissions of their software. By integrating with code editors and CI pipelines, it measures energy consumption, estimates CO2 output, and offers actionable recommendations. The project is backed by Climate+Tech Think‑Tank and aims to promote sustainable software development practices across the industry.
image: https://sootcase.org/og.png
json_schemas:
- name: Dataset
  property_count: 18
  slug: carbonara-co2-org-dataset
- name: RecommendResult
  property_count: 14
  slug: carbonara-co2-org-recommend-result
- name: RecommendSettings
  property_count: 16
  slug: carbonara-co2-org-recommend-settings
- name: Report
  property_count: 17
  slug: carbonara-co2-org-report
- name: Result
  property_count: 16
  slug: carbonara-co2-org-result
- name: Shipment
  property_count: 9
  slug: carbonara-co2-org-shipment
jsonld:
- class_count: 25
  name: Carbonara Co2 Org Context
  property_count: 143
  slug: carbonara-co2-org-context
layout: provider
modified: '2026-11-03'
name: Carbonara CO2
nav: Providers
network: true
overview: 'Carbonara CO2 publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calculate API, Factors API, Healthz API, and 4 more. Tagged areas include Company, Sustainability, Open Source, Climate Tech, and Software.


  The Carbonara CO2 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Carbonara CO2''s developer surface includes documentation and 11 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Carbonara CO2 API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: carbonara-co2-org-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 55.0
    developer_ergonomics: 4.8
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbonara Co2 Org Domain Security
  slug: carbonara-co2-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: carbonara-co2-org
tags:
- Company
- Sustainability
- Open Source
- Climate Tech
- Software
website: https://carbonara-co2.org/
---
