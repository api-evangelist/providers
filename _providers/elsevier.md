---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Elsevier Agentic Access
  operation_count: 8
  slug: elsevier-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: Scopus delivers a comprehensive view of the world of research, allowing tracking, analysis, and visualization of research data across publishers, journals, books, conference proceedings, and trade pub
  name: Elsevier Scopus APIs
  slug: elsevier-scopus-apis
- description: ScienceDirect APIs expose peer-reviewed full-text scientific, technical and medical content from all scholarly publications indexed by ScienceDirect, Elsevier's premier scientific platform.
  name: Elsevier ScienceDirect APIs
  slug: elsevier-sciencedirect-apis
- description: The SciVal API gives access to a comprehensive set of metrics for researchers (Scopus Author profiles) and 8,500+ institutions available in SciVal, Elsevier's platform for research performance benchma
  name: Elsevier SciVal API
  slug: elsevier-scival-api
- description: Engineering Village APIs provide programmatic access to engineering research literature, indexed publications, and engineering-focused content across multiple databases.
  name: Elsevier Engineering Village API
  slug: elsevier-engineering-village-api
- description: Embase APIs provide access to biomedical and pharmacological abstracts and indexing for life sciences research, drug development, and evidence-based medicine.
  name: Elsevier Embase API
  slug: elsevier-embase-api
- baseURL: https://api.elsevier.com
  baseurl_source: spec
  description: The Abstract API from Elsevier — 5 operation(s) for abstract.
  name: Elsevier Abstract API
  slug: elsevier-abstract-api
- baseURL: https://api.elsevier.com
  baseurl_source: spec
  description: The Search API from Elsevier — 3 operation(s) for search.
  name: Elsevier Search API
  slug: elsevier-search-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elsevier Scopus APIs Abstract API
  slug: open-elsevier-abstract-api
- collection_type: open
  name: Elsevier Scopus APIs Abstract Search API
  slug: open-elsevier-search-api
- collection_type: open
  name: Elsevier Scopus APIs
  slug: open-elsevier
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elsevier-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elsevier-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elsevier-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elsevier
- group: start
  title: ''
  type: Portal
  url: https://dev.elsevier.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.elsevier.com/getting_started.html
- group: docs
  title: ''
  type: Documentation
  url: https://dev.elsevier.com/api_docs.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.elsevier.com/api_service_agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://www.elsevier.com/locate/privacypolicy
- group: build
  title: ''
  type: Examples
  url: https://dev.elsevier.com/examples.html
- group: docs
  title: ''
  type: Guides
  url: https://dev.elsevier.com/technical_documentation.html
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ElsevierDev/elsapy
- group: operate
  title: ''
  type: Support
  url: https://dev.elsevier.com/support.html
- group: company
  title: ''
  type: Blog
  url: https://www.elsevier.com/connect
created: '2023-11-22'
description: Elsevier is a Dutch academic publishing company specializing in scientific, technical, and medical content. Its products include journals such as The Lancet and Cell, the ScienceDirect collection of electronic journals, the online citation database Scopus, the SciVal research performance platform, and the ClinicalKey search engine for clinicians.
finops:
- name: Elsevier Finops
  service_category: API
  slug: elsevier-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elsevier.png
layout: provider
modified: '2026-04-28'
name: Elsevier
nav: Providers
network: true
overview: 'Elsevier publishes 2 APIs on the [APIs.io](https://apis.io/) network: Abstract API and Search API. Tagged areas include Content, Journals, Medical, Research, and Scientific.


  Elsevier''s developer surface includes authentication, developer portal, getting-started guide, documentation, code examples, support, engineering blog, and 7 more developer resources.'
plans:
- name: Elsevier Plans Pricing
  plan_count: 3
  slug: elsevier-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Elsevier Rate Limits
  slug: elsevier-rate-limits
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/screenshots/elsevier-2026-06-20T180616.png
security:
- kind: authentication
  name: Elsevier Authentication
  slug: elsevier-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Elsevier Domain Security
  slug: elsevier-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: elsevier
tags:
- Content
- Journals
- Medical
- Research
- Scientific
- Technical
website: https://dev.elsevier.com/
---
