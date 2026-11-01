---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Insumermodel Com Agentic Access
  operation_count: 46
  slug: insumermodel-com-agentic-access
  summary_line: 46 operations · 30 acting
api_count: 1
apis:
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: The same discount decision returned in ACP (OpenAI/Stripe) and UCP (Google) formats for AI agent commerce flows.
  name: insumermodel-com Agent Commerce Protocols API
  slug: insumermodel-com-agent-commerce-protocols-api
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: 'How software gets and keeps access with no human in the loop. Buy a key or top up credits with USDC; the transaction sender wallet becomes the key identity, and the payment, signed by that wallet, is '
  name: insumermodel-com Agent Onboarding API
  slug: insumermodel-com-agent-onboarding-api
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: Turn a condition verdict into a price. Calculate a discount, create a signed code (INSR-XXXXX, valid 30 minutes), validate that code from a merchant backend, and confirm stablecoin payment.
  name: insumermodel-com Discounts & Codes API
  slug: insumermodel-com-discounts-codes-api
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: Browse merchants, tokens, and NFT collections in the public directory.
  name: insumermodel-com Discovery API
  slug: insumermodel-com-discovery-api
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: Key lifecycle and billing. Free email signup, on-chain purchase, card subscriptions, credit balance and top-ups, account lookup, billing portal.
  name: insumermodel-com Keys & Billing API
  slug: insumermodel-com-keys-billing-api
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: Create and administer a merchant programmatically. Token and NFT tiers, discount settings, domain verification, directory publishing, credits, ownership claims, and registry submissions. The API key t
  name: insumermodel-com Merchant Setup API
  slug: insumermodel-com-merchant-setup-api
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: Service health and chain-support requests.
  name: insumermodel-com Platform API
  slug: insumermodel-com-platform-api
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: 'In-person recognition. Partner-operated scanner PINs, login-less scanner sessions, and pass verification. The partner builds only UI; signing stays inside the primitive and is never exposed as an API '
  name: insumermodel-com Point of Sale API
  slug: insumermodel-com-point-of-sale-api
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: Structured, signed fact profiles for a wallet, organized by dimension, singly or in batches. No score, no opinion, just cryptographically verifiable evidence. Reachable with an API key, with wallet-si
  name: insumermodel-com Trust Fact Profiles API
  slug: insumermodel-com-trust-fact-profiles-api
- baseURL: https://api.insumermodel.com
  baseurl_source: declared
  description: The primitive. Read wallet state, evaluate it against caller-supplied conditions, return a signed boolean. Conditions in, signed attestations out. Balances are never exposed. This group also carries t
  name: insumermodel-com Wallet Auth API
  slug: insumermodel-com-wallet-auth-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/insumermodel-com/agentic-access/insumermodel-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/insumermodel-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/insumermodel-com/rules/insumermodel-com-rules.yml
  title: ''
  type: Spectral
  url: rules/insumermodel-com-rules.yml
- group: design
  href: https://artifacts.apis.io/insumermodel-com/json-ld/insumermodel-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/insumermodel-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/insumermodel-com/vocabulary/insumermodel-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/insumermodel-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/insumermodel-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/insumermodel-com/data-model/insumermodel-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/insumermodel-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/insumermodel-com/security/insumermodel-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/insumermodel-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/insumermodel-com/errors/insumermodel-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/insumermodel-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/insumermodel-com/conformance/insumermodel-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/insumermodel-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/insumermodel-com/llms/insumermodel-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/insumermodel-com-llms.txt
- group: build
  href: https://artifacts.apis.io/insumermodel-com/mcp/insumermodel-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/insumermodel-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/insumermodel-com/mcp/insumermodel-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/insumermodel-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/insumermodel-com/well-known/insumermodel-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/insumermodel-com-security.txt
- group: auth
  href: https://artifacts.apis.io/insumermodel-com/well-known/insumermodel-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/insumermodel-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/insumermodel-com/well-known/insumermodel-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/insumermodel-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/insumermodel-com/hosts/insumermodel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insumermodel-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/insumermodel-com/vendors/insumermodel-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/insumermodel-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/insumermodel-com/packages/insumermodel-com-packages.yml
  title: ''
  type: SDKs
  url: packages/insumermodel-com-packages.yml
- group: build
  href: https://artifacts.apis.io/insumermodel-com/packages/insumermodel-com-packages.yml
  title: ''
  type: Packages
  url: packages/insumermodel-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://insumermodel.com/developers/changelog/
- group: company
  title: ''
  type: Blog
  url: https://insumermodel.com/blog/
- group: auth
  href: https://artifacts.apis.io/insumermodel-com/authentication/insumermodel-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/insumermodel-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/insumermodel-com/security/insumermodel-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/insumermodel-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/insumermodel-com/security/insumermodel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insumermodel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://insumermodel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://insumermodel.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://insumermodel.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://insumermodel.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://insumermodel.com/developers/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://insumermodel.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://insumermodel.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://insumermodel.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insumermodel.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/insumerapi
created: '2026-10-30'
description: InsumerAPI, built by The Insumer Model™, provides condition‑based wallet authentication for developers and AI agents across 37 blockchain networks. By sending a wallet address and a programmable condition, callers receive an ECDSA‑signed boolean attestation that can be verified offline. The service never exposes wallet balances and supports optional Merkle proofs for on‑chain verification. It offers endpoints for token balance checks, NFT ownership, EAS attestations, custom view calls, and compliance templates, all secured without shared secrets or identity‑first credentials. Products are available for stores, clubs, and communities, and the platform is licensed to partners such as Skye Meta.
image: https://insumermodel.com/images/homepage-og.webp?v=6
json_schemas:
- name: ChainId
  property_count: 0
  slug: insumermodel-com-chain-id
- name: Condition
  property_count: 23
  slug: insumermodel-com-condition
- name: NftConfig
  property_count: 7
  slug: insumermodel-com-nft-config
- name: SenderSignature
  property_count: 0
  slug: insumermodel-com-sender-signature
- name: TokenConfig
  property_count: 10
  slug: insumermodel-com-token-config
- name: WalletProof
  property_count: 2
  slug: insumermodel-com-wallet-proof
jsonld:
- class_count: 22
  name: Insumermodel Com Context
  property_count: 125
  slug: insumermodel-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.insumermodel.com.
  name: insumermodel-com MCP Server
  slug: insumermodel-com-mcp-yml
modified: '2026-10-30'
name: insumermodel-com
nav: Providers
network: true
overview: 'insumermodel-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Commerce Protocols API, Agent Onboarding API, Discounts & Codes API, and 7 more. Tagged areas include Wallet Auth, Blockchain, AI Agents, Condition-Based Access, and Crypto.


  The insumermodel-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  insumermodel-com''s developer surface includes changelog, engineering blog, authentication, documentation, API reference, getting-started guide, support, and 27 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: insumermodel-com API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: insumermodel-com-rules
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 64.3
    developer_ergonomics: 70.7
    discoverability: 65.0
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Insumermodel Com Authentication
  slug: insumermodel-com-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Insumermodel Com Domain Security
  slug: insumermodel-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Insumermodel Com Vulnerability Disclosure
  slug: insumermodel-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: insumermodel-com-main
  slug: insumermodel-com-main-skill
slug: insumermodel-com
tags:
- Wallet Auth
- Blockchain
- AI Agents
- Condition-Based Access
- Crypto
- Developer Tools
website: https://insumermodel.com/
---
