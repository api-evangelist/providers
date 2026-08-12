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
  trial: false
  try_now: false
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
    event_surface_described: derived
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Keycorp Agentic Access
  operation_count: 4
  slug: keycorp-agentic-access
  summary_line: 4 operations
api_count: 10
apis:
- description: The Commercial Accounts Reporting API delivers real-time and historical account-level information for client-authorized commercial KeyBank accounts. It exposes operations to retrieve full account deta
  name: KeyBank Account Information API
  slug: account-information-api
- description: The ACH Origination API initiates secure, automated ACH fund transfers from commercial KeyBank accounts across the full range of Standard Entry Class codes — CCD, CTX, PPD, TEL, and WEB — for both sen
  name: KeyBank ACH Origination API
  slug: ach-origination-api
- description: 'The Wire Transfer API, delivered through KeyBank''s combined RTP and Wire Payments service, facilitates high-value domestic wire payments from commercial accounts. It provides operations to initiate a '
  name: KeyBank Wire Transfer API
  slug: wire-transfer-api
- description: The RTP Send Payment API initiates instant, irrevocable payments over The Clearing House Real-Time Payments (RTP) network from commercial KeyBank accounts. Sharing KeyBank's combined RTP and Wire Paym
  name: KeyBank RTP Send Payment API
  slug: rtp-send-payment-api
- description: The Account Validation v2 API verifies account details and ownership before commercial payments and transfers are initiated, matching the supplied account and owner information against the National Sh
  name: KeyBank Account Validation API
  slug: account-validation-api
- description: The ACH Inquiry API lets commercial clients check the current status and detail of ACH transactions posted to their KeyBank accounts. It provides operations to list ACH transactions, retrieve full det
  name: KeyBank ACH Inquiry API
  slug: ach-inquiry-api
- description: 'The Wire Inquiry API tracks the status and delivery of wire transfers associated with commercial KeyBank accounts. It exposes operations to list wire transactions, retrieve detailed information for a '
  name: KeyBank Wire Inquiry API
  slug: wire-inquiry-api
- description: The RTP Inquiry API confirms the delivery and status of Real-Time Payments sent through KeyBank on The Clearing House RTP network. It provides operations to list RTP transactions, retrieve full detail
  name: KeyBank RTP Inquiry API
  slug: rtp-inquiry-api
- description: The Check Services API manages stop payments and check image retrieval for commercial KeyBank accounts. It exposes operations to place a stop payment, list and retrieve check images, and a health chec
  name: KeyBank Check Services API
  slug: check-services-api
- description: The KeyBank Webhooks service delivers real-time payment event notifications to subscribed commercial client applications for ACH, Wire, and RTP alerts. It defines client-hosted callback endpoints (ale
  name: KeyBank Webhooks
  slug: webhooks
artifact_total: 19
asyncapis:
- description: ''
  name: Keycorp Payment Alerts Webhooks
  slug: keycorp-payment-alerts-webhooks
collections:
- collection_type: open
  name: KeyBank Commercial Banking APIs
  slug: open-keycorp
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/keycorp-originate-ach-payment.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.key.com/tos
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.key.com/guides/getting-started
- group: start
  title: ''
  type: Signup
  url: https://developer.key.com/secure/signup
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keycorp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keycorp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keycorp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/keycorp-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/keycorp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/keycorp-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/keycorp-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keycorp-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/keycorp-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/keycorp-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/keycorp-payment-alerts-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/keycorp-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/keycorp-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/keycorp-ach-originations-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keycorp-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.key.com/
- group: company
  title: ''
  type: Website
  url: https://www.keycorp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.key.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.key.com/docs/commercial/accounts
- group: operate
  title: ''
  type: Support
  url: https://developer.key.com/support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keybank
created: '2026-03-21'
description: KeyCorp (KeyBank) is one of the nation's largest bank-based financial services companies and a super-regional commercial bank headquartered in Cleveland, Ohio, providing deposit, lending, cash management, treasury, and investment services to individuals, small businesses, and middle-market companies. The KeyBank Developer Portal at developer.key.com publishes a self-service catalog of commercial and embedded-banking APIs covering account information reporting, ACH origination, RTP and wire payments, account validation, ACH/wire/RTP inquiry, check services, and payment event webhooks. Each product ships a downloadable OpenAPI 3.1 definition and is secured with OAuth2 bearer tokens, mutual TLS client certificates, and FAPI-style interaction-id headers.
finops:
- name: Keycorp Finops
  service_category: Banking
  slug: keycorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keycorp.png
layout: provider
mcp_servers:
- description: ''
  name: keycorp-mcp.yml
  slug: keycorp-mcpyml
modified: '2026-07-23'
name: KeyCorp
nav: Providers
network: true
overview: 'KeyCorp publishes 10 APIs on the [APIs.io](https://apis.io/) network, including KeyBank Account Information API, KeyBank ACH Origination API, KeyBank Wire Transfer API, and 7 more. Tagged areas include Banking, Commercial Banking, Financial Services, Fortune 500, and Payments.


  The KeyCorp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KeyCorp''s developer surface includes getting-started guide, signup flow, authentication, sandbox, documentation, support, and 20 more developer resources.'
plans:
- name: Keycorp Plans Pricing
  plan_count: 1
  slug: keycorp-plans-pricing
press:
- date: '2026-05-25'
  title: Google Cloud, KeyBank, and Deloitte today announced ...
  url: https://www.googlecloudpresscorner.com/2022-02-03-Google-Cloud-Announces-Cloud-First-Partnership-with-KeyBank
- date: '2026-05-25'
  title: KeyCorp (KEY) Latest Press Releases & Corporate News
  url: https://ca.finance.yahoo.com/quote/KEY/press-releases/
- date: '2026-05-25'
  title: KeyCorp bulks up investment banking with purchase of UK ...
  url: https://www.americanbanker.com/news/keycorp-bulks-up-investment-banking-with-purchase-of-uk-firm
- date: '2026-05-25'
  title: 'Keycorp AI Profile: Capabilities, IP and People'
  url: https://www.index42.com/companies/Keycorp
- date: '2026-05-25'
  title: Yesterday, we announced KeyCorp's First Quarter 2026 ...
  url: https://www.facebook.com/keybank/posts/yesterday-we-announced-keycorps-first-quarter-2026-earnings-learn-more-at/1351056593721210/
random_paper: 69
rate_limits:
- limit_count: 1
  name: Keycorp Rate Limits
  slug: keycorp-rate-limits
score:
  band: developing
  composite: 43.2
  delta: 0.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 70.9
    developer_ergonomics: 53.8
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 88.9
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 26.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keycorp/refs/heads/main/screenshots/keycorp-2026-06-20T184017.png
security:
- kind: authentication
  name: Keycorp Authentication
  slug: keycorp-authentication
  summary_line: http/mutualTLS · 2 schemes
- kind: domain-security
  name: Keycorp Domain Security
  slug: keycorp-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: keycorp
tags:
- Banking
- Commercial Banking
- Financial Services
- Fortune 500
- Payments
- United States
- Super-Regional Bank
- Treasury Management
- Embedded Banking
- ACH
- Real-Time Payments
- Wire Transfer
website: https://www.key.com/
---
