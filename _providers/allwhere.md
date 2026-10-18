---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 33.1
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Allwhere API provides endpoints for IT procurement and asset management as documented in the API Reference.
  name: Allwhere API
  slug: allwhere-api-2
- baseURL: https://api.allwhere.co
  baseurl_source: declared
  description: The Beta API from allwhere — 6 operation(s) for beta.
  name: allwhere Beta API
  slug: allwhere-beta-api
artifact_total: 12
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/rules/allwhere-rules.yml
  title: ''
  type: Spectral
  url: rules/allwhere-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/json-ld/allwhere-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allwhere-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/vocabulary/allwhere-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allwhere-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/data-model/allwhere-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allwhere-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/conventions/allwhere-conventions.yml
  title: ''
  type: Conventions
  url: conventions/allwhere-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/authentication/allwhere-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allwhere-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/conformance/allwhere-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allwhere-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/llms/allwhere-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allwhere-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/well-known/allwhere-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allwhere-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/hosts/allwhere-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allwhere-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/vendors/allwhere-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allwhere-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allwhere.co/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://www.allwhere.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.allwhere.co/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.allwhere.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.allwhere.co/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.allwhere.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/allwhere
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allwhere/refs/heads/main/security/allwhere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allwhere-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.allwhere.co/
coverage:
  checked: '2026-10-05'
  detail: Documentation is served via a JavaScript-rendered ReadMe site, preventing machine-readable spec extraction.
  evidence:
  - status: 200
    url: https://docs.allwhere.co/reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Allwhere provides global IT procurement, equipment, and asset management services for distributed workforce companies. It automates the device lifecycle from sourcing, deployment, retrieval, to resale or recycling, offering integrations with HRIS, MDM, and IDP tools, and supports enterprises worldwide.
image: https://cdn.prod.website-files.com/633497a6357b321a90a7ddc9/6374e4d9fc01b94ddc7430f5_Open%20Graph%20Image.webp
json_schemas:
- name: GetBetaAssetsAssetidResponse
  property_count: 24
  slug: allwhere-get-beta-assets-assetid-response
- name: GetBetaBetaidResponse
  property_count: 2
  slug: allwhere-get-beta-betaid-response
- name: GetBetaOrders152341AcmeResponse
  property_count: 7
  slug: allwhere-get-beta-orders152341-acme-response
- name: PostBetaEmployeesResponse
  property_count: 19
  slug: allwhere-post-beta-employees-response
- name: PostBetaOrdersOrderidRequest
  property_count: 6
  slug: allwhere-post-beta-orders-orderid-request
- name: PostBetaOrdersOrderidResponse
  property_count: 7
  slug: allwhere-post-beta-orders-orderid-response
jsonld:
- class_count: 11
  name: Allwhere Context
  property_count: 53
  slug: allwhere-context
layout: provider
modified: '2026-09-24'
name: allwhere
nav: Providers
network: true
overview: 'allwhere is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Beta API, and 1 more. Tagged areas include Company, IT, Asset-Management, Procurement, and Remote-Workforce.


  The allwhere catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  allwhere''s developer surface includes authentication, pricing, engineering blog, API reference, getting-started guide, documentation, and 14 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: allwhere API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: allwhere-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 29.0
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 26.5
    developer_ergonomics: 42.9
    discoverability: 64.3
    operational_transparency: 5.3
  previous_composite: 0.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Allwhere Authentication
  slug: allwhere-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Allwhere Domain Security
  slug: allwhere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allwhere
tags:
- Company
- IT
- Asset-Management
- Procurement
- Remote-Workforce
- Enterprise
website: https://www.allwhere.co/
---
