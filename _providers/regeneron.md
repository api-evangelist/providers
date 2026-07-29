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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regeneron-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/regeneron-mpds
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/regeneron-pharmaceuticals
- group: company
  title: ''
  type: Website
  url: https://www.regeneron.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.regeneron.com/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://clinicaltrials.regeneron.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.regeneron.com/
- group: other
  title: ''
  type: GeneticsCenter
  url: https://www.regeneron.com/science/regeneron-genetics-center
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/regeneron-vocabulary.yml
created: '2026-05-05'
description: Regeneron Pharmaceuticals is a leading biotechnology company that invents, develops, and commercializes life-transforming medicines, including EYLEA and EYLEA HD for ophthalmology, Dupixent in immunology (co-developed with Sanofi), Libtayo and Lynozyfic in oncology and hematology, and Praluent for cardiovascular disease. Regeneron does not publish a public developer API; its Regeneron Genetics Center collaborates on large-scale genomic research via the UK Biobank, DiscovEHR, and partner platforms rather than a self-hosted API.
features:
- description: EYLEA and EYLEA HD anti-VEGF therapies for retinal diseases
  name: Ophthalmology
- description: Dupixent for atopic dermatitis, asthma, and other IL-4/IL-13 indications
  name: Immunology
- description: Libtayo, Lynozyfic, and pipeline programs in oncology
  name: Oncology and Hematology
- description: Evkeeza, Veopoz, and other rare-disease therapies
  name: Rare Diseases
- description: Inmazeb antibody cocktail for Ebola
  name: Infectious Disease
- description: Regeneron Genetics Center sequencing collaborations including UK Biobank
  name: Genetics Research
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/regeneron.png
layout: provider
modified: '2026-05-16'
name: Regeneron
nav: Providers
network: true
overview: Regeneron is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceutical, Biotechnology, Healthcare, and Genomics.
random_paper: 17
score:
  band: minimal
  composite: 7.2
  delta: -3.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 10.4
    operational_transparency: 5.3
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/regeneron/refs/heads/main/screenshots/regeneron-2026-06-20T192817.png
security:
- kind: domain-security
  name: Regeneron Domain Security
  slug: regeneron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: regeneron
tags:
- Pharmaceutical
- Biotechnology
- Healthcare
- Genomics
use_cases:
- description: Patients and HCPs locate Regeneron-sponsored trials
  name: Clinical Trial Discovery
- description: HCPs access prescribing information for Regeneron medicines
  name: Drug Information
- description: Researchers partner with the Regeneron Genetics Center on large-cohort sequencing
  name: Genomic Discovery
website: https://www.regeneron.com/
---
