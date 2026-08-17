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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Textgears Agentic Access
  operation_count: 20
  slug: textgears-agentic-access
  summary_line: 20 operations · 16 acting
api_count: 7
apis:
- description: Account usage and quota management
  name: TextGears Account API
  slug: textgears-account-api
- description: Custom dictionary management
  name: TextGears Dictionaries API
  slug: textgears-dictionaries-api
- description: Custom exception (whitelist) management
  name: TextGears Exceptions API
  slug: textgears-exceptions-api
- description: Grammar and spelling error detection and correction
  name: TextGears Grammar API
  slug: textgears-grammar-api
- description: Language detection
  name: TextGears Language API
  slug: textgears-language-api
- description: Text readability scoring and analysis
  name: TextGears Readability API
  slug: textgears-readability-api
- description: Text summarization and keyword extraction
  name: TextGears Summarization API
  slug: textgears-summarization-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TextGears Account API
  slug: open-textgears-account-api
- collection_type: open
  name: TextGears Account Dictionaries API
  slug: open-textgears-dictionaries-api
- collection_type: open
  name: TextGears Account Exceptions API
  slug: open-textgears-exceptions-api
- collection_type: open
  name: TextGears Account Grammar API
  slug: open-textgears-grammar-api
- collection_type: open
  name: TextGears Account Language API
  slug: open-textgears-language-api
- collection_type: open
  name: TextGears Account Readability API
  slug: open-textgears-readability-api
- collection_type: open
  name: TextGears Account Summarization API
  slug: open-textgears-summarization-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/textgears-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/textgears-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/textgears-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://textgears.com
- group: docs
  title: ''
  type: Documentation
  url: https://textgears.com/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/textgears
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/textgears
- group: commercial
  title: ''
  type: Pricing
  url: https://textgears.com/#pricing
- group: other
  title: ''
  type: X
  url: https://x.com/textgears
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/textgears/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/textgears/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/textgears/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: TextGears is a grammar checking and text analysis REST API providing spelling corrections, grammar error detection, readability scoring, language detection, and text summarization across 11 languages. The service processes over 10.8 million API requests daily and offers distributed infrastructure across Estonia, Singapore, and the United States for low-latency access.
examples:
- key_count: 2
  name: Detect Language
  slug: detect-language
- key_count: 2
  name: Grammar Check
  slug: grammar-check
- key_count: 2
  name: Readability
  slug: readability
- key_count: 2
  name: Spelling Check
  slug: spelling-check
- key_count: 2
  name: Summarize
  slug: summarize
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/textgears.png
json_schemas:
- name: Language Detection Response
  property_count: 2
  slug: detect-response
- name: Grammar Check Request
  property_count: 7
  slug: grammar-request
- name: Grammar Check Response
  property_count: 4
  slug: grammar-response
jsonld:
- class_count: 0
  name: Textgears Context
  property_count: 0
  slug: textgears
layout: provider
modified: '2026-06-13'
name: TextGears
nav: Providers
network: true
overview: 'TextGears publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Dictionaries API, Exceptions API, and 4 more. Tagged areas include Grammar, Spelling, Text Analysis, Readability, and Natural Language Processing.


  The TextGears catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TextGears'' developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 89
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: TextGears API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: textgears-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/textgears/refs/heads/main/screenshots/textgears-2026-06-20T195206.png
security:
- kind: authentication
  name: Textgears Authentication
  slug: textgears-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Textgears Domain Security
  slug: textgears-domain-security
  summary_line: TLSv1.2
slug: textgears
tags:
- Grammar
- Spelling
- Text Analysis
- Readability
- Natural Language Processing
- NLP
- Text Summarization
- Language Detection
website: https://textgears.com
---
