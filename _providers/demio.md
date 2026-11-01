---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
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
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Demio Agentic Access
  operation_count: 7
  slug: demio-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- baseURL: https://my.demio.com/api/v1
  baseurl_source: declared
  description: Events, Event Sessions (Dates) and registration.
  name: Demio Events API
  slug: demio-events-api
- baseURL: https://my.demio.com/api/v1
  baseurl_source: declared
  description: Authorization checks.
  name: Demio Intro API
  slug: demio-intro-api
- baseURL: https://my.demio.com/api/v1
  baseurl_source: declared
  description: Participation and attendance reporting.
  name: Demio Reports API
  slug: demio-reports-api
artifact_total: 14
asyncapis:
- description: ''
  name: Demio Events
  slug: demio-events
collections:
- collection_type: open
  name: Public Demio API
  slug: open-demio
common:
- group: agent
  href: https://artifacts.apis.io/demio/agentic-access/demio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/demio-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/demio/security/demio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.demio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://publicdemioapi.docs.apiary.io
- group: docs
  title: ''
  type: Documentation
  url: https://publicdemioapi.docs.apiary.io
- group: docs
  title: ''
  type: APIReference
  url: https://publicdemioapi.docs.apiary.io
- group: start
  title: ''
  type: GettingStarted
  url: https://help.demio.com/en/articles/4544025-api-limitations
- group: operate
  title: ''
  type: Support
  url: https://help.demio.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.demio.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.demio.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meetdemio
- group: commercial
  title: ''
  type: Pricing
  url: https://www.demio.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.demio.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://my.demio.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.demio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.banzai.io/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demio.com
- group: docs
  href: https://artifacts.apis.io/demio/openapi/_original/demio-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/demio-openapi.yml
- group: other
  href: https://artifacts.apis.io/demio/openapi/demio-api-blueprint-original.apib
  title: ''
  type: APIBlueprint
  url: openapi/demio-api-blueprint-original.apib
- group: auth
  href: https://artifacts.apis.io/demio/authentication/demio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/demio-authentication.yml
- group: design
  href: https://artifacts.apis.io/demio/conventions/demio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/demio-conventions.yml
- group: design
  href: https://artifacts.apis.io/demio/errors/demio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/demio-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/demio/rate-limits/demio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/demio-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/demio/plans/demio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/demio-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/demio/lifecycle/demio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/demio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/demio/conformance/demio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/demio-conformance.yml
- group: design
  href: https://artifacts.apis.io/demio/data-model/demio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/demio-data-model.yml
- group: start
  href: https://artifacts.apis.io/demio/sandbox/demio-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/demio-sandbox.yml
- group: build
  href: https://artifacts.apis.io/demio/packages/demio-packages.yml
  title: ''
  type: Packages
  url: packages/demio-packages.yml
- group: build
  href: https://artifacts.apis.io/demio/packages/demio-packages.yml
  title: ''
  type: SDKs
  url: packages/demio-packages.yml
- group: design
  href: https://artifacts.apis.io/demio/components/demio-components.yml
  title: ''
  type: Components
  url: components/demio-components.yml
- group: build
  href: https://artifacts.apis.io/demio/mcp/demio-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/demio-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/demio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/demio/llms/demio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/demio-llms.txt
- group: agent
  href: https://artifacts.apis.io/demio/llms/demio-help-center-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/demio-help-center-llms.txt
- group: other
  href: https://artifacts.apis.io/demio/overlays/demio-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/demio-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/demio/examples/demio-examples.yml
  title: ''
  type: Examples
  url: examples/demio-examples.yml
created: '2026-08-12'
description: 'Demio is a browser-based webinar and virtual-event platform built for B2B marketing and sales teams, operated by Banzai International, Inc. (NASDAQ: BNZI). It runs live, automated/evergreen, on-demand and series webinars with no attendee download, and pairs them with customizable registration pages, embeddable registration forms, in-session engagement tools (polls, handouts, featured actions, chat), recordings, Showcase event listings and post-webinar analytics. Its public developer surface is the Public Demio API — a key/secret authorized REST API at https://my.demio.com/api/v1 covering Events, Event Sessions (Dates), attendee registration with unique join links, and per-Session participation reporting. Demio documents the API as an Apiary API Blueprint, publishes burst rate limits and daily call quotas, runs a public Atlassian Statuspage, ships one first-party PHP SDK from its meetdemio GitHub organization, and offers a Zapier app with registration, join, no-show and event-update
  triggers for teams that do not want to call the API directly.'
finops:
- has_sources: true
  method: derived
  name: Demio Finops
  primary_unit: host / paid yearly
  service_category: ''
  slug: demio-finops
  template: false
image: https://cdn.prod.website-files.com/639df5c77a191c7268d2f9a2/63d939e13b301514d7b3dbab_60ee09e2a0845e4356fd7641_5a86d4765e69d200011f70a5_favicon-256.png
layout: provider
modified: '2026-09-16'
name: Demio
nav: Providers
network: true
overview: 'Demio publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Events API, Intro API, and Reports API. Tagged areas include Company, Webinars, Virtual Events, Event Management, and Marketing.


  The Demio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Demio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Demio Plans Pricing
  plan_count: 6
  slug: demio-plans-pricing
- name: Demio Price Estimates
  plan_count: 0
  slug: demio-price-estimates
random_paper: 22
rate_limits:
- limit_count: 3
  name: Demio Rate Limits
  slug: demio-rate-limits
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 24.6
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 63.2
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/demio/demio-2026-08-17T080854.png
security:
- kind: authentication
  name: Demio Authentication
  slug: demio-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Demio Domain Security
  slug: demio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: Pull the attendance report for a webinar Session
  slug: demio-pull-session-attendance-report
- name: Register an attendee and return their unique join link
  slug: demio-register-attendee-and-return-join-link
slug: demio
tags:
- Company
- Webinars
- Virtual Events
- Event Management
- Marketing
- Marketing Technology
- Demand Generation
- Video
- Engagement Marketing
- Lead Generation
- Software-as-a-Service
website: https://www.demio.com
---
