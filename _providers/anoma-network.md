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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: The Vault API from Anoma Network — 1 operation(s) for vault.
  name: Anoma Network Vault API
  slug: anoma-network-vault-api
artifact_total: 5
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anoma-network/refs/heads/main/rules/anoma-network-rules.yml
  title: ''
  type: Spectral
  url: rules/anoma-network-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anoma-network/refs/heads/main/json-ld/anoma-network-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anoma-network-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anoma-network/refs/heads/main/vocabulary/anoma-network-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anoma-network-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anoma-network/refs/heads/main/data-model/anoma-network-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anoma-network-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anoma-network/refs/heads/main/conformance/anoma-network-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anoma-network-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anoma-network/refs/heads/main/llms/anoma-network-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anoma-network-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anoma-network/refs/heads/main/hosts/anoma-network-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anoma-network-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anoma-network/refs/heads/main/vendors/anoma-network-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anoma-network-vendors.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://anoma.net/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anoma
- group: company
  title: ''
  type: Blog
  url: https://anoma.net/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anoma.net/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anoma.net/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anoma-network/refs/heads/main/security/anoma-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anoma-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anoma.net
coverage:
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI, GraphQL or AsyncAPI files were found.
  evidence:
  - status: 404
    url: https://api.anoma.net/openapi.json
  - status: 404
    url: https://anoma.net/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Anoma Network is a decentralized operating system that enables developers to build, deploy, and manage applications across multiple blockchain networks. It abstracts away blockchain complexity, offering private, easy-to-use tools and SDKs for creating interoperable, sovereign applications. Anoma aims to empower a new generation of decentralized services with flexible, secure, and scalable infrastructure.
image: https://anoma.net/images/opengraph-v5.jpg
json_schemas:
- name: GetVaultNetworkVaultidQuoteResponse
  property_count: 8
  slug: anoma-network-get-vault-network-vaultid-quote-response
jsonld:
- class_count: 1
  name: Anoma Network Context
  property_count: 8
  slug: anoma-network-context
layout: provider
modified: '2026-09-24'
name: Anoma Network
nav: Providers
network: true
overview: 'Anoma Network publishes 1 API on the [APIs.io](https://apis.io/) network: Vault API. Tagged areas include Blockchain, Decentralized, Operating System, SDK, and Interoperability.


  The Anoma Network catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anoma Network''s developer surface includes engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 5
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Anoma Network API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: anoma-network-rules
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 51.9
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 16.4
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Anoma Network Domain Security
  slug: anoma-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: anoma-network
tags:
- Blockchain
- Decentralized
- Operating System
- SDK
- Interoperability
website: https://anoma.net
---
