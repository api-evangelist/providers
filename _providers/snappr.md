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
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Snappr Agentic Access
  operation_count: 14
  slug: snappr-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.snappr.com
  baseurl_source: declared
  description: Check available shoot start times.
  name: Snappr Availability API
  slug: snappr-availability-api
- baseURL: https://api.snappr.com
  baseurl_source: declared
  description: Create and retrieve photoshoot bookings.
  name: Snappr Bookings API
  slug: snappr-bookings-api
- baseURL: https://api.snappr.com
  baseurl_source: declared
  description: Check Snappr coverage for a location and shoot type.
  name: Snappr Coverage API
  slug: snappr-coverage-api
- baseURL: https://api.snappr.com
  baseurl_source: declared
  description: Available Snappr editing job types.
  name: Snappr Editing Job Types API
  slug: snappr-editing-job-types-api
- baseURL: https://api.snappr.com
  baseurl_source: declared
  description: Create and retrieve photo editing jobs (beta).
  name: Snappr Editing Jobs API
  slug: snappr-editing-jobs-api
- baseURL: https://api.snappr.com
  baseurl_source: declared
  description: Retrieve images for bookings and editing jobs.
  name: Snappr Images API
  slug: snappr-images-api
- baseURL: https://api.snappr.com
  baseurl_source: declared
  description: Editing presets defined in the Photography Portal.
  name: Snappr Presets API
  slug: snappr-presets-api
- baseURL: https://api.snappr.com
  baseurl_source: declared
  description: Available Snappr shoot types.
  name: Snappr Shoot Types API
  slug: snappr-shoot-types-api
- baseURL: https://api.snappr.com
  baseurl_source: declared
  description: Retrieve videos for bookings.
  name: Snappr Videos API
  slug: snappr-videos-api
artifact_total: 26
asyncapis:
- description: ''
  name: Snappr Webhooks
  slug: snappr-webhooks
collections:
- collection_type: open
  name: Snappr Availability API
  slug: open-snappr-availability-api
- collection_type: open
  name: Snappr Availability Bookings API
  slug: open-snappr-bookings-api
- collection_type: open
  name: Snappr Availability Coverage API
  slug: open-snappr-coverage-api
- collection_type: open
  name: Snappr Availability Editing Job Types API
  slug: open-snappr-editing-job-types-api
- collection_type: open
  name: Snappr Availability Editing Jobs API
  slug: open-snappr-editing-jobs-api
- collection_type: open
  name: Snappr Availability Images API
  slug: open-snappr-images-api
- collection_type: open
  name: Snappr Availability Presets API
  slug: open-snappr-presets-api
- collection_type: open
  name: Snappr Availability Shoot Types API
  slug: open-snappr-shoot-types-api
- collection_type: open
  name: Snappr Availability Videos API
  slug: open-snappr-videos-api
common:
- group: other
  href: https://artifacts.apis.io/snappr/overlays/snappr-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snappr-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/snappr/agentic-access/snappr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snappr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/snappr/security/snappr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snappr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snappr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.snappr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snappr.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.snappr.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.snappr.com/#introduction
- group: auth
  href: https://artifacts.apis.io/snappr/authentication/snappr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snappr-authentication.yml
- group: start
  href: https://artifacts.apis.io/snappr/sandbox/snappr-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/snappr-sandbox.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://snappr.statuspage.io
- group: design
  href: https://artifacts.apis.io/snappr/asyncapi/snappr-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/snappr-webhooks.yml
- group: design
  href: https://artifacts.apis.io/snappr/conventions/snappr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/snappr-conventions.yml
- group: agent
  href: https://artifacts.apis.io/snappr/mcp/snappr-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/snappr-mcp.yml
- group: agent
  href: https://artifacts.apis.io/snappr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/snappr/llms/snappr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snappr-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snappr
- group: operate
  title: ''
  type: Support
  url: https://www.snappr.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.snappr.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.snappr.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.snappr.com/enterprise
- group: start
  title: ''
  type: Login
  url: https://app.snappr.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.snappr.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.snappr.com/privacy
created: '2026-07-17'
description: Snappr is an on-demand visual content marketplace that connects businesses with a global network of professional photographers and videographers, plus automated and human-augmented photo editing services. The Snappr API (the "API for visual content", available to Snappr for Enterprise customers) lets developers programmatically check coverage and availability, book photoshoots, submit photo editing jobs against presets, and retrieve the resulting images and videos. Authentication is a bearer API key; a sandbox environment mirrors production for testing, and custom webhooks notify on booking changes. Backed by Foundry Group and surfaced into the API Evangelist network for enrichment.
image: https://cdn.prod.website-files.com/5ca95f7a3be192f65a7b4e4f/6993a952a20874ef53a0524e_snappr-og-photography-and-videography.jpg
layout: provider
modified: '2026-07-21'
name: Snappr
nav: Providers
network: true
overview: 'Snappr publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Coverage API, and 6 more. Tagged areas include Company, Marketplace, Photography, Videography, and Visual Content.


  The Snappr catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Snappr''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 17 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Snappr API Rules
  rule_count: 63
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 1
  slug: snappr-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 22.2
    developer_ergonomics: 60.1
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/snappr/snappr-2026-08-17T081939.png
security:
- kind: authentication
  name: Snappr Authentication
  slug: snappr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Snappr Domain Security
  slug: snappr-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Book a Snappr photoshoot
  slug: snappr-book-a-photoshoot
- name: Retrieve photoshoot images and videos
  slug: snappr-retrieve-shoot-assets
- name: Run a Snappr editing job
  slug: snappr-run-an-editing-job
slug: snappr
tags:
- Company
- Marketplace
- Photography
- Videography
- Visual Content
- Photo Editing
- On-Demand
- Enterprise
website: https://snappr.com
---
