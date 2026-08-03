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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.viome.com/
- group: company
  title: ''
  type: Blog
  url: https://www.viome.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.viome.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Viome
- group: commercial
  title: ''
  type: Pricing
  url: https://www.viome.com/products
- group: start
  title: ''
  type: Login
  url: https://my.viome.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.viome.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.viome.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/viome-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/viome-packages.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/viome_stock/
created: '2026-08-02'
description: Viome (Viome Life Sciences) is a health technology company founded in 2016 by Naveen Jain that uses metatranscriptomic RNA sequencing — a technique originally developed for biodefense at Los Alamos National Laboratory — combined with artificial intelligence to measure active gene expression across the gut microbiome, oral microbiome, and human cells. From at-home stool, saliva, and finger-prick blood samples the company produces over 50 health scores across eight categories (BioAge, Gut Health, Oral Health, Energy, Inflammaging, Mood/Memory/Focus, Immunity, and Heart and Metabolic Health), personalized food recommendations across more than 370 foods, and custom-blended precision supplements and biotics. Products include the Full Body Intelligence, Gut Intelligence, and Oral Health Intelligence tests plus the CancerDetect saliva screening test for oral and throat cancer. Viome operates in over 100 countries, publishes peer-reviewed research in NPJ Genomic Medicine, iScience,
  and Microbiome, and runs a Life Sciences research division. Viome publishes no public developer API or machine-readable API contract; its consumer app at my.viome.com is served by an undocumented private backend, and the only agent-facing artifact the company publishes is a curated llms.txt.
image: https://strapi.azure.viome.com/viome-strapi/uploads/1024x1024bb_16f1932f97.png
layout: provider
modified: '2026-08-02'
name: Viome
nav: Providers
network: true
overview: 'Viome is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Microbiome, and Genomics.


  Viome''s developer surface includes engineering blog, support, pricing, and 9 more developer resources.'
random_paper: 69
score:
  band: emerging
  composite: 17.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: domain-security
  name: Viome Domain Security
  slug: viome-domain-security
  summary_line: TLSv1.3 · DMARC
slug: viome
tags:
- Company
- Health
- Healthcare
- Microbiome
- Genomics
- Diagnostics
- Nutrition
- Life Sciences
- Artificial Intelligence
- Consumer Health
website: https://www.viome.com/
---
