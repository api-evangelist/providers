---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 43.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Zkme Agentic Access
  operation_count: 14
  slug: zkme-agentic-access
  summary_line: 14 operations · 14 acting
api_count: 5
apis:
- description: Access-token issuance for SDK integration
  name: zkMe Auth API
  slug: zkme-auth-api
- description: Know-Your-Transaction wallet-address and transaction risk screening
  name: zkMe KYT API
  slug: zkme-kyt-api
- description: Business entity and UBO verification status
  name: zkMe zkKYB API
  slug: zkme-zkkyb-api
- description: Customer identity verification results and proofs
  name: zkMe zkKYC API
  slug: zkme-zkkyc-api
- description: Open banking / accredited-investor (proof of accreditation)
  name: zkMe zkOBS API
  slug: zkme-zkobs-api
artifact_total: 10
common:
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


  zkMe''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, and 12 more developer resources.'
random_paper: 31
rate_limits:
- limit_count: 0
  name: Zkme Rate Limits
  slug: zkme-rate-limits
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 47.6
    developer_ergonomics: 52.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
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
