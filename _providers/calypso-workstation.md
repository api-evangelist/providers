---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'Calypso Workstation is the end-user desktop application for the Nasdaq Calypso platform. It delivers real-time market data, trade entry, order management, risk monitoring, P&L, scenario analysis, and '
  name: Calypso Workstation
  slug: calypso-workstation
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calypso-workstation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaq.com/products/fintech/calypso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nasdaq.com/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nasdaq.com/legal
- group: operate
  title: ''
  type: Support
  url: https://www.nasdaq.com/contact-us
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.nasdaq.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: security/calypso-workstation-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/calypso-workstation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/calypso-workstation-vulnerability-disclosure.yml
- group: learn
  title: ''
  type: Learning
  url: https://learncalypso.nasdaq.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/calypso-workstation-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Nasdaq publishes no API reference for Calypso at all — the product and Front Office Workstation pages contain zero mentions of an API — and the Calypso technical documentation reachable from them lives in the Okta-authenticated Nasdaq Customer Portal, where /client/resources 302s to /auth/login; the pre-acquisition calypso.com domain that once carried the developer surface now resolves to 72.167.45.186 and times out on both 80 and 443.
  evidence:
  - status: 302
    url: https://customerportal.nasdaq.com/client/resources
  - status: 200
    url: https://www.nasdaq.com/products/fintech/calypso
  - status: 404
    url: https://www.nasdaq.com/openapi.json
  - status: 0
    url: https://www.calypso.com/
  reason: customer-only-docs
  state: gated
created: '2024-01-15'
description: Nasdaq Calypso Workstation is the user-facing desktop component of the Nasdaq Calypso (formerly Adenza / Calypso Technology) capital markets platform. It gives capital markets professionals access to market data, trading operations, risk management, and portfolio analytics across asset classes. The Workstation is an integrated client application rather than a publicly documented REST API; programmatic integration is delivered through the broader Calypso platform interfaces used by banks, asset managers, central banks, and clearing houses.
finops:
- name: Calypso Workstation Finops
  service_category: API
  slug: calypso-workstation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calypso-workstation.png
layout: provider
modified: '2026-04-23'
name: Calypso Workstation
nav: Providers
network: true
overview: 'Calypso Workstation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Capital Markets, Financial Technology, Market Data, Portfolio-Management, and Risk Management.


  Calypso Workstation''s developer surface includes support and 10 more developer resources.'
plans:
- name: Calypso Workstation Plans Pricing
  plan_count: 0
  slug: calypso-workstation-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Calypso Workstation Rate Limits
  slug: calypso-workstation-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/calypso-workstation/refs/heads/main/screenshots/calypso-workstation-2026-06-20T173905.png
security:
- kind: domain-security
  name: Calypso Workstation Domain Security
  slug: calypso-workstation-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Calypso Workstation Vulnerability Disclosure
  slug: calypso-workstation-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Calypso Workstation Trust Center
  slug: calypso-workstation-trust-center
  summary_line: trust center published
slug: calypso-workstation
tags:
- Capital Markets
- Financial Technology
- Market Data
- Portfolio-Management
- Risk Management
- Trading
website: https://www.nasdaq.com/products/fintech/calypso
---
