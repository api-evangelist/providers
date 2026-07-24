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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 63.5
  scored_at: '2026-07-23'
api_count: 12
apis:
- description: 3D Secure is a security protocol designed to prevent fraud in online card transactions. It adds an additional layer of authentication during the payment process.
  name: Evervault 3D Secure API
  slug: evervault-3d-secure-api
- description: The Acquirer API allows you to enroll Acquirer details with Card Networks to enable use of other payment APIs such as [3D Secure](#3d-secure).
  name: Evervault Acquirers API
  slug: evervault-acquirers-api
- description: If your account has access to [Card Account Updater](/cards/card-account-updater) you can use the Card Account Updater API to register cards for automatic updates. If an update is available for a card
  name: Evervault Card Account Updates API
  slug: evervault-card-account-updates-api
- description: Client-Side Tokens are short-lived tokens that can be used to perform actions from your frontend applications.
  name: Evervault Client Tokens API
  slug: evervault-client-tokens-api
- description: The Core API from Evervault — 9 operation(s) for core.
  name: Evervault Core API
  slug: evervault-core-api
- description: Evervault [Functions](/functions) are secure serverless functions which allow you to process data encrypted by Evervault products. When you pass encrypted data to a Function, it is automatically decry
  name: Evervault Functions API
  slug: evervault-functions-api
- description: The Evervault API provides several endpoints which can be used to retrieve additional information for cards and bin ranges. This can be used for tasks such as fraud detection and payment routing.
  name: Evervault Insights API
  slug: evervault-insights-api
- description: The Merchants API from Evervault — 2 operation(s) for merchants.
  name: Evervault Merchants API
  slug: evervault-merchants-api
- description: The Network Tokens API from Evervault — 5 operation(s) for network tokens.
  name: Evervault Network Tokens API
  slug: evervault-network-tokens-api
- description: The Payments API from Evervault — 17 operation(s) for payments.
  name: Evervault Payments API
  slug: evervault-payments-api
- description: Relay is a network proxy that can be configured to encrypt or decrypt sensitive data as it passes between a client and a destination server. Relay can be used with your own API or with third-party API
  name: Evervault Relays API
  slug: evervault-relays-api
- description: The Webhooks API from Evervault — 2 operation(s) for webhooks.
  name: Evervault Webhooks API
  slug: evervault-webhooks-api
artifact_total: 17
asyncapis:
- description: ''
  name: Evervault Webhooks
  slug: evervault-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.evervault.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evervault.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.evervault.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.evervault.com/core-concepts
- group: company
  title: ''
  type: Blog
  url: https://evervault.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evervault
- group: commercial
  title: ''
  type: Pricing
  url: https://evervault.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.evervault.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evervault.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evervault.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.evervault.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://evervault.com/changelog
- group: auth
  title: ''
  type: Authentication
  url: authentication/evervault-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/evervault-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/evervault-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/evervault-cli.yml
- group: design
  title: ''
  type: Components
  url: components/evervault-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/evervault-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evervault-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evervault-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/evervault-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/evervault-security.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/evervault-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/evervault-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evervault-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/evervault-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evervault-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evervault-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.evervault.com/compliance/pci-compliance
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evervault-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/evervault-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://evervault.com/.well-known/security.txt
- group: company
  title: ''
  type: Website
  url: https://evervault.com
created: '2026-07-17'
description: 'Evervault is a data-security and payments-infrastructure platform that lets developers encrypt, tokenize, and process sensitive data - especially cardholder data - without it touching their own infrastructure. Its model stores encryption keys on Evervault''s side while customers hold the ciphertext, reducing breach scope. Core products include Relay (an encrypting/decrypting proxy), Functions (secure serverless runtimes), Enclaves (AWS Nitro Enclave workloads), UI Components for PCI-compliant card collection, plus payments tooling: network tokens, 3D Secure, BIN lookup, card account updater, and multi-PSP routing. Evervault is PCI DSS Level 1 and SOC 2 Type II, and supports HIPAA and GDPR.'
image: https://evervault.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: evervault-mcp.yml
  slug: evervault-mcpyml
modified: '2026-07-19'
name: Evervault
nav: Providers
network: true
overview: 'Evervault publishes 12 APIs on the [APIs.io](https://apis.io/) network, including 3D Secure API, Acquirers API, Card Account Updates API, and 9 more. Tagged areas include Company, Data, Security, Encryption, and Payments.


  The Evervault catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Evervault''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 27 more developer resources.'
random_paper: 21
score:
  band: strong
  composite: 64.3
  delta: 2.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 70.2
    developer_ergonomics: 82.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 61.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Evervault Authentication
  slug: evervault-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Evervault Domain Security
  slug: evervault-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Evervault Vulnerability Disclosure
  slug: evervault-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: evervault
tags:
- Company
- Data
- Security
- Encryption
- Payments
- PCI Compliance
- Tokenization
- Cards
- Developer Tools
website: https://evervault.com
---
