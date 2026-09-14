---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 2
apis:
- description: The buyer-side integration API described in the SAP Taulia Description of Software Services. It carries the accounts-payable object set — supplier master, business unit, purchase orders, invoices, pay
  name: Taulia Buyer API
  slug: taulia-buyer-api
- description: 'The supplier-side integration API described in the SAP Taulia Description of Software Services. It exchanges information between the Taulia Platform and a supplier''s accounts-receivable data: submitti'
  name: Taulia Supplier API
  slug: taulia-supplier-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://taulia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.taulia.com/technical-resources
- group: start
  title: ''
  type: GettingStarted
  url: https://support.taulia.com/article/Easy-Guide-to-Activating-SAP-Taulia-with-S-4HANA-Cloud-Public-Edition
- group: operate
  title: ''
  type: Support
  url: https://support.taulia.com/contactsupport
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.taulia.com/
- group: company
  title: ''
  type: Blog
  url: https://taulia.com/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://taulia.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taulia
- group: start
  title: ''
  type: Login
  url: https://login.na1prd.taulia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taulia.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taulia.com/privacy-statement/
- group: auth
  title: ''
  type: Compliance
  url: https://taulia.com/sap-taulia-agreements/
- group: other
  title: ''
  type: Glossary
  url: https://taulia.com/glossary/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.taulia.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taulia-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/taulia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/taulia-security.txt
- group: auth
  title: ''
  type: Security
  url: security/taulia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/taulia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taulia-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/taulia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taulia-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/taulia-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taulia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taulia-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/taulia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taulia-rate-limits.yml
created: '2026-08-29'
description: 'SAP Taulia is a working-capital and cash-flow acceleration platform for enterprises, their suppliers and their funding partners. Acquired by SAP in 2022 and now operated as SAP Taulia, it runs supply chain finance, dynamic discounting, ERP-embedded virtual cards, receivables finance, inventory finance, supplier self-service and supplier information management across SAP and non-SAP ERP estates. Its programmatic surface is an enterprise integration estate rather than a public developer platform: a Taulia Buyer API and Taulia Supplier API described in the Description of Software Services, an XMLRPC interface monitored per region on the public status page, a Taulia Connector supporting SFTP, AS2 and HTTP with EDI, cXML and XML payloads, and ERP add-ons for SAP, SAP Integration Suite managed gateway and Oracle EBS. No OpenAPI, AsyncAPI, GraphQL SDL, WSDL, Postman collection or SDK is published anywhere, and API credentials are provisioned during onboarding rather than through self-service.'
image: https://taulia.com/wp-content/uploads/2025/04/android-chrome-512x512-1-300x300.png
layout: provider
modified: '2026-08-29'
name: Taulia
nav: Providers
network: true
overview: 'Taulia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Working Capital, Supply Chain Finance, Dynamic Discounting, and Accounts Payable.


  Taulia''s developer surface includes documentation, getting-started guide, support, engineering blog, changelog, authentication, and 21 more developer resources.'
plans:
- name: Taulia Plans Pricing
  plan_count: 0
  slug: taulia-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Taulia Rate Limits
  slug: taulia-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/taulia/refs/heads/main/screenshots/taulia-2026-09-02T162611.png
security:
- kind: authentication
  name: Taulia Authentication
  slug: taulia-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Taulia Domain Security
  slug: taulia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Taulia Vulnerability Disclosure
  slug: taulia-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Taulia Trust Center
  slug: taulia-trust-center
  summary_line: SSAE SOC 1 Type 2, PCI DSS (website scanning), GDPR / data protection, Export control and sanctions compliance
slug: taulia
tags:
- Company
- Working Capital
- Supply Chain Finance
- Dynamic Discounting
- Accounts Payable
- Accounts Receivable
- Invoicing
- Payments
- Procurement
- Financial-Services
- ERP Integration
- SAP
website: https://taulia.com/
---
