---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AriBot API provides threat modeling, compliance automation, and AI security analysis endpoints.
  name: AriBot API
  slug: aribot-api
- baseURL: https://api.aribot.ayurak.com
  baseurl_source: declared
  description: 'ayurak-com API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: ayurak-com API
  slug: ayurak-com-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/ayurak-com/rules/ayurak-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ayurak-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ayurak-com/json-ld/ayurak-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ayurak-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ayurak-com/vocabulary/ayurak-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ayurak-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ayurak-com/data-model/ayurak-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ayurak-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/ayurak-com/cli/ayurak-com-cli.yml
  title: ''
  type: CLI
  url: cli/ayurak-com-cli.yml
- group: design
  href: https://artifacts.apis.io/ayurak-com/conformance/ayurak-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ayurak-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/ayurak-com/a2a/ayurak-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ayurak-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/ayurak-com/well-known/ayurak-com-aribot-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ayurak-com-aribot-security.txt
- group: agent
  href: https://artifacts.apis.io/ayurak-com/well-known/ayurak-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ayurak-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ayurak-com/hosts/ayurak-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ayurak-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/ayurak-com/packages/ayurak-com-packages.yml
  title: ''
  type: SDKs
  url: packages/ayurak-com-packages.yml
- group: build
  href: https://artifacts.apis.io/ayurak-com/packages/ayurak-com-packages.yml
  title: ''
  type: Packages
  url: packages/ayurak-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://ayurak.com/solutions/security
- group: auth
  href: https://artifacts.apis.io/ayurak-com/security/ayurak-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ayurak-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ayurak.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ayurak.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ayurak.com/
- group: company
  title: ''
  type: Blog
  url: https://ayurak.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ayurak.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ayurak.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ayurak.com/legal/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ayurak.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ayurak.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developer.ayurak.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ayurak
- group: build
  title: ''
  type: Postman
  url: https://ayurak.com/legal/privacy
coverage:
  checked: '2026-10-30'
  detail: API specification endpoints require authentication credentials, returning 403 errors.
  evidence:
  - status: 403
    url: https://api.aribot.ayurak.com/swagger.json
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Ayurak AI delivers enterprise AI solutions that integrate advanced security, healthcare intelligence, and emergency response capabilities. Their platform offers products like Aribot for security monitoring, Journey for Health medical insights, and Save‑Lives emergency coordination, empowering organizations to protect assets, improve patient outcomes, and respond swiftly to crises.
image: https://ayurak.com/ayurak-logo.png
json_schemas:
- name: PostAribotApiV2ThreatModelingAnalyzeRequest
  property_count: 4
  slug: ayurak-com-post-aribot-api-v2-threat-modeling-analyze-request
- name: PostAribotApiV2ThreatModelingAnalyzeResponse
  property_count: 1
  slug: ayurak-com-post-aribot-api-v2-threat-modeling-analyze-response
- name: PostV2ThreatModelingAnalyzeRequest
  property_count: 1
  slug: ayurak-com-post-v2-threat-modeling-analyze-request
jsonld:
- class_count: 3
  name: Ayurak Com Context
  property_count: 5
  slug: ayurak-com-context
layout: provider
modified: '2026-10-29'
name: ayurak-com
nav: Providers
network: true
overview: 'ayurak-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Security, Healthcare, and Emergency Response.


  The ayurak-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ayurak-com''s developer surface includes CLI, documentation, API reference, engineering blog, pricing, getting-started guide, support, and 19 more developer resources.'
plans:
- name: Ayurak Com Plans Pricing
  plan_count: 0
  slug: ayurak-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Ayurak Com Rate Limits
  slug: ayurak-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ayurak-com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ayurak-com-rules
scopes:
- name: Ayurak Com Scopes
  scope_count: 0
  slug: ayurak-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 39.3
    discoverability: 57.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ayurak-com/ayurak-com-2026-11-03T121454.png
security:
- kind: authentication
  name: Ayurak Com Authentication
  slug: ayurak-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ayurak Com Domain Security
  slug: ayurak-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ayurak-com
tags:
- Company
- Artificial Intelligence
- Security
- Healthcare
- Emergency Response
- Technology
website: https://ayurak.com/
---
