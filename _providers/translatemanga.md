---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Generate API keys and call the paid manga image translation API.
  name: TranslateManga API
  slug: translatemanga-api-2
- description: 'TranslateManga API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: TranslateManga API
  slug: translatemanga-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/translatemanga/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/translatemanga/plans/translatemanga-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/translatemanga-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/translatemanga/rules/translatemanga-rules.yml
  title: ''
  type: Spectral
  url: rules/translatemanga-rules.yml
- group: design
  href: https://artifacts.apis.io/translatemanga/vocabulary/translatemanga-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/translatemanga-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/translatemanga/conformance/translatemanga-conformance.yml
  title: ''
  type: Conformance
  url: conformance/translatemanga-conformance.yml
- group: other
  href: https://artifacts.apis.io/translatemanga/hosts/translatemanga-hosts.yml
  title: ''
  type: Hosts
  url: hosts/translatemanga-hosts.yml
- group: other
  href: https://artifacts.apis.io/translatemanga/vendors/translatemanga-vendors.yml
  title: ''
  type: Vendors
  url: vendors/translatemanga-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://translatemanga.net/changelog
- group: auth
  href: https://artifacts.apis.io/translatemanga/security/translatemanga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/translatemanga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://translatemanga.net
- group: docs
  title: ''
  type: Documentation
  url: https://translatemanga.net/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://translatemanga.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://translatemanga.net/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://translatemanga.net/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://translatemanga.net/#pricing
coverage:
  checked: '2026-11-02'
  detail: API requires a bearer token generated from an API key; no public OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://translatemanga.net/api
  reason: auth-required
  state: gated
created: '2026-11-02'
description: TranslateManga provides an online AI-powered manga translation service that converts manga images into multiple languages while preserving speech bubbles, artwork, and page layout. Users can upload JPG, PNG, or WEBP manga pages and receive translated images within seconds. The platform supports dozens of languages, offers free limited usage, and offers paid credit packs for higher volume. It aims to keep the original manga layout intact, making translated manga readable and downloadable.
image: https://translatemanga.net/logo.svg
layout: provider
modified: '2026-11-02'
name: TranslateManga
nav: Providers
network: true
overview: 'TranslateManga is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Manga, Translation, Artificial Intelligence, and Image Processing.


  The TranslateManga catalog on APIs.io includes 1 Spectral governance ruleset.


  TranslateManga''s developer surface includes changelog, documentation, support, pricing, and 11 more developer resources.'
plans:
- name: Translatemanga Plans Pricing
  plan_count: 3
  slug: translatemanga-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: TranslateManga API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: translatemanga-rules
scopes:
- name: Translatemanga Scopes
  scope_count: 0
  slug: translatemanga-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.8
    catalog_earned_first_party: 12.0
    catalog_gap: 70.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 13.6
    discoverability: 48.2
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Translatemanga Authentication
  slug: translatemanga-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Translatemanga Domain Security
  slug: translatemanga-domain-security
  summary_line: TLSv1.3 · DMARC
slug: translatemanga
tags:
- Manga
- Translation
- Artificial Intelligence
- Image Processing
website: https://translatemanga.net
---
