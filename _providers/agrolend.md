---
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://agrolend.agr.br/quem-somos/
- group: operate
  title: ''
  type: Support
  url: https://agrolend.agr.br/contato/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agrolend
- group: company
  title: ''
  type: Blog
  url: https://agrolend.agr.br/informativo-agrolend/
- group: auth
  title: ''
  type: Compliance
  url: https://agrolend.agr.br/relatorios/
- group: auth
  title: ''
  type: Security
  url: https://agrolend.agr.br/wp-content/uploads/2026/07/AGROLEND-CIBERSEGURANCA_FEV26.pdf
- group: design
  title: ''
  type: Conformance
  url: conformance/agrolend-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agrolend-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agrolend-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/agrolend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agrolend-rate-limits.yml
coverage:
  checked: '2026-09-13'
  detail: 'The only Agrolend API host, parceiro.agrolend.agr.br, sits behind blanket HTTP Basic auth and returns 401 with WWW-Authenticate: Basic on every path including /v3/api-docs and /openapi.json, while the docs.agrolend.agr.br and portal.agrolend.agr.br subdomains that would have carried the reference have been dead since their wildcard certificate expired on 2025-03-06 and now return 504 from an empty load balancer.'
  evidence:
  - status: 401
    url: https://parceiro.agrolend.agr.br/
  - status: 401
    url: https://parceiro.agrolend.agr.br/v3/api-docs.yaml
  - status: 504
    url: https://docs.agrolend.agr.br/
  - status: 504
    url: https://portal.agrolend.agr.br/
  - status: 404
    url: https://agrolend.agr.br/.well-known/api-catalog
  - status: 200
    url: https://data.directory.openbankingbrasil.org.br/participants
  reason: partner-login
  state: gated
created: '2026-09-13'
description: Agrolend is a Brazilian agricultural-credit fintech — legally Agrolend Sociedade de Credito, Financiamento e Investimento S/A (CNPJ 43.774.196/0001-84), a Banco Central do Brasil regulated SCFI headquartered in Sao Paulo. Founded in 2020, it originates working capital, receivables discount, liability-extension and inter-chain credit for small and mid-sized rural producers, distributing through agricultural retailers, cooperatives and input industries rather than direct to farm, and funds the book partly through FGC-covered LCA notes sold on third-party investment platforms. Its stated differentiator is a cloud-native, AI-assisted credit engine that underwrites without requiring farm or grain collateral. Agrolend publishes no developer portal, no API reference and no machine-readable contract; the only API surface reachable from the public internet is the partner-area backend at parceiro.agrolend.agr.br, which answers HTTP Basic 401 on every path.
image: https://agrolend.agr.br/wp-content/uploads/2023/05/Logo-Agrolend.png
layout: provider
modified: '2026-09-13'
name: Agrolend
nav: Providers
network: true
overview: 'Agrolend is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Agtech, Financial Services, and Lending.


  Agrolend''s developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Agrolend Plans Pricing
  plan_count: 0
  slug: agrolend-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Agrolend Rate Limits
  slug: agrolend-rate-limits
security:
- kind: domain-security
  name: Agrolend Domain Security
  slug: agrolend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agrolend
tags:
- Company
- Agriculture
- Agtech
- Financial Services
- Lending
- Credit
- Fintech
- Brazil
- Rural Finance
- Banking
website: https://agrolend.agr.br/quem-somos/
---
