---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://kotak.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.kotak.bank.in/en/home.html — a different registrable domain (kotak.com -> bank.in), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'The Kotak Mahindra Bank enterprise open-banking API platform. A curated corporate banking API stack of 39 published API products across six categories — Account Services, Payment Services, Collection '
  name: Kotak API Platform
  slug: kotak-api-platform
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://kotak.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.kotak.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.kotak.bank.in/en/open-banking.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.kotak.bank.in/explore
- group: start
  title: ''
  type: GettingStarted
  url: https://api.kotak.bank.in/auth/registration
- group: start
  title: ''
  type: SignUp
  url: https://api.kotak.bank.in/auth/registration
- group: start
  title: ''
  type: Login
  url: https://api.kotak.bank.in/auth/login
- group: operate
  title: ''
  type: Support
  url: https://api.kotak.bank.in/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.kotak.bank.in/en/help-center.html
- group: operate
  title: ''
  type: FAQ
  url: https://api.kotak.bank.in/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.kotak.bank.in/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kotak.com/en/privacy-policy.html
- group: company
  title: ''
  type: Partners
  url: https://api.kotak.bank.in/connectedbanking
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kotak-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kotak-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kotak-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kotak-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kotak-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kotak-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/kotak-api-catalog.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kotak-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kotak-llms.txt
created: '2026-07-17'
description: Kotak Mahindra Bank Limited is an Indian private-sector bank headquartered in Mumbai, and the first non-banking finance company in India to convert into a full commercial bank. Alongside retail, corporate, and NRI banking it operates the Kotak API Platform (api.kotak.com), an enterprise open-banking developer portal offering a curated stack of corporate banking APIs across six product categories — Account Services (balance enquiry, account statement), Payment Services (24x7 NEFT/RTGS/IFT, CMS bulk payments, corporate IMPS remittance, name enquiry, UPI merchant cashback), Collection Services (UPI web collect and autopay, e-collection virtual accounts, NACH physical/e-mandate/Aadhaar e-mandate, BBPS agent and biller integration, direct debit queryback), Trade Finance (import/export letters of credit, standby LCs, bankers guarantees, collections, inward/outward remittance, shipping guarantee, document upload), Onboarding (application, dedupe, offers, OTP), and Authorization Services
  (OAuth 2.0 access tokens). The platform is aimed at fintechs, ERP providers, and NBFCs through its Connected Banking partner program, and pairs an integrated sandbox testing environment with per-product documentation and downloadable kits that are released after developer registration and login.
image: https://api.kotak.bank.in/commonIcons/API_Banking_Kotak_Bank_Logo.png
layout: provider
modified: '2026-07-19'
name: Kotak Mahindra Bank
nav: Providers
network: true
overview: 'Kotak Mahindra Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial-Services, Open Banking, and Payments.


  Kotak Mahindra Bank''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, FAQ, sandbox, and 15 more developer resources.'
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/kotak/refs/heads/main/screenshots/kotak-2026-07-25T224245.png
security:
- kind: authentication
  name: Kotak Authentication
  slug: kotak-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Kotak Domain Security
  slug: kotak-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: kotak
tags:
- Company
- Banking
- Financial-Services
- Open Banking
- Payments
- Collection
- Trade Finance
- Corporate Banking
- India
- UPI
website: https://kotak.com
---
