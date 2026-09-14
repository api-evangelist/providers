---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/takeda-pharmaceutical-company-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.takeda.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.takeda.com/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.takeda.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.takeda.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.takeda.com/newsroom/press-releases/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/takeda-pharmaceutical-company-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/takeda-pharmaceutical-company-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/takeda-pharmaceutical-company-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/takeda-pharmaceutical-company-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/takeda-pharmaceutical-company-rate-limits.yml
coverage:
  checked: '2026-09-13'
  detail: 'Takeda runs large internal API platforms - AWS AppSync GraphQL for its data scientists, a PingFederate workforce IdP that robots.txt disallows - but exposes none of it outward: developer.takeda.com and api.takeda.com do not resolve at all, the corporate site 404s every well-known path, and the only supplier integration Takeda names is a third-party Apex Analytix payments portal, so there is no developer programme to gate or to read.'
  evidence:
  - status: 0
    url: https://developer.takeda.com/
  - status: 0
    url: https://api.takeda.com/
  - status: 404
    url: https://www.takeda.com/openapi.json
  - status: 404
    url: https://www.takeda.com/.well-known/api-catalog
  - status: 404
    url: https://www.takeda.com/.well-known/security.txt
  - status: 200
    url: https://www.takeda.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: 'Takeda Pharmaceutical Company Limited is a Japanese multinational biopharmaceutical company headquartered in Tokyo, founded in 1781 and listed on the Tokyo Stock Exchange (4502) and the New York Stock Exchange (TAK). It is the largest pharmaceutical company in Japan and Asia, and operates globally across oncology, rare genetic and hematologic diseases, neuroscience, gastroenterology, plasma-derived therapies and vaccines, a portfolio substantially expanded by its 2019 acquisition of Shire. Takeda is a software consumer rather than a software vendor: it runs large internal API and data platforms, but publishes no public developer program, API reference or machine-readable contract. The one machine-readable document it does serve to automated clients is an llms.txt at its corporate root, which indexes its verified country websites and states an explicit LLM usage and attribution policy.'
layout: provider
modified: '2026-09-13'
name: Takeda Pharmaceutical Company
nav: Providers
network: true
overview: 'Takeda Pharmaceutical Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Healthcare, Life Sciences, and Biotechnology.


  Takeda Pharmaceutical Company''s developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Takeda Pharmaceutical Company Plans Pricing
  plan_count: 0
  slug: takeda-pharmaceutical-company-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Takeda Pharmaceutical Company Rate Limits
  slug: takeda-pharmaceutical-company-rate-limits
security:
- kind: domain-security
  name: Takeda Pharmaceutical Company Domain Security
  slug: takeda-pharmaceutical-company-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: takeda-pharmaceutical-company
tags:
- Company
- Pharmaceuticals
- Healthcare
- Life Sciences
- Biotechnology
- Clinical Trials
- Japan
website: https://www.takeda.com/
---
