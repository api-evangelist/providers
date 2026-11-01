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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-31'
api_count: 3
apis:
- baseURL: https://api.hiro.so
  baseurl_source: declared
  description: 'Stacks api API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Stacks api API
  slug: api-api
- baseURL: https://api.hiro.so
  baseurl_source: declared
  description: 'Stacks core API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Stacks core API
  slug: core-api
- baseURL: https://api.hiro.so
  baseurl_source: declared
  description: 'Stacks stacks.js API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Stacks stacks.js API
  slug: stacks.js-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/blockstack-org/rules/blockstack-org-rules.yml
  title: ''
  type: Spectral
  url: rules/blockstack-org-rules.yml
- group: design
  href: https://artifacts.apis.io/blockstack-org/json-ld/blockstack-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blockstack-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/blockstack-org/vocabulary/blockstack-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blockstack-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blockstack-org/data-model/blockstack-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blockstack-org-data-model.yml
- group: operate
  href: https://artifacts.apis.io/blockstack-org/changelog/blockstack-org-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blockstack-org-changelog.yml
- group: design
  href: https://artifacts.apis.io/blockstack-org/conventions/blockstack-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blockstack-org-conventions.yml
- group: start
  href: https://artifacts.apis.io/blockstack-org/sandbox/blockstack-org-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/blockstack-org-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/blockstack-org/authentication/blockstack-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blockstack-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/blockstack-org/conformance/blockstack-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blockstack-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blockstack-org/llms/blockstack-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockstack-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/blockstack-org/well-known/blockstack-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blockstack-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/blockstack-org/hosts/blockstack-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockstack-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/blockstack-org/vendors/blockstack-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockstack-org-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.stacks.co/build/security
- group: operate
  title: ''
  type: Roadmap
  url: https://www.stacks.co/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alexgo-io
- group: company
  title: ''
  type: Blog
  url: https://www.stacks.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stacks.co/get-started/developer-quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockstack.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stacks.co/reference/api/stacks-blockchain-api.md
- group: auth
  href: https://artifacts.apis.io/blockstack-org/security/blockstack-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockstack-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blockstack.org
coverage:
  checked: '2026-10-24'
  detail: Docs are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://stacks.co/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: 'Stacks is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by union-square-ventures) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.prod.website-files.com/618b0aafa4afde65f2fe38fe/6834ec468b986650406f513f_webp-stacks-bitcoin-layer-smart-contracts-header.webp
json_schemas:
- name: GetV2AccountsPrincipalResponse
  property_count: 6
  slug: blockstack-org-get-v2-accounts-principal-response
- name: PostConstructionMetadataResponse
  property_count: 5
  slug: blockstack-org-post-construction-metadata-response
- name: PostConstructionPayloadsResponse
  property_count: 5
  slug: blockstack-org-post-construction-payloads-response
- name: PostConstructionPreprocessRequest
  property_count: 2
  slug: blockstack-org-post-construction-preprocess-request
- name: PostConstructionPreprocessResponse
  property_count: 5
  slug: blockstack-org-post-construction-preprocess-response
- name: PostDepositRequest
  property_count: 7
  slug: blockstack-org-post-deposit-request
jsonld:
- class_count: 34
  name: Blockstack Org Context
  property_count: 33
  slug: blockstack-org-context
layout: provider
modified: '2026-10-24'
name: Stacks
nav: Providers
network: true
overview: 'Stacks is listed with 3 APIs on the [APIs.io](https://apis.io/) network: api API, core API, and stacks.js API. Tagged areas include Bitcoin Staking, Self‑Custodial, DeFi, Smart Contracts, and Layer‑2.


  The Stacks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stacks'' developer surface includes changelog, sandbox, authentication, engineering blog, getting-started guide, documentation, API reference, and 15 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Stacks API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: blockstack-org-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 25.1
    developer_ergonomics: 50.0
    discoverability: 62.5
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 17
      marker_coverage: 100.0
      total: 17
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blockstack Org Authentication
  slug: blockstack-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blockstack Org Domain Security
  slug: blockstack-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blockstack-org
tags:
- Bitcoin Staking
- Self‑Custodial
- DeFi
- Smart Contracts
- Layer‑2
- Institutional Crypto
website: https://www.blockstack.org
---
