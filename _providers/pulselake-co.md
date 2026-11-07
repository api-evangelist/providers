---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: PulseLake provides an AI‑native operating system for market research and insights.
  name: PulseLake API
  slug: pulselake-api
- description: 'pulselake-co API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: pulselake-co API
  slug: pulselake-co-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/pulselake-co/well-known/pulselake-co-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pulselake-co-www-security.txt
- group: design
  href: https://artifacts.apis.io/pulselake-co/rules/pulselake-co-rules.yml
  title: ''
  type: Spectral
  url: rules/pulselake-co-rules.yml
- group: design
  href: https://artifacts.apis.io/pulselake-co/json-ld/pulselake-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pulselake-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/pulselake-co/vocabulary/pulselake-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pulselake-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pulselake-co/data-model/pulselake-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pulselake-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/pulselake-co/conformance/pulselake-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pulselake-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pulselake-co/llms/pulselake-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pulselake-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/pulselake-co/well-known/pulselake-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pulselake-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/pulselake-co/hosts/pulselake-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pulselake-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/pulselake-co/vendors/pulselake-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pulselake-co-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pulselake.co/get-started
- group: auth
  href: https://artifacts.apis.io/pulselake-co/security/pulselake-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pulselake-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pulselake.co/
- group: company
  title: ''
  type: Blog
  url: https://www.pulselake.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pulselake.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pulselake.co/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.pulselake.co/contact
coverage:
  checked: '2026-10-29'
  detail: Public documentation exists but no machine-readable OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 404
    url: https://api.pulselake.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: PulseLake provides an AI‑native operating system for market research and insights. The platform enables users to design studies, conduct AI‑led interviews, deploy research agents, capture institutional knowledge, and deliver results. Built to streamline the entire research workflow, PulseLake leverages large language models to automate questionnaire creation, data collection, analysis, and reporting, helping businesses accelerate insight generation while reducing manual effort. The service is delivered as a cloud‑based SaaS solution with integrations for data pipelines and collaboration tools.
image: https://www.pulselake.co/assets/logo.png
json_schemas:
- name: PostApiV3ResponseexportsRequest
  property_count: 2
  slug: pulselake-co-post-api-v3-responseexports-request
jsonld:
- class_count: 1
  name: Pulselake Co Context
  property_count: 2
  slug: pulselake-co-context
layout: provider
modified: '2026-10-29'
name: pulselake-co
nav: Providers
network: true
overview: 'pulselake-co is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Market Research, Insights, Analytics, and Platform.


  The pulselake-co catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pulselake-co''s developer surface includes getting-started guide, engineering blog, support, and 14 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: pulselake-co API Rules
  rule_count: 26
  severity_counts:
    error: 24
    hint: 0
    info: 1
    warn: 1
  slug: pulselake-co-rules
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 16.4
    developer_ergonomics: 9.5
    discoverability: 64.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.0
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pulselake-co/pulselake-co-2026-11-03T141711.png
security:
- kind: domain-security
  name: Pulselake Co Domain Security
  slug: pulselake-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pulselake-co
tags:
- Artificial Intelligence
- Market Research
- Insights
- Analytics
- Platform
website: https://pulselake.co/
---
