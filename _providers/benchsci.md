---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API for searching scientific reagents, experimental data, literature, antibodies, and accelerating preclinical drug discovery workflows. Provides programmatic access to BenchSci's curated databas
  name: BenchSci API
  slug: benchsci-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/benchsci-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/benchsci-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/benchsci-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.benchsci.com
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.benchsci.com/home
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/benchsci
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/benchsci
- group: company
  title: ''
  type: Blog
  url: https://www.benchsci.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.benchsci.com/contact
- group: other
  title: ''
  type: X
  url: https://twitter.com/benchsci
- group: commercial
  title: ''
  type: Plans
  url: plans/benchsci-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/benchsci-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/benchsci-finops.yml
created: '2026-06-13'
description: BenchSci is an AI-powered biopharma R&D platform offering EMET, an integrated biology workbench for autonomous preclinical drug discovery. The platform provides access to 85M+ reagent and model system records (including 16M antibodies, 22M RNAi entries, and 18M CRISPR records), 38M+ scientific publications curated by PhD scientists, and an 858M-node knowledge graph. BenchSci enables scientists to search scientific reagents, experimental data, and literature through REST APIs and agentic workflows, accelerating target identification, experiment design, and lead optimization for biopharma research.
finops:
- name: Benchsci Finops
  service_category: ''
  slug: benchsci-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/benchsci.png
layout: provider
modified: '2026-06-13'
name: BenchSci
nav: Providers
network: true
overview: 'BenchSci publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biopharma, Drug Discovery, AI, Reagents, and Antibodies.


  BenchSci''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Benchsci Plans Pricing
  plan_count: 3
  slug: benchsci-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Benchsci Rate Limits
  slug: benchsci-rate-limits
score:
  band: thin
  composite: 33.7
  delta: 0.6
  facets:
    commercial_clarity: 57.9
    contract_quality: 37.7
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 33.1
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/benchsci/refs/heads/main/screenshots/benchsci-2026-06-20T173155.png
security:
- kind: domain-security
  name: Benchsci Domain Security
  slug: benchsci-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Benchsci Vulnerability Disclosure
  slug: benchsci-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Benchsci Trust Center
  slug: benchsci-trust-center
  summary_line: SOC 2, GDPR
slug: benchsci
tags:
- Biopharma
- Drug Discovery
- AI
- Reagents
- Antibodies
- Scientific Research
- Life Sciences
- Preclinical Research
website: https://www.benchsci.com
---
