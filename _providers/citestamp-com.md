---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for CiteStamp citation graph platform
  name: CiteStamp API
  slug: citestamp-api
- description: 'CiteStamp API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CiteStamp API
  slug: citestamp-com-api
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/citestamp-com/well-known/citestamp-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citestamp-com-security.txt
- group: auth
  href: https://artifacts.apis.io/citestamp-com/well-known/citestamp-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citestamp-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/citestamp-com/well-known/citestamp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citestamp-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/citestamp-com/security/citestamp-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/citestamp-com-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Portal
  url: https://citestamp.com/for-ai
- group: docs
  title: ''
  type: Documentation
  url: https://citestamp.com/how-it-works
- group: docs
  title: ''
  type: APIReference
  url: https://citestamp.com/for-ai
- group: start
  title: ''
  type: GettingStarted
  url: https://citestamp.com/ground
- group: auth
  title: ''
  type: Authentication
  url: https://citestamp.com/for-ai
- group: operate
  title: ''
  type: RateLimits
  url: https://citestamp.com/for-ai
- group: start
  title: ''
  type: Console
  url: https://citestamp.com/ask
- group: start
  title: ''
  type: Login
  url: https://citestamp.com/account
- group: auth
  title: ''
  type: Security
  url: https://citestamp.com/.well-known/security.txt
- group: operate
  title: ''
  type: Support
  url: https://citestamp.com/about
- group: design
  title: ''
  type: Vocabulary
  url: https://citestamp.com/.well-known/citestamp.json
- group: agent
  title: ''
  type: LLMsTxt
  url: https://citestamp.com/llms.txt
- group: other
  title: ''
  type: APICatalog
  url: https://citestamp.com/.well-known/api-catalog
- group: commercial
  href: https://artifacts.apis.io/citestamp-com/plans/citestamp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citestamp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/citestamp-com/rules/citestamp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/citestamp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/citestamp-com/json-ld/citestamp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/citestamp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/citestamp-com/vocabulary/citestamp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/citestamp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/citestamp-com/data-model/citestamp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/citestamp-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/citestamp-com/conformance/citestamp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citestamp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citestamp-com/llms/citestamp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citestamp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/citestamp-com/hosts/citestamp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citestamp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/citestamp-com/vendors/citestamp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citestamp-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citestamp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citestamp.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://citestamp.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citestamp
- group: auth
  href: https://artifacts.apis.io/citestamp-com/security/citestamp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citestamp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citestamp.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://citestamp.com/pricing
created: '2026-11-03'
description: CiteStamp provides a free, open platform to explore citation graphs of academic papers. Users can open any paper and visualize its citations as an interactive map, with human‑signed claims and machine‑inferred edges kept separate. The service includes indie preprints and Zenodo deposits, and offers an AI‑assistant friendly API that requires no key. It aims to make scholarly citation data accessible without registration, under a CC0 license.
image: https://citestamp.com/assets/og-card.png
json_schemas:
- name: PostApiV1AskEdgesAboutRequest
  property_count: 3
  slug: citestamp-com-post-api-v1-ask-edges-about-request
- name: PostApiV1AskEdgesAboutResponse
  property_count: 5
  slug: citestamp-com-post-api-v1-ask-edges-about-response
jsonld:
- class_count: 2
  name: Citestamp Com Context
  property_count: 7
  slug: citestamp-com-context
layout: provider
modified: '2026-11-03'
name: CiteStamp
nav: Providers
network: true
overview: 'CiteStamp is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Citation Graph, Scholarly Metadata, Bibliography Checking, AI Integration, and Publishers.


  The CiteStamp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CiteStamp''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, developer console, support, and 26 more developer resources.'
plans:
- name: Citestamp Com Plans Pricing
  plan_count: 2
  slug: citestamp-com-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: CiteStamp API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: citestamp-com-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 61.9
    discoverability: 75.9
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citestamp Com Domain Security
  slug: citestamp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Citestamp Com Vulnerability Disclosure
  slug: citestamp-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: citestamp-com
tags:
- Citation Graph
- Scholarly Metadata
- Bibliography Checking
- AI Integration
- Publishers
website: https://citestamp.com/
---
