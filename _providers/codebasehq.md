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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 11
asyncapis:
- description: ''
  name: Codebasehq Webhooks
  slug: codebasehq-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/codebasehq/plans/codebasehq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/codebasehq-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/codebasehq/hosts/codebasehq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codebasehq-hosts.yml
- group: build
  href: https://artifacts.apis.io/codebasehq/packages/codebasehq-packages.yml
  title: ''
  type: SDKs
  url: packages/codebasehq-packages.yml
- group: build
  href: https://artifacts.apis.io/codebasehq/packages/codebasehq-packages.yml
  title: ''
  type: Packages
  url: packages/codebasehq-packages.yml
- group: auth
  href: https://artifacts.apis.io/codebasehq/security/codebasehq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codebasehq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.codebasehq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.codebasehq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.codebasehq.com/
- group: operate
  title: ''
  type: Support
  url: https://support.codebasehq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.codebasehq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.codebasehq.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.codebasehq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.codebasehq.com/privacy
created: '2026-10-26'
description: Codebase is the ultimate code hosting platform for professional development teams. It offers Git, Mercurial, and Subversion repositories along with robust project management features such as ticket tracking, time tracking, file sharing, and collaborative documentation. The service integrates source control, issue management, and team collaboration tools to streamline software delivery, improve productivity, and support seamless development workflows.
json_schemas:
- name: GetActivityResponse
  property_count: 6
  slug: codebasehq-get-activity-response
- name: GetRolesResponse
  property_count: 4
  slug: codebasehq-get-roles-response
- name: GetUsersResponse
  property_count: 12
  slug: codebasehq-get-users-response
- name: PostUploadsResponse
  property_count: 6
  slug: codebasehq-post-uploads-response
- name: PostUsersRequest
  property_count: 4
  slug: codebasehq-post-users-request
- name: PutProjectProjectIdRequest
  property_count: 3
  slug: codebasehq-put-project-project-id-request
jsonld:
- class_count: 12
  name: Codebasehq Context
  property_count: 32
  slug: codebasehq-context
layout: provider
modified: '2026-10-26'
name: Codebase
nav: Providers
network: true
overview: 'Codebase is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Version Control, Mercurial, Subversion, and Project Management.


  The Codebase catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Codebase''s developer surface includes documentation, support, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Codebasehq Plans Pricing
  plan_count: 5
  slug: codebasehq-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Codebase API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: codebasehq-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.5
    catalog_earned_first_party: 12.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 38.0
    developer_ergonomics: 20.2
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 35.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/codebasehq/codebasehq-2026-11-03T124719.png
security:
- kind: domain-security
  name: Codebasehq Domain Security
  slug: codebasehq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codebasehq
tags:
- Company
- Version Control
- Mercurial
- Subversion
- Project Management
- Ticketing
website: https://www.codebasehq.com/
---
