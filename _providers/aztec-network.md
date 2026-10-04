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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-03'
api_count: 2
apis:
- baseURL: https://install.aztec.network
  baseurl_source: declared
  description: The Aztec Network API API from Aztec Network — 2 operation(s) for aztec network api.
  name: Aztec Network Aztec Network API
  slug: aztec-network-aztec-network-api-api
- baseURL: https://install.aztec.network
  baseurl_source: declared
  description: The Status API from Aztec Network — 1 operation(s) for status.
  name: Aztec Network Status API
  slug: aztec-network-status-api
artifact_total: 7
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aztec.network/developers/getting_started_on_local_network
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/rules/aztec-network-rules.yml
  title: ''
  type: Spectral
  url: rules/aztec-network-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/json-ld/aztec-network-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aztec-network-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/vocabulary/aztec-network-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aztec-network-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/data-model/aztec-network-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aztec-network-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/changelog/aztec-network-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aztec-network-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/conformance/aztec-network-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aztec-network-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/llms/aztec-network-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aztec-network-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/hosts/aztec-network-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aztec-network-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/vendors/aztec-network-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aztec-network-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://aztec.network/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aztec-network/refs/heads/main/security/aztec-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aztec-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aztec.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aztec.network/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aztec.network/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aztec.network/developers/docs/aztec-js
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/aztec
- group: company
  title: ''
  type: Blog
  url: https://aztec.network/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AztecProtocol
- group: operate
  title: ''
  type: Roadmap
  url: https://aztec.network/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aztec.network/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aztec.network/privacy-policy
coverage:
  checked: '2026-09-27'
  detail: Developer documentation on docs.aztec.network provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 404
    url: https://docs.aztec.network/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Aztec Network is a decentralized, privacy‑preserving layer‑2 scaling solution on Ethereum. It enables developers to build applications with end‑to‑end privacy using its Noir programming language and zero‑knowledge proofs. The network focuses on composable privacy, programmable proof systems, and open‑source tooling, aiming to bring confidential smart contracts and private transactions to mainstream blockchain use cases.
image: https://cdn.prod.website-files.com/6847005bc403085c1aa846e0/689cacb514469cdab7b6c2cf_Aztec-cover.png
json_schemas:
- name: GetStatusResponse
  property_count: 2
  slug: aztec-network-get-status-response
- name: PostRequest
  property_count: 4
  slug: aztec-network-post-request
jsonld:
- class_count: 2
  name: Aztec Network Context
  property_count: 6
  slug: aztec-network-context
layout: provider
modified: '2026-09-27'
name: Aztec Network
nav: Providers
network: true
overview: 'Aztec Network publishes 2 APIs on the [APIs.io](https://apis.io/) network: Aztec Network API and Status API. Tagged areas include Company, Blockchain, Privacy, Layer 2, and Ethereum.


  The Aztec Network catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aztec Network''s developer surface includes getting-started guide, changelog, documentation, API reference, support, engineering blog, and 16 more developer resources.'
random_paper: 16
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Aztec Network API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: aztec-network-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 45.2
    discoverability: 75.0
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
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
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Aztec Network Domain Security
  slug: aztec-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aztec-network
tags:
- Company
- Blockchain
- Privacy
- Layer 2
- Ethereum
website: https://aztec.network/
---
