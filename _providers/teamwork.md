---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Teamwork Agentic Access
  operation_count: 3
  slug: teamwork-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: The Activity API from Teamwork.com — 1 operation(s) for activity.
  name: Teamwork.com Activity API
  slug: teamwork-activity-api
- description: The Projects API from Teamwork.com — 1 operation(s) for projects.
  name: Teamwork.com Projects API
  slug: teamwork-projects-api
- description: The Tasks API from Teamwork.com — 1 operation(s) for tasks.
  name: Teamwork.com Tasks API
  slug: teamwork-tasks-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Teamwork.com Projects API v3 Activity API
  slug: open-teamwork-activity-api
- collection_type: open
  name: Teamwork.com API v3 Activity Projects API
  slug: open-teamwork-projects-api
- collection_type: open
  name: Teamwork.com Projects API v3 Activity Tasks API
  slug: open-teamwork-tasks-api
- collection_type: open
  name: Teamwork.com Projects API v3
  slug: open-teamwork
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/teamwork-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teamwork-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teamwork-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teamwork-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamwork
- group: company
  title: ''
  type: Website
  url: https://www.teamwork.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.teamwork.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teamwork.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.teamwork.com/signup
- group: operate
  title: ''
  type: Support
  url: https://support.teamwork.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.teamwork.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teamwork-com
- group: company
  title: ''
  type: Blog
  url: https://www.teamwork.com/blog/
created: '2026-05-11'
description: Teamwork.com is a project management and client work platform built for client services, agencies, and professional services teams to manage projects, tasks, time tracking, billing, resource planning, and collaboration in one place. The platform provides product offerings including Projects, Desk, Chat, Spaces, and CRM with deep integrations across the client delivery lifecycle. Teamwork.com offers a comprehensive REST API (v3) for the Projects product allowing programmatic access to projects, tasks, time entries, milestones, people, and reporting, with Bearer Token (OAuth 2.0) and HTTP Basic authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-11'
name: Teamwork.com
nav: Providers
network: true
overview: 'Teamwork.com publishes 3 APIs on the [APIs.io](https://apis.io/) network: Activity API, Projects API, and Tasks API. Tagged areas include Project Management, Client Services, Task Management, Time Tracking, and Collaboration.


  Teamwork.com''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teamwork/refs/heads/main/screenshots/teamwork-2026-06-20T195100.png
security:
- kind: authentication
  name: Teamwork Authentication
  slug: teamwork-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Teamwork Domain Security
  slug: teamwork-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teamwork
tags:
- Project Management
- Client Services
- Task Management
- Time Tracking
- Collaboration
- Professional Services Automation
website: https://www.teamwork.com
---
