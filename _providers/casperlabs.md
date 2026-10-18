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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: API for Casper blockchain developers, providing endpoints for deploying contracts, querying state, and managing accounts.
  name: Casper Developer API
  slug: casper-developer-api
- baseURL: http://<node_address>:8888
  baseurl_source: declared
  description: The Casperlabs API API from Casperlabs — 1 operation(s) for casperlabs api.
  name: Casperlabs Casperlabs API
  slug: casperlabs-casperlabs-api-api
- baseURL: http://<node_address>:8888
  baseurl_source: declared
  description: The Metrics API from Casperlabs — 1 operation(s) for metrics.
  name: Casperlabs Metrics API
  slug: casperlabs-metrics-api
- baseURL: http://<node_address>:8888
  baseurl_source: declared
  description: The Status API from Casperlabs — 1 operation(s) for status.
  name: Casperlabs Status API
  slug: casperlabs-status-api
artifact_total: 9
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casperlabs/refs/heads/main/rules/casperlabs-rules.yml
  title: ''
  type: Spectral
  url: rules/casperlabs-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casperlabs/refs/heads/main/json-ld/casperlabs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/casperlabs-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casperlabs/refs/heads/main/vocabulary/casperlabs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/casperlabs-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casperlabs/refs/heads/main/data-model/casperlabs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/casperlabs-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casperlabs/refs/heads/main/conformance/casperlabs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/casperlabs-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/casperlabs/refs/heads/main/llms/casperlabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/casperlabs-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/casperlabs/refs/heads/main/hosts/casperlabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/casperlabs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/casperlabs/refs/heads/main/vendors/casperlabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/casperlabs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.casper.network/terms-of-use
- group: operate
  title: ''
  type: Roadmap
  url: https://www.casper.network/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.casper.network/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.casper.network/news
- group: other
  title: ''
  type: Leadership
  url: https://www.casper.network/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/casper-network
- group: company
  title: ''
  type: Blog
  url: https://www.casper.network/blog
- group: start
  title: ''
  type: GettingStarted
  url: http://docs.casper.network/condor/tags/setup
- group: docs
  title: ''
  type: Documentation
  url: https://developer.casper.network/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/casperlabs/refs/heads/main/security/casperlabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/casperlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.casper.network
coverage:
  checked: '2026-10-07'
  detail: The developer portal serves only HTML pages with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://developer.casper.network
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Casperlabs (formerly known as Casper Network) is a public, permissionless blockchain platform focused on real‑world asset tokenization, enterprise‑grade smart contracts, and AI‑enabled tooling. It offers a Proof‑of‑Stake consensus, WebAssembly execution, and a suite of developer resources including SDKs, documentation, and an AI Toolkit. The ecosystem supports decentralized finance, NFTs, liquid staking, and quantum‑safe cryptography, targeting institutions, developers, and end‑users seeking secure, scalable blockchain solutions.
image: https://cdn.prod.website-files.com/668fef77d8ac075ed5e3f57a/66900f439d0597692b64fcf2_Casper_Wordmark_Red_RGB.png
json_schemas:
- name: GetResponse
  property_count: 10
  slug: casperlabs-get-response
- name: GetStatusResponse
  property_count: 10
  slug: casperlabs-get-status-response
jsonld:
- class_count: 2
  name: Casperlabs Context
  property_count: 10
  slug: casperlabs-context
layout: provider
modified: '2026-10-07'
name: Casperlabs
nav: Providers
network: true
overview: 'Casperlabs is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Casperlabs API, Metrics API, Status API, and 1 more. Tagged areas include Blockchain, Smart-Contracts, Enterprise, AI-Toolkit, and Decentralized-Finance.


  The Casperlabs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Casperlabs'' developer surface includes engineering blog, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Casperlabs API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: casperlabs-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 42.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.1
    contract_governance: 22.0
    contract_quality: 22.3
    developer_ergonomics: 23.8
    discoverability: 73.2
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Casperlabs Domain Security
  slug: casperlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: casperlabs
tags:
- Blockchain
- Smart-Contracts
- Enterprise
- AI-Toolkit
- Decentralized-Finance
website: https://www.casper.network
---
