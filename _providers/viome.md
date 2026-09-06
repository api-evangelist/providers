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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
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
random_paper: 19
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/viome/refs/heads/main/screenshots/viome-2026-09-02T165943.png
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
