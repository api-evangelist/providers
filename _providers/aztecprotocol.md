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
api_count: 3
apis:
- description: Aztec provides a privacy‑first zkRollup API for developers.
  name: Aztec Protocol API
  slug: aztec-protocol-api
- baseURL: https://install.aztec.network
  baseurl_source: declared
  description: The Aztecprotocol API API from Aztecprotocol — 2 operation(s) for aztecprotocol api.
  name: Aztecprotocol Aztecprotocol API
  slug: aztecprotocol-aztecprotocol-api-api
- baseURL: https://install.aztec.network
  baseurl_source: declared
  description: The Status API from Aztecprotocol — 1 operation(s) for status.
  name: Aztecprotocol Status API
  slug: aztecprotocol-status-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/rules/aztecprotocol-rules.yml
  title: ''
  type: Spectral
  url: rules/aztecprotocol-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/json-ld/aztecprotocol-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aztecprotocol-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/vocabulary/aztecprotocol-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aztecprotocol-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/data-model/aztecprotocol-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aztecprotocol-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/changelog/aztecprotocol-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aztecprotocol-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/conformance/aztecprotocol-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aztecprotocol-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/llms/aztecprotocol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aztecprotocol-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/hosts/aztecprotocol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aztecprotocol-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/vendors/aztecprotocol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aztecprotocol-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://aztec.network/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aztecprotocol/refs/heads/main/security/aztecprotocol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aztecprotocol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aztec.network
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aztec.network
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aztec.network/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aztec.network/developers/getting_started_on_testnet
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/aztec
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
  type: Pricing
  url: https://aztec.network/token
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aztec.network/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aztec.network/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/aztecprotocol/workspace
coverage:
  checked: '2026-09-27'
  detail: Documentation is rendered via Docusaurus JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.aztec.network
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Aztecprotocol is a privacy‑first, zero‑knowledge rollup (zkRollup) built on Ethereum that enables confidential transactions and private smart contracts. It provides a decentralized, privacy‑preserving Layer 2 solution, offering developers tools, SDKs, and documentation to build secure, scalable applications while keeping transaction data hidden from public view.
image: https://cdn.prod.website-files.com/6847005bc403085c1aa846e0/689cacb514469cdab7b6c2cf_Aztec-cover.png
json_schemas:
- name: GetStatusResponse
  property_count: 5
  slug: aztecprotocol-get-status-response
- name: PostRequest
  property_count: 4
  slug: aztecprotocol-post-request
jsonld:
- class_count: 2
  name: Aztecprotocol Context
  property_count: 9
  slug: aztecprotocol-context
layout: provider
modified: '2026-09-27'
name: Aztecprotocol
nav: Providers
network: true
overview: 'Aztecprotocol publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Aztecprotocol API, Status API, and 1 more. Tagged areas include Blockchain, Privacy, ZK-Rollup, Ethereum, and Decentralized.


  The Aztecprotocol catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aztecprotocol''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
random_paper: 9
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Aztecprotocol API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: aztecprotocol-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 42.9
    discoverability: 71.4
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
  name: Aztecprotocol Domain Security
  slug: aztecprotocol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aztecprotocol
tags:
- Blockchain
- Privacy
- ZK-Rollup
- Ethereum
- Decentralized
website: https://aztec.network
---
