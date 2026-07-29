---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Languagetools Agentic Access
  operation_count: 5
  slug: languagetools-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 3
apis:
- description: The Check API from LanguageTool — 1 operation(s) for check.
  name: LanguageTool Check API
  slug: languagetools-check-api
- description: The Languages API from LanguageTool — 1 operation(s) for languages.
  name: LanguageTool Languages API
  slug: languagetools-languages-api
- description: The Words API from LanguageTool — 3 operation(s) for words.
  name: LanguageTool Words API
  slug: languagetools-words-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/languagetools-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/languagetools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://languagetool.org
- group: docs
  title: ''
  type: Documentation
  url: https://languagetool.org/http-api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/languagetool-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/languagetool
- group: company
  title: ''
  type: Blog
  url: https://languagetool.org/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://languagetool.org/proofreading-api
- group: other
  title: ''
  type: X
  url: https://x.com/languagetoolorg
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/languagetools/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/languagetools/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/languagetools/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Open-source grammar, style, and spell checking REST API supporting 25+ languages with AI-powered error detection, style suggestions, and text improvements. Used by 100+ companies to enhance software with proofreading capabilities via a simple HTTP API returning JSON responses. Hosted on GDPR-compliant servers in Germany with no text storage.
examples:
- key_count: 2
  name: Check Markup Request
  slug: check-markup-request
- key_count: 3
  name: Check Text Request
  slug: check-text-request
- key_count: 3
  name: Check Text Response
  slug: check-text-response
- key_count: 3
  name: Words Add Request
  slug: words-add-request
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/languagetools.png
json_schemas:
- name: CheckRequest
  property_count: 14
  slug: check-request
- name: CheckResponse
  property_count: 3
  slug: check-response
- name: Language
  property_count: 3
  slug: language
- name: WordsResponse
  property_count: 1
  slug: words-response
layout: provider
modified: '2026-06-13'
name: LanguageTool
nav: Providers
network: true
overview: 'LanguageTool publishes 3 APIs on the [APIs.io](https://apis.io/) network: Check API, Languages API, and Words API. Tagged areas include Grammar, Spell Check, Style, Proofreading, and NLP.


  The LanguageTool catalog on APIs.io includes 1 Spectral governance ruleset.


  LanguageTool''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 6
  slug: plans
random_paper: 20
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: LanguageTool API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: languagetools-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.3
  delta: -5.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/languagetools/refs/heads/main/screenshots/languagetools-2026-06-20T184312.png
security:
- kind: domain-security
  name: Languagetools Domain Security
  slug: languagetools-domain-security
  summary_line: TLSv1.3 · DMARC
slug: languagetools
tags:
- Grammar
- Spell Check
- Style
- Proofreading
- NLP
- Natural Language Processing
- Writing
- Open Source
website: https://languagetool.org
---
