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
  - rate-limits
  - security
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Acall Agentic Access
  operation_count: 13
  slug: acall-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.workstyleos.com/v1/
  baseurl_source: declared
  description: The Event API API from Acall — 2 operation(s) for event api.
  name: Acall Event API
  slug: acall-event-api-api
- baseURL: https://api.workstyleos.com/v1/
  baseurl_source: declared
  description: The Facility API API from Acall — 2 operation(s) for facility api.
  name: Acall Facility API
  slug: acall-facility-api-api
- baseURL: https://api.workstyleos.com/v1/
  baseurl_source: declared
  description: The Gate API API from Acall — 1 operation(s) for gate api.
  name: Acall Gate API
  slug: acall-gate-api-api
- baseURL: https://api.workstyleos.com/v1/
  baseurl_source: declared
  description: The Spot API API from Acall — 1 operation(s) for spot api.
  name: Acall Spot API
  slug: acall-spot-api-api
- baseURL: https://api.workstyleos.com/v1/
  baseurl_source: declared
  description: The Spot Reservation API API from Acall — 2 operation(s) for spot reservation api.
  name: Acall Spot Reservation API
  slug: acall-spot-reservation-api-api
- baseURL: https://api.workstyleos.com/v1/
  baseurl_source: declared
  description: The User API API from Acall — 2 operation(s) for user api.
  name: Acall User API
  slug: acall-user-api-api
artifact_total: 17
asyncapis:
- description: ''
  name: Acall Webhooks
  slug: acall-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://www.acall.inc/news/
- group: other
  href: https://artifacts.apis.io/acall/capabilities/acall-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/acall-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/acall/agentic-access/acall-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acall-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/acall/security/acall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acall-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/acall/authentication/acall-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acall-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.acall.inc/
- group: docs
  title: ''
  type: Documentation
  url: https://support.workstyleos.com/faq/show/598?site_domain=default
- group: docs
  title: ''
  type: APIReference
  url: https://www.workstyleos.com/publicapi/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.workstyleos.com/?site_domain=default
- group: start
  title: ''
  type: Login
  url: https://portal.workstyleos.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.workstyleos.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workstyleos.com/terms_of_use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acall.inc/privacypolicy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acall.inc/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.workstyleos.com/info/release/
- group: company
  title: ''
  type: Blog
  url: https://workstylelab.acall.inc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acall-inc
- group: auth
  title: ''
  type: Compliance
  url: https://www.workstyleos.com/security/
- group: design
  href: https://artifacts.apis.io/acall/conventions/acall-conventions.yml
  title: ''
  type: Conventions
  url: conventions/acall-conventions.yml
- group: design
  href: https://artifacts.apis.io/acall/errors/acall-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acall-problem-types.yml
- group: design
  href: https://artifacts.apis.io/acall/lifecycle/acall-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/acall-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/acall/conformance/acall-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acall-conformance.yml
- group: design
  href: https://artifacts.apis.io/acall/data-model/acall-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acall-data-model.yml
- group: build
  href: https://artifacts.apis.io/acall/packages/acall-packages.yml
  title: ''
  type: Packages
  url: packages/acall-packages.yml
- group: design
  href: https://artifacts.apis.io/acall/asyncapi/acall-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/acall-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/acall/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/acall/llms/acall-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acall-llms.txt
- group: other
  href: https://artifacts.apis.io/acall/overlays/acall-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/acall-public-api-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/acall/rate-limits/acall-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/acall-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/acall/plans/acall-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acall-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/acall/changelog/acall-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/acall-changelog.yml
created: '2026-09-06'
description: 'Acall Inc. (アコール株式会社) is a Japanese workplace-experience software company, founded in 2010 and headquartered in Tokyo with a Kobe office, whose Acall / WorkstyleOS platform runs the physical side of hybrid work for more than 7,000 organizations. The product is a set of check-in surfaces — Acall Reception (iPad visitor reception and entry/exit records), Acall Meeting (meeting-room booking and utilization), Acall Desktop (free-address desk and workspace "spot" reservation / hoteling), Acall Gate (entry-gate integration), AI Meeting, Neat device integration and a multi-tenant building mode — stitched to Microsoft 365 and Google Calendar, Teams/Slack/Chatwork notifications, and SSO/SCIM-style provisioning. Acall publishes a REST "Acall Public API" (v1, bearer token) covering workers, facilities, events, gate access logs, spots and spot reservations, plus an outbound Webhook surface for appointment and internal-meeting events. API access is not self-serve: a token is issued only
  after a request through the contact form, and the API is unavailable on the multi-tenant plan.'
finops:
- has_sources: true
  method: derived
  name: Acall Finops
  primary_unit: ''
  service_category: ''
  slug: acall-finops
  template: true
image: https://www.workstyleos.com/images/common/ogp/acall_ogp.png
layout: provider
modified: '2026-10-06'
name: Acall
nav: Providers
network: true
overview: 'Acall publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Event API, Facility API, Gate API, and 3 more. Tagged areas include Workplace Management, Visitor Management, Meeting Room Booking, Desk Booking, and Hybrid Work.


  The Acall catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Acall''s developer surface includes engineering blog, authentication, documentation, API reference, support, pricing, changelog, and 24 more developer resources.'
plans:
- name: Acall Plans Pricing
  plan_count: 2
  slug: acall-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Acall Rate Limits
  slug: acall-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Acall API Rules
  rule_count: 51
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 3
  slug: acall-rules
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 67.1
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/acall/acall-2026-10-11T092504.png
security:
- kind: authentication
  name: Acall Authentication
  slug: acall-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Acall Domain Security
  slug: acall-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Acall Trust Center
  slug: acall-trust-center
  summary_line: ISO/IEC 27001 (ISMS)
skill_count: 2
skills:
- name: Book a workspace for a worker in Acall
  slug: acall-book-a-workspace
- name: Reconcile Acall appointments against entry-gate access logs
  slug: acall-reconcile-visits-and-access
slug: acall
tags:
- Workplace Management
- Visitor Management
- Meeting Room Booking
- Desk Booking
- Hybrid Work
- Access Control
- Facilities
- Smart Office
- Japan
- Software-as-a-Service
website: https://www.acall.inc/
---
