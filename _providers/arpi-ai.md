---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Arpi Ai Agentic Access
  operation_count: 11
  slug: arpi-ai-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 1
apis:
- baseURL: https://openapi.arpi.ai
  baseurl_source: declared
  description: Token issuance endpoint using the OAuth 2.0 Client Credentials Grant. No prior authentication required — exchange your Client ID and Client Secret for a short-lived JWT access token.
  name: ARPI Inc. Authentication API
  slug: arpi-ai-authentication-api
- baseURL: https://openapi.arpi.ai
  baseurl_source: declared
  description: Medical image analysis API. Requires Bearer token.
  name: ARPI Inc. Diag API
  slug: arpi-ai-diag-api
artifact_total: 17
asyncapis:
- description: ''
  name: Arpi Ai Webhooks
  slug: arpi-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/arpi-ai/agentic-access/arpi-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arpi-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/arpi-ai/rules/arpi-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/arpi-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/arpi-ai/json-ld/arpi-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arpi-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/arpi-ai/vocabulary/arpi-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arpi-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arpi-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arpi-ai/asyncapi/arpi-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/arpi-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/arpi-ai/data-model/arpi-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arpi-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/arpi-ai/authentication/arpi-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arpi-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/arpi-ai/errors/arpi-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arpi-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arpi-ai/conformance/arpi-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arpi-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/arpi-ai/hosts/arpi-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arpi-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/arpi-ai/vendors/arpi-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arpi-ai-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.arpi.ai/news-media/media
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arpi.ai/#/#-quick-start
- group: auth
  href: https://artifacts.apis.io/arpi-ai/security/arpi-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arpi-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arpi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arpi.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.arpi.ai/en/news-media/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arpi.ai/en/terms//terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arpi.ai/en/terms//privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.arpi.ai/en/contact-us/request
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://arpi.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ARPI Inc. provides advanced ECG analysis AI solutions, developing the ECG Buddy suite of products that deliver AI-powered electrocardiogram interpretation for hospitals and clinics. Their platform sets a new standard in clinical settings with practical and innovative medical AI technology, recognized with a Ministerial Commendation in December 2025.
image: https://www.arpi.ai/meta/img_meta.png
json_schemas:
- name: AiCommentResponse
  property_count: 4
  slug: arpi-ai-ai-comment-response
- name: DiagAvailableResponse
  property_count: 10
  slug: arpi-ai-diag-available-response
- name: DiagProductsResponse
  property_count: 4
  slug: arpi-ai-diag-products-response
- name: DiagResultResponse
  property_count: 4
  slug: arpi-ai-diag-result-response
- name: HospitalTokenRequest
  property_count: 3
  slug: arpi-ai-hospital-token-request
- name: UsageSummaryResponse
  property_count: 8
  slug: arpi-ai-usage-summary-response
jsonld:
- class_count: 18
  name: Arpi Ai Context
  property_count: 55
  slug: arpi-ai-context
layout: provider
modified: '2026-11-01'
name: ARPI Inc.
nav: Providers
network: true
overview: 'ARPI Inc. publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Authentication API and Diag API. Tagged areas include Medical AI, Healthcare, ECG, Diagnostics, and Artificial Intelligence.


  The ARPI Inc. catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ARPI Inc.''s developer surface includes authentication, getting-started guide, documentation, engineering blog, support, and 16 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 0
  name: Arpi Ai Rate Limits
  slug: arpi-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: ARPI Inc. API Rules
  rule_count: 65
  severity_counts:
    error: 56
    hint: 0
    info: 2
    warn: 7
  slug: arpi-ai-rules
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 73.9
    developer_ergonomics: 32.6
    discoverability: 67.0
    operational_transparency: 7.9
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arpi Ai Authentication
  slug: arpi-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arpi Ai Domain Security
  slug: arpi-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: analysis
  slug: arpi-ai-analysis-skill
- name: authentication
  slug: arpi-ai-authentication-skill
slug: arpi-ai
tags:
- Medical AI
- Healthcare
- ECG
- Diagnostics
- Artificial Intelligence
website: https://arpi.ai/
---
