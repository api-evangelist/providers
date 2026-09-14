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
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.moneyboxapp.com/
- group: company
  title: ''
  type: Blog
  url: https://www.moneyboxapp.com/tech-blog/
- group: operate
  title: ''
  type: Support
  url: https://www.moneyboxapp.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moneyboxapp.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moneyboxapp.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MoneyBox
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/moneybox-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moneybox-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moneybox-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moneybox-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moneybox-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/moneybox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moneybox-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moneybox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/moneybox-vulnerability-disclosure.yml
coverage:
  checked: '2026-08-26'
  detail: Moneybox is a consumer savings and investing app that CONSUMES bank open banking APIs as a listed UK account aggregator; it ships no developer portal, no API reference and no machine-readable contract, and 7,075 archived moneyboxapp.com URLs contain not one /api, /developers or /docs path.
  evidence:
  - status: 200
    url: https://www.openbanking.org.uk/apps/moneybox-2/
  - status: 200
    url: https://apitracker.io/a/moneyboxapp
  - status: 403
    url: https://api.moneyboxapp.com/openapi.json
  - status: 200
    url: https://www.moneyboxapp.com/.well-known/security.txt
  - status: 200
    url: https://api.github.com/orgs/MoneyBox/repos
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Moneybox is a London-based digital wealth management company, operating as Digital Moneybox Limited, whose mobile app helps people in the United Kingdom save and invest — round-ups on everyday spending, Stocks & Shares ISAs, Cash ISAs, Lifetime ISAs, general investment accounts, savings accounts and personal pensions including pension consolidation. It is authorised and regulated by the Financial Conduct Authority and appears in the UK Open Banking app directory as an account aggregator, meaning it CONSUMES bank open banking APIs to read customer transactions rather than publishing an API of its own. As profiled on 2026-08-26, Moneybox runs no public developer program: no developer portal, API reference, machine-readable specification, SDK, sandbox or partner API surface exists on any Moneybox-controlled host. The one machine-readable artifact it publishes is an RFC 9116 security.txt served from every moneyboxapp.com host.'
image: https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/d2/28/64/d2286435-aee9-3e84-5794-af0a706a247a/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/512x512bb.jpg
layout: provider
modified: '2026-08-26'
name: Moneybox
nav: Providers
network: true
overview: 'Moneybox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Wealth Management, and Savings.


  Moneybox''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Moneybox Plans Pricing
  plan_count: 0
  slug: moneybox-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Moneybox Rate Limits
  slug: moneybox-rate-limits
security:
- kind: domain-security
  name: Moneybox Domain Security
  slug: moneybox-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Moneybox Vulnerability Disclosure
  slug: moneybox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: moneybox
tags:
- Company
- Financial-Services
- Fintech
- Wealth Management
- Savings
- Investing
- Pensions
- Open Banking
- Consumer Finance
- Mobile Apps
- United Kingdom
website: https://www.moneyboxapp.com/
---
