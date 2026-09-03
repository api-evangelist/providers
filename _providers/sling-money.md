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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://morsemoney.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avianlabs
- group: company
  title: ''
  type: Blog
  url: https://morsemoney.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.morsemoney.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.morsemoney.com
- group: commercial
  title: ''
  type: Pricing
  url: https://morsemoney.com/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://morsemoney.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://morsemoney.com/legal/privacypolicy-cookienotice
- group: auth
  title: ''
  type: Compliance
  url: https://morsemoney.com/legal/regulatory-compliance
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sling-money-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sling-money-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sling-money-llms.txt
- group: auth
  title: ''
  type: Security
  url: https://morsemoney.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sling-money-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sling-money-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sling-money-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sling-money-conformance.yml
created: '2026-07-17'
description: Sling Money — now operating as Morse, built by Avian Labs — is a consumer stablecoin-based global money-transfer app that lets people receive, hold, move, spend, send, and invest across 150+ countries and 40+ currencies from a single mobile app. Transfers settle on the Solana blockchain using regulated stablecoins (Paxos USDP, Circle EURC/USDC), and users can spend anywhere with a Visa card issued via Lead Bank. Avian Labs is MiCAR CASP-authorized by the AFM in the Netherlands (registration 41000005), a FinCEN-registered US Money Services Business (31000327638265), NMLS-registered (ID 2639252), and ISO/IEC 27001:2022 certified. Morse is a consumer fintech product and does not currently publish a public developer API, SDKs, or API documentation; this profile captures its identity, legal, security, and compliance surface.
image: https://morsemoney.com/og-default.png
layout: provider
modified: '2026-07-21'
name: Sling Money
nav: Providers
network: true
overview: 'Sling Money is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Stablecoins, Payments, and Money Transfer.


  Sling Money''s developer surface includes engineering blog, support, pricing, and 14 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 24.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sling-money/refs/heads/main/screenshots/sling-money-2026-09-02T155844.png
security:
- kind: domain-security
  name: Sling Money Domain Security
  slug: sling-money-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sling Money Vulnerability Disclosure
  slug: sling-money-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Sling Money Trust Center
  slug: sling-money-trust-center
  summary_line: ISO/IEC 27001:2022
slug: sling-money
tags:
- Company
- Crypto
- Stablecoins
- Payments
- Money Transfer
- Remittance
- Fintech
- Solana
- Consumer
website: https://morsemoney.com
---
