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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/athos-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://athostx.com/
- group: company
  title: ''
  type: Blog
  url: https://athostx.com/news-posts/
- group: company
  title: ''
  type: BlogRSS
  url: https://athostx.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://athostx.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://athostx.com/careers/
- group: other
  title: ''
  type: Team
  url: https://athostx.com/ourteam/
- group: other
  title: ''
  type: Product
  url: https://chironailabs.com/our-products
- group: other
  title: ''
  type: Company
  url: https://chironailabs.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/athostx
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/athostx
coverage:
  checked: '2026-08-06'
  detail: Athos is a clinical-stage biotech whose only software product, the Chiron AI Labs omics suite (formerly AthosOmics.AI), is marketed explicitly as "no-code" and is pre-launch behind a demo-waitlist email form; the eight-page athostx.com sitemap contains no developer, docs or API page and every well-known/spec path on both hosts returns 404.
  evidence:
  - status: 200
    url: https://athostx.com/page-sitemap.xml
  - status: 404
    url: https://athostx.com/openapi.json
  - status: 404
    url: https://athostx.com/.well-known/agent-card.json
  - status: 404
    url: https://chironailabs.com/openapi.json
  - status: 404
    url: https://chironailabs.com/llms.txt
  - status: 0
    url: https://api.athostx.com/
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Athos Therapeutics is a clinical-stage biopharmaceutical company in Torrance, California developing precision small-molecule therapeutics for autoimmune and chronic inflammatory diseases, led by co-founder and CEO Dr. Dimitrios Iliopoulos. Its AI/ML discovery platform integrates multi-omic patient data — genomics, transcriptomics, proteomics, epigenomics, metabolomics and microbiomics — collected with global hospital systems to identify novel drug and gene targets, and produced ATH-063, an AI-generated G9A methyltransferase inhibitor advancing in inflammatory bowel disease. The computational side of the business is commercialized through Chiron AI Labs (formerly AthosOmics.AI), a deliberately no-code omics analysis SaaS suite (Athos-Multi, Athos-T, Athos-P, Athos-G, Athos-PM) that is pre-launch and gated behind a demo waitlist. Athos publishes no public API, developer portal, SDK or machine-readable specification.
image: https://athostx.com/wp-content/uploads/2020/04/athos-favicon.jpg
layout: provider
modified: '2026-08-06'
name: Athos Therapeutics
nav: Providers
network: true
overview: 'Athos Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Drug Discovery.


  Athos Therapeutics'' developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 4.7
  delta: -1.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/athos-therapeutics/refs/heads/main/screenshots/athos-therapeutics-2026-08-07T161842.png
security:
- kind: domain-security
  name: Athos Therapeutics Domain Security
  slug: athos-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: athos-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Drug Discovery
- Artificial Intelligence
- Machine Learning
- Genomics
- Precision Medicine
- Health
website: https://athostx.com/
---
