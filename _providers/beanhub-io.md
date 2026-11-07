---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BeanHub API provides programmatic access to repository entries.
  name: BeanHub API
  slug: beanhub-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/beanhub-io/rules/beanhub-io-rules.yml
  title: ''
  type: Spectral
  url: rules/beanhub-io-rules.yml
- group: design
  href: https://artifacts.apis.io/beanhub-io/json-ld/beanhub-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beanhub-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/beanhub-io/vocabulary/beanhub-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beanhub-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/beanhub-io/conformance/beanhub-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beanhub-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beanhub-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/beanhub-io/data-model/beanhub-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beanhub-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/beanhub-io/authentication/beanhub-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beanhub-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/beanhub-io/errors/beanhub-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beanhub-io-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/beanhub-io/llms/beanhub-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beanhub-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/beanhub-io/well-known/beanhub-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beanhub-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/beanhub-io/hosts/beanhub-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beanhub-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/beanhub-io/vendors/beanhub-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beanhub-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beanhub.io/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://beanhub.io/tags/security/
- group: start
  title: ''
  type: Sandbox
  url: https://beanhub.io/tags/sandbox/
- group: company
  title: ''
  type: Blog
  url: https://beanhub.io/Blog
- group: start
  title: ''
  type: Login
  url: https://app.beanhub.io/sign-in
- group: start
  title: ''
  type: SignUp
  url: https://app.beanhub.io/sign-up
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beanhub.io/getting-started/quickstart/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beanhub.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.beanhub.io/redoc
- group: auth
  href: https://artifacts.apis.io/beanhub-io/security/beanhub-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beanhub-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beanhub.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.beanhub.io/openapi.json
  - status: 401
    url: https://api.beanhub.io/mcp
  - status: 200
    url: https://beanhub.io/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BeanHub provides a modern, smart accounting book service built on the popular open‑source version control system Git and the double‑entry accounting software Beancount. It offers a web‑based interface for managing financial records, supports automated transaction imports, and integrates with developer tools for versioned bookkeeping. Designed for freelancers, small businesses, and developers, BeanHub combines transparency, auditability, and ease of use in a SaaS platform.
image: https://beanhub.io/images/open-graph.png
jsonld:
- class_count: 105
  name: Beanhub Io Context
  property_count: 103
  slug: beanhub-io-context
layout: provider
modified: '2026-11-02'
name: BeanHub
nav: Providers
network: true
overview: 'BeanHub publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Software-as-a-Service, Open Source, Finance, and Bookkeeping.


  The BeanHub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BeanHub''s developer surface includes authentication, sandbox, engineering blog, signup flow, getting-started guide, documentation, API reference, and 16 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: BeanHub API Rules
  rule_count: 41
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 4
  slug: beanhub-io-rules
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
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
- kind: authentication
  name: Beanhub Io Authentication
  slug: beanhub-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Beanhub Io Domain Security
  slug: beanhub-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: beanhub-io-forms-submit
  slug: beanhub-io-forms-submit
- name: beanhub-io-manage-entries
  slug: beanhub-io-manage-entries
- name: beanhub-io-oauth-token-flow
  slug: beanhub-io-oauth-token-flow
slug: beanhub-io
tags:
- Accounting
- Software-as-a-Service
- Open Source
- Finance
- Bookkeeping
- Developer Tools
- Company
website: https://beanhub.io/
---
