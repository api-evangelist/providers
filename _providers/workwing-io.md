---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 66
  human_in_the_loop: 2
  name: Workwing Io Agentic Access
  operation_count: 125
  slug: workwing-io-agentic-access
  summary_line: 125 operations · 66 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Assigning resources to jobs
  name: workwing-io Assignments API
  slug: workwing-io-assignments-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Brand configuration (read-only)
  name: workwing-io Brands API
  slug: workwing-io-brands-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: API key introspection, capabilities, and organisation info
  name: workwing-io Context API
  slug: workwing-io-context-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: 'Custom field definitions: the schema (keys, labels, types) for job, customer and resource custom fields. Read them for discovery, create and update them to define the fields an integration fills in. S'
  name: workwing-io Custom Fields API
  slug: workwing-io-custom-fields-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Customers and their notes and attachments
  name: workwing-io Customers API
  slug: workwing-io-customers-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Service health check
  name: workwing-io Health API
  slug: workwing-io-health-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Running configured integrations and receiving their callbacks
  name: workwing-io Integrations API
  slug: workwing-io-integrations-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Recurring job schedules (create, lifecycle)
  name: workwing-io Job Schedules API
  slug: workwing-io-job-schedules-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Job status change audit trail (read-only)
  name: workwing-io Job Status History API
  slug: workwing-io-job-status-history-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Job types (read-only). The collection is `job_templates`, and a job's `template_id` points at one.
  name: workwing-io Job types API
  slug: workwing-io-job-types-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Jobs and their notes, parts, attachments, status, and custom fields
  name: workwing-io Jobs API
  slug: workwing-io-jobs-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: GPS traces and job segments (read-only)
  name: workwing-io Location History API
  slug: workwing-io-location-history-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Customer locations and their notes
  name: workwing-io Locations API
  slug: workwing-io-locations-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: OAuth connection management
  name: workwing-io OAuth API
  slug: workwing-io-oauth-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Parts catalogue and brand-specific pricing (read-only)
  name: workwing-io Parts Catalogue API
  slug: workwing-io-parts-catalogue-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: 'Projects: jobs that own a pool of jobs, with their window, crew, and progress. A project is a job, so it is updated with `PATCH /v1/jobs/{jobId}` and crew is added with `POST /v1/jobs/{jobId}/assignme'
  name: workwing-io Projects API
  slug: workwing-io-projects-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Resource groups (read-only)
  name: workwing-io Resource Groups API
  slug: workwing-io-resource-groups-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Resources (your engineers and other field staff) and their notes, skills, attachments, and working hours
  name: workwing-io Resources API
  slug: workwing-io-resources-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Resource scheduling, availability, and conflicts
  name: workwing-io Schedule API
  slug: workwing-io-schedule-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Skill definitions and categories (read-only)
  name: workwing-io Skills API
  slug: workwing-io-skills-api
- baseURL: https://api.workwing.io
  baseurl_source: declared
  description: Bulk operations and multi-step workflows
  name: workwing-io Workflows API
  slug: workwing-io-workflows-api
artifact_total: 28
asyncapis:
- description: ''
  name: Workwing Io Webhooks
  slug: workwing-io-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/workwing-io/agentic-access/workwing-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/workwing-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/workwing-io/plans/workwing-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/workwing-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/workwing-io/rules/workwing-io-rules.yml
  title: ''
  type: Spectral
  url: rules/workwing-io-rules.yml
- group: design
  href: https://artifacts.apis.io/workwing-io/vocabulary/workwing-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/workwing-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/workwing-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/workwing-io/asyncapi/workwing-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/workwing-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/workwing-io/conventions/workwing-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/workwing-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/workwing-io/conventions/workwing-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/workwing-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/workwing-io/authentication/workwing-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workwing-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/workwing-io/errors/workwing-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/workwing-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/workwing-io/conformance/workwing-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/workwing-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/workwing-io/llms/workwing-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workwing-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/workwing-io/well-known/workwing-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/workwing-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/workwing-io/hosts/workwing-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/workwing-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/workwing-io/vendors/workwing-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/workwing-io-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://auth.workwing.io/auth/signup?utm_source=marketing&utm_medium=website&utm_content=home-hero
- group: auth
  href: https://artifacts.apis.io/workwing-io/security/workwing-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workwing-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.workwing.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workwing.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.workwing.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://docs.workwing.io/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.workwing.io/getting-started/introduction/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.workwing.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workwing.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workwing.io/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.workwing.io/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.workwing.io/openapi.json
  - status: 401
    url: https://api.workwing.io/mcp
  - status: 200
    url: https://workwing.io/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: WorkWing provides field service management software with an open API, enabling companies to schedule jobs, track work, and integrate with CRM systems. The platform offers mobile apps for technicians, a unified dispatch board, and customizable reporting without per-user fees. It supports free trials and paid plans starting at £79 per month, targeting teams that need coordinated field operations and seamless data flow.
image: https://www.workwing.io/og-image.png
layout: provider
modified: '2026-10-31'
name: workwing-io
nav: Providers
network: true
overview: 'workwing-io publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assignments API, Brands API, Context API, and 18 more. Tagged areas include Field Service Management, Software-as-a-Service, Mobile, and OpenAPI.


  The workwing-io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  workwing-io''s developer surface includes authentication, signup flow, documentation, API reference, getting-started guide, pricing, support, and 19 more developer resources.'
plans:
- name: Workwing Io Plans Pricing
  plan_count: 4
  slug: workwing-io-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: workwing-io API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 2
  slug: workwing-io-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 52.0
    developer_ergonomics: 35.1
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Workwing Io Authentication
  slug: workwing-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Workwing Io Domain Security
  slug: workwing-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: getting-started
  slug: workwing-io-getting-started
slug: workwing-io
tags:
- Field Service Management
- Software-as-a-Service
- Mobile
- OpenAPI
website: https://www.workwing.io/
---
