---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 81
  human_in_the_loop: 1
  name: Planka Agentic Access
  operation_count: 100
  slug: planka-agentic-access
  summary_line: 100 operations · 81 acting · 1 human-in-the-loop
api_count: 1
artifact_total: 13
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.planka.cloud/docs/installation/automated/getting-started
- group: commercial
  href: https://artifacts.apis.io/planka/plans/planka-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/planka-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/planka/changelog/planka-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/planka-changelog.yml
- group: design
  href: https://artifacts.apis.io/planka/conformance/planka-conformance.yml
  title: ''
  type: Conformance
  url: conformance/planka-conformance.yml
- group: other
  href: https://artifacts.apis.io/planka/hosts/planka-hosts.yml
  title: ''
  type: Hosts
  url: hosts/planka-hosts.yml
- group: other
  href: https://artifacts.apis.io/planka/vendors/planka-vendors.yml
  title: ''
  type: Vendors
  url: vendors/planka-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://planka.app/security
- group: start
  title: ''
  type: Login
  url: https://planka.app/center/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://planka.app/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.planka.cloud
- group: auth
  href: https://artifacts.apis.io/planka/security/planka-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/planka-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://planka.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.planka.cloud
- group: operate
  title: ''
  type: Support
  url: https://planka.app/contact
- group: company
  title: ''
  type: Blog
  url: https://planka.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plankanban/planka
- group: commercial
  title: ''
  type: Pricing
  url: https://planka.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://planka.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://planka.app/privacy
coverage:
  checked: '2026-10-27'
  detail: Documentation is available but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://docs.planka.cloud
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: PLANKA is a self‑hosted Kanban board solution designed for agile teams seeking full control over their project management data. It offers a community edition that can be run on‑premise, as well as Pro and Enterprise editions with advanced features such as role‑based access, single sign‑on, templates, reporting, and custom SLAs. PLANKA emphasizes privacy, flexibility, and scalability, supporting small teams to large organisations, and provides extensive documentation, a public API, and open‑source components.
image: https://planka.app/assets/marketing/og-image.png?v=6a87a0a1
json_schemas:
- name: Board
  property_count: 11
  slug: planka-board
- name: Card
  property_count: 18
  slug: planka-card
- name: Config
  property_count: 11
  slug: planka-config
- name: Notification
  property_count: 12
  slug: planka-notification
- name: Project
  property_count: 10
  slug: planka-project
- name: User
  property_count: 24
  slug: planka-user
jsonld:
- class_count: 24
  name: Planka Context
  property_count: 84
  slug: planka-context
layout: provider
modified: '2026-10-27'
name: PLANKA
nav: Providers
network: true
overview: 'PLANKA publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Kanban, Project Management, Self-Hosted, Agile, and Open Source.


  The PLANKA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PLANKA''s developer surface includes getting-started guide, changelog, documentation, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Planka Plans Pricing
  plan_count: 3
  slug: planka-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: PLANKA API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: planka-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 54.5
    catalog_earned_first_party: 12.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 53.9
    contract_governance: 31.8
    contract_quality: 23.1
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 15.8
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/planka/planka-2026-11-03T141256.png
security:
- kind: authentication
  name: Planka Authentication
  slug: planka-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Planka Domain Security
  slug: planka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: planka-create-board
  slug: planka-create-board
slug: planka
tags:
- Kanban
- Project Management
- Self-Hosted
- Agile
- Open Source
website: https://planka.app/
---
