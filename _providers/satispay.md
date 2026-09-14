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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 3
apis:
- baseURL: https://authservices.satispay.com/g_business/v1
  baseurl_source: declared
  description: The Authentication Keys API from Satispay — 1 operation(s) for authentication keys.
  name: Satispay Authentication Keys API
  slug: satispay-authentication-keys-api
- baseURL: https://authservices.satispay.com/g_business/v1
  baseurl_source: declared
  description: The G Business API from Satispay — 13 operation(s) for g business.
  name: Satispay G Business API
  slug: satispay-g-business-api
- baseURL: https://authservices.satispay.com/g_business/v1
  baseurl_source: declared
  description: The Payments API from Satispay — 6 operation(s) for payments.
  name: Satispay Payments API
  slug: satispay-payments-api
- baseURL: https://authservices.satispay.com/g_business/v1
  baseurl_source: declared
  description: The Reports API from Satispay — 1 operation(s) for reports.
  name: Satispay Reports API
  slug: satispay-reports-api
- baseURL: https://authservices.satispay.com/g_business/v1
  baseurl_source: declared
  description: The Wally Services API from Satispay — 1 operation(s) for wally services.
  name: Satispay Wally Services API
  slug: satispay-wally-services-api
artifact_total: 11
asyncapis:
- description: ''
  name: Satispay Webhooks
  slug: satispay-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/satispay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/satispay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/satispay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.satispay.com/it-it/business
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.satispay.com/docs/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://developers.satispay.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developers.satispay.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.satispay.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.satispay.com/en/business
- group: company
  title: ''
  type: Blog
  url: https://www.satispay.com/it-it/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/satispay
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.satispay.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.satispay.com/it-it/business/costi/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.satispay.com/it-it/legal-hub/condizioni-generali/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.satispay.com/it-it/legal-hub/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.satispay.com/changelog
- group: build
  title: ''
  type: Packages
  url: packages/satispay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/satispay-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/satispay-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/satispay-security.txt
- group: auth
  title: ''
  type: Security
  url: security/satispay-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/satispay-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/satispay-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/satispay-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/satispay-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/satispay-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/satispay-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/satispay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/satispay-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/satispay-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/satispay-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/satispay-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/satispay-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/satispay-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/satispay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/satispay-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/satispay-gbusiness-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/satispay-production-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/satispay-sandbox-overlay.yaml
created: '2026-08-26'
description: Satispay is an Italian mobile payment network and e-money institution, founded in 2013 and headquartered in Milan, that lets consumers pay merchants directly from a bank account without card rails. For developers it publishes the Satispay GBusiness API — an HTTPS/JSON payments API served from authservices.satispay.com with a staging twin at staging.authservices.satispay.com — covering one-off payments (QR match-code, phone match-user, HOTP), automatic/pre-authorized recurring payments, funds lock, refunds, consumer lookup, shop profile, MQTT certificates for in-store devices, checkout sessions, daily closures and transaction reports. Authentication is RSA request signing following the "Signing HTTP Messages" (Cavage) draft rather than OAuth, POSTs accept an Idempotency-Key header, and payment status changes are delivered to a merchant callback_url. Satispay also ships first-party e-commerce plugins (Shopify, Shopware, WooCommerce, PrestaShop, Magento 2), a PHP SDK, and in-store
  Java and Swift SDKs.
image: https://www.satispay.com/favicon.ico
layout: provider
modified: '2026-08-26'
name: Satispay
nav: Providers
network: true
overview: 'Satispay publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication Keys API, G Business API, Payments API, and 2 more. Tagged areas include Payments, Mobile Payments, Fintech, E-Money, and E-Commerce.


  The Satispay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Satispay''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 33 more developer resources.'
plans:
- name: Satispay Plans Pricing
  plan_count: 2
  slug: satispay-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Satispay Rate Limits
  slug: satispay-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/satispay/refs/heads/main/screenshots/satispay-2026-09-02T154428.png
security:
- kind: authentication
  name: Satispay Authentication
  slug: satispay-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Satispay Domain Security
  slug: satispay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Satispay Vulnerability Disclosure
  slug: satispay-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: satispay
tags:
- Payments
- Mobile Payments
- Fintech
- E-Money
- E-Commerce
- Italy
- Europe
- Merchant Services
- Recurring Payments
- Refunds
- Meal Vouchers
- Company
website: https://www.satispay.com/it-it/business
---
