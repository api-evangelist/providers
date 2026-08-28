---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Public REST API used alongside the Ramp Instant widget. Exposes available on-ramp assets and prices, off-ramp assets and prices, supported fiat currencies, payment methods, payout methods, on-ramp pur
  name: Ramp Network Host API
  slug: ramp-network-host-api
- description: Client-side integration surface for Ramp Network. The Ramp Instant SDK renders the Ramp widget in overlay, embedded, hosted, mobile or auto variants and emits a typed event stream (WIDGET_CLOSE, WIDGE
  name: Ramp Instant SDK and Widget
  slug: ramp-network-instant-sdk
artifact_total: 9
asyncapis:
- description: ''
  name: Ramp Network Webhooks
  slug: ramp-network-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ramp-network-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://rampnetwork.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rampnetwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rampnetwork.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rampnetwork.com/rest-api-v3-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rampnetwork.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.rampnetwork.com/en/
- group: company
  title: ''
  type: Blog
  url: https://rampnetwork.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RampNetwork
- group: commercial
  title: ''
  type: Pricing
  url: https://rampnetwork.com/pricing-policy
- group: start
  title: ''
  type: SignUp
  url: https://rampnetwork.com/contact-sales
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rampnetwork.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rampnetwork.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/ramp-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ramp-network-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ramp-network-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ramp-network-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ramp-network-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ramp-network-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ramp-network-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/ramp-network-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/ramp-network-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ramp-network-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ramp-network-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ramp-network-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ramp-network-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ramp-network-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ramp-network-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ramp-network-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/ramp-network-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ramp-network-llms.txt
created: '2026-08-26'
description: Ramp Network (Ramp Swaps Ltd) is a London-headquartered fiat-to-crypto on-ramp and off-ramp provider that lets wallets, dApps, exchanges and consumer apps embed crypto purchase, sale and swap flows without becoming a regulated money-services business themselves. Integrators embed the Ramp Instant widget (overlay, embedded, hosted or auto variant) via the TypeScript/JavaScript SDK or the native Android, iOS, React Native and Flutter SDKs, and drive it from a public REST "Host API" at https://api.rampnetwork.com/api that exposes available on-ramp and off-ramp assets with live prices, supported fiat currencies, payment methods, payout methods, purchase and off-ramp sale quotations, and purchase/sale status lookup. Transaction lifecycle is delivered back to the integrator over ECDSA-signed webhooks and SDK events. Ramp Network is registered with the UK FCA as a cryptoasset firm, authorised as a Crypto Asset Service Provider by the Central Bank of Ireland, registered as an MSB with
  FinCEN, and holds SOC 2 Type 1 certification.
image: https://cdn.prod.website-files.com/63fe1b7ead2cd2d5e0af02e7/6a71d2700c40d60ae5214375_faviconwhite.png
layout: provider
modified: '2026-08-26'
name: Ramp Network
nav: Providers
network: true
overview: 'Ramp Network publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Payments, FinTech, On-Ramp, and Off-Ramp.


  The Ramp Network catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ramp Network''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Ramp Network Plans Pricing
  plan_count: 0
  slug: ramp-network-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Ramp Network Rate Limits
  slug: ramp-network-rate-limits
score:
  band: developing
  composite: 52.4
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Ramp Network Authentication
  slug: ramp-network-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Ramp Network Domain Security
  slug: ramp-network-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ramp Network Vulnerability Disclosure
  slug: ramp-network-vulnerability-disclosure
  summary_line: Intigriti
- kind: trust-center
  name: Ramp Network Trust Center
  slug: ramp-network-trust-center
  summary_line: SOC 2 Type 1, GDPR, SOC 2 / ISO 27001
slug: ramp-network
tags:
- Cryptocurrency
- Payments
- FinTech
- On-Ramp
- Off-Ramp
- Blockchain
- Web3
- Wallets
- Digital Assets
- Compliance
- Embedded Finance
website: https://rampnetwork.com
---
