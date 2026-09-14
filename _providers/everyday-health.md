---
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everyday-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.everydayhealth.com/
- group: other
  title: ''
  type: Company
  url: https://www.everydayhealthgroup.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.ziffdavis.com/
- group: company
  title: ''
  type: About
  url: https://www.everydayhealth.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.everydayhealth.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://www.everydayhealth.com/contact-us/
- group: company
  title: ''
  type: Press
  url: https://www.everydayhealth.com/press-center/
- group: company
  title: ''
  type: Careers
  url: https://www.everydayhealthgroup.com/everydayhealthgroup-careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.everydayhealth.com/privacyterms/#everyday-health-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.everydayhealth.com/privacyterms/#everyday_health_privacy_policy
- group: other
  title: ''
  type: EditorialPolicy
  url: https://www.everydayhealth.com/editorial-policies/
- group: company
  title: ''
  type: BlogRSS
  url: https://feeds.everydayhealth.com/google-discover.xml
- group: other
  title: ''
  type: Sitemap
  url: https://www.everydayhealth.com/sitemap.xml
- group: other
  title: ''
  type: Robots
  url: https://www.everydayhealth.com/robots.txt
- group: other
  title: ''
  type: AIPolicy
  url: llms/everyday-health-ai-crawler-policy.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/everyday-health-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/everyday-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/everyday-health-rate-limits.yml
coverage:
  checked: '2026-09-13'
  detail: Everyday Health Group is a health publisher and pharma-marketing business with no developer program at all — api.everydayhealth.com is a closed AWS API Gateway that answers 403 MissingAuthenticationToken on every path and is documented nowhere, and the company's robots.txt instead blocks 107 named AI and agent crawlers site-wide and routes commercial content access to licensing@ziffdavis.com.
  evidence:
  - status: 403
    url: https://api.everydayhealth.com/
  - status: 404
    url: https://www.everydayhealth.com/openapi.json
  - status: 404
    url: https://www.everydayhealth.com/.well-known/api-catalog
  - status: 200
    url: https://www.everydayhealth.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: 'Everyday Health is a consumer health media brand founded in 2002 and the flagship property of Everyday Health Group, a division of Ziff Davis (NASDAQ: ZD). The group operates a portfolio of consumer, pregnancy-and-parenting and healthcare-professional brands — Everyday Health, BabyCenter, What to Expect, MedPage Today, Castle Connolly, Diabetes Daily, DailyOM, Lose It!, Migraine Again, theSkimm, HealthCentral and Emma''s Diary — and sells pharma commercialization, digital health and wellness, and provider solutions to life sciences companies, hospitals, health systems and clinicians. It is a publisher and advertising business, not an API platform: there is no developer portal, no public API documentation, no OpenAPI or other machine-readable contract, no SDKs and no hosted MCP or agent surface on any Everyday Health host. This API Evangelist profile captures what the company does publish programmatically — a sitemap index, one public RSS/Media RSS content feed, an auth-gated
  AWS API Gateway host at api.everydayhealth.com, and an unusually explicit robots.txt that blocks 107 named AI and agent crawlers site-wide while carving out two commercial product-review URLs.'
image: https://images.everydayhealth.com/react-component-images/everyday-health-01.png
layout: provider
modified: '2026-09-13'
name: Everyday Health
nav: Providers
network: true
overview: 'Everyday Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Consumer Health, Media, and Publishing.


  Everyday Health''s developer surface includes support and 18 more developer resources.'
plans:
- name: Everyday Health Plans Pricing
  plan_count: 0
  slug: everyday-health-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Everyday Health Rate Limits
  slug: everyday-health-rate-limits
security:
- kind: domain-security
  name: Everyday Health Domain Security
  slug: everyday-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Everyday Health Vulnerability Disclosure
  slug: everyday-health-vulnerability-disclosure
  summary_line: Bugcrowd
slug: everyday-health
tags:
- Company
- Health
- Consumer Health
- Media
- Publishing
- Content
- Healthcare
- Advertising
- Pharma Marketing
- Pregnancy
- Parenting
website: https://www.everydayhealth.com/
---
