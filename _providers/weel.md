---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Weel Agentic Access
  operation_count: 51
  slug: weel-agentic-access
  summary_line: 51 operations · 27 acting
api_count: 1
apis:
- description: The Weel Open API is a single RESTful interface that programmatically reads and writes a business's spend data in Weel — budgets, budget members, budget owners, budget top-ups, users, roles, transacti
  name: Weel Open API
  slug: weel-open-api
artifact_total: 8
collections:
- collection_type: open
  name: Weel OpenAPI
  slug: open-weel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weel-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://letsweel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.letsweel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.letsweel.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.letsweel.com/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.letsweel.com/getting-started/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://letsweel.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://letsweel.com/product-updates
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.letsweel.com/
- group: auth
  title: ''
  type: Compliance
  url: security/weel-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/weel-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/weel-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/weel-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weel-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/weel-changelog.yml
- group: operate
  title: ''
  type: Support
  url: https://help.letsweel.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://letsweel.com/resources/the-weelhouse
- group: commercial
  title: ''
  type: TermsOfService
  url: https://letsweel.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://letsweel.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.letsweel.com/app/business-signup
created: '2026-07-24'
description: Weel (formerly DiviPay, operated by Weel Pty Ltd) is a Melbourne-based all-in-one spend management platform for finance teams in Australia and New Zealand, serving over 4,000 finance teams and 60,000+ card holders. Weel issues virtual and physical Visa debit cards with real-time limits and controls, and layers accounts payable automation, expense management, reimbursements, subscription management, budgets, and approval policies on top. Rather than operating payment rails directly, Weel sits on the spend and AP/AR seam, syncing approved spend into Xero, QuickBooks, MYOB, and NetSuite. On the API posture, Weel ships a genuine public developer portal at developer.letsweel.com (Redocly-based) documenting a single RESTful "Weel Open API" that both reads and writes budgets, users, transactions, custom fields, accounting codes, categories, invites, and top-ups, authenticated with a bearer API key generated in-app. API access is an Enterprise-tier capability. No public webhooks, Postman
  collection, or OAuth flow are documented as of this review.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Weel MCP Server
  slug: weel-mcp-server
modified: '2026-07-24'
name: Weel
nav: Providers
network: true
overview: 'Weel publishes 1 API on the [APIs.io](https://apis.io/) network: Open API. Tagged areas include Payments, Australia, Spend Management, Expense Management, and Corporate Cards.


  Weel''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, changelog, support, and 17 more developer resources.'
random_paper: 9
score:
  band: strong
  composite: 56.1
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 60.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weel/refs/heads/main/screenshots/weel-2026-08-17T082857.png
security:
- kind: authentication
  name: Weel Authentication
  slug: weel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Weel Domain Security
  slug: weel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Weel Vulnerability Disclosure
  slug: weel-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Weel Trust Center
  slug: weel-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, ISO 27001:2022
slug: weel
tags:
- Payments
- Australia
- Spend Management
- Expense Management
- Corporate Cards
- Accounts Payable
- Card Issuing
- Reimbursement
- Budgets
- Fintech
website: https://letsweel.com/
---
