---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-12'
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
  description: REST API (v1) for the Acall / WorkstyleOS workplace platform. Thirteen operations across six resource families — workers (users), facilities, events, gate access logs, spots, and spot reservations — w
  name: Acall Public API
  slug: acall-public-api
artifact_total: 8
asyncapis:
- description: ''
  name: Acall Webhooks
  slug: acall-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acall-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acall-domain-security.yml
- group: auth
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
  title: ''
  type: Conventions
  url: conventions/acall-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/acall-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acall-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acall-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acall-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/acall-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/acall-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acall-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/acall-public-api-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acall-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acall-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/acall-changelog.yml
created: '2026-09-06'
description: 'Acall Inc. (アコール株式会社) is a Japanese workplace-experience software company, founded in 2010 and headquartered in Tokyo with a Kobe office, whose Acall / WorkstyleOS platform runs the physical side of hybrid work for more than 7,000 organizations. The product is a set of check-in surfaces — Acall Reception (iPad visitor reception and entry/exit records), Acall Meeting (meeting-room booking and utilization), Acall Desktop (free-address desk and workspace "spot" reservation / hoteling), Acall Gate (entry-gate integration), AI Meeting, Neat device integration and a multi-tenant building mode — stitched to Microsoft 365 and Google Calendar, Teams/Slack/Chatwork notifications, and SSO/SCIM-style provisioning. Acall publishes a REST "Acall Public API" (v1, bearer token) covering workers, facilities, events, gate access logs, spots and spot reservations, plus an outbound Webhook surface for appointment and internal-meeting events. API access is not self-serve: a token is issued only
  after a request through the contact form, and the API is unavailable on the multi-tenant plan.'
image: https://www.workstyleos.com/images/common/ogp/acall_ogp.png
layout: provider
modified: '2026-09-06'
name: Acall
nav: Providers
network: true
overview: 'Acall publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Workplace Management, Visitor Management, Meeting Room Booking, Desk Booking, and Hybrid Work.


  The Acall catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Acall''s developer surface includes authentication, documentation, API reference, support, pricing, changelog, engineering blog, and 22 more developer resources.'
plans:
- name: Acall Plans Pricing
  plan_count: 0
  slug: acall-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Acall Rate Limits
  slug: acall-rate-limits
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    contract_governance: 4.5
    contract_quality: 59.1
    developer_ergonomics: 37.5
    discoverability: 68.5
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- SaaS
website: https://www.acall.inc/
---
