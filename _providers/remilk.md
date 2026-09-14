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
  url: security/remilk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.remilk.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.remilk.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.remilk.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.remilk.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/remilk
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/remilk-stock
coverage:
  checked: '2026-08-26'
  detail: Remilk sells a precision-fermented milk protein and the consumer dairy products made from it, so there is nothing to expose as an API — www.remilk.com is an eight-page Webflow marketing site (Our Mission, Science, Gains, Remilk Cares, Careers, Newsroom, Contact Us) whose only non-404 machine-readable path is a zero-byte robots.txt, every /.well-known/* path returns Webflow's "Invalid .well-known request" 404, and api./dev./docs./developer./app./platform./ mcp./portal.remilk.com do not resolve in DNS at all.
  evidence:
  - status: 200
    url: https://www.remilk.com/
  - status: 404
    url: https://www.remilk.com/openapi.json
  - status: 404
    url: https://www.remilk.com/graphql
  - status: 404
    url: https://www.remilk.com/llms.txt
  - status: 404
    url: https://www.remilk.com/.well-known/agent-card.json
  - status: 404
    url: https://www.remilk.com/.well-known/security.txt
  - status: 200
    url: https://www.remilk.com/robots.txt
  - status: 0
    url: https://api.remilk.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Remilk is a food-technology company, founded in 2019 by Aviv Wolff and Ori Cohavi and headquartered in Rehovot, Israel, that produces animal-free dairy proteins by precision fermentation. The company inserts the gene that codes for a cow milk protein into a yeast strain from the same family used in brewing and baking, ferments it at scale, and harvests a milk protein it describes as identical to the bovine original but free of lactose, cholesterol, hormones and antibiotics; the protein is then formulated with non-animal fat and sugar, vitamins and minerals into finished dairy products. Remilk has raised more than $150M, and was the first company to win regulatory clearance for a precision-fermented dairy protein in Israel, with subsequent clearances in Singapore, the United States (GRAS) and Canada. In November 2025 it commercialised the ingredient with Gad Dairies, Israel''s fourth-largest dairy company, launching "The New Milk" barista and retail line, and it has publicly
  paused its plan to build what would have been the world''s largest precision fermentation facility in Denmark. Remilk sells a food ingredient and consumer dairy products, not software: it operates no developer program, publishes no API, SDK, or machine-readable specification, and maintains no public source-code organization.'
layout: provider
modified: '2026-08-26'
name: Remilk
nav: Providers
network: true
overview: Remilk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Technology, Precision Fermentation, Biotechnology, and Alternative Proteins.
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/remilk/refs/heads/main/screenshots/remilk-2026-09-02T153341.png
security:
- kind: domain-security
  name: Remilk Domain Security
  slug: remilk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: remilk
tags:
- Company
- Food Technology
- Precision Fermentation
- Biotechnology
- Alternative Proteins
- Dairy
- Ingredients
- Synthetic Biology
- Sustainability
- Consumer Packaged Goods
website: https://www.remilk.com/
---
