---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 79
  human_in_the_loop: 2
  name: Stax Agentic Access
  operation_count: 133
  slug: stax-agentic-access
  summary_line: 133 operations · 79 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Stax REST API (published as "stax-api") exposes 133 operations across 101 paths at https://apiprod.fattlabs.com — the Merchant API for payments, payment methods, customers, invoices, payment links
  name: Stax API
  slug: stax-api
artifact_total: 10
asyncapis:
- description: ''
  name: Stax Webhooks
  slug: stax-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stax-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://staxpayments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.staxpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.staxpayments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.staxpayments.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.staxpayments.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.fattmerchant.com/
- group: company
  title: ''
  type: Blog
  url: https://staxpayments.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fattmerchantorg
- group: commercial
  title: ''
  type: Pricing
  url: https://staxpayments.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://staxpayments.com/request-sandbox/
- group: start
  title: ''
  type: Login
  url: https://app.staxpayments.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://staxpayments.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://staxpayments.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.staxpayments.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stax-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stax-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stax-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stax-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/stax-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stax-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stax-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stax-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/stax-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/stax-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stax-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/stax-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stax-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/stax-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stax-packages.yml
- group: design
  title: ''
  type: Components
  url: components/stax-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stax-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stax-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stax-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/stax-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stax-trust-center.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/stax-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stax-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/stax-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stax-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/stax-api-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/stax-api-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/stax-api-openapi.json
created: '2026-08-29'
description: Stax (formerly Fattmerchant) is an Orlando, Florida payments technology company that sells subscription-priced payment processing to small and large merchants (Stax Pay), embedded payments and merchant onboarding to SaaS platforms and ISVs (Stax Connect), compliant credit-card surcharging (CardX by Stax), automated subscription billing (Stax Bill), and full-stack processing for partners and ISOs (Stax Processing). Its public REST API at apiprod.fattlabs.com covers charges, credits, refunds and voids, stored payment methods and tokenization, customers, invoices and invoice schedules, payment links, catalog items, terminals and card-present devices, merchant enrollment and underwriting, disputes, statements and deposit reporting, teams, users and API keys, and merchant- and partner-level webhooks. Stax.js handles browser tokenization; iOS and Android SDKs cover card-present and Tap to Pay. Stax Payments, Inc. is a registered ISO/MSP of Fifth Third Bank and Synovus Bank and a registered
  partner/ISO of Elavon, Inc.
image: https://staxpayments.com/wp-content/uploads/2024/04/stax-logo-full.png
layout: provider
mcp_servers:
- description: 'Stax hosts a remote MCP server at https://docs.staxpayments.com/mcp. It answered an anonymous initialize + tools/list on 2026-08-29 (protocolVersion 2025-06-18, serverInfo {name: ''Stax Docs'', version:'
  name: Stax Docs MCP Server
  slug: stax-docs-mcp-server
modified: '2026-08-29'
name: Stax
nav: Providers
network: true
overview: 'Stax publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Payment Processing, Merchant Services, Embedded Payments, and ACH.


  The Stax catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Stax''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Stax Plans Pricing
  plan_count: 4
  slug: stax-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Stax Rate Limits
  slug: stax-rate-limits
score:
  band: exemplar
  composite: 74.9
  coverage:
    artifact_dirs: 24
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 62.6
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 74.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/screenshots/stax-2026-09-02T160822.png
security:
- kind: authentication
  name: Stax Authentication
  slug: stax-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Stax Domain Security
  slug: stax-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Stax Vulnerability Disclosure
  slug: stax-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Stax Trust Center
  slug: stax-trust-center
  summary_line: trust center published
slug: stax
tags:
- Payments
- Payment Processing
- Merchant Services
- Embedded Payments
- ACH
- Invoicing
- Subscription Billing
- Surcharging
- Point-of-Sale
- Tokenization
- Financial-Services
- Fintech
- Card Present
- Merchant Onboarding
website: https://staxpayments.com/
---
