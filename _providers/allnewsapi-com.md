---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Use one news API to get live breaking news, headlines and historical news data from over 250,000 sources in 196 countries, with up to 10 years of archive.
  name: AllNewsAPI API
  slug: allnewsapi-api
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/allnewsapi-com/well-known/allnewsapi-com-allnewsapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/allnewsapi-com-allnewsapi-security.txt
- group: agent
  href: https://artifacts.apis.io/allnewsapi-com/well-known/allnewsapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allnewsapi-com-well-known.yml
- group: commercial
  href: https://artifacts.apis.io/allnewsapi-com/plans/allnewsapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allnewsapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/allnewsapi-com/rules/allnewsapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/allnewsapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/allnewsapi-com/json-ld/allnewsapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allnewsapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/allnewsapi-com/vocabulary/allnewsapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allnewsapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/allnewsapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/allnewsapi-com/data-model/allnewsapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allnewsapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/allnewsapi-com/conventions/allnewsapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/allnewsapi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/allnewsapi-com/authentication/allnewsapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allnewsapi-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://allnewsapi.statuspage.io/
- group: design
  href: https://artifacts.apis.io/allnewsapi-com/lifecycle/allnewsapi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/allnewsapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/allnewsapi-com/errors/allnewsapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/allnewsapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/allnewsapi-com/conformance/allnewsapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allnewsapi-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/allnewsapi-com/hosts/allnewsapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allnewsapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/allnewsapi-com/vendors/allnewsapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allnewsapi-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allnewsapi.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allnewsapi.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://allnewsapi.com/blog
- group: auth
  href: https://artifacts.apis.io/allnewsapi-com/security/allnewsapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allnewsapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allnewsapi.com/
coverage:
  checked: '2026-10-30'
  detail: Documentation is public but no OpenAPI/AsyncAPI/GraphQL spec is owned by AllNewsAPI.
  evidence:
  - status: 200
    url: https://api.allnewsapi.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: AllNewsAPI provides a unified news API that aggregates live breaking news, headlines, and historical news data from over 250,000 sources across 196 countries. Developers can query articles using keywords, filters, and advanced query syntax, accessing up to ten years of archived content. The service offers free plans, fast response times, and comprehensive documentation.
image: https://cdn.allnewsapi.com/images/og-images/index.webp
jsonld:
- class_count: 83
  name: Allnewsapi Com Context
  property_count: 181
  slug: allnewsapi-com-context
layout: provider
modified: '2026-10-30'
name: allnewsapi-com
nav: Providers
network: true
overview: 'allnewsapi-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include News, Data, Media, Aggregation, and Company.


  The allnewsapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  allnewsapi-com''s developer surface includes authentication, engineering blog, and 19 more developer resources.'
plans:
- name: Allnewsapi Com Plans Pricing
  plan_count: 5
  slug: allnewsapi-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Allnewsapi Com Rate Limits
  slug: allnewsapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: allnewsapi-com API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: allnewsapi-com-rules
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 19.5
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 32.4
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/allnewsapi-com/allnewsapi-com-2026-11-03T120651.png
security:
- kind: authentication
  name: Allnewsapi Com Authentication
  slug: allnewsapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Allnewsapi Com Domain Security
  slug: allnewsapi-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: headlines
  slug: allnewsapi-com-headlines-skill
- name: search
  slug: allnewsapi-com-search-skill
slug: allnewsapi-com
tags:
- News
- Data
- Media
- Aggregation
- Company
website: https://allnewsapi.com/
---
