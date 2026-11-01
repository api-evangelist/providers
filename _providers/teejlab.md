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
api_count: 1
apis:
- description: 'TeejLab API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: TeejLab API
  slug: teejlab-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/teejlab/plans/teejlab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/teejlab-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/teejlab/rules/teejlab-rules.yml
  title: ''
  type: Spectral
  url: rules/teejlab-rules.yml
- group: design
  href: https://artifacts.apis.io/teejlab/json-ld/teejlab-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/teejlab-context.jsonld
- group: design
  href: https://artifacts.apis.io/teejlab/vocabulary/teejlab-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/teejlab-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/teejlab/data-model/teejlab-data-model.yml
  title: ''
  type: DataModel
  url: data-model/teejlab-data-model.yml
- group: design
  href: https://artifacts.apis.io/teejlab/conformance/teejlab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/teejlab-conformance.yml
- group: agent
  href: https://artifacts.apis.io/teejlab/llms/teejlab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/teejlab-llms.txt
- group: other
  href: https://artifacts.apis.io/teejlab/hosts/teejlab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teejlab-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://teejlab.com/terms
- group: auth
  title: ''
  type: Security
  url: https://teejlab.com/tag/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://teejlab.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://teejlab.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://apidiscovery.teejlab.com/accounts/login/
- group: company
  title: ''
  type: Blog
  url: https://teejlab.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://apidiscovery.teejlab.com/edsn/apidocs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teejlab
- group: auth
  href: https://artifacts.apis.io/teejlab/security/teejlab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teejlab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teejlab.com/
created: '2026-10-21'
description: TeejLab provides an API management platform that includes discovery of hidden APIs, automated security testing, a marketplace for consolidating external APIs, access‑control and monetization for public and private APIs, and end‑to‑end lifecycle governance. The platform is aimed at enterprises, entrepreneurs and large companies that develop, consume or monetize APIs.
image: https://16.52.171.21/wp-content/uploads/2020/11/Component-2.png
json_schemas:
- name: GetEdsnApiEndpointParameterResponse
  property_count: 4
  slug: teejlab-get-edsn-api-endpoint-parameter-response
- name: GetEdsnApiEndpointSearchResponse
  property_count: 5
  slug: teejlab-get-edsn-api-endpoint-search-response
- name: GetEdsnApiNetworksUserScansResponse
  property_count: 1
  slug: teejlab-get-edsn-api-networks-user-scans-response
- name: GetEdsnApiScannedProjectsResponse
  property_count: 5
  slug: teejlab-get-edsn-api-scanned-projects-response
- name: PostEdsnApiCvesearchRequest2
  property_count: 4
  slug: teejlab-post-edsn-api-cvesearch-request2
- name: PostEdsnApiCvesearchResponse
  property_count: 3
  slug: teejlab-post-edsn-api-cvesearch-response
jsonld:
- class_count: 29
  name: Teejlab Context
  property_count: 38
  slug: teejlab-context
layout: provider
modified: '2026-10-21'
name: TeejLab
nav: Providers
network: true
overview: 'TeejLab is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Discovery, API Security, API Governance, API Marketplace, and API Monetization.


  The TeejLab catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TeejLab''s developer surface includes pricing, engineering blog, API reference, and 15 more developer resources.'
plans:
- name: Teejlab Plans Pricing
  plan_count: 4
  slug: teejlab-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: TeejLab API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: teejlab-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
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
  name: Teejlab Domain Security
  slug: teejlab-domain-security
  summary_line: TLSv1.2 · DMARC
slug: teejlab
tags:
- API Discovery
- API Security
- API Governance
- API Marketplace
- API Monetization
- DevSecOps
- Compliance
website: https://teejlab.com/
---
