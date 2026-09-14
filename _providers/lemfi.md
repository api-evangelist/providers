---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lemfi-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lemfi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/lemfi-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lemfi-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/lemfi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lemfi-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lemfi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemfi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lemfi.com/en-us/
- group: company
  title: ''
  type: Blog
  url: https://blog.lemfi.com/
- group: operate
  title: ''
  type: Support
  url: https://lemfi.com/en-us/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.lemfi.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lemfi.com/en-us/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lemfi.com/en-us/legal/mobile-privacy
- group: auth
  title: ''
  type: Security
  url: https://lemfi.com/en-us/legal/vulnerability-disclosure-policy
coverage:
  checked: '2026-08-25'
  detail: LemFi is a consumer remittance app with no developer program at all — api., developer., developers., docs., business., partner. and sandbox..lemfi.com do not resolve in DNS, /en-us/developers and /en-us/api 404 on the Nuxt site, no GitHub organisation exists (github.com/lemfi is an unrelated individual), and no npm, PyPI, RubyGems or Packagist package is published; the only LemFi-controlled API host, api.lemonade.finance, is the private AWS API Gateway behind the mobile apps and answers 403 "Missing Authentication Token" on every path.
  evidence:
  - status: 404
    url: https://lemfi.com/en-us/developers
  - status: 404
    url: https://lemfi.com/en-us/api
  - status: 403
    url: https://api.lemonade.finance/openapi.json
  - status: 404
    url: https://lemfi.com/.well-known/agent-card.json
  - status: 404
    url: https://lemfi.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'LemFi (formerly Lemonade Finance) is a London-headquartered cross-border payments and remittance fintech built for immigrant communities, operating as a regulated Electronic Money Institution in the UK and as a FinCEN-registered money services business in the US through Pomelo Two US LLC (NMLS 2523778). Its consumer mobile apps let customers hold multi-currency balances, receive local bank details in their country of residence, request money, buy eSIM data, and send international transfers to 30+ receive markets across Africa, Asia, Europe and Latin America via direct integrations with tier-1 local banks. LemFi is a consumer-app company: as of this profile it publishes no developer portal, no public API reference, no OpenAPI or other machine-readable contract, no SDKs and no sandbox. What it does publish publicly is a Secureframe-hosted trust center naming SOC 2 Type II, PCI DSS Level 1, ISO 27001 and GDPR, and a formal vulnerability disclosure policy run through Inspectiv.'
image: https://lemfi.com/banner-bg.jpg
layout: provider
modified: '2026-08-25'
name: LemFi
nav: Providers
network: true
overview: 'LemFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Payments, and Remittances.


  LemFi''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Lemfi Plans Pricing
  plan_count: 0
  slug: lemfi-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Lemfi Rate Limits
  slug: lemfi-rate-limits
security:
- kind: domain-security
  name: Lemfi Domain Security
  slug: lemfi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lemfi Vulnerability Disclosure
  slug: lemfi-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lemfi Trust Center
  slug: lemfi-trust-center
  summary_line: SOC 2 Type II, PCI DSS, ISO 27001, GDPR
slug: lemfi
tags:
- Company
- Financial-Services
- Fintech
- Payments
- Remittances
- Cross-Border Payments
- Money Transfer
- Consumer Finance
- Mobile Banking
- eSIM
website: https://lemfi.com/en-us/
---
