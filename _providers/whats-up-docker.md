---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Welcome to the WUD REST API documentation.
  name: WUD REST API
  slug: wud-rest-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/whats-up-docker/rules/whats-up-docker-rules.yml
  title: ''
  type: Spectral
  url: rules/whats-up-docker-rules.yml
- group: design
  href: https://artifacts.apis.io/whats-up-docker/json-ld/whats-up-docker-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/whats-up-docker-context.jsonld
- group: design
  href: https://artifacts.apis.io/whats-up-docker/vocabulary/whats-up-docker-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/whats-up-docker-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/whats-up-docker/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/whats-up-docker/data-model/whats-up-docker-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whats-up-docker-data-model.yml
- group: design
  href: https://artifacts.apis.io/whats-up-docker/errors/whats-up-docker-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whats-up-docker-problem-types.yml
- group: design
  href: https://artifacts.apis.io/whats-up-docker/conformance/whats-up-docker-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whats-up-docker-conformance.yml
- group: other
  href: https://artifacts.apis.io/whats-up-docker/hosts/whats-up-docker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whats-up-docker-hosts.yml
- group: other
  href: https://artifacts.apis.io/whats-up-docker/vendors/whats-up-docker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whats-up-docker-vendors.yml
- group: auth
  href: https://artifacts.apis.io/whats-up-docker/security/whats-up-docker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whats-up-docker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getwud.app/
- group: docs
  title: ''
  type: Documentation
  url: https://getwud.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://getwud.app/docs/api/reference/wud-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://getwud.app/docs/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getwud
coverage:
  checked: '2026-10-28'
  detail: Provider's documentation only offers a generic self‑hosted OpenAPI spec without a base URL, none of which belongs to the hosted service.
  evidence:
  - status: 200
    url: https://getwud.app/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: WUD – What's up Docker? is an open‑source tool that continuously monitors containers across Docker, Kubernetes and other orchestrators, detects new image versions, and can notify or automatically trigger updates. It offers a lightweight, configurable watcher, supports multiple registries, provides a REST API, and can be run as a Docker container. The project is maintained by the WUD community and hosted on GitHub.
image: https://getwud.app/img/wud-logo-512.png
jsonld:
- class_count: 4
  name: Whats Up Docker Context
  property_count: 33
  slug: whats-up-docker-context
layout: provider
modified: '2026-10-28'
name: What's Up Docker
nav: Providers
network: true
overview: 'What''s Up Docker publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Container Management, Docker, Kubernetes, and Open Source.


  The What''s Up Docker catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  What''s Up Docker''s developer surface includes documentation, API reference, getting-started guide, and 12 more developer resources.'
plans:
- name: Whats Up Docker Plans Pricing
  plan_count: 0
  slug: whats-up-docker-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Whats Up Docker Rate Limits
  slug: whats-up-docker-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: What's Up Docker API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: whats-up-docker-rules
scopes:
- name: Whats Up Docker Scopes
  scope_count: 0
  slug: whats-up-docker-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 20.7
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/whats-up-docker/whats-up-docker-2026-11-03T150140.png
security:
- kind: authentication
  name: Whats Up Docker Authentication
  slug: whats-up-docker-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Whats Up Docker Domain Security
  slug: whats-up-docker-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: authentication
  slug: whats-up-docker-authentication
- name: container-management
  slug: whats-up-docker-container-management
slug: whats-up-docker
tags:
- Company
- Container Management
- Docker
- Kubernetes
- Open Source
- Automation
website: https://getwud.app/
---
