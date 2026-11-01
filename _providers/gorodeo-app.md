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
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/gorodeo-app/rules/gorodeo-app-rules.yml
  title: ''
  type: Spectral
  url: rules/gorodeo-app-rules.yml
- group: design
  href: https://artifacts.apis.io/gorodeo-app/json-ld/gorodeo-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gorodeo-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/gorodeo-app/vocabulary/gorodeo-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gorodeo-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gorodeo-app/data-model/gorodeo-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gorodeo-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/gorodeo-app/errors/gorodeo-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gorodeo-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gorodeo-app/conformance/gorodeo-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gorodeo-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gorodeo-app/llms/gorodeo-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gorodeo-app-llms.txt
- group: other
  href: https://artifacts.apis.io/gorodeo-app/a2a/gorodeo-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gorodeo-app-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gorodeo-app/well-known/gorodeo-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gorodeo-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/gorodeo-app/hosts/gorodeo-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gorodeo-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/gorodeo-app/vendors/gorodeo-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gorodeo-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.gorodeo.app/introduction/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.gorodeo.app/introduction/legal/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gorodeo.app/introduction/how-rodeo-works
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gorodeo.app/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gorodeo
- group: auth
  href: https://artifacts.apis.io/gorodeo-app/security/gorodeo-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gorodeo-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://gorodeo.app
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.gorodeo.app/mcp
  - status: 401
    url: https://api.gorodeo.app/mcp
  - status: 200
    url: http://gorodeo.app
  reason: partner-login
  state: gated
created: '2026-10-23'
description: Rodeo was a career‑focused startup that offered job‑search tools and resources to help professionals advance. The platform has now closed, with all user data deleted as of 16 October 2026. Rodeo’s mission was to simplify career progression through a suite of applications and community support.
jsonld:
- class_count: 2
  name: Gorodeo App Context
  property_count: 4
  slug: gorodeo-app-context
layout: provider
modified: '2026-10-23'
name: Rodeo
nav: Providers
network: true
overview: 'Rodeo publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Career, JobSearch, Startup, and Closed.


  The Rodeo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rodeo''s developer surface includes getting-started guide, documentation, and 16 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Rodeo API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: gorodeo-app-rules
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 6.7
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gorodeo App Domain Security
  slug: gorodeo-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gorodeo-app
tags:
- Company
- Career
- JobSearch
- Startup
- Closed
website: http://gorodeo.app
---
