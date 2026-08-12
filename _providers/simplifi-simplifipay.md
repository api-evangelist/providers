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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Simplifi Simplifipay Agentic Access
  operation_count: 52
  slug: simplifi-simplifipay-agentic-access
  summary_line: 52 operations · 39 acting
api_count: 9
apis:
- description: The Auth API from Simplifi/Simplifipay — 2 operation(s) for auth.
  name: Simplifi/Simplifipay Auth API
  slug: simplifi-simplifipay-auth-api
- description: The Card API from Simplifi/Simplifipay — 12 operation(s) for card.
  name: Simplifi/Simplifipay Card API
  slug: simplifi-simplifipay-card-api
- description: The Card Program API from Simplifi/Simplifipay — 9 operation(s) for card program.
  name: Simplifi/Simplifipay Card Program API
  slug: simplifi-simplifipay-card-program-api
- description: The Document API from Simplifi/Simplifipay — 2 operation(s) for document.
  name: Simplifi/Simplifipay Document API
  slug: simplifi-simplifipay-document-api
- description: The Fee API from Simplifi/Simplifipay — 5 operation(s) for fee.
  name: Simplifi/Simplifipay Fee API
  slug: simplifi-simplifipay-fee-api
- description: The Funding Source API from Simplifi/Simplifipay — 6 operation(s) for funding source.
  name: Simplifi/Simplifipay Funding Source API
  slug: simplifi-simplifipay-funding-source-api
- description: The Transaction API from Simplifi/Simplifipay — 3 operation(s) for transaction.
  name: Simplifi/Simplifipay Transaction API
  slug: simplifi-simplifipay-transaction-api
- description: The User API from Simplifi/Simplifipay — 4 operation(s) for user.
  name: Simplifi/Simplifipay User API
  slug: simplifi-simplifipay-user-api
- description: The Webhook API from Simplifi/Simplifipay — 4 operation(s) for webhook.
  name: Simplifi/Simplifipay Webhook API
  slug: simplifi-simplifipay-webhook-api
artifact_total: 14
asyncapis:
- description: 'Outbound webhook events SimpliFi delivers to a client-configured HTTPS endpoint. Async model: an API call returns 2xx/202 on receipt; the outcome arrives here. Each delivery carries X-SimpliFi-Webhook'
  name: SimpliFi Webhooks
  slug: simplifi-simplifipay-webhooks-asyncapi
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/simplifi-simplifipay-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidoc.simplifipay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.simplifipay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidoc.simplifipay.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://apidoc.simplifipay.com/introduction-1207172m0
- group: start
  title: ''
  type: SignUp
  url: https://simplifipay.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://prod-portal.simplifipay.com/simplifi-webapp/
- group: operate
  title: ''
  type: Support
  url: mailto:info@simplifipay.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simplifipay.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simplifipay.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/simplifi-simplifipay-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simplifi-simplifipay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simplifi-simplifipay-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simplifi-simplifipay-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simplifi-simplifipay-error-codes.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/simplifi-simplifipay-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/simplifi-simplifipay-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/simplifi-simplifipay-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/simplifi-simplifipay-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/simplifi-simplifipay-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/simplifi-simplifipay-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/simplifi-simplifipay-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simplifi-simplifipay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simplifi-simplifipay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/simplifi-simplifipay-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://simplifipay.com
created: '2026-07-17'
description: SimpliFi (simplifipay.com) is a Cards-as-a-Service platform powering virtual and physical card programs for fintechs, startups, and enterprises across the GCC (UAE, Saudi Arabia, Kuwait, Bahrain, Oman, Qatar). Regulated by the Dubai Financial Services Authority (DFSA), SimpliFi offers off-the-shelf and fully customizable card programs with multi-currency support (50+ currencies), digital-wallet enablement (Apple/Google/Samsung Pay), programmable authorization, velocity, and merchant controls, and real-time transaction and fraud monitoring. Its developer platform exposes a JWT-authenticated REST API (card programs, funding sources, cards, users, transactions, fees, rule groups, and webhook management) on an asynchronous, webhook-driven architecture, plus a PCI-DSS-compliant Virtual Card SDK for securely displaying card data. Surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplifi-simplifipay.png
layout: provider
mcp_servers:
- description: ''
  name: simplifi-simplifipay-mcp.yml
  slug: simplifi-simplifipay-mcpyml
modified: '2026-07-21'
name: Simplifi/Simplifipay
nav: Providers
network: true
overview: 'Simplifi/Simplifipay publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Card API, Card Program API, and 6 more. Tagged areas include Company, Cards, Card Issuing, Virtual Cards, and Fintech.


  The Simplifi/Simplifipay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Simplifi/Simplifipay''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 50.7
  delta: -2.4
  facets:
    commercial_clarity: 42.1
    contract_quality: 72.3
    developer_ergonomics: 60.3
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 53.1
  provenance:
    agentic_access: derived
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 53.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Simplifi Simplifipay Authentication
  slug: simplifi-simplifipay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Simplifi Simplifipay Domain Security
  slug: simplifi-simplifipay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: simplifi-simplifipay
tags:
- Company
- Cards
- Card Issuing
- Virtual Cards
- Fintech
- Payments
- Banking as a Service
- Embedded Finance
- GCC
- Webhooks
website: https://simplifipay.com
---
