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
    asyncapi_events: true
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 136
  human_in_the_loop: 2
  name: Drippay Agentic Access
  operation_count: 245
  slug: drippay-agentic-access
  summary_line: 245 operations · 136 acting · 2 human-in-the-loop
api_count: 23
apis:
- description: Evaluate and preview billable metrics.
  name: Drippay BillableMetrics API
  slug: drippay-billablemetrics-api
- description: Business-level settings and configuration.
  name: Drippay Business API
  slug: drippay-business-api
- description: View charge history and settlement status.
  name: Drippay Charges API
  slug: drippay-charges-api
- description: Per-customer commercial agreements with custom pricing, prepaid commits, and spend caps. All contract endpoints require a secret key (`sk_*`) with the `ADMIN` role.
  name: Drippay Contracts API
  slug: drippay-contracts-api
- description: Coupons and promotion codes for discounts.
  name: Drippay Coupons API
  slug: drippay-coupons-api
- description: Create, issue, and void credit notes.
  name: Drippay Credit Notes API
  slug: drippay-credit-notes-api
- description: Self-service customer portal for profile, subscriptions, and address management.
  name: Drippay Customer Portal API
  slug: drippay-customer-portal-api
- description: Create and manage billable customers.
  name: Drippay Customers API
  slug: drippay-customers-api
- description: The Drift API from Drippay — 6 operation(s) for drift.
  name: Drippay Drift API
  slug: drippay-drift-api
- description: Automatic retry + dunning email flow for failed payments. Configure a per-business retry schedule, list failed charges in collections, and manually re-trigger retries.
  name: Drippay Dunning API
  slug: drippay-dunning-api
- description: Quota management and pre-request access checks.
  name: Drippay Entitlements API
  slug: drippay-entitlements-api
- description: Record execution events for observability.
  name: Drippay Events API
  slug: drippay-events-api
- description: Manage billing, CRM, and marketplace integrations (Stripe, Xero, Salesforce).
  name: Drippay Integrations API
  slug: drippay-integrations-api
- description: The Internal API from Drippay — 1 operation(s) for internal.
  name: Drippay Internal API
  slug: drippay-internal-api
- description: Generate, issue, and manage invoices. Supports usage-based and subscription-based billing periods.
  name: Drippay Invoices API
  slug: drippay-invoices-api
- description: Define per-unit pricing for usage types. Creating, updating, and deleting plans requires a secret key (`sk_*`) with the `ADMIN` role.
  name: Drippay Pricing Plans API
  slug: drippay-pricing-plans-api
- description: Controlled taxonomy for strict-products governance. Groups pricing plans into service-line categories for ARR rollups and revenue reporting.
  name: Drippay Product Categories API
  slug: drippay-product-categories-api
- description: Start, update, and inspect agent runs.
  name: Drippay Runs API
  slug: drippay-runs-api
- description: Recurring billing and subscription lifecycle management.
  name: Drippay Subscriptions API
  slug: drippay-subscriptions-api
- description: 'Sales tax configuration: customer tax addresses, exemptions, business registrations, and jurisdiction rates. Requires a secret key with ADMIN role and full mode (`SIMPLE_MODE=false`).'
  name: Drippay Tax API
  slug: drippay-tax-api
- description: Record metered usage. Creates charges when a pricing plan matches.
  name: Drippay Usage API
  slug: drippay-usage-api
- description: Manage webhook endpoints for real-time event notifications.
  name: Drippay Webhooks API
  slug: drippay-webhooks-api
- description: Define workflow templates for agent execution.
  name: Drippay Workflows API
  slug: drippay-workflows-api
artifact_total: 30
asyncapis:
- description: ''
  name: Drippay Webhooks
  slug: drippay-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/drippay-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://usedrip.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usedrip.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usedrip.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usedrip.ai/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://usedrip.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://usedrip.ai/login
- group: start
  title: ''
  type: SignUp
  url: https://usedrip.ai/download/mac
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usedrip.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usedrip.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://usedrip.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://usedrip.ai/guides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DripYCx26
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usedrip.ai/
- group: operate
  title: ''
  type: RateLimits
  url: conventions/drippay-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://usedrip.ai/security
- group: auth
  title: ''
  type: Security
  url: https://usedrip.ai/security
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/drippay-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/drippay-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/drippay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drippay-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/drippay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/drippay-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/drippay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/drippay-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/drippay-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/drippay-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/drippay-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Drippay, Inc. ("drip") is a Y Combinator company (YC P26) building two connected products. drip is a local-first Mac app that turns LinkedIn, iMessage, and email conversations into a self-filling CRM with AI drafting, follow-up, and meeting booking. The Drip API is a usage-based billing and execution-ledger platform for AI agents — a Stripe-like metering and monetization backend exposing customers, subscriptions, pricing plans, billable metrics, usage events, invoices, credit notes, coupons, entitlements, charges, dunning, tax, contracts, drift detection, and webhooks over a REST interface at api.drippay.dev. It ships official Node, Python, and C++ SDKs, an idempotency-key contract, cursor pagination, a hosted MCP server, and a SOC 2 Type I security posture monitored with Vanta.
image: https://usedrip.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: drippay-mcp.yml
  slug: drippay-mcpyml
modified: '2026-07-18'
name: Drippay
nav: Providers
network: true
overview: 'Drippay publishes 23 APIs on the [APIs.io](https://apis.io/) network, including BillableMetrics API, Business API, Charges API, and 20 more. Tagged areas include Company, Billing, Usage-Based Billing, Metering, and Monetization.


  The Drippay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Drippay''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 22 more developer resources.'
random_paper: 41
score:
  band: developing
  composite: 55.2
  delta: -2.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.7
    developer_ergonomics: 64.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drippay/refs/heads/main/screenshots/drippay-2026-07-25T212410.png
security:
- kind: authentication
  name: Drippay Authentication
  slug: drippay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Drippay Domain Security
  slug: drippay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Drippay Vulnerability Disclosure
  slug: drippay-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Drippay Trust Center
  slug: drippay-trust-center
  summary_line: SOC 2
slug: drippay
tags:
- Company
- Billing
- Usage-Based Billing
- Metering
- Monetization
- Payments
- AI Agents
- Developer Tools
- Webhooks
- MCP
- CRM
- Sales Automation
website: https://usedrip.ai/
---
