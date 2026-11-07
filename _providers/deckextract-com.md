---
access_model:
  confidence: low
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'DeckExtract API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DeckExtract API
  slug: deckextract-com-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/deckextract-com/plans/deckextract-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deckextract-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deckextract-com/rules/deckextract-com-rules.yml
  title: ''
  type: Spectral
  url: rules/deckextract-com-rules.yml
- group: design
  href: https://artifacts.apis.io/deckextract-com/json-ld/deckextract-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deckextract-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/deckextract-com/vocabulary/deckextract-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deckextract-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deckextract-com/data-model/deckextract-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deckextract-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/deckextract-com/conformance/deckextract-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deckextract-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deckextract-com/llms/deckextract-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deckextract-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/deckextract-com/well-known/deckextract-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deckextract-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/deckextract-com/hosts/deckextract-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deckextract-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deckextract.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deckextract.com/privacy
- group: auth
  href: https://artifacts.apis.io/deckextract-com/security/deckextract-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deckextract-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deckextract.com/
- group: docs
  title: ''
  type: Documentation
  url: https://deckextract.com/docsend-to-pdf
- group: docs
  title: ''
  type: APIReference
  url: https://deckextract.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://deckextract.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://deckextract.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://deckextract.com/docsend-to-pdf
coverage:
  checked: '2026-11-05'
  detail: API documentation at https://deckextract.com/api returns HTML with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://deckextract.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DeckExtract provides a service to download any pitch deck as a PDF or PowerPoint. It supports view‑only deck links from platforms like DocSend, Papermark, and various data rooms. Users can access the conversion via a web interface, a Chrome extension, or programmatically through an API and MCP. The service offers five free conversions per month without requiring signup, targeting startups, investors, and sales teams needing quick access to presentation content.
image: https://deckextract.com/thumbnail.png
json_schemas:
- name: GetApiV2ExtractResponse
  property_count: 5
  slug: deckextract-com-get-api-v2-extract-response
- name: PatchServicesDataV600SobjectsOpportunityOpportunityidRequest
  property_count: 3
  slug: deckextract-com-patch-services-data-v600-sobjects-opportunity-opportunityid-request
- name: PatchV2ObjectsCompaniesRecordsRecordidRequest
  property_count: 3
  slug: deckextract-com-patch-v2-objects-companies-records-recordid-request
- name: PostCrmV3ObjectsNotesRequest
  property_count: 2
  slug: deckextract-com-post-crm-v3-objects-notes-request
- name: PostV1PagesRequest
  property_count: 2
  slug: deckextract-com-post-v1-pages-request
- name: PostV2NotesRequest
  property_count: 1
  slug: deckextract-com-post-v2-notes-request
jsonld:
- class_count: 11
  name: Deckextract Com Context
  property_count: 21
  slug: deckextract-com-context
layout: provider
modified: '2026-11-05'
name: DeckExtract
nav: Providers
network: true
overview: 'DeckExtract is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pitch Deck, Conversion, Startup Tools, and Investor Tools.


  The DeckExtract catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeckExtract''s developer surface includes documentation, API reference, pricing, engineering blog, getting-started guide, and 13 more developer resources.'
plans:
- name: Deckextract Com Plans Pricing
  plan_count: 3
  slug: deckextract-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: DeckExtract API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: deckextract-com-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deckextract Com Domain Security
  slug: deckextract-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: deckextract-com
tags:
- Pitch Deck
- Conversion
- Startup Tools
- Investor Tools
website: https://deckextract.com/
---
