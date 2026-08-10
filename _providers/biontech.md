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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biontech-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biontech-se
- group: company
  title: ''
  type: Website
  url: https://biontech.com/
- group: company
  title: ''
  type: Investors
  url: https://investors.biontech.de/
- group: other
  title: BioNTech for Healthcare Professionals
  type: MedicalAffairs
  url: https://medical.biontech.com/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://clinicaltrials.biontech.com/
- group: company
  title: ''
  type: Careers
  url: https://jobs.biontech.com/
- group: company
  title: ''
  type: News
  url: https://biontech.com/us/en/home/media.html
- group: operate
  title: ''
  type: PressReleases
  url: https://investors.biontech.de/news-releases
- group: company
  title: ''
  type: Blog
  url: https://biontech.com/us/en/home/mediaroom/news.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biontech.com/int/en/home/privacy-statement.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biontech.com/int/en/home/imprint.html
created: '2026-05-23'
description: BioNTech is a Mainz-based biotechnology company that pioneered the use of messenger RNA (mRNA) technology in human therapeutics. Best known for co-developing Comirnaty, the COVID-19 mRNA vaccine with Pfizer, BioNTech is building a broad oncology pipeline across mRNA cancer immunotherapies, next-generation immunomodulators such as the bispecific antibody BNT327, and targeted therapies, as well as continuing infectious disease vaccine development. BioNTech does not currently expose a public developer API; this index captures the company's products, pipeline, clinical trials, and corporate resources as an API Evangelist profile.
features:
- description: Proprietary messenger RNA platform underlying Comirnaty and the company's broader vaccine and oncology pipeline
  name: mRNA Platform
- description: COVID-19 mRNA vaccine co-developed and commercialized in collaboration with Pfizer
  name: Comirnaty
- description: Three complementary modalities across mRNA cancer immunotherapies, next-generation immunomodulators, and targeted therapies
  name: Oncology Pipeline
- description: Next-generation bispecific antibody candidate binding PD-L1 and VEGF-A for synergistic cancer treatment
  name: BNT327
- description: Individualized neoantigen cancer immunotherapies targeting residual tumor cells in adjuvant settings
  name: mRNA Cancer Immunotherapies
- description: Vaccine candidates extending the mRNA platform to additional high-burden infectious diseases
  name: Infectious Diseases Pipeline
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/biontech.png
integrations:
- description: Long-running co-development and commercialization partnership for Comirnaty and other mRNA programs
  name: Pfizer Collaboration
layout: provider
modified: '2026-05-23'
name: BioNTech
nav: Providers
network: true
overview: 'BioNTech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Pharmaceuticals, mRNA, Vaccines, and Oncology.


  BioNTech''s developer surface includes product news, engineering blog, and 10 more developer resources.'
random_paper: 32
score:
  band: minimal
  composite: 10.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biontech/refs/heads/main/screenshots/biontech-2026-06-20T173252.png
security:
- kind: domain-security
  name: Biontech Domain Security
  slug: biontech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biontech
tags:
- Biotechnology
- Pharmaceuticals
- mRNA
- Vaccines
- Oncology
- Immunotherapy
- Healthcare
use_cases:
- description: Continued supply of Comirnaty COVID-19 vaccine across global markets
  name: COVID-19 Vaccination
- description: 25+ Phase 2/3 oncology clinical trials and 10+ novel combination trials
  name: Cancer Immunotherapy
- description: Application of mRNA platform to rapidly developable vaccines against emerging infectious disease threats
  name: Pandemic Preparedness
- description: Dedicated medical affairs portal providing scientific and clinical data to clinicians
  name: Healthcare Professional Information
website: https://biontech.com/
---
