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
  url: security/coregen-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coregen-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.coregen.com/
- group: company
  title: ''
  type: About
  url: https://www.coregen.com/about
- group: other
  title: ''
  type: Science
  url: https://www.coregen.com/thescience
- group: other
  title: ''
  type: Research
  url: https://www.coregen.com/preclinicalstudies
- group: other
  title: ''
  type: Product
  url: https://www.coregen.com/pipeline
- group: other
  title: ''
  type: Publications
  url: https://www.coregen.com/publications
- group: other
  title: ''
  type: Team
  url: https://www.coregen.com/leadership
- group: company
  title: ''
  type: Newsroom
  url: https://www.coregen.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.coregen.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.coregen.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coregen.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coregen.com/terms-and-conditions
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/coregen_stock/
coverage:
  checked: '2026-08-11'
  detail: CoRegen is a clinical-stage cancer cell-therapy company, not a software company — coregen.com is a nine-page Wix marketing and science site (about, the science, preclinical studies, pipeline, publications, leadership, news, careers, contact) where /developers, /docs, /api, /graphql, /mcp, /openapi.json and /llms.txt all return a real 404 (verified against a control path that also 404s), every /.well-known/* path returns a hard Wix HTTP 400 error page, and no developer subdomain (api./docs./developer./mcp.coregen.com) resolves in DNS.
  evidence:
  - status: 200
    url: https://www.coregen.com/
  - status: 404
    url: https://www.coregen.com/developers
  - status: 400
    url: https://www.coregen.com/openapi.json
  - status: 404
    url: https://www.coregen.com/llms.txt
  - status: 404
    url: https://www.coregen.com/api
  - status: 400
    url: https://www.coregen.com/.well-known/agent-card.json
  - status: 400
    url: https://www.coregen.com/.well-known/security.txt
  - status: 404
    url: https://www.coregen.com/definitely-not-a-real-path-abc123xyz
  reason: not-a-software-company
  state: none
created: '2026-08-11'
description: 'CoRegen, Inc. (CoRegen Science) is a clinical-stage biopharmaceutical company in Houston, Texas developing adoptive cell therapies for aggressive solid tumors. Its platform, licensed exclusively from the O''Malley Lab at Baylor College of Medicine, uses CRISPR gene editing to knock out the SRC-3 steroid receptor coactivator gene in regulatory T (Treg) cells, reprogramming them from immunosuppressors into tumor-killing effectors. The lead program, CRG-150, received FDA IND clearance for a first-in-human Phase 1/2a trial in advanced solid tumors, and the underlying science won the 2023 Cozzarelli Prize. CoRegen is a therapeutics organization, not a software company: it publishes a nine-page marketing and science site (about, the science, preclinical studies, pipeline, publications, leadership, news, careers, contact) and no developer program, API, SDK, or machine-readable specification of any kind.'
image: https://static.wixstatic.com/media/6bbba7_0128eda3793342649faba3890102b461~mv2.png
layout: provider
modified: '2026-08-11'
name: CoRegen
nav: Providers
network: true
overview: CoRegen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Oncology, and Cell Therapy.
random_paper: 143
score:
  band: minimal
  composite: 11.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Coregen Domain Security
  slug: coregen-domain-security
  summary_line: TLSv1.3 · HSTS
slug: coregen
tags:
- Company
- Biotechnology
- Life Sciences
- Oncology
- Cell Therapy
- Immunotherapy
- Gene Editing
- Pharmaceuticals
- Clinical Stage
website: https://www.coregen.com/
---
