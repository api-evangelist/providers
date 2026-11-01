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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://app.interakt.co
  baseurl_source: declared
  description: 'Resulticks API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: Resulticks API
  slug: interakt-co-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/interakt-co/plans/interakt-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/interakt-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/interakt-co/rules/interakt-co-rules.yml
  title: ''
  type: Spectral
  url: rules/interakt-co-rules.yml
- group: design
  href: https://artifacts.apis.io/interakt-co/json-ld/interakt-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/interakt-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/interakt-co/vocabulary/interakt-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/interakt-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/interakt-co/data-model/interakt-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/interakt-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/interakt-co/conformance/interakt-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/interakt-co-conformance.yml
- group: other
  href: https://artifacts.apis.io/interakt-co/hosts/interakt-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/interakt-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/interakt-co/vendors/interakt-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/interakt-co-vendors.yml
- group: auth
  href: https://artifacts.apis.io/interakt-co/security/interakt-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/interakt-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://interakt.co
- group: docs
  title: ''
  type: Documentation
  url: https://interakt.co/docs_subdomain/index/
- group: docs
  title: ''
  type: APIReference
  url: https://interakt.co/docs_subdomain/api/
- group: operate
  title: ''
  type: Support
  url: https://interakt.co/docs_subdomain/index/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://interakt.co
coverage:
  checked: '2026-10-25'
  detail: The API reference page provides only HTML documentation without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://interakt.co/docs_subdomain/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Resulticks provides a cloud-based marketing automation platform that enables businesses to orchestrate personalized, real‑time customer journeys across channels such as email, SMS, push notifications, and social media. Leveraging AI‑driven insights, the platform helps marketers segment audiences, trigger actions based on behavior, and measure campaign performance with robust analytics. Founded in 2012 and backed by 500‑global, Resulticks serves enterprises worldwide, offering APIs for campaign management, contact handling, and analytics integration, empowering developers to embed advanced engagement capabilities directly into their applications.
json_schemas:
- name: PostApiV1LeadsRequest
  property_count: 6
  slug: interakt-co-post-api-v1-leads-request
- name: PostApiV1MembersRequest
  property_count: 6
  slug: interakt-co-post-api-v1-members-request
jsonld:
- class_count: 2
  name: Interakt Co Context
  property_count: 9
  slug: interakt-co-context
layout: provider
modified: '2026-10-25'
name: Resulticks
nav: Providers
network: true
overview: 'Resulticks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Automation, Cloud, and AI.


  The Resulticks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Resulticks'' developer surface includes documentation, API reference, support, and 11 more developer resources.'
plans:
- name: Interakt Co Plans Pricing
  plan_count: 17
  slug: interakt-co-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Resulticks API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: interakt-co-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 31.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Interakt Co Domain Security
  slug: interakt-co-domain-security
  summary_line: TLSv1.3 · HSTS
slug: interakt-co
tags:
- Company
- Marketing
- Automation
- Cloud
- AI
website: https://interakt.co
---
