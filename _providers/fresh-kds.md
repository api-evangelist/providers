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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Fresh KDS API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Fresh KDS API
  slug: fresh-kds-api
artifact_total: 10
asyncapis:
- description: ''
  name: Fresh Kds Webhooks
  slug: fresh-kds-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/fresh-kds/plans/fresh-kds-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fresh-kds-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fresh-kds/rules/fresh-kds-rules.yml
  title: ''
  type: Spectral
  url: rules/fresh-kds-rules.yml
- group: design
  href: https://artifacts.apis.io/fresh-kds/json-ld/fresh-kds-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fresh-kds-context.jsonld
- group: design
  href: https://artifacts.apis.io/fresh-kds/vocabulary/fresh-kds-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fresh-kds-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fresh-kds/asyncapi/fresh-kds-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fresh-kds-webhooks.yml
- group: design
  href: https://artifacts.apis.io/fresh-kds/data-model/fresh-kds-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fresh-kds-data-model.yml
- group: design
  href: https://artifacts.apis.io/fresh-kds/conformance/fresh-kds-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fresh-kds-conformance.yml
- group: auth
  href: https://artifacts.apis.io/fresh-kds/well-known/fresh-kds-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fresh-kds-help-security.txt
- group: agent
  href: https://artifacts.apis.io/fresh-kds/well-known/fresh-kds-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fresh-kds-well-known.yml
- group: other
  href: https://artifacts.apis.io/fresh-kds/hosts/fresh-kds-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fresh-kds-hosts.yml
- group: other
  href: https://artifacts.apis.io/fresh-kds/vendors/fresh-kds-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fresh-kds-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.fresh.technology/kds/pos/register-pos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fresh.technology/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/fresh-kds/security/fresh-kds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fresh-kds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fresh.technology/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fresh.technology/kds/developer-guide
- group: docs
  title: ''
  type: Documentation
  url: https://www.fresh.technology/kds/developer-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://www.fresh.technology/kds/book-a-demo
- group: operate
  title: ''
  type: Support
  url: https://help.freshkds.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.fresh.technology/kds/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fresh.technology/kds/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fresh.technology/legal/terms-of-service
coverage:
  checked: '2026-10-27'
  detail: Developer guide page provides HTML docs but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://www.fresh.technology/kds/developer-guide
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Fresh KDS provides a cloud‑based kitchen display system (KDS) that helps restaurants manage orders, stations, and staff across multiple locations. The platform offers real‑time order visibility, performance analytics, and customizable workflows for cafes, fast‑casual, casual dining, food trucks, and breweries. Trusted by over 10,000 establishments, Fresh KDS aims to improve service speed, reduce errors, and streamline kitchen operations through a tablet‑friendly interface and integrations with POS systems.
image: https://cdn.prod.website-files.com/5fd7d7dfd939618064b6f97b/6a73d6aa35a6f5ed0d491872_Home%20Open%20Graph%20(1).jpg
json_schemas:
- name: PostIntegradoresKdsOrdersRequest
  property_count: 7
  slug: fresh-kds-post-integradores-kds-orders-request
- name: PostIntegradoresKdsOrdersResponse
  property_count: 2
  slug: fresh-kds-post-integradores-kds-orders-response
- name: PutIntegradoresKdsOrdersRequest
  property_count: 9
  slug: fresh-kds-put-integradores-kds-orders-request
- name: PutIntegradoresKdsOrdersResponse
  property_count: 2
  slug: fresh-kds-put-integradores-kds-orders-response
jsonld:
- class_count: 4
  name: Fresh Kds Context
  property_count: 6
  slug: fresh-kds-context
layout: provider
modified: '2026-10-27'
name: Fresh KDS
nav: Providers
network: true
overview: 'Fresh KDS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Kitchen Display System, Restaurants, POS Integration, Enterprise, and Tablet-based.


  The Fresh KDS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Fresh KDS''s developer surface includes signup flow, documentation, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Fresh Kds Plans Pricing
  plan_count: 5
  slug: fresh-kds-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Fresh KDS API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: fresh-kds-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 26.7
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
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
  name: Fresh Kds Domain Security
  slug: fresh-kds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fresh-kds
tags:
- Kitchen Display System
- Restaurants
- POS Integration
- Enterprise
- Tablet-based
- Food Service
website: https://fresh.technology/
---
