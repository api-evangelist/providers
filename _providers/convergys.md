---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.concentrix.com/
- group: company
  title: ''
  type: About
  url: https://www.concentrix.com/about/
- group: company
  title: ''
  type: Newsroom
  url: https://www.concentrix.com/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.prnewswire.com/news-releases/synnex-corporation-announces-acquisition-of-convergys-to-close-on-october-5-2018-300724049.html
- group: company
  title: ''
  type: Careers
  url: https://jobs.concentrix.com/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.concentrix.com/contact/
- group: company
  title: ''
  type: Partners
  url: https://www.concentrix.com/partners/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.concentrix.com/wp-content/uploads/2024/04/Concentrix-Website-Terms-of-Use.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.concentrix.com/legal/privacy-notice/
- group: company
  title: ''
  type: Blog
  url: https://www.concentrix.com/feed/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/convergys-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convergys-domain-security.yml
coverage:
  checked: '2026-09-07'
  detail: Convergys was merged into Concentrix in October 2018 and its own web estate has since been switched off — www.convergys.com is an Azure App Service redirect app that now answers "403 Site Disabled" on every path (including a control path that cannot exist) behind an expired TLS certificate, and developer.convergys.com still resolves to a Concentrix CVG Brite Voice Systems address block with TCP 80 and 443 both closed, so there is no surviving Convergys host left to read a contract from.
  evidence:
  - status: 403
    url: http://www.convergys.com/
  - status: 403
    url: http://www.convergys.com/.well-known/security.txt
  - status: 404
    url: https://www.concentrix.com/.well-known/api-catalog
  reason: defunct
  state: none
created: '2026-03-23'
description: 'Convergys Corporation was a global leader in customer management services — contact center outsourcing, workforce management, customer analytics and digital customer experience platforms — serving communications, financial services, healthcare, retail and technology clients. SYNNEX acquired Convergys in October 2018 and merged it into Concentrix; the brand was retired and its offerings were folded into the Concentrix portfolio. Convergys published no public API or developer program that survives. Probed 2026-09-07: www.convergys.com is an Azure App Service redirect app that has been switched off and now answers "403 Site Disabled" on every path with an expired TLS certificate, and developer.convergys.com still resolves to an address block registered to Concentrix CVG Brite Voice Systems LLC with both HTTP ports closed. The successor company, Concentrix, is profiled separately and delivers most platform integration through enterprise contracts rather than a public developer
  program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/convergys.png
layout: provider
modified: '2026-09-07'
name: Convergys
nav: Providers
network: true
overview: 'Convergys is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, Analytics, Business Process Outsourcing, Concentrix, and Contact Center.


  Convergys'' developer surface includes engineering blog and 11 more developer resources.'
press:
- date: '2026-05-25'
  title: NEC to acquire Convergys data management business for US ...
  url: https://www.computerworld.com/article/1445866/nec-to-acquire-convergys-data-management-business-for-us-449-million.html
- date: '2026-05-25'
  title: Convergys Analytics
  url: https://www.cxnetwork.com/cx-experience/articles/convergys-analytics
- date: '2026-05-25'
  title: Concentrix gets up close and personal with ...
  url: https://www.horsesforsources.com/convergys-concentrix_062918/
- date: '2026-05-25'
  title: SYNNEX Corporation Announces Acquisition of Convergys ...
  url: https://www.prnewswire.com/news-releases/synnex-corporation-announces-acquisition-of-convergys-to-close-on-october-5-2018-300724049.html
- date: '2026-05-25'
  title: 'It''s here. #Concentrix completes the acquisition of # ...'
  url: https://www.facebook.com/convergysglobal/posts/its-here-concentrix-completes-the-acquisition-of-convergys-creating-the-worlds-g/10156626173185786/
random_paper: 5
screenshot: https://raw.githubusercontent.com/api-evangelist/convergys/refs/heads/main/screenshots/convergys-2026-06-20T174957.png
security:
- kind: domain-security
  name: Convergys Domain Security
  slug: convergys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: convergys
tags:
- Acquired
- Analytics
- Business Process Outsourcing
- Concentrix
- Contact Center
- Customer Experience
- Customer Management
- Workforce Management
website: https://www.concentrix.com/
---
