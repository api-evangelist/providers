---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Bastion''s REST API for regulated stablecoin infrastructure: create and manage custodial wallets, issue and convert stablecoins, run on/off-ramps, and move digital assets, with built-in KYC/AML complia'
  name: Bastion API
  slug: bastion-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bastion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/bastion-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bastion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bastion.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bastion.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bastion.com/recipes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bastion.com/
- group: auth
  title: ''
  type: Compliance
  url: https://bastion.com/disclosures
- group: auth
  title: ''
  type: TrustCenter
  url: https://bastion.com/subprocessor-list
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bastion.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bastion.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://bastion.com/request-demo
- group: company
  title: ''
  type: Careers
  url: https://bastion.com/careers
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Bastion
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bastionplatforms
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bastion-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bastion-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bastion-conformance.yml
created: '2026-07-17'
description: Bastion is a full-stack, regulated stablecoin infrastructure platform for enterprises and financial institutions. Founded in 2023 and based in Campbell, California by former a16z crypto leaders, Bastion lets companies securely issue, custody, move, and convert USD-backed stablecoins under Bastion's licenses or their own. Its API-first product suite spans a Regulated Wallet API (create unlimited custodial wallets with Cloud HSM and enclave-based key management), stablecoin issuance, on/off-ramps, and payments, plus Compliance-as-a-Service that handles KYC and AML. Bastion Platforms Trust Company, LLC is chartered as a limited purpose trust company by the New York State Department of Financial Services, and Bastion Platforms US, LLC is a registered MSB (NMLS ID 2523302) with broad money-transmitter-license coverage across the United States. Bastion has raised over $40M from a16z crypto, Coinbase Ventures, and others.
image: https://framerusercontent.com/images/pTrMs5MJstsls9S7X45qlr99Pc.png
layout: provider
modified: '2026-07-18'
name: Bastion
nav: Providers
network: true
overview: 'Bastion publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Stablecoins, Payments, Wallets, and Custody.


  Bastion''s developer surface includes documentation, API reference, getting-started guide, signup flow, and 14 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 30.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bastion/refs/heads/main/screenshots/bastion-2026-07-25T202432.png
security:
- kind: domain-security
  name: Bastion Domain Security
  slug: bastion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bastion Vulnerability Disclosure
  slug: bastion-vulnerability-disclosure
  summary_line: contact published
slug: bastion
tags:
- Company
- Stablecoins
- Payments
- Wallets
- Custody
- Web3
- Compliance
- Crypto Infrastructure
- Financial-Services
- On/Off-Ramps
website: https://bastion.com/
---
