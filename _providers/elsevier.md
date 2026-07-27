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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Elsevier Agentic Access
  operation_count: 8
  slug: elsevier-agentic-access
  summary_line: 8 operations
api_count: 7
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
- description: The Abstract API from Elsevier — 5 operation(s) for abstract.
  name: Elsevier Abstract API
  slug: elsevier-abstract-api
- description: The Search API from Elsevier — 3 operation(s) for search.
  name: Elsevier Search API
  slug: elsevier-search-api
artifact_total: 14
collections:
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
random_paper: 47
rate_limits:
- limit_count: 5
  name: Elsevier Rate Limits
  slug: elsevier-rate-limits
score:
  band: developing
  composite: 48.1
  delta: 1.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.0
    developer_ergonomics: 52.2
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 46.4
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 43.5
  schema_version: 0.5
  scored_at: '2026-07-27'
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
