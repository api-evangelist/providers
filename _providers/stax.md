---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.3
  scored_at: '2026-09-16'
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
  description: The Admin API from Stax — 1 operation(s) for admin.
  name: Stax Admin API
  slug: stax-admin-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Charge API from Stax — 1 operation(s) for charge.
  name: Stax Charge API
  slug: stax-charge-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Credit API from Stax — 1 operation(s) for credit.
  name: Stax Credit API
  slug: stax-credit-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Customer API from Stax — 3 operation(s) for customer.
  name: Stax Customer API
  slug: stax-customer-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Ephemeral API from Stax — 1 operation(s) for ephemeral.
  name: Stax Ephemeral API
  slug: stax-ephemeral-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The File API from Stax — 5 operation(s) for file.
  name: Stax File API
  slug: stax-file-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The File{id} API from Stax — 1 operation(s) for file{id}.
  name: Stax File{id} API
  slug: stax-file-id-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Forgot API from Stax — 1 operation(s) for forgot.
  name: Stax Forgot API
  slug: stax-forgot-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Invoice API from Stax — 9 operation(s) for invoice.
  name: Stax Invoice API
  slug: stax-invoice-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Item API from Stax — 5 operation(s) for item.
  name: Stax Item API
  slug: stax-item-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Merchant API from Stax — 7 operation(s) for merchant.
  name: Stax Merchant API
  slug: stax-merchant-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Payment Method API from Stax — 4 operation(s) for payment method.
  name: Stax Payment Method API
  slug: stax-payment-method-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Query API from Stax — 14 operation(s) for query.
  name: Stax Query API
  slug: stax-query-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Reset API from Stax — 1 operation(s) for reset.
  name: Stax Reset API
  slug: stax-reset-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Self API from Stax — 4 operation(s) for self.
  name: Stax Self API
  slug: stax-self-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Surcharge API from Stax — 1 operation(s) for surcharge.
  name: Stax Surcharge API
  slug: stax-surcharge-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Team API from Stax — 8 operation(s) for team.
  name: Stax Team API
  slug: stax-team-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Terminal API from Stax — 13 operation(s) for terminal.
  name: Stax Terminal API
  slug: stax-terminal-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Transaction API from Stax — 11 operation(s) for transaction.
  name: Stax Transaction API
  slug: stax-transaction-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Underwriting API from Stax — 5 operation(s) for underwriting.
  name: Stax Underwriting API
  slug: stax-underwriting-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Verify API from Stax — 1 operation(s) for verify.
  name: Stax Verify API
  slug: stax-verify-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Webhook API from Stax — 2 operation(s) for webhook.
  name: Stax Webhook API
  slug: stax-webhook-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Webhookadmin API from Stax — 2 operation(s) for webhookadmin.
  name: Stax Webhookadmin API
  slug: stax-webhookadmin-api
artifact_total: 32
asyncapis:
- description: ''
  name: Stax Webhooks
  slug: stax-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/agentic-access/stax-agentic-access.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/changelog/stax-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/stax-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/lifecycle/stax-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stax-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/authentication/stax-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stax-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/conventions/stax-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stax-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/conventions/stax-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/stax-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/rate-limits/stax-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stax-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/plans/stax-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stax-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/errors/stax-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stax-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/errors/stax-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/stax-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/asyncapi/stax-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/stax-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/mcp/stax-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stax-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/mcp/stax-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/stax-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/llms/stax-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stax-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/packages/stax-packages.yml
  title: ''
  type: Packages
  url: packages/stax-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/packages/stax-packages.yml
  title: ''
  type: SDKs
  url: packages/stax-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/components/stax-components.yml
  title: ''
  type: Components
  url: components/stax-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/sandbox/stax-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/stax-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/data-model/stax-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stax-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/conformance/stax-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stax-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/conformance/stax-conformance.yml
  title: ''
  type: Compliance
  url: conformance/stax-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/security/stax-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stax-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/well-known/stax-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stax-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/security/stax-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stax-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/security/stax-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/stax-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/security/stax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stax-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/examples/stax-api-examples.yml
  title: ''
  type: Examples
  url: examples/stax-api-examples.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/overlays/stax-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stax-api-overlay.yaml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/stax/refs/heads/main/openapi/_original/stax-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/stax-api-openapi.json
created: '2026-08-29'
description: Stax (formerly Fattmerchant) is an Orlando, Florida payments technology company that sells subscription-priced payment processing to small and large merchants (Stax Pay), embedded payments and merchant onboarding to SaaS platforms and ISVs (Stax Connect), compliant credit-card surcharging (CardX by Stax), automated subscription billing (Stax Bill), and full-stack processing for partners and ISOs (Stax Processing). Its public REST API at apiprod.fattlabs.com covers charges, credits, refunds and voids, stored payment methods and tokenization, customers, invoices and invoice schedules, payment links, catalog items, terminals and card-present devices, merchant enrollment and underwriting, disputes, statements and deposit reporting, teams, users and API keys, and merchant- and partner-level webhooks. Stax.js handles browser tokenization; iOS and Android SDKs cover card-present and Tap to Pay. Stax Payments, Inc. is a registered ISO/MSP of Fifth Third Bank and Synovus Bank and a registered
  partner/ISO of Elavon, Inc.
image: https://staxpayments.com/wp-content/uploads/2024/04/stax-logo-full.png
layout: provider
mcp_servers:
- description: 'Stax hosts a remote MCP server at https://docs.staxpayments.com/mcp. It answered an anonymous initialize + tools/list on 2026-08-29 (protocolVersion 2025-06-18, serverInfo {name: ''Stax Docs'', version:'
  name: Stax Docs MCP Server
  slug: stax-docs-mcp-server
modified: '2026-09-16'
name: Stax
nav: Providers
network: true
overview: 'Stax publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Charge API, Credit API, and 20 more. Tagged areas include Payments, Payment Processing, Merchant Services, Embedded Payments, and ACH.


  The Stax catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Stax''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Stax Plans Pricing
  plan_count: 4
  slug: stax-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Stax Rate Limits
  slug: stax-rate-limits
score:
  band: exemplar
  composite: 76.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 67.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 84.2
  previous_composite: 75.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
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
