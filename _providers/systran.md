---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Systran Agentic Access
  operation_count: 55
  slug: systran-agentic-access
  summary_line: 55 operations · 30 acting
api_count: 8
apis:
- description: The Corpus API from SYSTRAN — 11 operation(s) for corpus.
  name: SYSTRAN Corpus API
  slug: systran-corpus-api
- description: The Dictionary API from SYSTRAN — 14 operation(s) for dictionary.
  name: SYSTRAN Dictionary API
  slug: systran-dictionary-api
- description: The File Translation API from SYSTRAN — 8 operation(s) for file translation.
  name: SYSTRAN File Translation API
  slug: systran-file-translation-api
- description: The Language Detection API from SYSTRAN — 2 operation(s) for language detection.
  name: SYSTRAN Language Detection API
  slug: systran-language-detection-api
- description: The NLP API from SYSTRAN — 4 operation(s) for nlp.
  name: SYSTRAN NLP API
  slug: systran-nlp-api
- description: The Profiles API from SYSTRAN — 7 operation(s) for profiles.
  name: SYSTRAN Profiles API
  slug: systran-profiles-api
- description: The Supported Languages API from SYSTRAN — 4 operation(s) for supported languages.
  name: SYSTRAN Supported Languages API
  slug: systran-supported-languages-api
- description: The Translation API from SYSTRAN — 4 operation(s) for translation.
  name: SYSTRAN Translation API
  slug: systran-translation-api
artifact_total: 15
collections:
- collection_type: open
  name: SYSTRAN Translate & NLP API
  slug: open-systran
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/systran-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/systran-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/systran-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SYSTRAN
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/systran
- group: company
  title: ''
  type: Website
  url: https://www.systran.net
- group: docs
  title: ''
  type: Documentation
  url: https://docs.systran.net/translateAPI/en/
- group: commercial
  title: ''
  type: Plans
  url: plans/systran-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/systran-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/systran-finops.yml
created: '2026-07-03'
description: SYSTRAN is a machine translation and natural language processing company offering neural (Pure Neural Machine Translation / PNMT) translation across 50+ languages. The SYSTRAN Translate API is a RESTful service (base https://api-translate.systran.net) that translates text, files, and HTML, detects and lists supported languages, and manages translation profiles, user dictionaries, and corpora. The broader SYSTRAN Platform / SYSTRAN.io surface adds NLP operations - morphology, tokenization, segmentation, named entity recognition, and language identification. Requests authenticate with an API key (key query parameter or Authorization header). SYSTRAN sells access as a Developer cloud subscription (14-day / 500,000-character free trial) plus Professional SaaS and Enterprise cloud/on-premise plans, billed per character.
finops:
- name: Systran Finops
  service_category: Machine Learning and AI
  slug: systran-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/systran.png
layout: provider
modified: '2026-07-03'
name: SYSTRAN
nav: Providers
network: true
overview: 'SYSTRAN publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Corpus API, Dictionary API, File Translation API, and 5 more. Tagged areas include Machine Translation, Translation, NLP, Neural Machine Translation, and Localization.


  SYSTRAN''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Systran Plans Pricing
  plan_count: 4
  slug: systran-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 4
  name: Systran Rate Limits
  slug: systran-rate-limits
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Systran Authentication
  slug: systran-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Systran Domain Security
  slug: systran-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: systran
tags:
- Machine Translation
- Translation
- NLP
- Neural Machine Translation
- Localization
- Language Detection
website: https://www.systran.net
---
