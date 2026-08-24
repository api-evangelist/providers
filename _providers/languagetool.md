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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Languagetool Agentic Access
  operation_count: 5
  slug: languagetool-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 3
apis:
- description: The Check API from LanguageTool — 1 operation(s) for check.
  name: LanguageTool Check API
  slug: languagetool-check-api
- description: The Languages API from LanguageTool — 1 operation(s) for languages.
  name: LanguageTool Languages API
  slug: languagetool-languages-api
- description: The Words API from LanguageTool — 3 operation(s) for words.
  name: LanguageTool Words API
  slug: languagetool-words-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LanguageTool HTTP Check API
  slug: open-languagetool-check-api
- collection_type: open
  name: LanguageTool HTTP Check Languages API
  slug: open-languagetool-languages-api
- collection_type: open
  name: LanguageTool HTTP Check Words API
  slug: open-languagetool-words-api
- collection_type: open
  name: LanguageTool HTTP API
  slug: open-languagetool
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/languagetool-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/languagetool-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/languagetool
- group: company
  title: ''
  type: Website
  url: https://languagetool.org
- group: docs
  title: ''
  type: Documentation
  url: https://languagetool.org/http-api/
- group: other
  title: ''
  type: Developer
  url: https://dev.languagetool.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/languagetool-org/languagetool
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://languagetool.org/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://languagetool.org/legal/terms
created: '2025-02-08'
description: LanguageTool is an open-source proofreading and grammar checking tool that supports more than 25 languages. The HTTP API enables developers to programmatically check texts for grammar and style issues, list supported languages, and manage personal dictionaries.
finops:
- name: Languagetool Finops
  service_category: API
  slug: languagetool-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/languagetool.png
json_schemas:
- name: LanguageTool Match
  property_count: 8
  slug: languagetool-match
layout: provider
modified: '2026-05-19'
name: LanguageTool
nav: Providers
network: true
overview: 'LanguageTool publishes 3 APIs on the [APIs.io](https://apis.io/) network: Check API, Languages API, and Words API. Tagged areas include Grammar, Language, Proofreading, Spell Check, and Style Check.


  The LanguageTool catalog on APIs.io includes 1 Spectral governance ruleset.


  LanguageTool''s developer surface includes documentation, GitHub presence, and 7 more developer resources.'
plans:
- name: Languagetool Plans Pricing
  plan_count: 3
  slug: languagetool-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Languagetool Rate Limits
  slug: languagetool-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: LanguageTool API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: languagetool-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.3
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 55.0
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/languagetool/refs/heads/main/screenshots/languagetool-2026-06-20T184310.png
security:
- kind: domain-security
  name: Languagetool Domain Security
  slug: languagetool-domain-security
  summary_line: TLSv1.3 · DMARC
slug: languagetool
tags:
- Grammar
- Language
- Proofreading
- Spell Check
- Style Check
- Text Analysis
website: https://languagetool.org
---
