---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Appcues Agentic Access
  operation_count: 44
  slug: appcues-agentic-access
  summary_line: 44 operations · 25 acting
api_count: 1
apis:
- description: Appcues Public API exposes flows, mobile experiences, pins, launchpads, banners, checklists, embeds, NPS, segments, users, groups, events, jobs, and SDK key management. US and EU regions are supported
  name: Appcues Public API
  slug: appcues-public-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Banners API from Appcues — 4 operation(s) for banners.
  name: Appcues Banners API
  slug: appcues-banners-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Events API from Appcues — 1 operation(s) for events.
  name: Appcues Events API
  slug: appcues-events-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Exports API from Appcues — 1 operation(s) for exports.
  name: Appcues Exports API
  slug: appcues-exports-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Flows API from Appcues — 4 operation(s) for flows.
  name: Appcues Flows API
  slug: appcues-flows-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Groups API from Appcues — 2 operation(s) for groups.
  name: Appcues Groups API
  slug: appcues-groups-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Imports API from Appcues — 3 operation(s) for imports.
  name: Appcues Imports API
  slug: appcues-imports-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Jobs API from Appcues — 2 operation(s) for jobs.
  name: Appcues Jobs API
  slug: appcues-jobs-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Launchpads API from Appcues — 4 operation(s) for launchpads.
  name: Appcues Launchpads API
  slug: appcues-launchpads-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Mobile API from Appcues — 4 operation(s) for mobile.
  name: Appcues Mobile API
  slug: appcues-mobile-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Pins API from Appcues — 4 operation(s) for pins.
  name: Appcues Pins API
  slug: appcues-pins-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Segments API from Appcues — 5 operation(s) for segments.
  name: Appcues Segments API
  slug: appcues-segments-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Tags API from Appcues — 2 operation(s) for tags.
  name: Appcues Tags API
  slug: appcues-tags-api
- baseURL: https://api.appcues.com
  baseurl_source: declared
  description: The Users API from Appcues — 1 operation(s) for users.
  name: Appcues Users API
  slug: appcues-users-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Appcues Public Banners API
  slug: open-appcues-banners-api
- collection_type: open
  name: Appcues Public Banners Events API
  slug: open-appcues-events-api
- collection_type: open
  name: Appcues Public Banners Exports API
  slug: open-appcues-exports-api
- collection_type: open
  name: Appcues Public Banners Flows API
  slug: open-appcues-flows-api
- collection_type: open
  name: Appcues Public Banners Groups API
  slug: open-appcues-groups-api
- collection_type: open
  name: Appcues Public Banners Imports API
  slug: open-appcues-imports-api
- collection_type: open
  name: Appcues Public Banners Jobs API
  slug: open-appcues-jobs-api
- collection_type: open
  name: Appcues Public Banners Launchpads API
  slug: open-appcues-launchpads-api
- collection_type: open
  name: Appcues Public Banners Mobile API
  slug: open-appcues-mobile-api
- collection_type: open
  name: Appcues Public Banners Pins API
  slug: open-appcues-pins-api
- collection_type: open
  name: Appcues Public Banners Segments API
  slug: open-appcues-segments-api
- collection_type: open
  name: Appcues Public Banners Tags API
  slug: open-appcues-tags-api
- collection_type: open
  name: Appcues Public Banners Users API
  slug: open-appcues-users-api
- collection_type: open
  name: Appcues Public API
  slug: open-appcues
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appcues-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appcues-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appcues-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appcues
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appcues
- group: company
  title: ''
  type: Website
  url: https://www.appcues.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.appcues.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/appcues-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appcues-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/appcues-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.appcues.com/blog
created: '2026-05-08'
description: Appcues is a product-led growth platform for in-app onboarding, announcements, surveys, and user engagement experiences.
finops:
- name: Appcues Finops
  service_category: Product
  slug: appcues-finops
graphqls:
- description: This conceptual GraphQL schema represents the Appcues platform — a product-led growth and in-app onboarding tool. Appcues enables teams to build flows, checklists, pins, NPS surveys, and launchpad exp
  name: Appcues GraphQL Schema
  slug: appcues-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appcues.png
layout: provider
modified: '2026-05-08'
name: Appcues
nav: Providers
network: true
overview: 'Appcues publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Banners API, Events API, Exports API, and 10 more. Tagged areas include Product, Onboarding, In-App Guidance, Analytics, and Customer Success.


  Appcues'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Appcues Plans Pricing
  plan_count: 1
  slug: appcues-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Appcues Rate Limits
  slug: appcues-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appcues/refs/heads/main/screenshots/appcues-2026-06-20T172312.png
security:
- kind: authentication
  name: Appcues Authentication
  slug: appcues-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Appcues Domain Security
  slug: appcues-domain-security
  summary_line: TLSv1.3 · DMARC
slug: appcues
tags:
- Product
- Onboarding
- In-App Guidance
- Analytics
- Customer Success
website: https://www.appcues.com/
---
