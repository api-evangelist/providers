---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Ezeebit API provides payment, payout, wallet and merchant services as documented.
  name: Ezeebit API
  slug: ezeebit-api-2
- baseURL: https://uat-api.ezeebit.com
  baseurl_source: declared
  description: 'Ezeebit API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Ezeebit API
  slug: ezeebit-api
artifact_total: 8
asyncapis:
- description: ''
  name: Ezeebit Webhooks
  slug: ezeebit-webhooks
common:
- group: design
  href: https://artifacts.apis.io/ezeebit/rules/ezeebit-rules.yml
  title: ''
  type: Spectral
  url: rules/ezeebit-rules.yml
- group: design
  href: https://artifacts.apis.io/ezeebit/json-ld/ezeebit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ezeebit-context.jsonld
- group: design
  href: https://artifacts.apis.io/ezeebit/vocabulary/ezeebit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ezeebit-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ezeebit/asyncapi/ezeebit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ezeebit-webhooks.yml
- group: design
  href: https://artifacts.apis.io/ezeebit/data-model/ezeebit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ezeebit-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ezeebit/authentication/ezeebit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ezeebit-authentication.yml
- group: design
  href: https://artifacts.apis.io/ezeebit/errors/ezeebit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ezeebit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ezeebit/conformance/ezeebit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ezeebit-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ezeebit/llms/ezeebit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ezeebit-llms.txt
- group: agent
  href: https://artifacts.apis.io/ezeebit/well-known/ezeebit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ezeebit-well-known.yml
- group: other
  href: https://artifacts.apis.io/ezeebit/hosts/ezeebit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ezeebit-hosts.yml
- group: other
  href: https://artifacts.apis.io/ezeebit/vendors/ezeebit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ezeebit-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ezeebit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ezeebit.com/
- group: auth
  href: https://artifacts.apis.io/ezeebit/security/ezeebit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ezeebit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ezeebit.com/
created: '2026-10-29'
description: Ezeebit enables businesses in Africa to accept cryptocurrency payments instantly through its ePOS system, processing transactions in under half a second. It supports multiple stablecoins and offers settlement in local currency ZAR, aiming to boost crypto adoption among merchants. The platform provides a seamless checkout experience, robust security, and compliance with regional regulations, positioning itself as a bridge between blockchain technology and everyday commerce.
image: https://www.ezeebit.com/favicon.png
json_schemas:
- name: PostOpenApiV1NeworderRequest
  property_count: 4
  slug: ezeebit-post-open-api-v1-neworder-request
jsonld:
- class_count: 1
  name: Ezeebit Context
  property_count: 4
  slug: ezeebit-context
layout: provider
modified: '2026-10-29'
name: Ezeebit
nav: Providers
network: true
overview: 'Ezeebit is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cryptocurrency, Africa, and EPOS.


  The Ezeebit catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ezeebit''s developer surface includes authentication, documentation, and 14 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Ezeebit API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ezeebit-rules
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 3.9
    contract_governance: 22.0
    contract_quality: 25.6
    developer_ergonomics: 16.7
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.6
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ezeebit/ezeebit-2026-11-03T131746.png
security:
- kind: authentication
  name: Ezeebit Authentication
  slug: ezeebit-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ezeebit Domain Security
  slug: ezeebit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ezeebit
tags:
- Company
- Payments
- Cryptocurrency
- Africa
- EPOS
website: https://www.ezeebit.com/
---
