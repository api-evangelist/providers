---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'REST API providing partner access to OnDeck''s small business lending platform, supporting credit pre-qualifications, loan application submission, business health score retrieval via the OnDeck Score, '
  name: OnDeck Lending API
  slug: ondeck-lending-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: Security
  url: https://www.ondeck.com/security-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ondeck-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinodf.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinodf.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://form.fillout.com/t/x2fuWdEqkSus
- group: operate
  title: ''
  type: Support
  url: https://admissions.joinodf.com/
- group: operate
  title: ''
  type: Community
  url: https://community.joinodf.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ondeck-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ondeck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ondeck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ondeck.com/partner
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ondeck/
- group: other
  title: ''
  type: X
  url: https://twitter.com/OnDeckCapital/
- group: company
  title: ''
  type: Blog
  url: https://www.ondeck.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ondeck.com/partner
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/ondeck/refs/heads/main/plans/ondeck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/ondeck/refs/heads/main/rate-limits/ondeck-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/ondeck/refs/heads/main/finops/ondeck-finops.yml
created: '2026-06-13'
description: OnDeck is a small business lending platform that provides partner APIs for submitting loan applications, checking business health scores via the OnDeck Score, managing loan products including term loans and lines of credit, and processing repayments. The API enables banks, brokers, and online service providers to embed OnDeck lending capabilities directly into their own platforms through credit pre-qualification, pre-approval, and full loan application submission workflows. OnDeck is an Enova International brand serving 185,000+ small businesses with $25 billion+ in capital delivered.
finops:
- name: Ondeck Finops
  service_category: ''
  slug: ondeck-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ondeck.png
layout: provider
modified: '2026-06-13'
name: OnDeck
nav: Providers
network: true
overview: 'OnDeck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Small Business Lending, Fintech, Loans, Credit Scoring, and Business Health.


  OnDeck''s developer surface includes signup flow, support, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Ondeck Plans Pricing
  plan_count: 1
  slug: ondeck-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Ondeck Rate Limits
  slug: ondeck-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/ondeck/refs/heads/main/screenshots/ondeck-2026-06-20T190706.png
security:
- kind: domain-security
  name: Ondeck Domain Security
  slug: ondeck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ondeck Vulnerability Disclosure
  slug: ondeck-vulnerability-disclosure
  summary_line: Hackerone
slug: ondeck
tags:
- Small Business Lending
- Fintech
- Loans
- Credit Scoring
- Business Health
- Term Loans
- Line of Credit
- Loan Origination
website: https://www.ondeck.com/
---
