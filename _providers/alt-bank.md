---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  - '{''url'': ''https://altbank.ai/en/'', ''status'': 301, ''note'': ''declared website redirects to https://www.novutech.com.br/ — a different registrable domain (altbank.ai -> novutech.com.br), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Real-time consumer credit underwriting / risk-assessment API. Partners POST an underwriting request for a credit-card applicant and receive a Guard Score, risk band and credit-limit decision. The call
  name: GUARD API
  slug: guard-api
- description: Credit-card module integration API (private, partner B2B) for issuing and managing alt.bank white-label credit cards.
  name: CC Integration API
  slug: cc-integration-api
- description: Identity verification / KYC SDK and API for onboarding and verifying applicants as part of the alt.bank credit and card flows.
  name: SDK KYC API
  slug: sdk-kyc-api
- baseURL: https://guard.altbank.ai
  baseurl_source: declared
  description: Credit underwriting and risk scoring for partner card issuance.
  name: Alt Bank Underwriting API
  slug: alt-bank-underwriting-api
artifact_total: 9
asyncapis:
- description: ''
  name: Alt Bank Guard Webhooks
  slug: alt-bank-guard-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: alt.bank GUARD Underwriting API
  slug: open-alt-bank-underwriting-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/alt-bank-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alt-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altbank.ai/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.altbank.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.altbank.ai/docs/guard-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.altbank.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.altbank.ai/docs/guard
- group: operate
  title: ''
  type: Support
  url: https://altbank.ai/en/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alt-bank
- group: auth
  title: ''
  type: Authentication
  url: authentication/alt-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alt-bank-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alt-bank-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/alt-bank-guard-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/alt-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alt-bank-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alt-bank-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: alt.bank (Alt Bank) is a Brazilian fintech providing a fully integrated, turnkey credit-card and consumer-credit platform for partners who want to launch prepaid and postpaid cards without becoming a financial institution. Its flagship product, GUARD, is a machine-learning underwriting / credit-risk engine ("Brazil's most accurate credit model") that returns a Guard Score, risk band and credit-limit decision through a real-time partner API. The platform also bundles white-label credit cards (novücard), Visa BIN sponsorship, KYC, anti-fraud, dispute management and Pix/boleto payment processing. Partners integrate over a documented HTTPS API secured with a per-partner X-Partner-Auth token plus IP allow-listing, with a mirrored staging sandbox and asynchronous callback delivery of underwriting results. Backed by Anthemis, Union Square Ventures, Repeat Ventures and SquareOne Capital, alt.bank targets financial inclusion for underbanked consumers.
image: https://altbank.ai/wp-content/uploads/2020/08/cropped-alt.bank-logo-square-300x300.png
layout: provider
modified: '2026-08-08'
name: Alt Bank
nav: Providers
network: true
overview: 'Alt Bank publishes 1 API on the [APIs.io](https://apis.io/) network: Underwriting API. Tagged areas include Company, Fintech, Banking, Credit, and Underwriting.


  The Alt Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Alt Bank''s developer surface includes documentation, getting-started guide, API reference, support, authentication, sandbox, and 11 more developer resources.'
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/alt-bank/refs/heads/main/screenshots/alt-bank-2026-07-25T195815.png
security:
- kind: authentication
  name: Alt Bank Authentication
  slug: alt-bank-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alt Bank Domain Security
  slug: alt-bank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alt-bank
tags:
- Company
- Fintech
- Banking
- Credit
- Underwriting
- Credit Cards
- Payments
- KYC
- Risk
- Brazil
- Financial Inclusion
- Banking as a Service
website: https://altbank.ai/en/
---
