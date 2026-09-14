---
api_count: 0
artifact_total: 3
common:
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/advancetechlending-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/advancetechlending-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advancetechlending-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/advancetechlending-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advancetechlending-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advance.ph/
- group: company
  title: ''
  type: About
  url: https://advance.ph/about
- group: operate
  title: ''
  type: Support
  url: https://advance.ph/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://advance.ph/faqs
- group: company
  title: ''
  type: Blog
  url: https://advance.ph/blog
- group: start
  title: ''
  type: SignUp
  url: https://advance.ph/sign-up
- group: start
  title: ''
  type: Login
  url: https://advance.ph/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://advance.ph/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://advance.ph/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/advancetechlending
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/advancetechlending
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/advance-tech-lending
coverage:
  checked: '2026-09-09'
  detail: Advance Tech Lending publishes nothing developer-facing on its own hosts - advance.ph is a 15-page Webflow marketing site whose complete sitemap contains no /developers, /docs or /api path, api.advance.ph does not resolve in DNS, and partner.advance.ph redirects every path to /login?next=/ - so the only externally visible API for an Advance product is the third-party "Salary Loan by Advance Tech" partner listing inside UnionBank's api.ph marketplace, which itself answered 503 from its Akamai edge on every request during this pass.
  evidence:
  - status: 503
    url: https://api.ph/marketplace/partner-advance-lending/83/business/overview
  - status: 200
    url: https://advance.ph/sitemap.xml
  - status: 404
    url: https://advance.ph/openapi.json
  - status: 404
    url: https://advance.ph/.well-known/api-catalog
  - status: 200
    url: https://partner.advance.ph/
  - status: 404
    url: https://partner.advance.ph/openapi.json
  reason: marketplace-only
  state: gated
created: '2026-09-09'
description: 'Advance Tech Lending Inc. (operating as Advance, advance.ph) is a Philippine fintech lender founded in 2018 by Jaime de los Angeles and Addi Guevara and headquartered in Taguig, Metro Manila. It operates an on-demand salary access and working-capital platform for Southeast Asia: employees of enrolled employers can draw a Salary Advance of up to 50% of their monthly basic salary, and businesses can unlock cash through Direct Disbursement (invoice/receivables financing) and Payroll Disbursement (payroll funding during cash-flow gaps). The company is registered with the Philippine SEC (Company Reg. No. CS201819635) and holds Certificate of Authority No. 2765 as a lending company, and has raised roughly USD 16-17M in pre-Series A funding from investors including Accion Venture Lab, Lendable, Next Billion Ventures and Do Ventures. As of this profile Advance publishes no first-party developer program, API reference or machine-readable API contract: advance.ph is a 15-page marketing
  site with no developer path, partner.advance.ph redirects every path to a login, and the only externally visible API listing for its salary-loan product sits inside UnionBank''s api.ph partner marketplace.'
image: https://cdn.prod.website-files.com/65f7b73881129a65c906fbaa/6603cdd2a7f553cc07e761db_Logo%20Blue.png
layout: provider
modified: '2026-09-09'
name: Advance Tech Lending
nav: Providers
network: true
overview: 'Advance Tech Lending is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Fintech, Lending, Salary Advance, and Earned Wage Access.


  Advance Tech Lending''s developer surface includes support, engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Advancetechlending Plans Pricing
  plan_count: 0
  slug: advancetechlending-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Advancetechlending Rate Limits
  slug: advancetechlending-rate-limits
security:
- kind: domain-security
  name: Advancetechlending Domain Security
  slug: advancetechlending-domain-security
  summary_line: TLSv1.2 · DMARC
slug: advancetechlending
tags:
- Financial Services
- Fintech
- Lending
- Salary Advance
- Earned Wage Access
- Invoice Financing
- Payroll
- Employee Benefits
- Philippines
- Southeast Asia
- Company
website: https://advance.ph/
---
