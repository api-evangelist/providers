---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Bunq Agentic Access
  operation_count: 28
  slug: bunq-agentic-access
  summary_line: 28 operations · 11 acting
api_count: 9
apis:
- description: Upload and retrieve attachment content.
  name: bunq Attachment API
  slug: bunq-attachment-api
- description: Debit and credit cards linked to monetary accounts.
  name: bunq Card API
  slug: bunq-card-api
- description: Generate and download account statement exports (CSV, MT940, PDF).
  name: bunq Customer Statement API
  slug: bunq-customer-statement-api
- description: Installation, device registration, and session bootstrap. Establishes the RSA-signed API context.
  name: bunq Handshake API
  slug: bunq-handshake-api
- description: Bank, savings, and joint accounts holding money.
  name: bunq Monetary Account API
  slug: bunq-monetary-account-api
- description: Manage URL (webhook) and push notification callbacks for account events.
  name: bunq Notification Filter API
  slug: bunq-notification-filter-api
- description: Execute and read payments (including SEPA) for a monetary account.
  name: bunq Payment API
  slug: bunq-payment-api
- description: Create and read payment requests (money you ask another party to pay).
  name: bunq Request Inquiry API
  slug: bunq-request-inquiry-api
- description: The authenticated user (person, company, or payment service provider).
  name: bunq User API
  slug: bunq-user-api
artifact_total: 17
collections:
- collection_type: open
  name: bunq Public API
  slug: open-bunq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bunq-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bunq-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bunq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bunq-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bunq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bunq
- group: company
  title: ''
  type: Website
  url: https://www.bunq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.bunq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bunq.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/bunq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bunq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bunq-finops.yml
- group: start
  title: ''
  type: Sandbox
  url: https://beta.doc.bunq.com/basics/sandbox
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bunq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bunq.com/en-us/documents/pricing-sheet
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bunq.com/documents/terms-conditions
- group: company
  title: ''
  type: Blog
  url: https://medium.com/bunq-developers-corner
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/bunq-developers-corner
created: '2023-11-13'
description: bunq is a European (Dutch) neobank offering personal and business accounts across the EU. Its Public API is a REST API over HTTPS (https://api.bunq.com/v1, sandbox https://public-api.sandbox.bunq.com/v1) that lets account holders and licensed third parties read accounts, initiate SEPA and internal payments, send and answer payment requests, manage cards, export statements, upload attachments, and subscribe to event callbacks. bunq uses a distinctive multi-step handshake - installation (register an RSA public key), device-server, then session-server - after which requests are RSA-signed with X-Bunq-Client-Signature and authenticated with a session token in X-Bunq-Client-Authentication.
finops:
- name: Bunq Finops
  service_category: Banking / Fintech
  slug: bunq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bunq.png
layout: provider
modified: '2026-07-12'
name: bunq
nav: Providers
network: true
overview: 'bunq publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Attachment API, Card API, Customer Statement API, and 6 more. Tagged areas include Banking, Neobank, Payments, Accounts, and SEPA.


  bunq''s developer surface includes authentication, documentation, sandbox, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Bunq Plans Pricing
  plan_count: 7
  slug: bunq-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 6
  name: Bunq Rate Limits
  slug: bunq-rate-limits
score:
  band: developing
  composite: 45.6
  delta: -4.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.2
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bunq/refs/heads/main/screenshots/bunq-2026-06-20T173803.png
security:
- kind: authentication
  name: Bunq Authentication
  slug: bunq-authentication
  summary_line: apiKey/signature · 3 schemes
- kind: domain-security
  name: Bunq Domain Security
  slug: bunq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bunq Vulnerability Disclosure
  slug: bunq-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bunq
tags:
- Banking
- Neobank
- Payments
- Accounts
- SEPA
- Open Banking
- Fintech
- Europe
- Netherlands
website: https://www.bunq.com/
---
