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
  band: agent-ready
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
    error_semantics: verified
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Coincover Agentic Access
  operation_count: 21
  slug: coincover-agentic-access
  summary_line: 21 operations · 17 acting
api_count: 3
apis:
- description: API for orchestrating identity verification and key management workflows
  name: Control Orchestrator API
  slug: control-orchestrator-api
- description: Direct integration for institutions backing up their digital asset wallets
  name: Recover for Institutions API
  slug: recover-for-institutions-api
- baseURL: https://orchestrator.control.coincover.com
  baseurl_source: declared
  description: The Backup API from Coincover — 1 operation(s) for backup.
  name: Coincover Backup API
  slug: coincover-backup-api
- baseURL: https://orchestrator.control.coincover.com
  baseurl_source: declared
  description: Store and verify encrypted backup data and files.
  name: Coincover Backups API
  slug: coincover-backups-api
- baseURL: https://orchestrator.control.coincover.com
  baseurl_source: declared
  description: The Key API from Coincover — 1 operation(s) for key.
  name: Coincover Key API
  slug: coincover-key-api
- baseURL: https://orchestrator.control.coincover.com
  baseurl_source: declared
  description: Generate, assign, and verify cryptographic keys.
  name: Coincover Keys API
  slug: coincover-keys-api
- baseURL: https://orchestrator.control.coincover.com
  baseurl_source: declared
  description: The Partner API from Coincover — 2 operation(s) for partner.
  name: Coincover Partner API
  slug: coincover-partner-api
- baseURL: https://orchestrator.control.coincover.com
  baseurl_source: declared
  description: The Secure API from Coincover — 1 operation(s) for secure.
  name: Coincover Secure API
  slug: coincover-secure-api
- baseURL: https://orchestrator.control.coincover.com
  baseurl_source: declared
  description: Start, check, and simulate biometric identity verification.
  name: Coincover Verification API
  slug: coincover-verification-api
artifact_total: 36
common:
- group: agent
  href: https://artifacts.apis.io/coincover/agentic-access/coincover-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coincover-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/coincover/errors/coincover-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coincover-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/coincover/authentication/coincover-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coincover-authentication.yml
- group: design
  href: https://artifacts.apis.io/coincover/rules/coincover-rules.yml
  title: ''
  type: Spectral
  url: rules/coincover-rules.yml
- group: design
  href: https://artifacts.apis.io/coincover/json-ld/coincover-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coincover-context.jsonld
- group: design
  href: https://artifacts.apis.io/coincover/vocabulary/coincover-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coincover-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/coincover/data-model/coincover-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coincover-data-model.yml
- group: operate
  href: https://artifacts.apis.io/coincover/changelog/coincover-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/coincover-changelog.yml
- group: design
  href: https://artifacts.apis.io/coincover/conformance/coincover-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coincover-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coincover/llms/coincover-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coincover-llms.txt
- group: other
  href: https://artifacts.apis.io/coincover/a2a/coincover-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/coincover-a2a.yml
- group: agent
  href: https://artifacts.apis.io/coincover/well-known/coincover-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coincover-well-known.yml
- group: other
  href: https://artifacts.apis.io/coincover/hosts/coincover-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coincover-hosts.yml
- group: other
  href: https://artifacts.apis.io/coincover/vendors/coincover-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coincover-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coincover.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coincover.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.coincover.com/press
- group: docs
  title: ''
  type: APIReference
  url: https://developer.coincover.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coincover
- group: auth
  href: https://artifacts.apis.io/coincover/security/coincover-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coincover-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coincover.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.coincover.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coincover.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.coincover.com/
- group: company
  title: ''
  type: Blog
  url: https://www.coincover.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.coincover.com/contact
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://developer.coincover.com/mcp
  - status: 403
    url: https://www.coincover.com/mcp
  - status: 200
    url: https://www.coincover.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: CoinCover provides digital asset recovery and security services for institutions and retail users. It offers products such as CoinCover Protect, CoinCover Recover, and specialized solutions for exchanges, on‑ramps, custodians, and DeFi platforms. The company focuses on preventing loss of crypto wallets, mitigating cyber threats, and delivering compliance‑ready recovery infrastructure, backed by a Trust Center and extensive resources like guides, playbooks, and a developer portal.
image: https://www.coincover.com/hubfs/CC%20Meta%20Image.png
json_schemas:
- name: AssignKeyRequest
  property_count: 6
  slug: coincover-assign-key-request
- name: AssignKeyResponse
  property_count: 8
  slug: coincover-assign-key-response
- name: BackupRecoverRequest
  property_count: 3
  slug: coincover-backup-recover-request
- name: BackupStoreRequest
  property_count: 5
  slug: coincover-backup-store-request
- name: BackupStoreResponse
  property_count: 3
  slug: coincover-backup-store-response
- name: GetV1PartnerKeysResponse
  property_count: 8
  slug: coincover-get-v1-partner-keys-response
- name: KeyGenerateRequest
  property_count: 3
  slug: coincover-key-generate-request
- name: KeyGenerateResponse
  property_count: 5
  slug: coincover-key-generate-response
- name: PartnerAssignKeyRequest
  property_count: 6
  slug: coincover-partner-assign-key-request
- name: PartnerAssignKeyResponse
  property_count: 8
  slug: coincover-partner-assign-key-response
- name: PartnerSecureDataRequest
  property_count: 5
  slug: coincover-partner-secure-data-request
- name: PartnerSecureFileRequest
  property_count: 3
  slug: coincover-partner-secure-file-request
- name: PostV1KeyGenerateResponse
  property_count: 5
  slug: coincover-post-v1-key-generate-response
- name: PostV1PartnerKeysRequest
  property_count: 10
  slug: coincover-post-v1-partner-keys-request
- name: PostV1PartnerKeysResponse
  property_count: 5
  slug: coincover-post-v1-partner-keys-response
- name: PostV1PartnerSecureSecureidRequest
  property_count: 8
  slug: coincover-post-v1-partner-secure-secureid-request
- name: PostV1SecureSecureidRequest
  property_count: 2
  slug: coincover-post-v1-secure-secureid-request
- name: SecureDataRequest
  property_count: 5
  slug: coincover-secure-data-request
- name: SecureDataResponse
  property_count: 5
  slug: coincover-secure-data-response
- name: SecureFileRequest
  property_count: 3
  slug: coincover-secure-file-request
- name: SecureFileResponse
  property_count: 3
  slug: coincover-secure-file-response
- name: VerificationSimulateRequest
  property_count: 2
  slug: coincover-verification-simulate-request
jsonld:
- class_count: 14
  name: Coincover Context
  property_count: 32
  slug: coincover-context
layout: provider
modified: '2026-10-09'
name: Coincover
nav: Providers
network: true
overview: 'Coincover publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Backup API, Backups API, Key API, and 6 more. Tagged areas include Company, Cryptocurrency, Security, Recovery, and Fintech.


  The Coincover catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coincover''s developer surface includes authentication, changelog, API reference, documentation, engineering blog, support, and 20 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Coincover API Rules
  rule_count: 52
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 5
  slug: coincover-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 14.5
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 28.6
    discoverability: 79.5
    operational_transparency: 18.4
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 87.5
      total: 8
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/coincover/coincover-2026-11-03T124813.png
security:
- kind: authentication
  name: Coincover Authentication
  slug: coincover-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Coincover Domain Security
  slug: coincover-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coincover
tags:
- Company
- Cryptocurrency
- Security
- Recovery
- Fintech
website: https://www.coincover.com
---
