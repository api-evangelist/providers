---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Nowsta Agentic Access
  operation_count: 6
  slug: nowsta-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- description: Allow-listed partner API for publishing workforce data into Nowsta. Six bulk "publications" endpoints - events (with nested shifts), venues, clients, uniforms, positions and workers - each accepting u
  name: Nowsta Integration API
  slug: nowsta-integration-api
artifact_total: 6
collections:
- collection_type: open
  name: Nowsta Integration API
  slug: open-nowsta-integration
common:
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
overview: 'Nowsta publishes 1 API on the [APIs.io](https://apis.io/) network: Integration API. Tagged areas include Workforce Management, staff-scheduling, shift-scheduling, Time and Attendance, and Hourly Workforce.


  Nowsta''s developer surface includes API reference, support, engineering blog, and 24 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 16.7
    contract_quality: 62.2
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 32.9
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
