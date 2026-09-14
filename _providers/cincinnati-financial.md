---
access_model:
  confidence: medium
  label: No fee at present, but access is granted only after a named individual at a named organization accepts the API Terms and Conditions Agreement and Cincinnati responds.
  onboarding: unknown
  pricing: free
  public: false
  source:
  - https://www.cinfin.com/legal/api-terms-conditions-acceptance
  - https://edge.sitecorecloud.io/cincinna-x33xq9h6/media/Project/Cincinnati-Financial/CinFin/Files/api-terms-conditions.pdf
  trial: false
  try_now: false
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cincinnati-financial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cincinnati-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cinfin.com/
- group: company
  title: ''
  type: About
  url: https://www.cinfin.com/about-us
- group: other
  title: ''
  type: AgentLocator
  url: https://www.cinfin.com/cincinnati-insurance-agents
- group: start
  title: ''
  type: PolicyholderPortal
  url: https://onlineservice.cinfin.com/b2c/Account_Self_Service/Login.aspx
- group: other
  title: ''
  type: MobileApp
  url: https://www.cinfin.com/mobile
- group: other
  title: ''
  type: Claims
  url: https://www.cinfin.com/contact-us/claims
- group: operate
  title: ''
  type: Support
  url: https://www.cinfin.com/contact-us/online-services-support
- group: operate
  title: ''
  type: FAQ
  url: https://www.cinfin.com/contact-us/faq
- group: other
  title: ''
  type: Accessibility
  url: https://www.cinfin.com/legal-footer/accessibility
- group: operate
  title: ''
  type: Contact
  url: https://www.cinfin.com/contact-us
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cincinnati-financial-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cincinnati-financial-security.txt
- group: auth
  title: ''
  type: Security
  url: security/cincinnati-financial-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cincinnati-financial-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cincinnati-financial-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cincinnati-financial-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cincinnati-financial-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cincinnati-financial-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cinfin.com/legal-footer/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cinfin.com/legal-footer/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://blog.cinfin.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.cinfin.com/legal/api-terms-conditions-acceptance
coverage:
  checked: '2026-09-05'
  detail: Cincinnati Insurance does run an API program — it publishes an API Terms and Conditions Agreement licensing "the Cincinnati Insurance APIs" and charges no fee for them — but the only public page in its 231-URL sitemap that touches the program is an acceptance form that collects name, email, title and organization behind a reCAPTCHA and answers "We'll be in contact with you shortly"; the per-API "API Policy" documentation the agreement incorporates by reference nine times is never published, and no OpenAPI, reference, base URL or auth scheme is reachable anonymously on any cinfin.com host.
  evidence:
  - status: 200
    url: https://www.cinfin.com/legal/api-terms-conditions-acceptance
  - status: 200
    url: https://edge.sitecorecloud.io/cincinna-x33xq9h6/media/Project/Cincinnati-Financial/CinFin/Files/api-terms-conditions.pdf
  - status: 302
    url: https://cincilink.cinfin.com/
  - status: 404
    url: https://www.cinfin.com/llms.txt
  - status: 0
    url: https://api.cinfin.com/openapi.json
  reason: sales-gate
  state: gated
created: '2025-02-21'
description: 'Cincinnati Financial Corporation (NASDAQ: CINF) is a property and casualty insurance holding company in Fairfield, Ohio, whose subsidiaries — The Cincinnati Insurance Company, The Cincinnati Indemnity Company, The Cincinnati Casualty Company, The Cincinnati Specialty Underwriters Insurance Company and The Cincinnati Life Insurance Company — market business, home, auto and life insurance plus fixed annuities exclusively through independent insurance agencies. Cincinnati Insurance does run an API program for integration partners: it publishes an API Terms and Conditions Agreement licensing "the Cincinnati Insurance APIs" and charges no fee at present. But that agreement is a legal instrument only — it names no protocol, endpoint or auth scheme, and the per-API "API Policy" it incorporates by reference is never published. Access starts with an acceptance form, after which Cincinnati contacts the applicant; there is no developer portal, public reference or machine-readable contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cincinnati-financial.png
layout: provider
modified: '2026-09-05'
name: Cincinnati Financial
nav: Providers
network: true
overview: 'Cincinnati Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Auto Insurance, Business Insurance, Financial-Services, Home Insurance, and Independent Agency.


  Cincinnati Financial''s developer surface includes support, FAQ, engineering blog, signup flow, and 20 more developer resources.'
plans:
- name: Cincinnati Financial Plans Pricing
  plan_count: 0
  slug: cincinnati-financial-plans-pricing
press:
- date: '2026-05-25'
  title: Cincinnati Financial Reports Second-Quarter 2025 Results
  url: https://investors.cinfin.com/2025-07-28-Cincinnati-Financial-Reports-Second-Quarter-2025-Results
- date: '2026-05-25'
  title: Cincinnati Financial shareholders reelect board - CINF
  url: https://www.stocktitan.net/news/CINF/cincinnati-financial-corporation-holds-shareholders-and-directors-2zkm6xgkc13f.html
- date: '2026-05-25'
  title: Cincinnati Financial Reports Fourth-Quarter and Full-Year ...
  url: https://www.prnewswire.com/news-releases/cincinnati-financial-reports-fourth-quarter-and-full-year-2025-results-302682915.html
- date: '2026-05-25'
  title: cinf-20260502
  url: https://www.sec.gov/Archives/edgar/data/20286/000002028626000030/cinf-20260502.htm
- date: '2026-05-25'
  title: News Releases
  url: https://investors.cinfin.com/2026-01-30-Cincinnati-Financial-Corporation-Increases-Regular-Quarterly-Cash-Dividend
random_paper: 18
rate_limits:
- limit_count: 0
  name: Cincinnati Financial Rate Limits
  slug: cincinnati-financial-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/cincinnati-financial/refs/heads/main/screenshots/cincinnati-financial-2026-06-20T174346.png
security:
- kind: domain-security
  name: Cincinnati Financial Domain Security
  slug: cincinnati-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cincinnati Financial Vulnerability Disclosure
  slug: cincinnati-financial-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cincinnati-financial
tags:
- Auto Insurance
- Business Insurance
- Financial-Services
- Home Insurance
- Independent Agency
- Insurance
- Life Insurance
- No Public API
- Property Casualty
- Fortune 1000
website: https://www.cinfin.com/
---
