---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'blumify-io API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: blumify-io API
  slug: blumify-io-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/blumify-io/plans/blumify-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blumify-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blumify-io/rules/blumify-io-rules.yml
  title: ''
  type: Spectral
  url: rules/blumify-io-rules.yml
- group: design
  href: https://artifacts.apis.io/blumify-io/json-ld/blumify-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blumify-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/blumify-io/vocabulary/blumify-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blumify-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blumify-io/data-model/blumify-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blumify-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/blumify-io/conformance/blumify-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blumify-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blumify-io/llms/blumify-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blumify-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/blumify-io/well-known/blumify-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blumify-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/blumify-io/hosts/blumify-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blumify-io-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://blumify.io/people/peter-navarro/topics/media
- group: other
  title: ''
  type: Leadership
  url: https://blumify.io/people/david-sacks/topics/leadership
- group: auth
  href: https://artifacts.apis.io/blumify-io/security/blumify-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blumify-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blumify.io/
- group: docs
  title: ''
  type: Documentation
  url: https://blumify.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://blumify.io/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://blumify.io/pro?from=pricing_url
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blumify.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blumify.io/privacy
created: '2026-10-29'
description: Blumify provides AI-powered transcription of videos and podcasts, tracking statements from leaders in artificial intelligence and finance. Users can follow up to three influencers for free, with paid Unlimited plans offering unlimited follows, email alerts, and higher transcription limits. The platform aggregates interviews, speeches, posts, and central bank statements, presenting searchable transcripts, summaries, and change‑of‑view analyses.
image: https://blumify.io/og/home
json_schemas:
- name: PostApiMediaV1MeTranscriptsRequest
  property_count: 1
  slug: blumify-io-post-api-media-v1-me-transcripts-request
- name: PostApiMediaV1TranscribeRequest
  property_count: 1
  slug: blumify-io-post-api-media-v1-transcribe-request
jsonld:
- class_count: 2
  name: Blumify Io Context
  property_count: 1
  slug: blumify-io-context
layout: provider
modified: '2026-10-29'
name: blumify-io
nav: Providers
network: true
overview: 'blumify-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Finance, Transcription, and Data.


  The blumify-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  blumify-io''s developer surface includes documentation, API reference, pricing, and 15 more developer resources.'
plans:
- name: Blumify Io Plans Pricing
  plan_count: 2
  slug: blumify-io-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Blumify Io Rate Limits
  slug: blumify-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: blumify-io API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: blumify-io-rules
scopes:
- name: Blumify Io Scopes
  scope_count: 0
  slug: blumify-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 16.7
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blumify Io Authentication
  slug: blumify-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Blumify Io Domain Security
  slug: blumify-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blumify-io
tags:
- Company
- AI
- Finance
- Transcription
- Data
- Analytics
website: https://blumify.io/
---
