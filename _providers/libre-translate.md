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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Libre Translate Agentic Access
  operation_count: 7
  slug: libre-translate-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: The misc API from LibreTranslate — 3 operation(s) for misc.
  name: LibreTranslate misc API
  slug: libre-translate-misc-api
- description: The translate API from LibreTranslate — 4 operation(s) for translate.
  name: LibreTranslate translate API
  slug: libre-translate-translate-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LibreTranslate misc API
  slug: open-libre-translate-misc-api
- collection_type: open
  name: LibreTranslate misc translate API
  slug: open-libre-translate-translate-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/libre-translate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/libre-translate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://libretranslate.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.libretranslate.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/LibreTranslate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/libretranslate
- group: company
  title: ''
  type: Blog
  url: https://community.libretranslate.com
- group: commercial
  title: ''
  type: Pricing
  url: https://portal.libretranslate.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.libretranslate.com
- group: other
  title: ''
  type: X
  url: https://x.com/libretranslate
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/libre-translate/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/libre-translate/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/libre-translate/refs/heads/main/finops/finops.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-06-13'
description: Free and open-source machine translation REST API supporting 30+ languages with self-hostable deployment and no third-party service dependency. Powered by the open-source Argos Translate library, LibreTranslate provides endpoints for text translation, language detection, file translation, and translation suggestions. Deployable on-premise for full offline capability or accessible via the managed hosted service.
examples:
- key_count: 4
  name: Detect Language
  slug: detect-language
- key_count: 4
  name: List Languages
  slug: list-languages
- key_count: 4
  name: Translate Auto Detect
  slug: translate-auto-detect
- key_count: 4
  name: Translate Batch
  slug: translate-batch
- key_count: 4
  name: Translate Text
  slug: translate-text
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/libre-translate.png
json_schemas:
- name: DetectRequest
  property_count: 2
  slug: detect-request
- name: Language
  property_count: 3
  slug: language
- name: TranslateRequest
  property_count: 6
  slug: translate-request
- name: TranslateResponse
  property_count: 3
  slug: translate-response
layout: provider
modified: '2026-08-08'
name: LibreTranslate
nav: Providers
network: true
overview: 'LibreTranslate publishes 2 APIs on the [APIs.io](https://apis.io/) network: misc API and translate API. Tagged areas include Translation, Machine Translation, Natural Language Processing, Open-Source, and Self-Hosted.


  The LibreTranslate catalog on APIs.io includes 1 Spectral governance ruleset.


  LibreTranslate''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 12
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: LibreTranslate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: libre-translate-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 44.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 42.5
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 21.1
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/libre-translate/refs/heads/main/screenshots/libre-translate-2026-06-20T184504.png
security:
- kind: domain-security
  name: Libre Translate Domain Security
  slug: libre-translate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: libre-translate
tags:
- Translation
- Machine Translation
- Natural Language Processing
- Open-Source
- Self-Hosted
website: https://libretranslate.com
---
