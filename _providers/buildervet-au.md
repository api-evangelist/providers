---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BuilderVet API providing builder verification and coverage endpoints.
  name: BuilderVet API
  slug: buildervet-api
- baseURL: https://api.buildervet.au
  baseurl_source: declared
  description: Dated NSW and QLD licence, company and regulatory evidence. Consult per-source coverage before interpreting an absent finding. No safety rating, phoenix detection, solvency prediction or complete DA c
  name: BuilderVet API API
  slug: buildervet-api-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/buildervet-au/rules/buildervet-au-rules.yml
  title: ''
  type: Spectral
  url: rules/buildervet-au-rules.yml
- group: design
  href: https://artifacts.apis.io/buildervet-au/json-ld/buildervet-au-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buildervet-au-context.jsonld
- group: design
  href: https://artifacts.apis.io/buildervet-au/vocabulary/buildervet-au-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buildervet-au-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buildervet-au/conformance/buildervet-au-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildervet-au-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/buildervet-au/plans/buildervet-au-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildervet-au-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buildervet-au/data-model/buildervet-au-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buildervet-au-data-model.yml
- group: design
  href: https://artifacts.apis.io/buildervet-au/errors/buildervet-au-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buildervet-au-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/buildervet-au/llms/buildervet-au-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildervet-au-llms.txt
- group: agent
  href: https://artifacts.apis.io/buildervet-au/well-known/buildervet-au-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildervet-au-well-known.yml
- group: other
  href: https://artifacts.apis.io/buildervet-au/hosts/buildervet-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildervet-au-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildervet-au/vendors/buildervet-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildervet-au-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buildervet.au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildervet.au/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.buildervet.au`,location.pathname
- group: auth
  href: https://artifacts.apis.io/buildervet-au/security/buildervet-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildervet-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildervet.au/
- group: docs
  title: ''
  type: Documentation
  url: https://buildervet.au/guides
- group: docs
  title: ''
  type: APIReference
  url: https://api.buildervet.au
- group: commercial
  title: ''
  type: Pricing
  url: https://buildervet.au/pricing
- group: operate
  title: ''
  type: Support
  url: mailto:hello@buildervet.au
created: '2026-11-03'
description: BuilderVet provides free builder checks for NSW and QLD homeowners, offering licence, company and regulator records with sources and dates. It also offers a paid Build Watch service for ongoing monitoring. The service aggregates public data to help homeowners assess builder reliability before committing to a build.
image: https://buildervet.au/social/buildervet-report-v2.jpg
json_schemas:
- name: AccountView
  property_count: 6
  slug: buildervet-au-account-view
- name: BuilderProfile
  property_count: 9
  slug: buildervet-au-builder-profile
- name: ReferralStatus
  property_count: 3
  slug: buildervet-au-referral-status
- name: SearchResults
  property_count: 2
  slug: buildervet-au-search-results
- name: Timeline
  property_count: 2
  slug: buildervet-au-timeline
jsonld:
- class_count: 6
  name: Buildervet Au Context
  property_count: 26
  slug: buildervet-au-context
layout: provider
modified: '2026-11-03'
name: BuilderVet
nav: Providers
network: true
overview: 'BuilderVet publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company.


  The BuilderVet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BuilderVet''s developer surface includes documentation, API reference, pricing, support, and 16 more developer resources.'
plans:
- name: Buildervet Au Plans Pricing
  plan_count: 3
  slug: buildervet-au-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: BuilderVet API Rules
  rule_count: 41
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 2
  slug: buildervet-au-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 52.2
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buildervet Au Domain Security
  slug: buildervet-au-domain-security
  summary_line: TLSv1.3 · DMARC
slug: buildervet-au
tags:
- Company
website: https://buildervet.au/
---
