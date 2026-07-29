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
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sanofi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sanofi
- group: company
  title: ''
  type: Website
  url: https://www.sanofi.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sanofi
- group: start
  title: ''
  type: ClinicalTrials
  url: https://www.sanofi.com/en/your-health/clinical-trials-and-results
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sanofi-vocabulary.yml
created: '2026-05-05'
description: Sanofi is a French multinational pharmaceutical and healthcare company focused on immunology, oncology, rare diseases, and vaccines, and a leading vaccines manufacturer. Sanofi does not publish a public developer API. Its GitHub organization exists but has no public repositories. The company operates patient assistance and HCP portals as well as clinical trial information services that require authenticated access.
features:
- description: Therapies for rare diseases, multiple sclerosis, and hematology
  name: Specialty Care
- description: Dupixent and broader immunology franchise
  name: Immunology
- description: Sanofi Vaccines is a global leader, including influenza and pediatric vaccines
  name: Vaccines
- description: Sarclisa and oncology pipeline programs
  name: Oncology
- description: Insulin and diabetes portfolio
  name: Diabetes
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sanofi.png
layout: provider
modified: '2026-05-16'
name: Sanofi
nav: Providers
network: true
overview: Sanofi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceutical, Healthcare, Vaccines, and Biotechnology.
random_paper: 24
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
screenshot: https://raw.githubusercontent.com/api-evangelist/sanofi/refs/heads/main/screenshots/sanofi-2026-06-20T193409.png
security:
- kind: domain-security
  name: Sanofi Domain Security
  slug: sanofi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sanofi
tags:
- Pharmaceutical
- Healthcare
- Vaccines
- Biotechnology
use_cases:
- description: Patients and HCPs find Sanofi trials via clinicaltrials.sanofi.com
  name: Clinical Trial Discovery
- description: Sanofi provides patient assistance programs and adherence services
  name: Patient Support Programs
- description: Sanofi runs HCP portals for prescribing information and medical inquiries
  name: HCP Engagement
website: https://www.sanofi.com/
---
