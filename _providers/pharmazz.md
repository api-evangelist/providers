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
  url: security/pharmazz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pharmazz.com/
- group: company
  title: ''
  type: About
  url: https://www.pharmazz.com/about-us.php
- group: operate
  title: ''
  type: Contact
  url: https://www.pharmazz.com/contact-us.php
- group: company
  title: ''
  type: Careers
  url: https://www.pharmazz.com/career.php
- group: company
  title: ''
  type: Press
  url: https://www.pharmazz.com/press-releases.php
- group: company
  title: ''
  type: Investors
  url: https://www.pharmazz.com/investors.php
- group: other
  title: ''
  type: Publications
  url: https://www.pharmazz.com/publications.php
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pharmazz
- group: other
  title: ''
  type: Sitemap
  url: https://www.pharmazz.com/sitemap.xml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pharmazz-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Pharmazz is a clinical-stage drug developer whose entire public presence is a 33-page static PHP brochure site listing its centhaquine and sovateltide trial programs; there is no /developers, /docs or /api path, no GitHub organization, and every contract-discovery probe against www.pharmazz.com returned the site's standard 404 page.
  evidence:
  - status: 404
    url: https://www.pharmazz.com/developers
  - status: 404
    url: https://www.pharmazz.com/openapi.json
  - status: 404
    url: https://www.pharmazz.com/.well-known/agent-card.json
  - status: 200
    url: https://www.pharmazz.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Pharmazz, Inc. is a privately held, clinical-stage biopharmaceutical company headquartered in Willowbrook, Illinois, founded and led by pharmacologist Dr. Anil Gulati. The company discovers, develops and commercializes first-in-class therapeutics for critical care and neurovascular medicine, built around two lead small-molecule candidates: centhaquine (Lyfaquin), a resuscitative agent for hypovolemic shock that holds marketing authorization from the Drugs Controller General of India and is licensed to Dr. Reddy''s Laboratories for the Indian market, and sovateltide (Tycamzzi), an endothelin-B receptor agonist for cerebral ischemic stroke. Additional pipeline programs target septic shock, acute kidney injury, cardiac arrest, acute spinal cord injury, hypoxic-ischemic encephalopathy and Alzheimer''s disease. Pharmazz is a drug-development company, not a software vendor; its public web presence is a corporate and investor brochure site and it operates no developer program, public
  API, SDK or machine-readable interface.'
layout: provider
modified: '2026-08-26'
name: Pharmazz
nav: Providers
network: true
overview: Pharmazz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Healthcare.
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/pharmazz/refs/heads/main/screenshots/pharmazz-2026-09-02T151137.png
security:
- kind: domain-security
  name: Pharmazz Domain Security
  slug: pharmazz-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: pharmazz
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Healthcare
- Clinical Trials
- Critical Care
- Drug Development
website: https://www.pharmazz.com/
---
