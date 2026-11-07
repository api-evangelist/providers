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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Protocol Labs API as documented publicly: 198 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Protocol Labs API
  slug: pl-xyz-api
artifact_total: 11
common:
- group: auth
  href: https://artifacts.apis.io/pl-xyz/well-known/pl-xyz-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pl-xyz-docs-security.txt
- group: design
  href: https://artifacts.apis.io/pl-xyz/rules/pl-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/pl-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/pl-xyz/json-ld/pl-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pl-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/pl-xyz/vocabulary/pl-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pl-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pl-xyz/data-model/pl-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pl-xyz-data-model.yml
- group: auth
  href: https://artifacts.apis.io/pl-xyz/authentication/pl-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pl-xyz-authentication.yml
- group: design
  href: https://artifacts.apis.io/pl-xyz/conformance/pl-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pl-xyz-conformance.yml
- group: auth
  href: https://artifacts.apis.io/pl-xyz/well-known/pl-xyz-about-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pl-xyz-about-security.txt
- group: agent
  href: https://artifacts.apis.io/pl-xyz/well-known/pl-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pl-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/pl-xyz/hosts/pl-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pl-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/pl-xyz/vendors/pl-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pl-xyz-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://pl.xyz/media/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ipfs.tech/how-to/command-line-quick-start/
- group: auth
  href: https://artifacts.apis.io/pl-xyz/security/pl-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pl-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pl.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ipfs.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ipfs.io/
- group: company
  title: ''
  type: Blog
  url: https://pl.xyz/blog/
coverage:
  checked: '2026-10-29'
  detail: Protocol Labs provides documentation and blogs but no public developer program or API specifications were found.
  evidence:
  - status: 200
    url: https://docs.ipfs.io/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Protocol Labs is a pioneering research, development, and deployment organization focused on building the protocols, tools, and services that underpin the decentralized web. Founded by leading technologists, the company creates open-source infrastructure such as IPFS, Filecoin, and libp2p, enabling distributed storage, content addressing, and peer-to-peer networking. Its mission is to accelerate the adoption of decentralized technologies by fostering innovation, supporting developers, and collaborating with a global community of contributors and partners across the blockchain and web3 ecosystem.
image: https://pl.xyz/images/og-default.jpg
json_schemas:
- name: PostApiV0BitswapLedgerResponse
  property_count: 9
  slug: pl-xyz-post-api-v0-bitswap-ledger-response
- name: PostApiV0CidHashesResponse
  property_count: 8
  slug: pl-xyz-post-api-v0-cid-hashes-response
- name: PostApiV0CidInspectResponse
  property_count: 3
  slug: pl-xyz-post-api-v0-cid-inspect-response
- name: PostApiV0MountResponse
  property_count: 5
  slug: pl-xyz-post-api-v0-mount-response
- name: PostApiV0NameGetResponse
  property_count: 5
  slug: pl-xyz-post-api-v0-name-get-response
- name: PostApiV0SwarmPeeringRmResponse
  property_count: 1
  slug: pl-xyz-post-api-v0-swarm-peering-rm-response
jsonld:
- class_count: 120
  name: Pl Xyz Context
  property_count: 132
  slug: pl-xyz-context
layout: provider
modified: '2026-10-29'
name: Protocol Labs
nav: Providers
network: true
overview: 'Protocol Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Decentralized, Open Source, Web3, and Infrastructure.


  The Protocol Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Protocol Labs'' developer surface includes authentication, getting-started guide, documentation, engineering blog, and 14 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Protocol Labs API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: pl-xyz-rules
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 28.6
    discoverability: 58.0
    operational_transparency: 10.5
  previous_composite: 24.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pl-xyz/pl-xyz-2026-11-03T141248.png
security:
- kind: authentication
  name: Pl Xyz Authentication
  slug: pl-xyz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pl Xyz Domain Security
  slug: pl-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pl-xyz
tags:
- Company
- Decentralized
- Open Source
- Web3
- Infrastructure
website: https://pl.xyz/
---
