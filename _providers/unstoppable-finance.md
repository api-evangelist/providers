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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.iron.xyz/api
  baseurl_source: declared
  description: Wallet and bank account registration Every wallet address that interacts with Iron must be registered (linked) to a customer **before** it can be used in any flow — onramp, offramp, or swap. This is a
  name: Unstoppable Finance (Iron) Addresses API
  slug: unstoppable-finance-addresses-api
- baseURL: https://api.iron.xyz/api
  baseurl_source: declared
  description: Operations on Autoramp
  name: Unstoppable Finance (Iron) Autoramp API
  slug: unstoppable-finance-autoramp-api
- baseURL: https://api.iron.xyz/api
  baseurl_source: declared
  description: Operations on Currencies
  name: Unstoppable Finance (Iron) Currencies API
  slug: unstoppable-finance-currencies-api
- baseURL: https://api.iron.xyz/api
  baseurl_source: declared
  description: Operations on Customers
  name: Unstoppable Finance (Iron) Customer API
  slug: unstoppable-finance-customer-api
- baseURL: https://api.iron.xyz/api
  baseurl_source: declared
  description: Operations on Exchange Rate
  name: Unstoppable Finance (Iron) ExchangeRate API
  slug: unstoppable-finance-exchangerate-api
- baseURL: https://api.iron.xyz/api
  baseurl_source: declared
  description: Operations on Fee Profiles
  name: Unstoppable Finance (Iron) FeeProfiles API
  slug: unstoppable-finance-feeprofiles-api
- baseURL: https://api.iron.xyz/api
  baseurl_source: declared
  description: Operations for Sandbox Testing
  name: Unstoppable Finance (Iron) Sandbox API
  slug: unstoppable-finance-sandbox-api
- baseURL: https://api.iron.xyz/api
  baseurl_source: declared
  description: Operations on Terms and Conditions
  name: Unstoppable Finance (Iron) TermsAndConditions API
  slug: unstoppable-finance-termsandconditions-api
- baseURL: https://api.iron.xyz/api
  baseurl_source: declared
  description: Operations on Webhooks
  name: Unstoppable Finance (Iron) Webhooks API
  slug: unstoppable-finance-webhooks-api
artifact_total: 33
asyncapis:
- description: ''
  name: Unstoppable Finance Webhooks
  slug: unstoppable-finance-webhooks
collections:
- collection_type: postman
  name: Iron API - Sandbox Addresses API
  slug: postman-unstoppable-finance-addresses-api
- collection_type: postman
  name: Iron API - Sandbox Addresses Autoramp API
  slug: postman-unstoppable-finance-autoramp-api
- collection_type: postman
  name: Iron API - Sandbox Addresses Currencies API
  slug: postman-unstoppable-finance-currencies-api
- collection_type: postman
  name: Iron API - Sandbox Addresses Customer API
  slug: postman-unstoppable-finance-customer-api
- collection_type: postman
  name: Iron API - Sandbox Addresses ExchangeRate API
  slug: postman-unstoppable-finance-exchangerate-api
- collection_type: postman
  name: Iron API - Sandbox Addresses FeeProfiles API
  slug: postman-unstoppable-finance-feeprofiles-api
- collection_type: postman
  name: Iron API - Addresses Sandbox API
  slug: postman-unstoppable-finance-sandbox-api
- collection_type: postman
  name: Iron API - Sandbox Addresses TermsAndConditions API
  slug: postman-unstoppable-finance-termsandconditions-api
- collection_type: postman
  name: Iron API - Sandbox Addresses Webhooks API
  slug: postman-unstoppable-finance-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Iron API - Sandbox Addresses API
  slug: open-unstoppable-finance-addresses-api
- collection_type: open
  name: Iron API - Sandbox Addresses Autoramp API
  slug: open-unstoppable-finance-autoramp-api
- collection_type: open
  name: Iron API - Sandbox Addresses Currencies API
  slug: open-unstoppable-finance-currencies-api
- collection_type: open
  name: Iron API - Sandbox Addresses Customer API
  slug: open-unstoppable-finance-customer-api
- collection_type: open
  name: Iron API - Sandbox Addresses ExchangeRate API
  slug: open-unstoppable-finance-exchangerate-api
- collection_type: open
  name: Iron API - Sandbox Addresses FeeProfiles API
  slug: open-unstoppable-finance-feeprofiles-api
- collection_type: open
  name: Iron API - Addresses Sandbox API
  slug: open-unstoppable-finance-sandbox-api
- collection_type: open
  name: Iron API - Sandbox Addresses TermsAndConditions API
  slug: open-unstoppable-finance-termsandconditions-api
- collection_type: open
  name: Iron API - Sandbox Addresses Webhooks API
  slug: open-unstoppable-finance-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/unstoppable-finance-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/unstoppable-finance-iron/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unstoppable-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iron.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.iron.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iron.xyz/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iron.xyz/onboarding
- group: auth
  title: ''
  type: Authentication
  url: authentication/unstoppable-finance-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unstoppable-finance-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unstoppable-finance-webhooks.yml
- group: build
  title: ''
  type: CLI
  url: cli/unstoppable-finance-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/unstoppable-finance-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unstoppable-finance-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/unstoppable-finance-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unstoppable-finance-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/unstoppable-finance-iron-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/unstoppable-finance-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://iron.xyz/compliance
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unstoppable-finance-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unstoppable-finance-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iron.xyz
- group: design
  title: ''
  type: Conventions
  url: conventions/unstoppable-finance-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/unstoppable-finance-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unstoppable-finance-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unstoppable-finance-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unstoppable-finance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://iron.xyz/security
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.iron.xyz/support
- group: commercial
  title: ''
  type: Pricing
  url: https://iron.xyz/prices
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moonpay.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moonpay.com/legal/privacy_policy
- group: start
  title: ''
  type: Login
  url: https://app.iron.xyz/signin
created: '2026-07-17'
description: Unstoppable Finance is the Berlin fintech behind Iron (iron.xyz), the Stablecoin Payment Network - fiat-to-stablecoin and stablecoin-to-fiat infrastructure for businesses. Founded as Unstoppable Finance GmbH and builder of the Ultimate self-custodial DeFi wallet, the company rebranded to Iron and was acquired by MoonPay in 2025. The Iron API provides onramp, offramp, and swap flows via Autoramps (standing fiat/crypto conversion rules), customer onboarding with tiered KYC/KYB, Travel Rule wallet verification, virtual accounts, fee profiles, exchange rates, stablecoin issuance, and Standard Webhooks event delivery, with a fully simulated sandbox environment.
image: https://framerusercontent.com/images/HAx7iVFXocaeIm27aAOhEsYTyfE.png
layout: provider
modified: '2026-07-21'
name: Unstoppable Finance (Iron)
nav: Providers
network: true
overview: 'Unstoppable Finance (Iron) publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Autoramp API, Currencies API, and 6 more. Tagged areas include Company, Stablecoins, Payments, On-Ramp, and Off-Ramp.


  The Unstoppable Finance (Iron) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unstoppable Finance (Iron)''s developer surface includes documentation, getting-started guide, authentication, sandbox, CLI, support, pricing, and 26 more developer resources.'
random_paper: 13
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 64.1
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 56.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unstoppable-finance/refs/heads/main/screenshots/unstoppable-finance-2026-08-17T082634.png
security:
- kind: authentication
  name: Unstoppable Finance Authentication
  slug: unstoppable-finance-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Unstoppable Finance Domain Security
  slug: unstoppable-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unstoppable Finance Vulnerability Disclosure
  slug: unstoppable-finance-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Unstoppable Finance Trust Center
  slug: unstoppable-finance-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27701, ISO 27018, PCI DSS, CMMC, GDPR
slug: unstoppable-finance
tags:
- Company
- Stablecoins
- Payments
- On-Ramp
- Off-Ramp
- Cryptocurrency
- Banking
- Fintech
- Compliance
website: https://iron.xyz
---
