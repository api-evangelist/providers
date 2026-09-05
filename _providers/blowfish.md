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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-04'
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
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: Authentication
  url: authentication/blowfish-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blowfish-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blowfish-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blowfish-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blowfish-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/blowfish-scan-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blowfish-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/blowfish-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blowfish-packages.yml
- group: design
  title: ''
  type: Components
  url: components/blowfish-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/blowfish-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blowfish-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blowfish-agentic-access.yml
- group: auth
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
overview: 'Blowfish publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Download blocklist API, Scan domain API, Scan message API, and 1 more. Tagged areas include Company, Security, Web3, Blockchain, and Wallets.


  Blowfish''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, pricing, support, and 20 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 8.3
    contract_quality: 59.2
    developer_ergonomics: 41.1
    discoverability: 75.9
    governance: 8.3
    operational_transparency: 2.6
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blowfish/refs/heads/main/screenshots/blowfish-2026-07-25T203426.png
security:
- kind: authentication
  name: Blowfish Authentication
  slug: blowfish-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blowfish Domain Security
  slug: blowfish-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
