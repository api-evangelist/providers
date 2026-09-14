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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marketerhire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marketerhire.com
- group: company
  title: ''
  type: Blog
  url: https://marketerhire.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://marketerhire.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://marketerhire.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://marketerhire.com/policies/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marketerhire.com/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MarketerHire
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/MarketerHire/mh-brain
- group: start
  title: ''
  type: SignUp
  url: https://app.marketerhire.com/sign-in
- group: operate
  title: ''
  type: FAQ
  url: https://marketerhire.com/faqs/all
- group: company
  title: ''
  type: Careers
  url: https://marketerhire.com/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marketerhire-llms.txt
coverage:
  checked: '2026-08-25'
  detail: MarketerHire sells human marketing talent through a Webflow marketing site and a sign-in-only client app; there is no developer portal, no API reference and no spec at any path or host — api./docs./developers.marketerhire.com resolve only via a wildcard Vercel DNS record and present no valid TLS certificate, and the only first-party HTTP service (BrightMatter, in github.com/MarketerHire/mh-brain) documents no base URL other than http://localhost:8100.
  evidence:
  - status: 404
    url: https://marketerhire.com/openapi.json
  - status: 404
    url: https://marketerhire.com/.well-known/api-catalog
  - status: 404
    url: https://marketerhire.com/llms.txt
  - status: 500
    url: https://app.marketerhire.com/openapi.json
  - status: 200
    url: https://marketerhire.com/pricing
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: MarketerHire is a curated marketing-talent marketplace that matches startups, growth-stage businesses and Fortune 500 brands with pre-vetted senior freelance and fractional marketers — growth marketers, paid-media buyers, SEO and content strategists, email/lifecycle specialists, brand and creative talent — typically within 48 hours, backed by a two-week trial. The company operates a public marketing site and blog on Webflow, a client/talent application at app.marketerhire.com, and a talent portal on talent.marketerhire.com. MarketerHire publishes no public developer program, API reference, or machine-readable API contract; its only public engineering surface is a small GitHub organization, including mh-brain, the source for its internal "BrightMatter" growth-intelligence HTTP service.
image: https://cdn.prod.website-files.com/5ec70e2719e95acb889006a3/6250be9b66c2423cf2d71534_MH-full-logo-lockup-horizontal-on-white.png
layout: provider
modified: '2026-08-25'
name: MarketerHire
nav: Providers
network: true
overview: 'MarketerHire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Talent Marketplace, Freelance, and Recruiting.


  MarketerHire''s developer surface includes engineering blog, pricing, signup flow, FAQ, and 9 more developer resources.'
plans:
- name: Marketerhire Plans Pricing
  plan_count: 0
  slug: marketerhire-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Marketerhire Rate Limits
  slug: marketerhire-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/marketerhire/refs/heads/main/screenshots/marketerhire-2026-09-02T150432.png
security:
- kind: domain-security
  name: Marketerhire Domain Security
  slug: marketerhire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marketerhire
tags:
- Company
- Marketing
- Talent Marketplace
- Freelance
- Recruiting
- Staffing
- Growth Marketing
- Human Resources
- Marketplace
website: https://marketerhire.com
---
