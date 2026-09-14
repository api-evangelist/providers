---
api_count: 1
apis:
- description: A live, anonymous Model Context Protocol endpoint served from aetherAI's own host. It exposes nine tools over JSON-RPC 2.0 (streamable HTTP) for reading business details, searching site content, brows
  name: aetherAI Site MCP
  slug: aetherai-site-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aetherai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aetherai.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aetherai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aetherai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/aetherai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aetherai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aetherai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/aetherai-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/aetherai-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aetherai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aetherai-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aetherAI
- group: company
  title: ''
  type: Blog
  url: https://www.aetherai.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.aetherai.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aetherai.com/privacypolicy
- group: start
  title: ''
  type: Login
  url: https://demo.aetherai.com/dpai/login/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.aetherai.com/investorpage
coverage:
  checked: '2026-09-12'
  detail: aetherAI sells FDA-cleared digital-pathology software (aetherSlide, aetherWeb, Hema, Endo, Ortho) only as an end-user clinical product — there is no developer program, no developer portal, no OpenAPI and no API documentation on any host, and the DPAI application at demo.aetherai.com is a login-walled single-page app whose /api/, /openapi.json and /api/schema/ paths all return 404 to an anonymous client; the only callable public endpoint is the Wix platform's site MCP at www.aetherai.com/_api/mcp, which serves marketing-site content rather than any clinical product.
  evidence:
  - status: 400
    url: https://www.aetherai.com/openapi.json
  - status: 404
    url: https://demo.aetherai.com/openapi.json
  - status: 404
    url: https://demo.aetherai.com/api/
  - status: 200
    url: https://www.aetherai.com/products
  - status: 200
    url: https://www.aetherai.com/_api/mcp
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'aetherAI (雲象科技, aetherAI Co., Ltd.) is a Taipei-based medical-imaging AI company and one of Asia''s leading digital-pathology vendors. It builds regulated diagnostic software for hospitals, reference laboratories and pharmaceutical R&D: aetherSlide, an FDA-cleared (K233126), CE-marked and TFDA-approved whole-slide image management and viewing system; aetherWeb, a cloud digital pathology education platform; aetherAI Hema for bone-marrow smear differential counting; aetherAI Endo for real-time computer-aided polyp detection in colonoscopy; and aetherAI Ortho for whole-spine radiograph measurement. The company was founded in Taiwan, raised NT$765 million in Series B funding led by CDIB Capital, Quanta Computer, Taiwan Business Bank VC and Cathay Venture, listed on Taiwan''s Emerging Stock Board in November 2024, holds ISO/IEC 27001 certification, and has filed for the Taiwan Innovation Board. aetherAI publishes no public developer API, no OpenAPI or other machine-readable contract,
  and no developer portal; its clinical software is sold and deployed through a direct enterprise motion and its application sits behind a customer login. The single publicly callable surface is a Wix-provided Site MCP endpoint on its own domain, which serves website content rather than any clinical product.'
image: https://static.wixstatic.com/media/5feca6_8ade720b19a64d2fb13934d0ad55a0b9~mv2.jpg/v1/fill/w_2500,h_1600,al_c/5feca6_8ade720b19a64d2fb13934d0ad55a0b9~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: aetherAI Site MCP Server
  slug: aetherai-site-mcp-server
- description: ''
  name: aetherAI MCP Server
  slug: aetherai-mcp-server
modified: '2026-09-12'
name: aetherAI
nav: Providers
network: true
overview: 'aetherAI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Digital Pathology, Medical Imaging, Artificial Intelligence, and Diagnostics.


  aetherAI''s developer surface includes authentication, engineering blog, support, and 14 more developer resources.'
plans:
- name: Aetherai Plans Pricing
  plan_count: 0
  slug: aetherai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Aetherai Rate Limits
  slug: aetherai-rate-limits
security:
- kind: authentication
  name: Aetherai Authentication
  slug: aetherai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aetherai Domain Security
  slug: aetherai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aetherai
tags:
- Healthcare
- Digital Pathology
- Medical Imaging
- Artificial Intelligence
- Diagnostics
- Machine Learning
- Medical Devices
- Life Sciences
- MCP
- Taiwan
website: https://www.aetherai.com/
---
