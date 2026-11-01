---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: WebCapture API for converting URLs to PDF, images, or markdown.
  name: WebCapture API
  slug: webcapture-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/webcapture/rules/webcapture-rules.yml
  title: ''
  type: Spectral
  url: rules/webcapture-rules.yml
- group: design
  href: https://artifacts.apis.io/webcapture/json-ld/webcapture-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/webcapture-context.jsonld
- group: agent
  href: https://artifacts.apis.io/webcapture/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/webcapture/data-model/webcapture-data-model.yml
  title: ''
  type: DataModel
  url: data-model/webcapture-data-model.yml
- group: operate
  href: https://artifacts.apis.io/webcapture/rate-limits/webcapture-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/webcapture-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/webcapture/plans/webcapture-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/webcapture-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/webcapture/vocabulary/webcapture-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/webcapture-vocabulary.yml
- group: start
  href: https://artifacts.apis.io/webcapture/sandbox/webcapture-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/webcapture-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://webcapture.io/security
- group: auth
  href: https://artifacts.apis.io/webcapture/authentication/webcapture-authentication.yml
  title: ''
  type: Authentication
  url: authentication/webcapture-authentication.yml
- group: design
  href: https://artifacts.apis.io/webcapture/errors/webcapture-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/webcapture-problem-types.yml
- group: design
  href: https://artifacts.apis.io/webcapture/conformance/webcapture-conformance.yml
  title: ''
  type: Conformance
  url: conformance/webcapture-conformance.yml
- group: agent
  href: https://artifacts.apis.io/webcapture/llms/webcapture-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/webcapture-llms.txt
- group: other
  href: https://artifacts.apis.io/webcapture/a2a/webcapture-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/webcapture-a2a.yml
- group: auth
  href: https://artifacts.apis.io/webcapture/well-known/webcapture-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webcapture-security.txt
- group: agent
  href: https://artifacts.apis.io/webcapture/well-known/webcapture-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/webcapture-well-known.yml
- group: other
  href: https://artifacts.apis.io/webcapture/hosts/webcapture-hosts.yml
  title: ''
  type: Hosts
  url: hosts/webcapture-hosts.yml
- group: other
  href: https://artifacts.apis.io/webcapture/vendors/webcapture-vendors.yml
  title: ''
  type: Vendors
  url: vendors/webcapture-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://webcapture.io/status
- group: auth
  title: ''
  type: Security
  url: https://webcapture.io/security
- group: start
  title: ''
  type: GettingStarted
  url: https://webcapture.io/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://webcapture.io/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/webcapture/security/webcapture-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/webcapture-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/webcapture/security/webcapture-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/webcapture-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/webcapture/security/webcapture-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webcapture-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://webcapture.io
- group: docs
  title: ''
  type: Documentation
  url: https://webcapture.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://webcapture.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://webcapture.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webcapture.io/privacy
created: '2026-10-30'
description: webcapture provides a REST and MCP API that renders any public web page into a print‑stable PDF, as well as full‑page or viewport PNG/JPEG/WebP screenshots and clean Markdown extraction. The service runs headless Chromium under the hood and offers Free, Pro, and Scale plans with tiered render quotas, webhook delivery, and artifact retention options. Developers can integrate a single API call to generate PDFs or images from URLs, simplifying archiving, reporting, and content sharing workflows.
image: https://webcapture.io/logo.png
jsonld:
- class_count: 7
  name: Webcapture Context
  property_count: 22
  slug: webcapture-context
layout: provider
modified: '2026-10-30'
name: webcapture
nav: Providers
network: true
overview: 'webcapture publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include WebCapture, PDF, API, SaaS, and Automation.


  The webcapture catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  webcapture''s developer surface includes sandbox, authentication, getting-started guide, API reference, documentation, pricing, and 24 more developer resources.'
plans:
- name: Webcapture Plans Pricing
  plan_count: 3
  slug: webcapture-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Webcapture Rate Limits
  slug: webcapture-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: webcapture API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: webcapture-rules
scopes:
- name: Webcapture Scopes
  scope_count: 0
  slug: webcapture-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 90.3
    catalog_earned_first_party: 0.0
    catalog_gap: 24.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 75.8
    contract_governance: 79.1
    contract_quality: 14.7
    developer_ergonomics: 54.0
    discoverability: 66.1
    operational_transparency: 54.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Webcapture Authentication
  slug: webcapture-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Webcapture Domain Security
  slug: webcapture-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Webcapture Vulnerability Disclosure
  slug: webcapture-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Webcapture Trust Center
  slug: webcapture-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: webcapture
tags:
- WebCapture
- PDF
- API
- SaaS
- Automation
website: https://webcapture.io
---
