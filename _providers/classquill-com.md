---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Classquill Com Agentic Access
  operation_count: 99
  slug: classquill-com-agentic-access
  summary_line: 99 operations · 35 acting
api_count: 1
apis:
- description: The Billing API from ClassQuill — 6 operation(s) for billing.
  name: ClassQuill Billing API
  slug: classquill-com-billing-api
- description: The Blog API from ClassQuill — 3 operation(s) for blog.
  name: ClassQuill Blog API
  slug: classquill-com-blog-api
- description: The Bookings API from ClassQuill — 4 operation(s) for bookings.
  name: ClassQuill Bookings API
  slug: classquill-com-bookings-api
- description: The Coursework API from ClassQuill — 7 operation(s) for coursework.
  name: ClassQuill Coursework API
  slug: classquill-com-coursework-api
- description: The Curriculum API from ClassQuill — 7 operation(s) for curriculum.
  name: ClassQuill Curriculum API
  slug: classquill-com-curriculum-api
- description: The General API from ClassQuill — 21 operation(s) for general.
  name: ClassQuill General API
  slug: classquill-com-general-api
- description: The Operations API from ClassQuill — 5 operation(s) for operations.
  name: ClassQuill Operations API
  slug: classquill-com-operations-api
- description: The Pricing API from ClassQuill — 3 operation(s) for pricing.
  name: ClassQuill Pricing API
  slug: classquill-com-pricing-api
- description: The Reports API from ClassQuill — 1 operation(s) for reports.
  name: ClassQuill Reports API
  slug: classquill-com-reports-api
- description: The Sessions API from ClassQuill — 6 operation(s) for sessions.
  name: ClassQuill Sessions API
  slug: classquill-com-sessions-api
- description: The Students & Parents API from ClassQuill — 11 operation(s) for students & parents.
  name: ClassQuill Students & Parents API
  slug: classquill-com-students-parents-api
- description: The Tutors API from ClassQuill — 7 operation(s) for tutors.
  name: ClassQuill Tutors API
  slug: classquill-com-tutors-api
artifact_total: 30
asyncapis:
- description: ''
  name: Classquill Com Webhooks
  slug: classquill-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/classquill-com/agentic-access/classquill-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/classquill-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/classquill-com/rate-limits/classquill-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/classquill-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/classquill-com/plans/classquill-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/classquill-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/classquill-com/rules/classquill-com-rules.yml
  title: ''
  type: Spectral
  url: rules/classquill-com-rules.yml
- group: design
  href: https://artifacts.apis.io/classquill-com/json-ld/classquill-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/classquill-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/classquill-com/vocabulary/classquill-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/classquill-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/classquill-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/classquill-com/asyncapi/classquill-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/classquill-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/classquill-com/data-model/classquill-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/classquill-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/classquill-com/conventions/classquill-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/classquill-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/classquill-com/conventions/classquill-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/classquill-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/classquill-com/authentication/classquill-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/classquill-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/classquill-com/errors/classquill-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/classquill-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/classquill-com/conformance/classquill-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/classquill-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/classquill-com/llms/classquill-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/classquill-com-llms.txt
- group: other
  href: https://artifacts.apis.io/classquill-com/a2a/classquill-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/classquill-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/classquill-com/well-known/classquill-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/classquill-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/classquill-com/hosts/classquill-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/classquill-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/classquill-com/vendors/classquill-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/classquill-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://classquill.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://classquill.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://classquill.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://classquill.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://classquill.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://classquill.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.classquill.com/guides/org-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.classquill.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.classquill.com/introduction
- group: auth
  href: https://artifacts.apis.io/classquill-com/security/classquill-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/classquill-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://classquill.com/
created: '2026-11-03'
description: ClassQuill provides scheduling, invoicing, payroll, and a learning platform for tutoring businesses. It offers an operating system that automates lesson creation, auto‑marks practice, and gives tutors and parents visibility into results. Pricing starts at US$20 per month for the first tutor, with additional tutors at US$6 each.
image: https://classquill.com/og-image.png
json_schemas:
- name: BlogPostCreate
  property_count: 15
  slug: classquill-com-blog-post-create
- name: BlogPost
  property_count: 21
  slug: classquill-com-blog-post
- name: BlogPostUpdate
  property_count: 13
  slug: classquill-com-blog-post-update
- name: InviteCreate
  property_count: 8
  slug: classquill-com-invite-create
- name: Result
  property_count: 10
  slug: classquill-com-result
- name: Tutor
  property_count: 27
  slug: classquill-com-tutor
jsonld:
- class_count: 120
  name: Classquill Com Context
  property_count: 267
  slug: classquill-com-context
layout: provider
modified: '2026-11-03'
name: ClassQuill
nav: Providers
network: true
overview: 'ClassQuill publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Blog API, Bookings API, and 9 more. Tagged areas include Tutoring, Scheduling, Invoicing, Payroll, and Learning Platform.


  The ClassQuill catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ClassQuill''s developer surface includes authentication, support, pricing, changelog, engineering blog, getting-started guide, documentation, and 23 more developer resources.'
plans:
- name: Classquill Com Plans Pricing
  plan_count: 2
  slug: classquill-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Classquill Com Rate Limits
  slug: classquill-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: ClassQuill API Rules
  rule_count: 60
  severity_counts:
    error: 49
    hint: 0
    info: 3
    warn: 8
  slug: classquill-com-rules
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 73.8
    catalog_earned_first_party: 16.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 66.6
    developer_ergonomics: 31.5
    discoverability: 57.1
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Classquill Com Authentication
  slug: classquill-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Classquill Com Domain Security
  slug: classquill-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: classquill-com-billing-retrieve-payment
  slug: classquill-com-billing-retrieve-payment
- name: classquill-com-create-and-get-lead
  slug: classquill-com-create-and-get-lead
- name: classquill-com-create-and-list-sessions
  slug: classquill-com-create-and-list-sessions
- name: classquill-com-create-student-and-link-parent
  slug: classquill-com-create-student-and-link-parent
slug: classquill-com
tags:
- Tutoring
- Scheduling
- Invoicing
- Payroll
- Learning Platform
- Education
website: https://classquill.com/
---
