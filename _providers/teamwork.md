---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Teamwork Agentic Access
  operation_count: 3
  slug: teamwork-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: REST API for the Teamwork.com Projects product providing programmatic access to projects, tasks, milestones, time entries, people, companies, tags, and reporting. Authentication supports OAuth 2.0 Bea
  name: Teamwork.com Projects API v3
  slug: projects-api-v3
artifact_total: 5
collections:
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
overview: 'Teamwork.com publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API v3. Tagged areas include Project Management, Client Services, Task Management, Time Tracking, and Collaboration.


  Teamwork.com''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 27.0
  delta: -7.7
  facets:
    commercial_clarity: 10.5
    contract_quality: 40.3
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
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
