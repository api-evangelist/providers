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
    agent_skills: derived
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Blowfish Agentic Access
  operation_count: 5
  slug: blowfish-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.blowfish.xyz
  baseurl_source: declared
  description: Endpoints related to downloading blocklists
  name: Blowfish Download blocklist API
  slug: blowfish-download-blocklist-api
- baseURL: https://api.blowfish.xyz
  baseurl_source: declared
  description: Endpoints related to scanning dApp domains
  name: Blowfish Scan domain API
  slug: blowfish-scan-domain-api
- baseURL: https://api.blowfish.xyz
  baseurl_source: declared
  description: Endpoints related to scanning blockchain messages
  name: Blowfish Scan message API
  slug: blowfish-scan-message-api
- baseURL: https://api.blowfish.xyz
  baseurl_source: declared
  description: Endpoints related to scanning blockchain transactions
  name: Blowfish Scan transaction API
  slug: blowfish-scan-transaction-api
artifact_total: 15
collections:
- collection_type: open
  name: API reference Download blocklist API
  slug: open-blowfish-download-blocklist-api
- collection_type: open
  name: API reference Download blocklist Scan domain API
  slug: open-blowfish-scan-domain-api
- collection_type: open
  name: API reference Download blocklist Scan message API
  slug: open-blowfish-scan-message-api
- collection_type: open
  name: API reference Download blocklist Scan transaction API
  slug: open-blowfish-scan-transaction-api
common:
- group: other
  href: https://artifacts.apis.io/blowfish/capabilities/blowfish-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/blowfish-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/blowfish/overlays/blowfish-v20230308-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/blowfish-v20230308-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blowfish.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blowfish.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blowfish.xyz/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blowfish.xyz/docs/introduction
- group: start
  title: ''
  type: SignUp
  url: https://portal.blowfish.xyz/
- group: company
  title: ''
  type: Blog
  url: https://blog.blowfish.xyz
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blowfishxyz
- group: commercial
  title: ''
  type: Pricing
  url: https://blowfish.xyz
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://extension.blowfish.xyz/privacy
- group: operate
  title: ''
  type: Support
  url: https://form.typeform.com/to/BHue5Hg0
- group: auth
  href: https://artifacts.apis.io/blowfish/authentication/blowfish-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blowfish-authentication.yml
- group: design
  href: https://artifacts.apis.io/blowfish/conventions/blowfish-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blowfish-conventions.yml
- group: design
  href: https://artifacts.apis.io/blowfish/errors/blowfish-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blowfish-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blowfish/lifecycle/blowfish-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/blowfish-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/blowfish/conformance/blowfish-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blowfish-conformance.yml
- group: design
  href: https://artifacts.apis.io/blowfish/vocabulary/blowfish-scan-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blowfish-scan-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blowfish/data-model/blowfish-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blowfish-data-model.yml
- group: build
  href: https://artifacts.apis.io/blowfish/packages/blowfish-packages.yml
  title: ''
  type: Packages
  url: packages/blowfish-packages.yml
- group: build
  href: https://artifacts.apis.io/blowfish/packages/blowfish-packages.yml
  title: ''
  type: SDKs
  url: packages/blowfish-packages.yml
- group: design
  href: https://artifacts.apis.io/blowfish/components/blowfish-components.yml
  title: ''
  type: Components
  url: components/blowfish-components.yml
- group: agent
  href: https://artifacts.apis.io/blowfish/mcp/blowfish-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/blowfish-mcp.yml
- group: agent
  href: https://artifacts.apis.io/blowfish/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/blowfish/llms/blowfish-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blowfish-llms.txt
- group: agent
  href: https://artifacts.apis.io/blowfish/agentic-access/blowfish-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blowfish-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/blowfish/security/blowfish-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blowfish-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blowfish.xyz
created: '2026-07-17'
description: Blowfish is a proactive web3 security platform that scans EVM and Solana transactions, EVM messages, and dApp domains before a user signs, returning a recommended action (NONE, WARN, or BLOCK), severity-sorted warnings, and human-readable transaction simulation results. Its Scan API and downloadable domain blocklist help wallets and dApps protect users from scams, malicious token approvals, and phishing across 10+ blockchains. Backed by Paradigm.
image: https://raw.githubusercontent.com/blowfishxyz/blowfish-openapi-specs/HEAD/blowfish.png
layout: provider
modified: '2026-07-18'
name: Blowfish
nav: Providers
network: true
overview: 'Blowfish publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Download blocklist API, Scan domain API, Scan message API, and 1 more. Tagged areas include Company, Security, Web3, Blockchain, and Wallets.


  The Blowfish catalog on APIs.io includes 1 Spectral governance ruleset.


  Blowfish''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, pricing, support, and 21 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Blowfish API Rules
  rule_count: 67
  severity_counts:
    error: 65
    hint: 0
    info: 1
    warn: 1
  slug: blowfish-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 59.2
    developer_ergonomics: 41.1
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/blowfish/blowfish-2026-07-25T203426.png
security:
- kind: authentication
  name: Blowfish Authentication
  slug: blowfish-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blowfish Domain Security
  slug: blowfish-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Scan a dApp domain for safety
  slug: blowfish-scan-domain
- name: Scan an EVM transaction before signing
  slug: blowfish-scan-evm-transaction
- name: Scan Solana transactions before signing
  slug: blowfish-scan-solana-transaction
slug: blowfish
tags:
- Company
- Security
- Web3
- Blockchain
- Wallets
- Transaction Scanning
- Fraud Prevention
- Cryptocurrency
website: https://blowfish.xyz
---
