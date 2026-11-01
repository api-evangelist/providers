---
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Ribbon
  name: Ribbon API
  slug: ribbon-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/ribbon/rules/ribbon-rules.yml
  title: ''
  type: Spectral
  url: rules/ribbon-rules.yml
- group: design
  href: https://artifacts.apis.io/ribbon/json-ld/ribbon-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ribbon-context.jsonld
- group: design
  href: https://artifacts.apis.io/ribbon/vocabulary/ribbon-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ribbon-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ribbon/data-model/ribbon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ribbon-data-model.yml
- group: design
  href: https://artifacts.apis.io/ribbon/errors/ribbon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ribbon-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ribbon/conformance/ribbon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ribbon-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ribbon/llms/ribbon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ribbon-llms.txt
- group: other
  href: https://artifacts.apis.io/ribbon/a2a/ribbon-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ribbon-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ribbon/well-known/ribbon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ribbon-well-known.yml
- group: other
  href: https://artifacts.apis.io/ribbon/hosts/ribbon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ribbon-hosts.yml
- group: other
  href: https://artifacts.apis.io/ribbon/vendors/ribbon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ribbon-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ribbon.ai/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://app.ribbon.ai/recruit/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ribbon.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ribbon.ai/changelog
- group: auth
  href: https://artifacts.apis.io/ribbon/security/ribbon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ribbon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ribbon.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ribbon.ai/ribbon-api
- group: docs
  title: ''
  type: APIReference
  url: https://www.ribbon.ai/ribbon-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ribbon.ai/request-a-demo
- group: company
  title: ''
  type: Blog
  url: https://www.ribbon.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://app.ribbon.ai/recruit/sign-in
created: '2026-10-29'
description: Ribbon AI offers an agentic recruiting platform that automates interview scheduling, email communication, and SMS outreach. Through its APIs, developers can integrate recruiting workflows, manage candidate pipelines, and customize recruitment messaging. The service targets staffing agencies, enterprises, and hiring teams, providing tools for interview coordination, candidate engagement, and analytics. Backed by Radical Ventures, Ribbon AI aims to streamline hiring processes and improve recruitment efficiency.
image: https://cdn.prod.website-files.com/63b6c43d8a44f00d7d134ee6/68e67894b358281a34d02fb6_OpenGraph%20(Updated).png
jsonld:
- class_count: 24
  name: Ribbon Context
  property_count: 69
  slug: ribbon-context
layout: provider
modified: '2026-10-29'
name: Ribbon
nav: Providers
network: true
overview: 'Ribbon publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, API, Automation, and Banking.


  The Ribbon catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ribbon''s developer surface includes signup flow, changelog, API reference, getting-started guide, engineering blog, support, and 16 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: Ribbon API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 1
  slug: ribbon-rules
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 19.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ribbon Domain Security
  slug: ribbon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ribbon
tags:
- Fintech
- Payments
- API
- Automation
- Banking
website: https://www.ribbon.ai
---
