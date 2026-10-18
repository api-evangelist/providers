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
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-10-17'
api_count: 5
apis:
- baseURL: https://api.shift4.com
  baseurl_source: declared
  description: The Charges API from Credorax — 1 operation(s) for charges.
  name: Credorax Charges API
  slug: credorax-charges-api
- baseURL: https://api.shift4.com
  baseurl_source: declared
  description: The Customers API from Credorax — 1 operation(s) for customers.
  name: Credorax Customers API
  slug: credorax-customers-api
- baseURL: https://api.shift4.com
  baseurl_source: declared
  description: The Events API from Credorax — 1 operation(s) for events.
  name: Credorax Events API
  slug: credorax-events-api
- baseURL: https://api.shift4.com
  baseurl_source: declared
  description: The Plans API from Credorax — 1 operation(s) for plans.
  name: Credorax Plans API
  slug: credorax-plans-api
- baseURL: https://api.shift4.com
  baseurl_source: declared
  description: The Tokens API from Credorax — 1 operation(s) for tokens.
  name: Credorax Tokens API
  slug: credorax-tokens-api
artifact_total: 15
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/rules/credorax-rules.yml
  title: ''
  type: Spectral
  url: rules/credorax-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/json-ld/credorax-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/credorax-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/vocabulary/credorax-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/credorax-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/data-model/credorax-data-model.yml
  title: ''
  type: DataModel
  url: data-model/credorax-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/changelog/credorax-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/credorax-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/conventions/credorax-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/credorax-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/conventions/credorax-conventions.yml
  title: ''
  type: Conventions
  url: conventions/credorax-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/authentication/credorax-authentication.yml
  title: ''
  type: Authentication
  url: authentication/credorax-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/conformance/credorax-conformance.yml
  title: ''
  type: Conformance
  url: conformance/credorax-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/llms/credorax-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/credorax-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/a2a/credorax-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/credorax-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/well-known/credorax-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/credorax-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/well-known/credorax-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/credorax-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/well-known/credorax-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/credorax-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/hosts/credorax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/credorax-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/vendors/credorax-vendors.yml
  title: ''
  type: Vendors
  url: vendors/credorax-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/packages/credorax-packages.yml
  title: ''
  type: SDKs
  url: packages/credorax-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/packages/credorax-packages.yml
  title: ''
  type: Packages
  url: packages/credorax-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.shift4.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shift4.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.shift4.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://matterhorn-api.redocly.app/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://dev.shift4.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shift4.com/apis/payments-platform-rest/openapi.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credorax/refs/heads/main/security/credorax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credorax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shift4.com
coverage:
  checked: '2026-10-11'
  detail: API reference page at https://dev.shift4.com/docs/api is a JavaScript‑rendered SPA with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://dev.shift4.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Credorax, now part of Shift4, provides a unified payments and commerce technology platform. It offers integrated solutions for online payments, point‑of‑sale, mobile, and contactless technologies across industries such as food & beverage, hospitality, sports & entertainment, travel, and retail. The platform enables businesses to deliver seamless customer experiences, manage fraud prevention, and access analytics through a comprehensive API suite.
image: https://www.shift4.com/images/default-og-image2.jpg
json_schemas:
- name: PostChargesRequest
  property_count: 20
  slug: credorax-post-charges-request
- name: PostChargesResponse
  property_count: 43
  slug: credorax-post-charges-response
- name: PostCustomersCustomeridCardsResponse
  property_count: 23
  slug: credorax-post-customers-customerid-cards-response
- name: PostPlansResponse
  property_count: 13
  slug: credorax-post-plans-response
- name: PostTokensRequest
  property_count: 13
  slug: credorax-post-tokens-request
- name: PostTokensResponse
  property_count: 22
  slug: credorax-post-tokens-response
jsonld:
- class_count: 12
  name: Credorax Context
  property_count: 75
  slug: credorax-context
layout: provider
modified: '2026-10-11'
name: Credorax
nav: Providers
network: true
overview: 'Credorax is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Charges API, Customers API, Events API, and 2 more. Tagged areas include Company.


  The Credorax catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Credorax''s developer surface includes changelog, authentication, support, getting-started guide, documentation, API reference, and 20 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Credorax API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: credorax-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 52.4
    discoverability: 69.6
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
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
  name: Credorax Authentication
  slug: credorax-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Credorax Domain Security
  slug: credorax-domain-security
  summary_line: TLSv1.3 · DMARC
slug: credorax
tags:
- Company
website: https://www.shift4.com
---
