---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.admitkard.com/
- group: company
  title: ''
  type: Blog
  url: https://www.admitkard.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/admitkard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.admitkard.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.admitkard.com/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/admitkard-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/admitkard-llms.txt
coverage:
  checked: '2026-09-07'
  detail: AdmitKard sells study-abroad counselling to students, not a developer product — there is no developer portal, API reference, SDK or machine-readable contract anywhere on its surface, and its own API host api.admitkard.com answers every path with a Cloudflare 522 origin timeout.
  evidence:
  - status: 522
    url: https://api.admitkard.com/openapi.json
  - status: 404
    url: https://www.admitkard.com/openapi.json
  - status: 404
    url: https://www.admitkard.com/llms.txt
  - status: 404
    url: https://www.admitkard.com/.well-known/api-catalog
  - status: 200
    url: https://github.com/admitkard
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: 'AdmitKard is a Noida, India based study-abroad EdTech company, founded in 2016 by IIT-IIM alumni Piyush Bhartiya and Rachit Agrawal, that guides Indian students through the full overseas-education journey: university and course shortlisting, profile building, test preparation, applications, SOP/LOR support, scholarships, education loans, foreign-exchange remittance, student visas and accommodation. The company is an ICEF-accredited and AIRC-certified agency and raised a Rs 50 crore (about $6M) Series A led by GSV Ventures in 2023. It sells counselling services to students and universities rather than a developer product: as of this profile it publishes no public API, developer portal, SDK or machine-readable contract, and its api.admitkard.com host answers with a Cloudflare 522 origin timeout.'
image: https://www.admitkard.com/admitkard-logo-color.png
layout: provider
modified: '2026-09-07'
name: Admitkard
nav: Providers
network: true
overview: 'Admitkard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Study Abroad, and Higher Education.


  Admitkard''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 0
security:
- kind: domain-security
  name: Admitkard Domain Security
  slug: admitkard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: admitkard
tags:
- Company
- Education
- EdTech
- Study Abroad
- Higher Education
- Student Recruitment
- Admissions
- Counseling
- India
website: https://www.admitkard.com/
---
