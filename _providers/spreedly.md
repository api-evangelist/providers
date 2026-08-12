---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Spreedly Agentic Access
  operation_count: 84
  slug: spreedly-agentic-access
  summary_line: 84 operations · 48 acting
api_count: 7
apis:
- description: The Spreedly Core Transactional API — the primary REST surface for the Payments Orchestration platform. Covers payment method tokenization/vaulting, gateway creation and management, and the full trans
  name: Spreedly Core Transactional API
  slug: spreedly-core-api
- description: Create, retain, redact, recache, update, and inspect tokenized payment methods held in Spreedly's PCI-compliant universal vault, including field-level encryption and payment method event history. Part
  name: Spreedly Payment Methods & Vault API
  slug: spreedly-payment-methods-api
- description: Workflow-driven orchestration endpoints (Composer) that execute an authorization, purchase, or verification against a configured routing workflow rather than a single named gateway, enabling failover,
  name: Spreedly Composer (Workflows) API
  slug: spreedly-composer-api
- description: 'Retrieve card metadata and lifecycle status for network tokens (Visa, Mastercard, Amex network-provisioned tokens) managed through Spreedly, supporting network tokenization for improved authorization '
  name: Spreedly Network Tokenization API
  slug: spreedly-network-tokenization-api
- description: Card Refresher / account updater inquiries that refresh stored card credentials (expiration dates and PANs) against the card networks' account updater services to reduce declines on stored payment met
  name: Spreedly Account Updater (Card Refresher) API
  slug: spreedly-account-updater-api
- description: Receivers let merchants forward securely vaulted payment data from the Spreedly vault to arbitrary third-party HTTP endpoints, extending tokenization beyond payment gateways to any API that needs card
  name: Spreedly Receivers API
  slug: spreedly-receivers-api
- description: Strong Customer Authentication endpoints to authenticate a given payment method and manage SCA providers on a merchant profile, supporting 3-D Secure 2.x authentication flows for cardholder verificati
  name: Spreedly 3-D Secure / SCA Authentication API
  slug: spreedly-sca-api
artifact_total: 14
asyncapis:
- description: ''
  name: Spreedly Webhooks
  slug: spreedly-webhooks
collections:
- collection_type: postman
  name: Spreedly API V1
  slug: postman-spreedly-api-v1
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spreedly/overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/spreedly-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.spreedly.com/security-compliance
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spreedly-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spreedly-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spreedly-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/spreedly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/spreedly-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spreedly-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/spreedly-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spreedly-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spreedly-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/spreedly-api-v1-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/spreedly-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spreedly-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/spreedly-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spreedly-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.spreedly.com/docs/major-changes
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spreedly-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spreedly-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/spreedly-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spreedly-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spreedly-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/spreedly-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spreedly-changelog.yml
- group: build
  title: ''
  type: Postman
  url: https://docs.spreedlypostman.com/
- group: operate
  title: ''
  type: Support
  url: https://support.spreedly.com/
- group: company
  title: ''
  type: Website
  url: https://www.spreedly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.spreedly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spreedly.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.spreedly.com/reference/api-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.spreedly.com/docs/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.spreedly.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spreedly
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spreedly.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spreedly.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.spreedly.com/blog
- group: auth
  title: ''
  type: Security
  url: https://www.spreedly.com/security
- group: start
  title: ''
  type: SignUp
  url: https://id.spreedly.com/readme/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spreedly.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.spreedly.com/#privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spreedly
created: '2026-07-24'
description: 'Spreedly is a United States payments orchestration platform and PCI-compliant card vault that lets merchants and platforms securely tokenize payment methods once and then transact against hundreds of payment gateways, processors, and third-party APIs through a single integration. Founded in 2008 and headquartered in Durham, North Carolina, Spreedly sits in the gateway/PSP layer of the deep, fragmented US payments market as an independent, network-agnostic intermediary rather than a card network or acquirer. Its Payments Orchestration offering combines a universal token vault, a normalized transaction API across many gateways, workflow-based routing (Composer), network tokenization, account updater (Card Refresher), 3-D Secure / SCA authentication, and Receivers for forwarding stored payment data to arbitrary third-party endpoints. Spreedly is strongly API-native: it publishes a public developer portal with complete reference documentation and a downloadable OpenAPI 3.1 specification
  for its Core Transactional API (https://core.spreedly.com/v1), authenticated with HTTP Basic auth using per-environment key/secret credentials.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: spreedly-mcp.yml
  slug: spreedly-mcpyml
modified: '2026-07-24'
name: Spreedly
nav: Providers
network: true
overview: 'Spreedly publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Core Transactional API, Payment Methods & Vault API, Composer (Workflows) API, and 4 more. Tagged areas include Payments, United States, Payment Gateway, Payment Orchestration, and Payment Processing.


  The Spreedly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spreedly''s developer surface includes authentication, sandbox, changelog, support, documentation, API reference, getting-started guide, and 36 more developer resources.'
random_paper: 60
score:
  band: strong
  composite: 61.0
  delta: -4.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.2
    developer_ergonomics: 79.9
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Spreedly Authentication
  slug: spreedly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spreedly Domain Security
  slug: spreedly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Spreedly Trust Center
  slug: spreedly-trust-center
  summary_line: SOC 2, PCI DSS
slug: spreedly
tags:
- Payments
- United States
- Payment Gateway
- Payment Orchestration
- Payment Processing
- Card Vault
- Tokenization
- Network Tokenization
- PCI Compliance
- Subscriptions
website: https://www.spreedly.com/
---
