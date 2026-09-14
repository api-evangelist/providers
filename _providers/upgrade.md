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
api_count: 3
apis:
- baseURL: https://partner.upgrade.com/api/flexpay
  baseurl_source: declared
  description: Marketing Offers API
  name: Upgrade Marketing Offers API
  slug: upgrade-marketing-offers-api
- baseURL: https://partner.upgrade.com/api/flexpay
  baseurl_source: declared
  description: Checkout Orders API
  name: Upgrade Orders API
  slug: upgrade-orders-api
- baseURL: https://partner.upgrade.com/api/flexpay
  baseurl_source: declared
  description: Transactions API (Direct Settle disbursement)
  name: Upgrade Transactions API
  slug: upgrade-transactions-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flex Pay API (Upgrade) Marketing Offers API
  slug: open-upgrade-marketing-offers-api
- collection_type: open
  name: Flex Pay API (Upgrade) Marketing Offers Orders API
  slug: open-upgrade-orders-api
- collection_type: open
  name: Flex Pay API (Upgrade) Marketing Offers Transactions API
  slug: open-upgrade-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/upgrade-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/upgrade-flexpay-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/upgrade-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.upgrade.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upgrade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upgrade.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.uplift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uplift.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.uplift.com/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.uplift.com/docs/how-to-use-this-guide
- group: operate
  title: ''
  type: Support
  url: https://www.upgrade.com/help/
- group: auth
  title: ''
  type: Authentication
  url: authentication/upgrade-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upgrade-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/upgrade-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/upgrade-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/upgrade-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/upgrade-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/upgrade-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/upgrade-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/upgrade-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/upgrade-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/upgrade-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.upgrade.com/security/
- group: build
  title: ''
  type: Packages
  url: packages/upgrade-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/upgrade-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/upgrade-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upgrade.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upgrade.com/funnel/borrower-documents/TERMS_OF_USE
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upgrade.com/funnel/borrower-documents/PRIVACY_POLICY?productType=PERSONAL_LOAN
- group: start
  title: ''
  type: Login
  url: https://www.upgrade.com/portal/
created: '2026-07-17'
description: 'Upgrade is a San Francisco-based consumer fintech offering personal loans, the Upgrade Card, Rewards Checking, savings accounts, and Flex Pay — the buy now, pay later platform formerly known as Uplift, serving travel and retail merchants in the US and Canada. Upgrade is a financial technology company, not a bank; products are offered through bank partners. Its developer surface is the Flex Pay partner platform: OAuth 2.0-secured Marketing Offers, Checkout Orders, and Transactions REST APIs, an embeddable up.js checkout with the up-from-pricing web component, and iOS/Android SDKs, documented at docs.uplift.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upgrade.png
layout: provider
modified: '2026-07-21'
name: Upgrade
nav: Providers
network: true
overview: 'Upgrade publishes 3 APIs on the [APIs.io](https://apis.io/) network: Marketing Offers API, Orders API, and Transactions API. Tagged areas include Company, Fintech, Lending, Buy Now Pay Later, and Payments.


  Upgrade''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 25 more developer resources.'
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/upgrade/refs/heads/main/screenshots/upgrade-2026-08-17T082636.png
security:
- kind: authentication
  name: Upgrade Authentication
  slug: upgrade-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Upgrade Domain Security
  slug: upgrade-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Upgrade Vulnerability Disclosure
  slug: upgrade-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Upgrade Trust Center
  slug: upgrade-trust-center
  summary_line: SOC 2, ISO 27001
slug: upgrade
tags:
- Company
- Fintech
- Lending
- Buy Now Pay Later
- Payments
- Credit Cards
- Banking
- Travel
website: https://www.upgrade.com
---
