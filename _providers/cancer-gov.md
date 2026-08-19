---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cancer Gov Agentic Access
  operation_count: 6
  slug: cancer-gov-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 10
apis:
- description: RESTful API that lets developers build applications, search tools, and digital platforms over NCI-supported cancer clinical trials data sourced from NCI's Clinical Trials Reporting Program (CTRP). The
  name: NCI Clinical Trials Search API
  slug: clinical-trials-api
- description: 'The external-facing REST interface for the NCI Genomic Data Commons. Drives the GDC Data Portal and GDC Submission Portal and is open for programmatic access. Provides query, download, and submission '
  name: NCI Genomic Data Commons (GDC) API
  slug: gdc-api
- description: RESTful API for the Surveillance, Epidemiology, and End Results (SEER) Program. Supports SEER datasets plus staging APIs for cancer staging (TNM and Collaborative Stage algorithms), enabling developer
  name: NCI SEER API
  slug: seer-api
- description: The NCI Model and Data Clearinghouse (MoDaC) API provides programmatic access to cancer research data, computational models, and associated tools hosted in MoDaC. Developers can search, retrieve metad
  name: NCI MoDaC API
  slug: modac-api
- description: 'Enterprise Vocabulary Services (EVS) exposes NCI Thesaurus and NCI Metathesaurus content — over 192,000 concepts, 154,000 textual definitions, 623,000 synonyms and 630,000 inter-concept relationships '
  name: NCI EVS Terminology API
  slug: evs-api
- description: A suite of syndicated content channels — RSS feeds, the NCI Dictionary Widget, and syndicated publication content — that partner sites and health platforms can embed to deliver authoritative cancer co
  name: NCI Content Syndication Services
  slug: syndication-services
- description: The Diseases API from Cancer.gov — 1 operation(s) for diseases.
  name: Cancer.gov Diseases API
  slug: cancer-gov-diseases-api
- description: The Interventions API from Cancer.gov — 1 operation(s) for interventions.
  name: Cancer.gov Interventions API
  slug: cancer-gov-interventions-api
- description: The Terms API from Cancer.gov — 1 operation(s) for terms.
  name: Cancer.gov Terms API
  slug: cancer-gov-terms-api
- description: The Trials API from Cancer.gov — 2 operation(s) for trials.
  name: Cancer.gov Trials API
  slug: cancer-gov-trials-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NCI Clinical Trials Search Diseases API
  slug: open-cancer-gov-diseases-api
- collection_type: open
  name: NCI Clinical Trials Search Diseases Interventions API
  slug: open-cancer-gov-interventions-api
- collection_type: open
  name: NCI Clinical Trials Search Diseases Terms API
  slug: open-cancer-gov-terms-api
- collection_type: open
  name: NCI Clinical Search Diseases Trials API
  slug: open-cancer-gov-trials-api
- collection_type: open
  name: NCI Clinical Trials Search API
  slug: open-cancer-gov
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cancer-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cancer-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cancer-gov-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NCIOCPL
- group: company
  title: ''
  type: Website
  url: https://www.cancer.gov/
- group: start
  title: ''
  type: Portal
  url: https://api.cancer.gov/
- group: other
  title: ''
  type: SyndicationServices
  url: https://www.cancer.gov/syndication
- group: other
  title: ''
  type: DataScience
  url: https://datascience.cancer.gov/
- group: other
  title: ''
  type: OpenDataPolicy
  url: https://www.cancer.gov/research/resources/open-science
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cancer.gov/policies/privacy-security
- group: other
  title: ''
  type: LicensingAndReuse
  url: https://www.cancer.gov/policies/copyright-reuse
- group: company
  title: ''
  type: Blog
  url: https://www.cancer.gov/publishedcontent/rss/news-events/cancer-currents-blog.rss
created: '2024-07-02'
description: Cancer.gov is the web presence of the National Cancer Institute (NCI), the U.S. federal government's principal agency for cancer research and training. NCI and its partner programs expose a rich set of open APIs covering cancer clinical trials, genomic data, cancer-incidence surveillance, research data and models, terminology and vocabularies, and PDQ content — giving researchers, advocacy groups, clinicians, and application developers programmatic access to authoritative cancer data and content.
finops:
- name: Cancer Gov Finops
  service_category: API
  slug: cancer-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cancer-gov.png
layout: provider
modified: '2026-04-23'
name: Cancer.gov
nav: Providers
network: true
overview: 'Cancer.gov publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Diseases API, Interventions API, Terms API, and 1 more. Tagged areas include Cancer, Federal Government, Healthcare, Research, and Clinical Trials.


  Cancer.gov''s developer surface includes authentication, developer portal, engineering blog, and 9 more developer resources.'
plans:
- name: Cancer Gov Plans Pricing
  plan_count: 3
  slug: cancer-gov-plans-pricing
random_paper: 103
rate_limits:
- limit_count: 5
  name: Cancer Gov Rate Limits
  slug: cancer-gov-rate-limits
score:
  band: thin
  composite: 31.3
  delta: 0.6
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cancer-gov/refs/heads/main/screenshots/cancer-gov-2026-06-20T173920.png
security:
- kind: authentication
  name: Cancer Gov Authentication
  slug: cancer-gov-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cancer Gov Domain Security
  slug: cancer-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cancer-gov
tags:
- Cancer
- Federal Government
- Healthcare
- Research
- Clinical Trials
- Genomics
- Surveillance
- Open Data
website: https://www.cancer.gov/
---
