---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: Partner-gated programmatic access to Helix Exome+ sequencing data - more than 100 million base pairs including SNPs, indels, and copy number variants, with panel-grade coverage of clinically important
  name: Helix Genomics API
  slug: helix-genomics-api
- description: Partner-gated ancestry results derived from a participant's Exome+ sequence - continental ancestry across 6 global populations or regional ancestry across 26+ populations. Access is provisioned throug
  name: Helix Ancestry API
  slug: helix-ancestry-api
- description: Partner-gated user-specific results for hundreds of genetic traits and conditions, ranging from single-marker traits to complex polygenic risk scores computed with machine-learning models over Helix E
  name: Helix Insight API
  slug: helix-insight-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helix-genomics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.helix.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/my-helix
- group: docs
  title: ''
  type: Documentation
  url: https://genomics.helix.com/
created: '2026-07-05'
description: Helix is a population genomics company operating an end-to-end precision health platform - a proprietary Exome+ next-generation sequencing assay, a CLIA/CAP-certified clinical lab, and bioinformatics tooling - that enables health systems, life sciences companies, and payers to integrate genomic data into clinical care and research at population scale. Through its DNA Product Studio, Helix exposes a partner-gated developer surface - a Genomics API (direct programmatic access to 100M+ base pairs including SNPs, indels, and copy number variants with panel-grade coverage of actionable genes), an Ancestry API (continental ancestry for 6 global populations or regional ancestry for 26+ populations), and an Insight API (user-specific results for hundreds of traits and conditions, from single-marker traits to machine-learning polygenic risk scores) - alongside Embedded Apps and an App Acceleration Framework for building white-label DNA products. API access is enterprise/partner-gated
  and provisioned through Helix partnerships; there is no public self-serve developer portal or openly published API specification, so the API surface below is modeled from Helix's public product documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/helix-genomics.png
layout: provider
modified: '2026-07-05'
name: Helix
nav: Providers
network: true
overview: 'Helix publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Genomics, Population Genomics, Sequencing, Exome, and Precision Health.


  Helix''s developer surface includes documentation and 3 more developer resources.'
random_paper: 116
score:
  band: minimal
  composite: 8.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/helix-genomics/refs/heads/main/screenshots/helix-genomics-2026-07-25T220915.png
security:
- kind: domain-security
  name: Helix Genomics Domain Security
  slug: helix-genomics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: helix-genomics
tags:
- Genomics
- Population Genomics
- Sequencing
- Exome
- Precision Health
- Bioinformatics
- Healthcare
- DNA
- Partner API
website: https://www.helix.com
---
