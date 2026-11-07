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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.bloq.it
  baseurl_source: declared
  description: The Bloqs API from Bloqit — 9 operation(s) for bloqs.
  name: Bloqit Bloqs API
  slug: bloqit-bloqs-api
- baseURL: https://api.bloq.it
  baseurl_source: declared
  description: The Public API from Bloqit — 1 operation(s) for public.
  name: Bloqit Public API
  slug: bloqit-public-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/bloqit/rules/bloqit-rules.yml
  title: ''
  type: Spectral
  url: rules/bloqit-rules.yml
- group: design
  href: https://artifacts.apis.io/bloqit/json-ld/bloqit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bloqit-context.jsonld
- group: design
  href: https://artifacts.apis.io/bloqit/vocabulary/bloqit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bloqit-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bloqit/data-model/bloqit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bloqit-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bloqit/changelog/bloqit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bloqit-changelog.yml
- group: design
  href: https://artifacts.apis.io/bloqit/conformance/bloqit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bloqit-conformance.yml
- group: other
  href: https://artifacts.apis.io/bloqit/hosts/bloqit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloqit-hosts.yml
- group: other
  href: https://artifacts.apis.io/bloqit/vendors/bloqit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bloqit-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloq.it/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloq.it/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://bloq.it/resources/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.bloq.it/
- group: auth
  href: https://artifacts.apis.io/bloqit/security/bloqit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloqit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bloq.it/
coverage:
  checked: '2026-09-29'
  detail: Bloqit website provides HTML documentation but no machine‑readable OpenAPI, GraphQL, or other contract files were found.
  evidence:
  - status: 200
    url: https://bloq.it/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Bloqit is a technology company focused on providing blockchain-based solutions for secure data storage and transaction processing. The company aims to enable enterprises to integrate decentralized ledger technology into their existing workflows, offering APIs for data immutability, smart contract execution, and audit trails. Bloqit’s platform emphasizes scalability, compliance with financial regulations, and developer-friendly SDKs across multiple programming languages. While still emerging, Bloqit positions itself as a bridge between traditional enterprise systems and the decentralized web, targeting sectors such as finance, supply chain, and digital identity.
image: https://cdn.prod.website-files.com/65080d564070276c57b51ad1/6a3d2897df280ddd0aa23cea_opengraphs_HOME.jpg
json_schemas:
- name: GetApiV1PublicBloqsResponse
  property_count: 4
  slug: bloqit-get-api-v1-public-bloqs-response
- name: GetBloqsBloqidResponse
  property_count: 7
  slug: bloqit-get-bloqs-bloqid-response
- name: PutBloqsBloqidCouriersAccessCodesRequest
  property_count: 6
  slug: bloqit-put-bloqs-bloqid-couriers-access-codes-request
- name: PutBloqsBloqidLockersLockeridIdResponse
  property_count: 11
  slug: bloqit-put-bloqs-bloqid-lockers-lockerid-id-response
- name: PutBloqsBloqidLockersOpenResponse
  property_count: 10
  slug: bloqit-put-bloqs-bloqid-lockers-open-response
- name: PutBloqsBloqidRequest
  property_count: 12
  slug: bloqit-put-bloqs-bloqid-request
jsonld:
- class_count: 14
  name: Bloqit Context
  property_count: 22
  slug: bloqit-context
layout: provider
modified: '2026-09-29'
name: Bloqit
nav: Providers
network: true
overview: 'Bloqit is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Bloqs API and Public API. Tagged areas include Company, Blockchain, Data Storage, API Platform, and Fintech.


  The Bloqit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bloqit''s developer surface includes changelog, documentation, and 12 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bloqit API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: bloqit-rules
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 24.9
    developer_ergonomics: 4.8
    discoverability: 67.0
    operational_transparency: 15.8
  previous_composite: 25.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/bloqit/bloqit-2026-10-11T102454.png
security:
- kind: domain-security
  name: Bloqit Domain Security
  slug: bloqit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloqit
tags:
- Company
- Blockchain
- Data Storage
- API Platform
- Fintech
- Lisbon
website: https://www.bloq.it/
---
