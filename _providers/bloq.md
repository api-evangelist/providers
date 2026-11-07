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
    agentic_access: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Bloq Agentic Access
  operation_count: 25
  slug: bloq-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 7
apis:
- baseURL: https://api.bloq.com
  baseurl_source: declared
  description: The Auth API from Bloq — 3 operation(s) for auth.
  name: Bloq Auth API
  slug: bloq-auth-api
- baseURL: https://api.bloq.com
  baseurl_source: declared
  description: The Bloq API API from Bloq — 1 operation(s) for bloq api.
  name: Bloq Bloq API
  slug: bloq-bloq-api-api
- baseURL: https://api.bloq.com
  baseurl_source: declared
  description: The Chains API from Bloq — 1 operation(s) for chains.
  name: Bloq Chains API
  slug: bloq-chains-api
- baseURL: https://api.bloq.com
  baseurl_source: declared
  description: The Logs API from Bloq — 1 operation(s) for logs.
  name: Bloq Logs API
  slug: bloq-logs-api
- baseURL: https://api.bloq.com
  baseurl_source: declared
  description: The Staking API from Bloq — 7 operation(s) for staking.
  name: Bloq Staking API
  slug: bloq-staking-api
- baseURL: https://api.bloq.com
  baseurl_source: declared
  description: The Status API from Bloq — 1 operation(s) for status.
  name: Bloq Status API
  slug: bloq-status-api
- baseURL: https://api.bloq.com
  baseurl_source: declared
  description: The Users API from Bloq — 7 operation(s) for users.
  name: Bloq Users API
  slug: bloq-users-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/bloq/agentic-access/bloq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bloq-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bloq/well-known/bloq-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bloq-clarity-security.txt
- group: build
  href: https://artifacts.apis.io/bloq/integrations/bloq-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/bloq-integration-edges.yml
- group: design
  href: https://artifacts.apis.io/bloq/rules/bloq-rules.yml
  title: ''
  type: Spectral
  url: rules/bloq-rules.yml
- group: design
  href: https://artifacts.apis.io/bloq/json-ld/bloq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bloq-context.jsonld
- group: design
  href: https://artifacts.apis.io/bloq/vocabulary/bloq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bloq-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bloq/data-model/bloq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bloq-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: auth
  href: https://artifacts.apis.io/bloq/authentication/bloq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bloq-authentication.yml
- group: design
  href: https://artifacts.apis.io/bloq/conformance/bloq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bloq-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bloq/llms/bloq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bloq-llms.txt
- group: agent
  href: https://artifacts.apis.io/bloq/well-known/bloq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bloq-well-known.yml
- group: other
  href: https://artifacts.apis.io/bloq/hosts/bloq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloq-hosts.yml
- group: other
  href: https://artifacts.apis.io/bloq/vendors/bloq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bloq-vendors.yml
- group: build
  href: https://artifacts.apis.io/bloq/packages/bloq-packages.yml
  title: ''
  type: SDKs
  url: packages/bloq-packages.yml
- group: build
  href: https://artifacts.apis.io/bloq/packages/bloq-packages.yml
  title: ''
  type: Packages
  url: packages/bloq-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloq.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://bloq.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloq.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://bloq.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://bloq.com/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloq
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bloq.com/readme/bloq-account-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bloq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bloq.com
- group: auth
  href: https://artifacts.apis.io/bloq/security/bloq-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloq-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bloq/security/bloq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloq.com
coverage:
  checked: '2026-09-29'
  detail: API spec endpoints on https://api.bloq.com return HTTP 403, indicating access requires a partner or sales login.
  evidence:
  - status: 403
    url: https://api.bloq.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-29'
description: Bloq is a Web3 infrastructure company offering a suite of decentralized finance, mining, metaverse, and blockchain application tools. Their platform includes BloqCloud, Lumerin hashpower marketplace, Vesper DeFi services, Metronome synthetic assets, and more, targeting enterprises and developers building on decentralized technologies.
image: https://bloq.com/wp-content/uploads/2022/03/bloq-opengraph.png
json_schemas:
- name: GetStakingEthereumChainIdResponse
  property_count: 5
  slug: bloq-get-staking-ethereum-chain-id-response
- name: GetStakingEthereumChainValidatorsPubkeyPerformanceResponse
  property_count: 8
  slug: bloq-get-staking-ethereum-chain-validators-pubkey-performance-response
- name: GetStakingEthereumChainValidatorsPubkeyResponse
  property_count: 12
  slug: bloq-get-staking-ethereum-chain-validators-pubkey-response
- name: GetUsersMeNodesIdResponse
  property_count: 16
  slug: bloq-get-users-me-nodes-id-response
- name: PostResponse
  property_count: 16
  slug: bloq-post-response
- name: PostStakingEthereumChainValidatorsResponse
  property_count: 9
  slug: bloq-post-staking-ethereum-chain-validators-response
jsonld:
- class_count: 27
  name: Bloq Context
  property_count: 56
  slug: bloq-context
layout: provider
modified: '2026-09-29'
name: Bloq
nav: Providers
network: true
overview: 'Bloq is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Bloq API, Chains API, and 4 more. Tagged areas include Company, Web3, Infrastructure, DeFi, and Blockchain.


  The Bloq catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bloq''s developer surface includes authentication, support, getting-started guide, documentation, and 24 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Bloq API Rules
  rule_count: 47
  severity_counts:
    error: 41
    hint: 0
    info: 3
    warn: 3
  slug: bloq-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 36.9
    discoverability: 80.4
    operational_transparency: 7.9
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bloq/bloq-2026-10-11T102448.png
security:
- kind: authentication
  name: Bloq Authentication
  slug: bloq-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bloq Domain Security
  slug: bloq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bloq Vulnerability Disclosure
  slug: bloq-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloq
tags:
- Company
- Web3
- Infrastructure
- DeFi
- Blockchain
website: https://bloq.com
---
