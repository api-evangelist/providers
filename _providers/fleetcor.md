---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Corpay's commercial card portfolio covers the Corpay Mastercard, Corpay World Elite Mastercard, virtual / ghost cards, and supplier-direct payment cards. Integration with ERP and expense systems is de
  name: Corpay Commercial Cards
  slug: commercial-cards
- description: Corpay's AP automation platform covers invoice capture and approval routing, payments automation across virtual card / ACH / check, purchase order automation with PO-to-invoice matching, and pre-built
  name: Corpay AP Automation
  slug: ap-automation
- description: Corpay Cross-Border (formerly Cambridge Global Payments, acquired in 2017 for $690M, and further expanded by the 2025 $2.2B acquisition of Alpha Group International) processes 4.1+ million payments an
  name: Corpay Cross-Border Payments
  slug: cross-border
- description: The original FLEETCOR business line, covering fuel cards, fleet cards, and trucking-focused payments — including the Comdata brand (acquired 2014 for $3.45B) for the over-the-road trucking market. Car
  name: Corpay Fuel & Fleet Cards
  slug: fuel-fleet-cards
- description: Corpay's lodging and corporate travel offering for workforces with project, crew, and contractor lodging needs — booking, management, and consolidated billing. No public developer or API surface.
  name: Corpay Workforce Lodging & Travel
  slug: lodging
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fleetcor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.corpay.com
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.fleetcor.com
- group: company
  title: ''
  type: About
  url: https://www.corpay.com/about
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.corpay.com
- group: other
  title: ''
  type: NYSETicker
  url: https://www.nyse.com/quote/XNYS:CPAY
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/corpay
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corpay.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corpay.com/terms-of-use
- group: operate
  title: ''
  type: Contact
  url: https://www.corpay.com/contact
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Corpay
created: '2026-05-22'
description: 'Corpay is a global S&P 500 corporate payments company (NYSE: CPAY) that resulted from the March 2024 rebrand of FLEETCOR Technologies. The company serves more than 800,000 business clients across 200+ countries in 140+ currencies and processed approximately $400 billion in payments in 2024 with reported revenue of about $4.0B. Corpay operates across five product lines built largely through acquisition — Commercial Cards (including Corpay Mastercard), AP Automation (extended by the 2024 acquisition of Paymerang), Cross-Border Payments (built on the 2017 acquisition of Cambridge Global Payments and the 2025 acquisition of Alpha Group International), Fuel & Fleet Cards (the original FLEETCOR business plus the 2014 acquisition of Comdata), and Workforce Lodging & Travel. Despite this scale, Corpay does not operate a public developer portal — there is no developer.corpay.com, no public OpenAPI catalog, no public GitHub presence, and no self-service API key issuance. All integration
  surfaces (ERP connectors for NetSuite, Sage, Microsoft Dynamics, QuickBooks, Acumatica, CMiC, Deltek, Trimble; the former Cambridge cross-border payments API; AP-automation API hooks) are sales-led and gated behind enterprise contracts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fleetcor.png
layout: provider
modified: '2026-05-23'
name: Corpay (formerly FLEETCOR)
nav: Providers
network: true
overview: Corpay (formerly FLEETCOR) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include B2B Payments, Corporate Payments, Fleet Cards, Fuel Cards, and Commercial Cards.
random_paper: 32
score:
  band: minimal
  composite: 10.7
  delta: -2.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fleetcor/refs/heads/main/screenshots/fleetcor-2026-06-20T181309.png
security:
- kind: domain-security
  name: Fleetcor Domain Security
  slug: fleetcor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fleetcor
tags:
- B2B Payments
- Corporate Payments
- Fleet Cards
- Fuel Cards
- Commercial Cards
- AP Automation
- Accounts Payable
- Cross-Border Payments
- Foreign Exchange
- Lodging
- Expense Management
- ERP Integration
website: https://www.corpay.com
---
