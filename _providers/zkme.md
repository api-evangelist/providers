---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Zkme Agentic Access
  operation_count: 14
  slug: zkme-agentic-access
  summary_line: 14 operations · 14 acting
api_count: 1
apis:
- baseURL: https://agw.zk.me
  baseurl_source: declared
  description: Access-token issuance for SDK integration
  name: zkMe Auth API
  slug: zkme-auth-api
- baseURL: https://agw.zk.me
  baseurl_source: declared
  description: Know-Your-Transaction wallet-address and transaction risk screening
  name: zkMe KYT API
  slug: zkme-kyt-api
- baseURL: https://agw.zk.me
  baseurl_source: declared
  description: Business entity and UBO verification status
  name: zkMe zkKYB API
  slug: zkme-zkkyb-api
- baseURL: https://agw.zk.me
  baseurl_source: declared
  description: Customer identity verification results and proofs
  name: zkMe zkKYC API
  slug: zkme-zkkyc-api
- baseURL: https://agw.zk.me
  baseurl_source: declared
  description: Open banking / accredited-investor (proof of accreditation)
  name: zkMe zkOBS API
  slug: zkme-zkobs-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: zkMe Protocol Auth API
  slug: open-zkme-auth-api
- collection_type: open
  name: zkMe Protocol Auth KYT API
  slug: open-zkme-kyt-api
- collection_type: open
  name: zkMe Protocol Auth zkKYB API
  slug: open-zkme-zkkyb-api
- collection_type: open
  name: zkMe Protocol Auth zkKYC API
  slug: open-zkme-zkkyc-api
- collection_type: open
  name: zkMe Protocol Auth zkOBS API
  slug: open-zkme-zkobs-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zkme-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zkme-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zkme-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zkme-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zk.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zk.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zk.me/hub/start/onboarding
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zk.me/hub/start/onboarding/integration/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zk.me/hub/start/onboarding
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zkMeLabs
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.zk.me
- group: operate
  title: ''
  type: Support
  url: https://docs.zk.me
- group: build
  title: ''
  type: Packages
  url: packages/zkme-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zkme-packages.yml
- group: design
  title: ''
  type: Components
  url: components/zkme-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zkme-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zkme-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.zk.me/hub/explore/bounty
created: '2026-07-17'
description: zkMe is a decentralized identity network delivering privacy-preserving compliance for Web3. Using zero-knowledge proofs, self-sovereign identity (SSI) wallets, DID methods and soulbound tokens, zkMe lets applications verify their users and businesses without ever handling raw personal data. Its product suite spans zkKYC (customer identity with sanction, age, citizenship, location and uniqueness/anti-Sybil proofs), zkKYB (business entity and UBO verification), zkOBS (open-banking proof of accredited investor and proof of address), and KYT (on-chain wallet-address and transaction risk screening). Verification runs client-side through embeddable JavaScript and mobile widgets; integrators then query outcomes through the zkMe Open API on agw.zk.me using an AppID + API key pair. zkMe also publishes zkTLS verifier SDKs, DID registry/resolver tooling and smart contracts through its zkMeLabs GitHub org.
image: https://zk.me/favicon.ico
layout: provider
modified: '2026-07-21'
name: zkMe
nav: Providers
network: true
overview: 'zkMe publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, KYT API, zkKYB API, and 2 more. Tagged areas include Company, Crypto Web3, Identity, KYC, and KYB.


  zkMe''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, and 14 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 1
  name: Zkme Rate Limits
  slug: zkme-rate-limits
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 11.9
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zkme/refs/heads/main/screenshots/zkme-2026-09-02T171816.png
security:
- kind: authentication
  name: Zkme Authentication
  slug: zkme-authentication
  summary_line: apiKey/bearerToken · 2 schemes
- kind: domain-security
  name: Zkme Domain Security
  slug: zkme-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zkme Vulnerability Disclosure
  slug: zkme-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: zkme
tags:
- Company
- Crypto Web3
- Identity
- KYC
- KYB
- Compliance
- Zero Knowledge
- Decentralized Identity
- Anti-Sybil
- Transaction Monitoring
website: https://zk.me
---
