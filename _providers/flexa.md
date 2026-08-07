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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Flexa Agentic Access
  operation_count: 8
  slug: flexa-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 4
apis:
- description: Assets encompass all the value that flows through the Flexa platform. In the Flexa API, both national currencies (“fiat“) and digital currencies (“crypto“ or “digital assets“) are returned together in
  name: Flexa Assets API
  slug: flexa-assets-api
- description: Commerce intents offer a versatile way to process digital asset payments from your customers using any sales channel.
  name: Flexa Commerce Intents API
  slug: flexa-commerce-intents-api
- description: Events are created when any of the core resources on the Flexa platform change in a meaningful way, such as when a commerce intent succeeds or a digital asset transaction is requested. Clients subscri
  name: Flexa Events API
  slug: flexa-events-api
- description: Refunds are the only way by which a Flexa payment can be reversed. Refunds are always initiated by the recipient, and can be made for either a partial amount or the full value of the original payment.
  name: Flexa Refunds API
  slug: flexa-refunds-api
artifact_total: 10
asyncapis:
- description: ''
  name: Flexa Events Webhooks
  slug: flexa-events-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flexa-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://flexa.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flexa.co/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flexa.co/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flexa.co/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flexa.co/payments/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.flexa.co/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flexa.co/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flexa.co/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flexa
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flexa-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/flexa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flexa-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flexa-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flexa-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flexa-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flexa-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flexa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://flexa.co/security/bug-bounty-program
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flexa-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flexa-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flexa-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flexa-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flexa-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/flexa-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flexa-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flexa-events-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/flexa-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Flexa is a digital-currency payments network that lets businesses accept crypto and other digital assets from customers anywhere, with instant authorization, fraud-resistant settlement, and automatic conversion into a preferred payout currency so merchants avoid price volatility. The Flexa Payments API is built around the "commerce intent" resource, which represents any attempt to collect a digital-currency payment and tracks requested debits against actual credits; supporting resources include assets, refunds, events, links, brands, and flexcodes. Flexa ships prebuilt mobile UI Components for iOS, Android, and React Native, plus in-person (Point of Sale) and online acceptance options, and a production-grade test mode that uses a valueless ERC-20 "Credit" (CR) token. Flexa is backed by Pantera Capital and supports 99+ digital assets across Ethereum, Bitcoin, Lightning, Solana, and more.
image: https://framerusercontent.com/assets/GHzfAvG7SahlNocEC2Agsubvp0.png
layout: provider
mcp_servers:
- description: ''
  name: flexa-mcp.yml
  slug: flexa-mcpyml
modified: '2026-07-19'
name: Flexa
nav: Providers
network: true
overview: 'Flexa publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Commerce Intents API, Events API, and 1 more. Tagged areas include Company, Crypto, Payments, Digital Currency, and Cryptocurrency.


  The Flexa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flexa''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 23 more developer resources.'
random_paper: 76
score:
  band: developing
  composite: 49.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 72.2
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 49.2
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
    score: 48.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flexa/refs/heads/main/screenshots/flexa-2026-07-25T214746.png
security:
- kind: authentication
  name: Flexa Authentication
  slug: flexa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Flexa Domain Security
  slug: flexa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flexa Vulnerability Disclosure
  slug: flexa-vulnerability-disclosure
  summary_line: contact published
slug: flexa
tags:
- Company
- Crypto
- Payments
- Digital Currency
- Cryptocurrency
- Fintech
- Blockchain
- Merchant Payments
- Web3
website: https://flexa.co/
---
