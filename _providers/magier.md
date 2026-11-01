---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Shield API provides content redaction and transformation via a single REST endpoint.
  name: Magier AI Shield API
  slug: magier-ai-shield-api
- baseURL: https://api.magier.ai
  baseurl_source: declared
  description: 'Magier AI API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Magier AI API
  slug: magier-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/magier/rules/magier-rules.yml
  title: ''
  type: Spectral
  url: rules/magier-rules.yml
- group: design
  href: https://artifacts.apis.io/magier/json-ld/magier-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/magier-context.jsonld
- group: design
  href: https://artifacts.apis.io/magier/vocabulary/magier-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/magier-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/magier/data-model/magier-data-model.yml
  title: ''
  type: DataModel
  url: data-model/magier-data-model.yml
- group: design
  href: https://artifacts.apis.io/magier/conformance/magier-conformance.yml
  title: ''
  type: Conformance
  url: conformance/magier-conformance.yml
- group: other
  href: https://artifacts.apis.io/magier/hosts/magier-hosts.yml
  title: ''
  type: Hosts
  url: hosts/magier-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://magier.ai/press
- group: auth
  href: https://artifacts.apis.io/magier/security/magier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/magier-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://magier.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://magier.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://magier.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://magier.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://magier.ai/docs/start-guide
- group: company
  title: ''
  type: Blog
  url: https://magier.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://magier.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://magier.ai/legal/term
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://magier.ai/legal/privacy
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are HTML without machine‑readable OpenAPI or other contracts.
  evidence:
  - status: 200
    url: https://magier.ai/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Magier AI provides end-to-end LLM cybersecurity solutions, offering compliance enforcement, risk management, and AI governance tools. Their platform includes AI pentesting, data redaction, policy generation, and audit-ready evidence across frameworks like ISO 42001, NIST AI RMF, HIPAA, SOC 2, and GDPR. Targeting startups to enterprises, Magier AI helps organizations monitor AI vendor risk, enforce data controls, and streamline compliance reporting.
image: https://magier.ai/magier-social-preview.png
json_schemas:
- name: PostApiDlpTransformRedactRequest
  property_count: 4
  slug: magier-post-api-dlp-transform-redact-request
jsonld:
- class_count: 1
  name: Magier Context
  property_count: 4
  slug: magier-context
layout: provider
modified: '2026-10-18'
name: Magier AI
nav: Providers
network: true
overview: 'Magier AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Cybersecurity, Compliance, and Governance.


  The Magier AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Magier AI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, and 12 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Magier AI API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: magier-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 40.5
    discoverability: 58.9
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Magier Domain Security
  slug: magier-domain-security
  summary_line: TLSv1.3 · DMARC
slug: magier
tags:
- Company
- Artificial Intelligence
- Cybersecurity
- Compliance
- Governance
website: https://magier.ai/
---
