---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://aegletherapeutics.com/
- group: company
  title: ''
  type: About
  url: https://aegletherapeutics.com/company/
- group: operate
  title: ''
  type: Contact
  url: https://aegletherapeutics.com/contact/
- group: company
  title: ''
  type: Newsroom
  url: https://aegletherapeutics.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aegletherapeutics.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aegletherapeutics
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aegle-therapeutics-domain-security.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/aegle-therapeutics-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aegle-therapeutics-llms.txt
coverage:
  checked: '2026-09-09'
  detail: Aegle Therapeutics is a clinical-stage extracellular-vesicle drug developer whose entire public surface is a seven-page WordPress marketing site (home, company, EV therapy, pipeline, news, contact, policies) — its sitemap lists no developer, API, docs or pricing page, and the only machine-readable endpoint on the domain is the site's own /wp-json/ CMS route, which returns 401 rest_authentication_error to anonymous callers.
  evidence:
  - status: 200
    url: https://aegletherapeutics.com/page-sitemap.xml
  - status: 404
    url: https://aegletherapeutics.com/openapi.json
  - status: 404
    url: https://aegletherapeutics.com/llms.txt
  - status: 404
    url: https://aegletherapeutics.com/.well-known/agent-card.json
  - status: 401
    url: https://aegletherapeutics.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-09'
description: Aegle Therapeutics Corporation is a privately held, clinical-stage regenerative medicine company developing extracellular vesicle (EV) therapy — a cell-free therapeutic composite of EVs, including exosomes, isolated from allogeneic bone marrow-derived mesenchymal stem cells using its proprietary EV harvesting technology. Its lead candidate, AGLE-102, is in a Phase 1/2 clinical study for Recessive Dystrophic Epidermolysis Bullosa (RDEB) and other severe dermatological disorders with significant unmet medical need. The company publishes a seven-page WordPress marketing site and no developer program, API, SDK or machine-readable specification of any kind.
image: https://cdn.aegletherapeutics.com/app/uploads/2023/01/cropped-aegle-icon-1-270x270.png
layout: provider
modified: '2026-09-09'
name: Aegle Therapeutics
nav: Providers
network: true
overview: Aegle Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Regenerative Medicine, and Clinical Stage.
random_paper: 4
security:
- kind: domain-security
  name: Aegle Therapeutics Domain Security
  slug: aegle-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aegle-therapeutics
tags:
- Company
- Biotechnology
- Life Sciences
- Regenerative Medicine
- Clinical Stage
- Pharmaceuticals
- Rare Disease
- Health
website: https://aegletherapeutics.com/
---
