---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: The Portico Gateway is Heartland's primary payment processing API for card-not-present and ecommerce transactions, supporting authorization, capture, refund, void, recurring billing, tokenization, and
  name: Heartland Portico Gateway API
  slug: portico-api
- description: Heartland's Card Present APIs support both semi-integrated and fully-integrated EMV solutions for in-person payments, including terminal SDKs, P2PE, and PIN debit handling.
  name: Heartland Card Present API
  slug: card-present-api
- description: The Heartland Bill Pay API enables invoice and bill payment processing for merchants accepting recurring or one-time bill payments from customers across multiple channels.
  name: Heartland Bill Pay API
  slug: bill-pay-api
- description: The Heartland Gift and Loyalty API supports stored value cards, gift card issuance and redemption, and loyalty program integration for merchants.
  name: Heartland Gift and Loyalty API
  slug: gift-loyalty-api
- description: Heartland's Payroll APIs support employee payroll processing, tax filings, and HR integrations for small to mid-sized businesses.
  name: Heartland Payroll API
  slug: payroll-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heartland-payment-systems-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heartland-payment-systems
- group: company
  title: ''
  type: Website
  url: https://www.heartland.us
- group: other
  title: ''
  type: ParentCompany
  url: https://www.globalpayments.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.globalpayments.com/heartland/getting-started/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developer.globalpayments.com/heartland/getting-started/overview
- group: design
  title: ''
  type: Testing
  url: https://developer.globalpayments.com/heartland/Certification/Testing
- group: operate
  title: ''
  type: Support
  url: mailto:onlinepayments@heartland.us
- group: operate
  title: ''
  type: Contact
  url: mailto:integratormanagement@e-hps.com
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.globalpayments.com/llms.txt
created: '2025'
description: Heartland Payment Systems is a payment processing company offering payroll, customer engagement, point-of-sale, and other business solutions to merchants across the United States. Heartland is now a brand of Global Payments, and developer resources for Heartland integrations are published through the Global Payments developer portal. The platform supports online and in-person payments, bill pay, IoT/connected device payments, gift and loyalty, payroll, and PCI-validated point-to-point encryption.
finops:
- name: Heartland Payment Systems Finops
  service_category: Payments
  slug: heartland-payment-systems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heartland-payment-systems.png
layout: provider
modified: '2026-04-28'
name: Heartland Payment Systems
nav: Providers
network: true
overview: 'Heartland Payment Systems publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bill Pay, Card Present, Card Not Present, E-Commerce, and Payment Processing.


  Heartland Payment Systems'' developer surface includes documentation, support, and 9 more developer resources.'
plans:
- name: Heartland Payment Systems Plans Pricing
  plan_count: 1
  slug: heartland-payment-systems-plans-pricing
press:
- date: '2026-05-25'
  title: Cybersecurity Impact on Audits and Financial Statement ...
  url: https://www.researchgate.net/publication/344096444_Heartland_Payment_Systems_Cybersecurity_Impact_on_Audits_and_Financial_Statement_Contingencies
- date: '2026-05-25'
  title: Data Theft Hits the Heartland
  url: https://redmondmag.com/articles/2009/01/21/data-theft-hits-the-heartland.aspx?admgarea=BDNA
- date: '2026-05-25'
  title: Heartland Founder, Philanthropist, and Author Robert O. ...
  url: https://www.prnewswire.com/news-releases/heartland-founder-philanthropist-and-author-robert-o-carr-launches-beyond--an-employee-owned-pos-payments-lending-vending-integrated-hr-tools--services-company-300448840.html
- date: '2026-05-25'
  title: Heartland Adds ACH To Its Remote-Deposit Service
  url: https://www.americanbanker.com/payments/news/heartland-adds-ach-to-its-remote-deposit-service
- date: '2026-05-25'
  title: Liquid Payments' Integration with Heartland, a Global ...
  url: https://www.fintechfutures.com/press-releases/liquid-payments-integration-with-heartland-a-global-payments-company-is-good-news-for-healthcare-providers
random_paper: 12
rate_limits:
- limit_count: 1
  name: Heartland Payment Systems Rate Limits
  slug: heartland-payment-systems-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heartland-payment-systems/refs/heads/main/screenshots/heartland-payment-systems-2026-06-20T182615.png
security:
- kind: domain-security
  name: Heartland Payment Systems Domain Security
  slug: heartland-payment-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: heartland-payment-systems
tags:
- Bill Pay
- Card Present
- Card Not Present
- E-Commerce
- Payment Processing
- Payments
- Payroll
- Point-of-Sale
- Fortune 1000
website: https://www.heartland.us
---
