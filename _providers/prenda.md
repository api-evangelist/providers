---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prenda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prenda.com/
- group: company
  title: ''
  type: Blog
  url: https://www.prenda.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.prenda.com/knowledge
- group: start
  title: ''
  type: SignUp
  url: https://discover.prenda.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prenda.com/page/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prenda.com/page/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prenda-school
- group: company
  title: ''
  type: About
  url: https://www.prenda.com/who-we-are
- group: operate
  title: ''
  type: Contact
  url: https://www.prenda.com/contact
- group: company
  title: ''
  type: Press
  url: https://www.prenda.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.prenda.com/page/jobs
- group: build
  title: ''
  type: Packages
  url: packages/prenda-packages.yml
- group: design
  title: ''
  type: Components
  url: components/prenda-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prenda-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/prenda_stock/
coverage:
  checked: '2026-08-26'
  detail: 'Prenda ships a closed, end-user microschool platform: api./developer./docs./dev./app.prenda.com all NXDOMAIN, and /openapi.json, /llms.txt and every /.well-known path 404 on all four live hosts, leaving the MIT-licensed Prenda Design System React library as the only developer-facing artifact the company publishes.'
  evidence:
  - status: 404
    url: https://www.prenda.com/openapi.json
  - status: 404
    url: https://www.prenda.com/llms.txt
  - status: 404
    url: https://www.prenda.com/.well-known/api-catalog
  - status: 404
    url: https://www.prenda.com/.well-known/agent-card.json
  - status: 0
    url: https://api.prenda.com/
  - status: 200
    url: https://github.com/prenda-school
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Prenda, Inc. is a Mesa, Arizona education technology company that makes it possible for an adult to open and run a K-8 microschool — a tight-knit learning community of roughly five to ten students — out of a home, studio, or office. Founded by Kelly Smith out of the Prenda Code Club he started at a public library in 2013, Prenda opened its first microschool in January 2018 and now supports more than 1,000 "guides" running microschools for nearly 10,000 learners across multiple US states, funded largely through school-choice and education savings account programs. The product is a plug-and-play software platform bundled with curriculum, training, and coaching: guides use it to manage enrollment, run adaptive diagnostic assessments in math and reading, track learner progress against Prenda''s four-mode "connect, conquer, collaborate, create" learning day, process payments, and publish a marketing site for their school. Prenda is venture-backed, having raised a $20M round led
  by 776 in 2022. The platform is closed and end-user facing — Prenda publishes no public API, developer portal, or machine-readable contract of any kind. Its only public developer surface is the Prenda Design System, an open-source MUI v6 React component and icon library published from the prenda-school GitHub organization.'
image: https://cdn.prod.website-files.com/61783ff414c9d8285b7d8e7a/64764d133a61e6cc9217b146_Dezirea%20Contreras_1st%20-%207th_2022-2023_GILBERT%20AZ263%201.png
layout: provider
modified: '2026-08-26'
name: Prenda
nav: Providers
network: true
overview: 'Prenda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Education Technology, Microschools, and K-12.


  Prenda''s developer surface includes engineering blog, support, signup flow, and 13 more developer resources.'
random_paper: 4
screenshot: https://raw.githubusercontent.com/api-evangelist/prenda/refs/heads/main/screenshots/prenda-2026-09-02T151933.png
security:
- kind: domain-security
  name: Prenda Domain Security
  slug: prenda-domain-security
  summary_line: TLSv1.3 · HSTS
slug: prenda
tags:
- Company
- Education
- Education Technology
- Microschools
- K-12
- Learning Management
- Curriculum
- School Choice
- Homeschooling
- Design Systems
website: https://www.prenda.com/
---
