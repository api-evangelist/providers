---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agrimwholesale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agrim.app/
- group: company
  title: ''
  type: About
  url: https://agrim.app/about-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agrim.app/policy/tnc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agrim.app/policy/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agrimindia/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agrimwholesale-llms.txt
coverage:
  checked: '2026-09-13'
  detail: Agrim ships its marketplace only as Android retailer and seller apps plus a Next.js marketing site; agrim.app has no developer, API or integration section anywhere in its navigation, and the company's own backend host api.agrim.app answers a bare "Hello, Welcome to AGRIM" HTML page on / while returning 404 for every OpenAPI, Swagger, GraphQL, MCP and /.well-known/ discovery path probed.
  evidence:
  - status: 200
    url: https://api.agrim.app/
  - status: 404
    url: https://api.agrim.app/openapi.json
  - status: 404
    url: https://api.agrim.app/graphql
  - status: 404
    url: https://agrim.app/llms.txt
  - status: 404
    url: https://agrim.app/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: Agrim Wholesale Private Limited (branded AGRIM) is a Gurugram, India based business-to-business e-commerce marketplace for agricultural inputs, connecting agri-input manufacturers and wholesale suppliers with small rural retailers. Founded in 2020 by Avi Jain and Mukul Garg, the company lists more than 30,000 seed, crop-protection, fertiliser and farm-equipment products from over 1,200 manufacturers and fulfils orders across a pan-India network. The platform is delivered to retailers and sellers as Android applications and a marketing website at agrim.app; as of this profile the company publishes no public developer program, API reference, or machine-readable API contract.
image: https://agrim.app/favicon.png
layout: provider
modified: '2026-09-13'
name: Agrim Wholesale
nav: Providers
network: true
overview: Agrim Wholesale is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Agritech, Wholesale, and B2B.
random_paper: 1
security:
- kind: domain-security
  name: Agrimwholesale Domain Security
  slug: agrimwholesale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agrimwholesale
tags:
- Company
- Agriculture
- Agritech
- Wholesale
- B2B
- Marketplace
- E-Commerce
- Supply Chain
- India
website: https://agrim.app/
---
