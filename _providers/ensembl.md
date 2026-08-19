---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Ensembl REST API (v15.12) provides language-agnostic HTTP access to genome annotation data across hundreds of vertebrate and eukaryotic species. It exposes 19 endpoint categories covering genome s
  name: Ensembl REST API
  slug: rest-api
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Ensembl/ensembl-rest/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Ensembl/.github/blob/master/CODE_OF_CONDUCT.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ensembl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ensembl.org
- group: docs
  title: ''
  type: Documentation
  url: https://rest.ensembl.org/documentation
- group: operate
  title: ''
  type: RateLimits
  url: https://github.com/Ensembl/ensembl-rest/wiki/Rate-Limits
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ensembl
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Ensembl/ensembl-rest
- group: learn
  title: ''
  type: Tutorial
  url: https://github.com/Ensembl/rest-api-jupyter-course
- group: commercial
  title: ''
  type: License
  url: https://github.com/Ensembl/ensembl-rest/blob/main/LICENSE
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ensembl.org/info/about/legal/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ebi.ac.uk/data-protection/ensembl/privacy-notice
- group: commercial
  title: ''
  type: Plans
  url: plans/ensembl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ensembl-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ensembl-finops.yml
created: '2026-06-13'
description: Ensembl is a genome annotation database and browser maintained by the European Bioinformatics Institute (EMBL-EBI) and the Wellcome Sanger Institute. It provides comprehensive genome data for vertebrates and other eukaryotic organisms, covering gene annotation, variant data, regulatory features, comparative genomics, and evolutionary analysis across hundreds of species. The Ensembl REST API offers language-agnostic HTTP access to this genome data without requiring local database installations or Perl API dependencies.
finops:
- name: Ensembl Finops
  service_category: Bioinformatics / Genomics Data
  slug: ensembl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ensembl.png
layout: provider
modified: '2026-06-13'
name: Ensembl
nav: Providers
network: true
overview: 'Ensembl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Genomics, Bioinformatics, Genome Annotation, Variant Annotation, and Comparative Genomics.


  Ensembl''s developer surface includes documentation, tutorials, and 13 more developer resources.'
plans:
- name: Ensembl Plans Pricing
  plan_count: 1
  slug: ensembl-plans-pricing
random_paper: 146
rate_limits:
- limit_count: 2
  name: Ensembl Rate Limits
  slug: ensembl-rate-limits
score:
  band: emerging
  composite: 17.4
  delta: -3.9
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 21.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ensembl/refs/heads/main/screenshots/ensembl-2026-06-20T180726.png
security:
- kind: domain-security
  name: Ensembl Domain Security
  slug: ensembl-domain-security
  summary_line: TLSv1.3
slug: ensembl
tags:
- Genomics
- Bioinformatics
- Genome Annotation
- Variant Annotation
- Comparative Genomics
- Life Sciences
- REST API
website: https://www.ensembl.org
---
