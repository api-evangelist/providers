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
- baseURL: https://www.computop-paygate.com
  baseurl_source: declared
  description: 'Computop API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Computop API
  slug: computop-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/computop/rules/computop-rules.yml
  title: ''
  type: Spectral
  url: rules/computop-rules.yml
- group: design
  href: https://artifacts.apis.io/computop/json-ld/computop-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/computop-context.jsonld
- group: design
  href: https://artifacts.apis.io/computop/vocabulary/computop-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/computop-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/computop/data-model/computop-data-model.yml
  title: ''
  type: DataModel
  url: data-model/computop-data-model.yml
- group: design
  href: https://artifacts.apis.io/computop/conformance/computop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/computop-conformance.yml
- group: other
  href: https://artifacts.apis.io/computop/hosts/computop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/computop-hosts.yml
- group: other
  href: https://artifacts.apis.io/computop/vendors/computop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/computop-vendors.yml
- group: auth
  href: https://artifacts.apis.io/computop/security/computop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/computop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://computop.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.computop.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.computop.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.computop.com
- group: operate
  title: ''
  type: Support
  url: https://computop.com/de/support/
- group: company
  title: ''
  type: Blog
  url: https://computop.com/de/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://computop.com/de/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://computop.com/de/datenschutz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/computop
created: '2026-10-28'
description: Computop is a German payment service provider offering an omnichannel payment gateway for e‑commerce, mobile commerce, point‑of‑sale and payment‑by‑link solutions. It supports a wide range of payment methods, provides analytics, fraud prevention and integration plugins for many shop systems, and serves merchants across Europe and beyond.
image: https://developer.computop.com/favicon.ico
json_schemas:
- name: PostCbpaypalAspxRequest
  property_count: 3
  slug: computop-post-cbpaypal-aspx-request
- name: PostPaypalcompleteAspxRequest
  property_count: 15
  slug: computop-post-paypalcomplete-aspx-request
- name: PostPaypalcompleteAspxResponse
  property_count: 7
  slug: computop-post-paypalcomplete-aspx-response
- name: PostPaypalvaultAspxRequest
  property_count: 9
  slug: computop-post-paypalvault-aspx-request
- name: PostPaypalvaultAspxResponse
  property_count: 7
  slug: computop-post-paypalvault-aspx-response
jsonld:
- class_count: 6
  name: Computop Context
  property_count: 29
  slug: computop-context
layout: provider
modified: '2026-10-28'
name: Computop
nav: Providers
network: true
overview: 'Computop is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, FinTech, E-commerce, Germany, and SaaS.


  The Computop catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Computop''s developer surface includes documentation, API reference, support, engineering blog, and 13 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Computop API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: computop-rules
scopes:
- name: Computop Scopes
  scope_count: 0
  slug: computop-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Computop Authentication
  slug: computop-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Computop Domain Security
  slug: computop-domain-security
  summary_line: TLSv1.3 · DMARC
slug: computop
tags:
- Payments
- FinTech
- E-commerce
- Germany
- SaaS
website: https://computop.com/
---
