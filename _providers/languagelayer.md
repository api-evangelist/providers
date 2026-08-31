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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Languagelayer Agentic Access
  operation_count: 2
  slug: languagelayer-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: The Batch API from languagelayer — 1 operation(s) for batch.
  name: languagelayer Batch API
  slug: languagelayer-batch-api
- description: The Detect API from languagelayer — 1 operation(s) for detect.
  name: languagelayer Detect API
  slug: languagelayer-detect-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: languagelayer Batch API
  slug: open-languagelayer-batch-api
- collection_type: open
  name: languagelayer Batch Detect API
  slug: open-languagelayer-detect-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/languagelayer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/languagelayer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/languagelayer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://languagelayer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://languagelayer.com/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/apilayer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apilayer/
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://languagelayer.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://languagelayer.com/api-status
- group: other
  title: ''
  type: X
  url: https://x.com/apilayernet
- group: commercial
  title: ''
  type: Plans
  url: plans/languagelayer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/languagelayer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/languagelayer-finops.yml
created: '2026-06-13'
description: Language detection REST API that identifies 173 languages and accents from text with confidence scores, character usage statistics, and batch processing support, powered by an AI-based detection algorithm via the APILayer platform.
examples:
- key_count: 4
  name: Batch Detect
  slug: batch-detect
- key_count: 4
  name: Detect English
  slug: detect-english
finops:
- name: Languagelayer Finops
  service_category: ''
  slug: languagelayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/languagelayer.png
json_schemas:
- name: DetectResponse
  property_count: 3
  slug: detect-response
- name: LanguageResult
  property_count: 5
  slug: language-result
jsonld:
- class_count: 0
  name: Languagelayer Context
  property_count: 0
  slug: languagelayer
layout: provider
modified: '2026-06-13'
name: languagelayer
nav: Providers
network: true
overview: 'languagelayer publishes 2 APIs on the [APIs.io](https://apis.io/) network: Batch API and Detect API. Tagged areas include Language Detection, Natural Language Processing, Text Analysis, Machine-Learning, and Artificial Intelligence.


  The languagelayer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  languagelayer''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Languagelayer Plans Pricing
  plan_count: 4
  slug: languagelayer-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Languagelayer Rate Limits
  slug: languagelayer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: languagelayer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: languagelayer-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 59.9
    developer_ergonomics: 22.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/languagelayer/refs/heads/main/screenshots/languagelayer-2026-06-20T184308.png
security:
- kind: authentication
  name: Languagelayer Authentication
  slug: languagelayer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Languagelayer Domain Security
  slug: languagelayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: languagelayer
tags:
- Language Detection
- Natural Language Processing
- Text Analysis
- Machine-Learning
- Artificial Intelligence
website: https://languagelayer.com/
---
