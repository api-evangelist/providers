---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: SERP and Google Maps API offering search results, rankings, place details, and AI overviews.
  name: semscraper API
  slug: semscraper-api
- baseURL: https://api.semscraper.com
  baseurl_source: declared
  description: 'semscraper-com API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: semscraper-com API
  slug: semscraper-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/semscraper-com/plans/semscraper-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/semscraper-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/semscraper-com/rules/semscraper-com-rules.yml
  title: ''
  type: Spectral
  url: rules/semscraper-com-rules.yml
- group: design
  href: https://artifacts.apis.io/semscraper-com/json-ld/semscraper-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/semscraper-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/semscraper-com/vocabulary/semscraper-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/semscraper-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/semscraper-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/semscraper-com/data-model/semscraper-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/semscraper-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/semscraper-com/conformance/semscraper-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/semscraper-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/semscraper-com/hosts/semscraper-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/semscraper-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/semscraper-com/vendors/semscraper-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/semscraper-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/semscraper-com/security/semscraper-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/semscraper-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.semscraper.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.semscraper.com/en/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.semscraper.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.semscraper.com/en/terms-and-conditions
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.semscraper.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.semscraper.com/en/contact-us
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.semscraper.com/en/documentation
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Semscraper provides SERP and Google Maps APIs for extracting search results, rankings, pixel positions, place details, and AI-generated overviews. It offers both single-request and bulk asynchronous processing, with transparent pricing per 1,000 SERPs. The platform includes an MCP server for integration with AI agents, comprehensive documentation, guides, and a free trial. It targets developers building search-driven applications, data pipelines, and AI tools.
image: https://www.semscraper.com/img/og_en.png?v=2
json_schemas:
- name: GetV1SerpResponse
  property_count: 3
  slug: semscraper-com-get-v1-serp-response
jsonld:
- class_count: 1
  name: Semscraper Com Context
  property_count: 1
  slug: semscraper-com-context
layout: provider
modified: '2026-10-31'
name: semscraper-com
nav: Providers
network: true
overview: 'semscraper-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SERP, Google-Maps, AI-Overviews, and Bulk-Processing.


  The semscraper-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  semscraper-com''s developer surface includes documentation, pricing, and 14 more developer resources.'
plans:
- name: Semscraper Com Plans Pricing
  plan_count: 3
  slug: semscraper-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: semscraper-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: semscraper-com-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 73.9
    catalog_earned_first_party: 0.0
    catalog_gap: 41.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 49.5
    contract_governance: 79.1
    contract_quality: 46.9
    developer_ergonomics: 25.5
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Semscraper Com Domain Security
  slug: semscraper-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: semscraper-com
tags:
- Company
- SERP
- Google-Maps
- AI-Overviews
- Bulk-Processing
website: https://www.semscraper.com/en/
---
