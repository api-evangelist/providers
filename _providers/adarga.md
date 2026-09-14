---
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adarga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adarga.ai/
- group: company
  title: ''
  type: About
  url: https://www.adarga.ai/about
- group: other
  title: ''
  type: CaseStudies
  url: https://www.adarga.ai/case-studies
- group: company
  title: ''
  type: Blog
  url: https://www.adarga.ai/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.adarga.ai/news?format=rss
- group: operate
  title: ''
  type: Support
  url: https://support.adarga.ai/support/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adarga.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adarga-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/adargaai
- group: company
  title: ''
  type: Careers
  url: https://adarga.recruitee.com/
- group: build
  title: ''
  type: Packages
  url: packages/adarga-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adarga-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adarga-llms.txt
coverage:
  checked: '2026-09-07'
  detail: Adarga markets Catalyst as "The Developer Platform" where customers build "agents, tools and APIs", but the only documentation surface is a Freshservice customer portal at support.adarga.ai whose category list is public while every article folder returns HTTP 401 Unauthorized to an anonymous reader, and adarga.ai itself is a 14-page Squarespace estate with no developer section.
  evidence:
  - status: 401
    url: https://support.adarga.ai/support/solutions/folders/51000033057
  - status: 403
    url: https://support.adarga.ai/api/_/solutions/categories
  - status: 200
    url: https://www.adarga.ai/sitemap.xml
  - status: 404
    url: https://www.adarga.ai/openapi.json
  - status: 404
    url: https://www.adarga.ai/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-09-07'
description: Adarga is a British artificial-intelligence software company, founded in London in 2016 by Rob Bassett Cross, that builds information-intelligence and decision-advantage software for Defence, National Security and Resilience customers. Its products include Adarga Vantage, an AI analysis platform that extracts, contextualises and connects information from millions of internal and external sources in more than 75 languages; Adarga Augur, an alerting and intelligence tool; and Catalyst, a multidomain data-fusion and developer platform that the company markets as a Sovereign AI Stack. Adarga sells to the UK Ministry of Defence and Strategic Command and to US federal customers, and partners with Oracle to run Vantage on Oracle Cloud Infrastructure. Adarga publishes no public developer portal, API documentation, or machine-readable API contract; its product documentation sits behind a customer support portal.
image: http://static1.squarespace.com/static/69b8196e37339d1a13c7da39/t/69b81b862863403cb2492195/1773673350751/Adarga_White_16x9.gif?format=1500w
layout: provider
modified: '2026-09-07'
name: Adarga
nav: Providers
network: true
overview: 'Adarga is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Defense, National Security, and Intelligence.


  Adarga''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Adarga Plans Pricing
  plan_count: 0
  slug: adarga-plans-pricing
random_paper: 20
security:
- kind: domain-security
  name: Adarga Domain Security
  slug: adarga-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: adarga
tags:
- Company
- Artificial Intelligence
- Defense
- National Security
- Intelligence
- Analytics
- Natural Language Processing
- Data Fusion
- Machine Learning
- United Kingdom
website: https://www.adarga.ai/
---
