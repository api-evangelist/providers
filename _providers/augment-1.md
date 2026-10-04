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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-03'
api_count: 2
apis:
- description: API for Augment platform
  name: Augment API
  slug: augment-api
- baseURL: https://webservice.augment.com
  baseurl_source: declared
  description: The Rest API from Augment — 5 operation(s) for rest.
  name: Augment Rest API
  slug: augment-1-rest-api
artifact_total: 12
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/augment-1/refs/heads/main/plans/augment-1-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/augment-1-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augment-1/refs/heads/main/rules/augment-1-rules.yml
  title: ''
  type: Spectral
  url: rules/augment-1-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augment-1/refs/heads/main/json-ld/augment-1-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/augment-1-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augment-1/refs/heads/main/vocabulary/augment-1-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/augment-1-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augment-1/refs/heads/main/data-model/augment-1-data-model.yml
  title: ''
  type: DataModel
  url: data-model/augment-1-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augment-1/refs/heads/main/conformance/augment-1-conformance.yml
  title: ''
  type: Conformance
  url: conformance/augment-1-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augment-1/refs/heads/main/hosts/augment-1-hosts.yml
  title: ''
  type: Hosts
  url: hosts/augment-1-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augment-1/refs/heads/main/vendors/augment-1-vendors.yml
  title: ''
  type: Vendors
  url: vendors/augment-1-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.augment.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Augment
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augment-1/refs/heads/main/security/augment-1-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augment-1-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.augment.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.augment.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.augment.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.augment.com/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://www.augment.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.augment.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.augment.com/privacy-policy
coverage:
  checked: 2026-09-26
  detail: Developers site renders docs via JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://developers.augment.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Augment is a leading Augmented Reality (AR) platform that enables brands and retailers to create immersive 3D product visualizations. By integrating AR experiences into e‑commerce, field sales, and marketing, Augment helps increase online conversion, improve in‑store engagement, and streamline product presentation. The platform offers tools for 3D model management, AR viewer embedding, and collaborative workflows, serving industries such as consumer goods, fashion, and manufacturing.
image: https://augment.com/images/home/header.png
json_schemas:
- name: DeleteRestV1OauthTokenResponse
  property_count: 1
  slug: augment-1-delete-rest-v1-oauth-token-response
- name: GetRestV1CatalogsCatalogidProductsResponse
  property_count: 4
  slug: augment-1-get-rest-v1-catalogs-catalogid-products-response
- name: GetRestV1CatalogsResponse
  property_count: 1
  slug: augment-1-get-rest-v1-catalogs-response
- name: PostRestV1CatalogsCatalogidProductsRequest
  property_count: 1
  slug: augment-1-post-rest-v1-catalogs-catalogid-products-request
- name: PostRestV1OauthTokenResponse
  property_count: 5
  slug: augment-1-post-rest-v1-oauth-token-response
- name: PutRestV1CatalogsRequest
  property_count: 2
  slug: augment-1-put-rest-v1-catalogs-request
jsonld:
- class_count: 14
  name: Augment 1 Context
  property_count: 9
  slug: augment-1-context
layout: provider
modified: '2026-09-26'
name: Augment
nav: Providers
network: true
overview: 'Augment publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Rest API, and 1 more. Tagged areas include Company, Augmented Reality, E-Commerce, 3D Visualization, and Software-as-a-Service.


  The Augment catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Augment''s developer surface includes documentation, API reference, getting-started guide, pricing, support, and 13 more developer resources.'
plans:
- name: Augment 1 Plans Pricing
  plan_count: 3
  slug: augment-1-plans-pricing
random_paper: 11
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Augment API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: augment-1-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 26.4
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Augment 1 Domain Security
  slug: augment-1-domain-security
  summary_line: TLSv1.3 · DMARC
slug: augment-1
tags:
- Company
- Augmented Reality
- E-Commerce
- 3D Visualization
- Software-as-a-Service
website: https://www.augment.com/
---
