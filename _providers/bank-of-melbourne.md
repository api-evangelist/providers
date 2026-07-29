---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bank Of Melbourne Agentic Access
  operation_count: 19
  slug: bank-of-melbourne-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 5
apis:
- description: PUBLIC, unauthenticated Consumer Data Right (CDR) Product Reference Data API exposing Bank of Melbourne's banking products (term deposits, credit and charge cards, personal loans, residential mortgage
  name: Bank of Melbourne CDR Product Reference Data API
  slug: bank-of-melbourne-cdr-product-reference-data-api
- description: CONSUMER-AUTHORIZED Consumer Data Right (CDR) Accounts & Balances surface of the shared DSB Banking API that Bank of Melbourne implements as an accredited CDR data holder on shared Westpac Group infra
  name: Bank of Melbourne CDR Accounts & Balances API
  slug: bank-of-melbourne-cdr-accounts-balances-api
- description: CONSUMER-AUTHORIZED Consumer Data Right (CDR) Transactions surface of the shared DSB Banking API implemented by Bank of Melbourne as an accredited CDR data holder. Access requires an Accredited Data R
  name: Bank of Melbourne CDR Transactions API
  slug: bank-of-melbourne-cdr-transactions-api
- description: CONSUMER-AUTHORIZED Consumer Data Right (CDR) Direct Debits and Scheduled Payments surface of the shared DSB Banking API implemented by Bank of Melbourne as an accredited CDR data holder. Access requi
  name: Bank of Melbourne CDR Direct Debits & Scheduled Payments API
  slug: bank-of-melbourne-cdr-direct-debits-scheduled-payments-api
- description: CONSUMER-AUTHORIZED Consumer Data Right (CDR) Payees surface of the shared DSB Banking API implemented by Bank of Melbourne as an accredited CDR data holder. Access requires an Accredited Data Recipie
  name: Bank of Melbourne CDR Payees API
  slug: bank-of-melbourne-cdr-payees-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-of-melbourne-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bank-of-melbourne-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-melbourne-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bankofmelbourne.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankofmelbourne.com.au/online-services/open-banking
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankofmelbourne.com.au/help/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankofmelbourne.com.au/privacy/privacy-statement
- group: auth
  title: ''
  type: Security
  url: https://www.bankofmelbourne.com.au/online-services/security-centre
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-of-melbourne-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bank-of-melbourne-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bank-of-melbourne-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bank-of-melbourne-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bank-of-melbourne-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bank-of-melbourne-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bank-of-melbourne-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-of-melbourne-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bank-of-melbourne-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bank-of-melbourne-browse-products.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bank-of-melbourne-llms.txt
created: '2026-07-20'
description: Bank of Melbourne is a Victorian retail and business banking brand operated by Westpac Banking Corporation (ASX code WBC) as part of the Westpac Group. The original Bank of Melbourne was acquired by Westpac in 1997 and the brand was relaunched in 2011; today it operates under the St.George Bank banking authority within Westpac and is NOT a customer-owned mutual - it is a division of a publicly listed, APRA-regulated authorised deposit-taking institution (ADI). As an accredited Consumer Data Right (CDR) data holder, Bank of Melbourne exposes a public, unauthenticated Product Reference Data (PRD) API that conforms to the Australian Consumer Data Standards, confirmed live on shared Westpac Group infrastructure at digital-api.bankofmelbourne.com.au. Consumer data sharing runs through the regulated CDR / Accredited Data Recipient (ADR) model using OAuth2 / OpenID Connect (FAPI) authorization; the bank does not run a broader third-party developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-of-melbourne.png
layout: provider
mcp_servers:
- description: ''
  name: bank-of-melbourne-mcp.yml
  slug: bank-of-melbourne-mcpyml
modified: '2026-07-21'
name: Bank of Melbourne
nav: Providers
network: true
overview: 'Bank of Melbourne publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CDR Product Reference Data API, CDR Accounts & Balances API, CDR Transactions API, and 2 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Bank of Melbourne''s developer surface includes documentation, authentication, and 17 more developer resources.'
random_paper: 67
score:
  band: thin
  composite: 32.7
  delta: -5.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 32.3
    developer_ergonomics: 23.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 18.4
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-melbourne/refs/heads/main/screenshots/bank-of-melbourne-2026-07-21T114702.png
security:
- kind: authentication
  name: Bank Of Melbourne Authentication
  slug: bank-of-melbourne-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bank Of Melbourne Domain Security
  slug: bank-of-melbourne-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bank Of Melbourne Vulnerability Disclosure
  slug: bank-of-melbourne-vulnerability-disclosure
  summary_line: disclosure policy published
slug: bank-of-melbourne
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
- Westpac Group
website: https://www.bankofmelbourne.com.au/
---
