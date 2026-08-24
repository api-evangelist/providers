---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 62.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 13
  human_in_the_loop: 13
  name: Justt Agentic Access
  operation_count: 23
  slug: justt-agentic-access
  summary_line: 23 operations · 13 acting · 13 human-in-the-loop
api_count: 3
apis:
- description: The Justt REST API lets merchants read and manage chargebacks, enrich them with transaction data and evidence files, decide whether Justt should fight or accept a dispute, manage merchants and PSP int
  name: Justt REST API
  slug: rest-api
- description: Justt official REST API for pre-chargeback alerts. Retrieve alerts sourced from Ethoca, Verifi CDRN and RDR by search criteria or by id, so a merchant can refund or resolve a transaction before it bec
  name: Justt Pre-Chargeback Alerts API
  slug: pre-chargeback-alerts
- description: OpenAPI 3.1 specification of the eleven webhook events Justt sends to merchant endpoints — chargeback created/updated/status-updated, evidence submitted, chargeback accepted, pre-chargeback alert rece
  name: Justt Webhook Events
  slug: webhook-events
arazzos:
- description: 'Pull pre-chargeback alerts from Ethoca / Verifi, read one, and report its outcome back to Justt using the alert networks'' own outcome vocabulary. Note the read operations and the write operation live '
  name: Work a Justt pre-chargeback alert to a reported outcome
  slug: justt-alert-to-outcome
- description: Create a test chargeback from raw Stripe dispute data in the sandbox, advance it to under_review, then resolve it as won — firing a webhook at each transition so an integration can be validated end to
  name: Drive a chargeback through its lifecycle in the Justt sandbox
  slug: justt-sandbox-lifecycle
- description: Read an open chargeback, upload an evidence file, submit it to the PSP, and poll the asynchronous submission to a terminal state.
  name: Submit evidence for a Justt chargeback
  slug: justt-submit-evidence
- description: 'List open chargebacks, enrich one with additional merchant data, and override whether Justt should represent it. Acceptance is deliberately NOT part of this workflow — it is irreversible and requires '
  name: Triage Justt chargebacks and set the representment decision
  slug: justt-triage-and-decide
artifact_total: 16
asyncapis:
- description: ''
  name: Justt Webhook Events
  slug: justt-webhook-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/justt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/justt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/justt-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://justt.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.justt.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.justt.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.justt.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.justt.ai/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developers.justt.ai/docs/contact-us
- group: company
  title: ''
  type: Blog
  url: https://justt.ai/blog/
- group: start
  title: ''
  type: Login
  url: https://app.justt.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://justt.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://justt.ai/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.justt.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.justt.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.justt.ai/
- group: other
  title: ''
  type: APICatalog
  url: well-known/justt-well-known.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/justt-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/justt-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/justt-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/justt-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/justt-rest-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/justt-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/justt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/justt-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.justt.ai/docs/legacy-api-to-rest-api-migration-guide
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/justt-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/justt-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/justt-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/justt-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/justt-webhook-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/justt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/justt-rate-limits.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
created: '2026-08-23'
description: Justt is an AI-native chargeback management and dispute-representment platform for high-volume merchants. Its Dynamic Arguments engine assembles evidence-backed representment packages for card disputes across 30+ payment service providers (Stripe, Adyen, PayPal, Braintree, Checkout.com, Worldpay, Chase Paymentech, Nuvei and others), and it also handles pre-chargeback alerts from Ethoca, Verifi CDRN and RDR. Justt publishes a public developer portal at developers.justt.ai with three OpenAPI definitions — a REST API for chargebacks, transactions, evidence, files, merchants and integrations; a Pre-Chargeback Alerts API; and an OpenAPI 3.1 webhook-events specification covering eleven signed event types — plus an RFC 9727 /.well-known/api-catalog, an llms.txt documentation index, a sandbox environment, and a Vanta-hosted trust center.
image: https://justt.ai/wp-content/uploads/2025/03/blog-7-1.jpg
layout: provider
mcp_servers:
- description: ''
  name: Justt MCP Server
  slug: justt-mcp-server
modified: '2026-08-23'
name: Justt
nav: Providers
network: true
overview: 'Justt publishes 3 APIs on the [APIs.io](https://apis.io/) network: REST API, Pre-Chargeback Alerts API, and Webhook Events. Tagged areas include Company, Payments, Chargebacks, Disputes, and Fraud.


  The Justt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Justt''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 28 more developer resources.'
plans:
- name: Justt Plans Pricing
  plan_count: 0
  slug: justt-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Justt Rate Limits
  slug: justt-rate-limits
scopes:
- name: Justt Scopes
  scope_count: 1
  slug: justt-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 62.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 30.3
    contract_quality: 55.5
    developer_ergonomics: 71.4
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 52.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Justt Authentication
  slug: justt-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Justt Domain Security
  slug: justt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Justt Trust Center
  slug: justt-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018
slug: justt
tags:
- Company
- Payments
- Chargebacks
- Disputes
- Fraud
- Risk
- Financial Services
- E-Commerce
- Artificial Intelligence
- Webhooks
website: https://justt.ai/
---
