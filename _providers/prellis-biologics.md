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
  url: security/prellis-biologics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prellisbio.com/
- group: company
  title: ''
  type: About
  url: https://prellisbio.com/about
- group: company
  title: ''
  type: Blog
  url: https://prellisbio.com/news-and-media
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prellisbio.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://prellisbio.com/contacts
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PrellisBiologics
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prellis-biologics-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Prellis Biologics sells antibody discovery collaborations and licensed therapeutic programs to pharma partners rather than software — its entire site is fourteen marketing pages with no developer, docs, platform or login section, and api./docs./developer./app.prellisbio.com do not resolve at all.
  evidence:
  - status: 200
    url: https://prellisbio.com/sitemap.xml
  - status: 404
    url: https://prellisbio.com/openapi.json
  - status: 404
    url: https://prellisbio.com/.well-known/agent-card.json
  - status: 404
    url: https://prellisbio.com/llms.txt
  - status: 404
    url: https://prellisbio.com/graphql
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Prellis Biologics is a Berkeley, California biotechnology company that discovers fully human antibody therapeutics by combining wet-lab human immunology with machine learning. Its EXIS (Externalized Immune System) platform uses LNO lymph node organoids — 3D tissue printed with holographic two-photon photolithography — to recreate human lymph node biology in vitro, raise true human antibody responses across genetically diverse donors, and feed the resulting sequence and characterization data into generative AI models that predict and optimize candidates in an iterative lab loop. The company sells antibody discovery collaborations and licensed therapeutic programs to pharmaceutical partners rather than software, and publishes no public developer program, API, SDK, or machine-readable specification.
image: https://cdn.sanity.io/images/km3brrze/production/7c3deebab6b574ce1b0943968cacc7c22cf94f20-1200x630.jpg
layout: provider
modified: '2026-08-05'
name: Prellis Biologics
nav: Providers
network: true
overview: 'Prellis Biologics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Antibody Discovery, and Drug Discovery.


  Prellis Biologics'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 124
score:
  band: minimal
  composite: 10.2
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Prellis Biologics Domain Security
  slug: prellis-biologics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: prellis-biologics
tags:
- Company
- Biotechnology
- Life Sciences
- Antibody Discovery
- Drug Discovery
- Artificial Intelligence
- Machine Learning
- Bioprinting
- Therapeutics
- Research
website: https://prellisbio.com/
---
