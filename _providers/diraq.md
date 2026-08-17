---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diraq-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/diraq-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.diraq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.diraq.com/newsdesk
- group: company
  title: ''
  type: BlogRSS
  url: https://www.diraq.com/newsdesk?format=rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diraq.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.diraq.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.diraq.com/contact
- group: company
  title: ''
  type: About
  url: https://www.diraq.com/about
- group: other
  title: ''
  type: Research
  url: https://www.diraq.com/research-papers
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/diraq-stock
coverage:
  checked: '2026-08-12'
  detail: Diraq is a pre-commercial silicon-spin-qubit hardware company whose entire public web presence is a nine-page Squarespace marketing site — home, technology, about, contact, research papers, research insights, newsdesk, privacy, terms — with no developer, docs, or API page in its own sitemap; the one API-shaped hostname, api.diraq.com, is a CNAME to ghs.googlehosted.com that 302-redirects to the marketing site and 404s every spec path.
  evidence:
  - status: 200
    url: https://www.diraq.com/sitemap.xml
  - status: 404
    url: https://api.diraq.com/openapi.json
  - status: 302
    url: https://api.diraq.com/
  - status: 404
    url: https://www.diraq.com/llms.txt
  - status: 404
    url: https://www.diraq.com/.well-known/agent-card.json
  - status: 404
    url: https://www.diraq.com/docs
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Diraq is a quantum computing company headquartered in Sydney, Australia, with offices in Palo Alto, California and Boston, Massachusetts. Spun out of UNSW Sydney in 2022 by Professor Andrew Dzurak, Diraq builds quantum processors from silicon spin qubits — quantum information encoded in the spin of single electrons held in quantum dots formed inside structures derived from conventional CMOS transistors, so the qubits can be fabricated on standard semiconductor foundry lines. The company works with imec, NVIDIA and Quantum Machines, has advanced through DARPA''s utility-scale quantum computing initiative, and targets a first commercial processor toward the end of the decade. Diraq is a pre-commercial hardware and research organization: as of this profile it publishes no developer program, public API, SDK, or machine-readable contract of any kind, and its stated commercial pathway — cloud access to its processors — is still on the roadmap rather than in market.'
image: https://www.diraq.com/favicon.ico
layout: provider
modified: '2026-08-12'
name: Diraq
nav: Providers
network: true
overview: 'Diraq is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum Computing, Semiconductors, Deep Tech, and Hardware.


  Diraq''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 82
score:
  band: minimal
  composite: 11.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Diraq Domain Security
  slug: diraq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: diraq
tags:
- Company
- Quantum Computing
- Semiconductors
- Deep Tech
- Hardware
- Research
- Australia
website: https://www.diraq.com/
---
