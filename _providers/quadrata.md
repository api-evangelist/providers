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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'Server-side REST API for Quadrata Passport: login/access-token authentication, ECDSA-signed privacy data requests, on-chain AML wallet screening, and passport attribute queries. Distributed as the @qu'
  name: Quadrata Passport API
  slug: quadrata-passport-api
artifact_total: 4
asyncapis:
- description: ''
  name: Quadrata Webhooks
  slug: quadrata-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://quadrata.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.quadrata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quadrata.com/integration/introduction/introduction-to-quadrata
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.quadrata.com/integration/how-to-integrate/quadrata-sdk/get-started-quickly
- group: docs
  title: ''
  type: APIReference
  url: https://docs.quadrata.com/integration/how-to-integrate/quadrata-sdk/advanced/api-libraries/api-service-libraries
- group: start
  title: ''
  type: SignUp
  url: https://quadrata.com/onboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quadrata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quadrata.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://medium.com/quadrata-network
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/67QgzrymHW
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/QuadrataNetwork
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quadrata-inc/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.quadrata.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/quadrata-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quadrata-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/quadrata-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/quadrata-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/quadrata-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/quadrata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/quadrata-packages.yml
- group: design
  title: ''
  type: Components
  url: components/quadrata-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/quadrata-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quadrata-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quadrata-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quadrata-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/quadrata-sandbox.yml
created: '2026-07-17'
description: Quadrata is a privacy-preserving on-chain identity network for Web3, issuing a non-transferable (soulbound) NFT "Passport" that binds verified identity, compliance and reputation attributes to a user wallet without storing personal data on-chain. Integrators use the Quadrata SDK and REST API to onboard users (KYC), businesses (KYB), and accredited/sophisticated investors, run AML risk and on-chain wallet screening, request consented privacy (PII) data, and query passport attributes on-chain via smart contracts or off-chain via API. Passport attributes include DID (sybil resistance), AML score, COUNTRY, IS_BUSINESS, INVESTOR_STATUS, and Cred Protocol credit score. Supported networks include Ethereum, Polygon, Arbitrum, Optimism, Avalanche, Evmos, and KAVA.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quadrata.png
layout: provider
modified: '2026-07-20'
name: Quadrata
nav: Providers
network: true
overview: 'Quadrata publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Identity, Digital Identity, and KYC.


  The Quadrata catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Quadrata''s developer surface includes documentation, getting-started guide, API reference, signup flow, engineering blog, support, sandbox, and 19 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 40.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quadrata/refs/heads/main/screenshots/quadrata-2026-09-02T152551.png
security:
- kind: authentication
  name: Quadrata Authentication
  slug: quadrata-authentication
  summary_line: apiKey/http-basic/ecdsa-request-signature/jwt-access-token · 4 schemes
- kind: domain-security
  name: Quadrata Domain Security
  slug: quadrata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quadrata
tags:
- Company
- Crypto Web3
- Identity
- Digital Identity
- KYC
- KYB
- AML
- Compliance
- Wallet Screening
- Blockchain
- Web3
- Decentralized Identity
website: https://quadrata.com
---
