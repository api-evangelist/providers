---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/afficiency-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.afficiency.com/
- group: build
  title: ''
  type: Integration
  url: https://www.afficiency.com/how-afficiency-can-work-for-you/
- group: operate
  title: ''
  type: Support
  url: https://www.afficiency.com/customer-support/
- group: operate
  title: ''
  type: FAQ
  url: https://www.afficiency.com/frequently-asked-questions/
- group: company
  title: ''
  type: News
  url: https://www.afficiency.com/press-room/
- group: company
  title: ''
  type: About
  url: https://www.afficiency.com/meet-the-team/
- group: company
  title: ''
  type: Careers
  url: https://www.afficiency.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.afficiency.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.afficiency.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.afficiency.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/afficiency
- group: design
  title: ''
  type: Conformance
  url: conformance/afficiency-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/afficiency-conformance.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/afficiency-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/afficiency-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/afficiency-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/afficiency-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/afficiency-packages.yml
coverage:
  checked: '2026-09-12'
  detail: Afficiency markets a "robust RESTful API suite" for quote-to-policy-issue but points every documentation request at support.afficiency.com, a HubSpot customer portal that returns HTTP 404 to anonymous clients on its own root, while api.afficiency.com sits behind Cloudflare with an origin that never answers (HTTP 522) — so the contract exists only for signed customers and the only public route to it is the Book a Demo form.
  evidence:
  - status: 404
    url: https://support.afficiency.com/
  - status: 522
    url: https://api.afficiency.com/openapi.json
  - status: 200
    url: https://www.afficiency.com/embedded-insurance/
  - status: 404
    url: https://www.afficiency.com/.well-known/api-catalog
  - status: 404
    url: https://www.afficiency.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-09-12'
description: Afficiency is a New York-based insurtech that designs, digitally underwrites and issues life insurance products on behalf of carrier and reinsurance partners, and distributes them through a 100% digital, API-first platform. Its product suite spans level term, final expense whole life, participating whole life, indexed universal life and annual renewable term, all issued without a medical exam and with instant underwriting decisions in a single session. Partners integrate through one of three models — a hosted white-label storefront, a direct REST API integration covering the full quote-to-policy-issue journey, or a hybrid of the two — which lets agencies, P&C agents, financial advisors, worksite and affinity channels and embedded fintech partners offer life insurance inside their own customer journeys. Afficiency states it is SOC 2 Type II certified. Its REST API suite is marketed publicly, but the reference and any machine-readable contract are reachable only through the customer
  support portal or a sales conversation.
image: https://www.afficiency.com/images/logos/globalLogo.svg
layout: provider
modified: '2026-09-12'
name: Afficiency
nav: Providers
network: true
overview: 'Afficiency is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Life Insurance, Insurtech, and Embedded Insurance.


  Afficiency''s developer surface includes support, FAQ, product news, and 16 more developer resources.'
plans:
- name: Afficiency Plans Pricing
  plan_count: 0
  slug: afficiency-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Afficiency Rate Limits
  slug: afficiency-rate-limits
security:
- kind: domain-security
  name: Afficiency Domain Security
  slug: afficiency-domain-security
  summary_line: TLSv1.3 · DMARC
slug: afficiency
tags:
- Company
- Insurance
- Life Insurance
- Insurtech
- Embedded Insurance
- Underwriting
- Financial Services
- Policy Administration
website: https://www.afficiency.com/
---
