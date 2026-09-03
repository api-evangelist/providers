---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Nowsta Agentic Access
  operation_count: 6
  slug: nowsta-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.nowsta.com
  baseurl_source: declared
  description: Bulk publication of clients referenced by events.
  name: Nowsta Clients API
  slug: nowsta-clients-api
- baseURL: https://api.nowsta.com
  baseurl_source: declared
  description: Bulk publication of events and their nested shifts.
  name: Nowsta Events API
  slug: nowsta-events-api
- baseURL: https://api.nowsta.com
  baseurl_source: declared
  description: Bulk publication of positions referenced by shifts.
  name: Nowsta Positions API
  slug: nowsta-positions-api
- baseURL: https://api.nowsta.com
  baseurl_source: declared
  description: Bulk publication of uniforms referenced by events.
  name: Nowsta Uniforms API
  slug: nowsta-uniforms-api
- baseURL: https://api.nowsta.com
  baseurl_source: declared
  description: Bulk publication of venues referenced by events.
  name: Nowsta Venues API
  slug: nowsta-venues-api
- baseURL: https://api.nowsta.com
  baseurl_source: declared
  description: Bulk publication of company users (workers).
  name: Nowsta Workers API
  slug: nowsta-workers-api
artifact_total: 11
collections:
- collection_type: open
  name: Nowsta Integration API
  slug: open-nowsta-integration
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nowsta-integration-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nowsta-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.nowsta.com/
- group: docs
  title: ''
  type: APIReference
  url: https://web.archive.org/web/20240603053309/https://developer.nowsta.com/
- group: operate
  title: ''
  type: Support
  url: https://community.nowsta.com/support/tickets/new
- group: operate
  title: ''
  type: HelpCenter
  url: https://intercom.help/nowstasupport/en/
- group: company
  title: ''
  type: Blog
  url: https://www.nowsta.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.nowsta.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nowsta
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nowsta.com/
- group: start
  title: ''
  type: Login
  url: https://app.nowsta.com/
- group: start
  title: ''
  type: Demo
  url: https://www.nowsta.com/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nowsta.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nowsta.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.nowsta.com/cookie-policy/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nowsta-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nowsta-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nowsta-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nowsta-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nowsta-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nowsta-llms.txt
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/nowsta-workers/id1172538924
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.nowsta.workers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nowsta
- group: other
  title: ''
  type: X
  url: https://x.com/nowsta
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/nowsta
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/nowsta/
created: '2026-08-01'
description: Nowsta is a Brooklyn, New York workforce management platform for hourly, gig and contingent labor, used by more than 25,000 teams across hospitality and food service, events and venues, healthcare, logistics and distribution, education and retail. The platform covers the full shift lifecycle - talent sourcing and onboarding with a built-in ATS, AI-assisted shift scheduling with demand forecasting and templates, GPS/geofenced time and attendance with automated alerts and timesheet approval, labor-cost and compliance reporting, and payroll/accounting handoff - alongside a vendor management module for coordinating staffing agencies. Workers use a dedicated iOS/Android app and the my.nowsta.com portal to claim shifts, set availability and clock in; coordinators work in app.nowsta.com. For partners, Nowsta publishes an allow-listed Integration API that lets an upstream system (event management, CRM, catering or venue software) publish events, shifts, positions, venues, clients, uniforms
  and workers into Nowsta in bulk.
image: https://www.nowsta.com/wp-content/uploads/2025/02/cropped-nowsta-favicon-v2-270x270.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from the Integration API (not published by Nowsta)
  slug: candidate-mcp-tool-surface-derived-from-the-integration-api-not-published-by-nowsta
modified: '2026-08-01'
name: Nowsta
nav: Providers
network: true
overview: 'Nowsta publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Events API, Positions API, and 3 more. Tagged areas include Workforce Management, staff-scheduling, shift-scheduling, Time and Attendance, and Hourly Workforce.


  Nowsta''s developer surface includes API reference, support, engineering blog, and 25 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 60.5
    developer_ergonomics: 32.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 34.1
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nowsta/refs/heads/main/screenshots/nowsta-2026-08-07T185642.png
security:
- kind: authentication
  name: Nowsta Authentication
  slug: nowsta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nowsta Domain Security
  slug: nowsta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nowsta
tags:
- Workforce Management
- staff-scheduling
- shift-scheduling
- Time and Attendance
- Hourly Workforce
- gig-work
- event-staffing
- Hospitality
- staffing-agency
- Vendor Management
- Payroll
- Human Resources
website: https://www.nowsta.com/
---
