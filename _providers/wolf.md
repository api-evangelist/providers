---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 13.7
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'Multi-tenant REST API for building client- and job-seeker-facing staffing interfaces on the Wolf platform: authentication, jobs/shifts, tenders, availability, timesheets, notifications, job-seeker and'
  name: Wolf Staffing API
  slug: wolf-staffing-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wolf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fromwolf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fromwolf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fromwolf.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fromwolf.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fromwolf.com/glossary/core-attributes-of-all-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/wolf-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wolf-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wolf-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Wolf (fromwolf.com) is a white-label, multi-tenant staffing and gig-work platform that lets staffing companies run their own branded on-demand workforce. Its API coordinates job seekers, clients, campaigns (client orders), shifts, tenders (a seeker's request to work a shift), applications, timesheets, availability, notifications, and in-app chat — everything needed to build a client- or worker-facing staffing interface on top of the Wolf backend. Each tenant runs on its own database and authenticates with a tenant key plus a platform API key or per-user authentication token. Wolf was surfaced as a Techstars portfolio company and profiled by the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wolf.png
layout: provider
mcp_servers:
- description: ''
  name: wolf-mcp.yml
  slug: wolf-mcpyml
modified: '2026-07-21'
name: Wolf
nav: Providers
network: true
overview: 'Wolf publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, Gig Economy, Workforce Management, and Jobs.


  Wolf''s developer surface includes documentation, API reference, getting-started guide, authentication, and 6 more developer resources.'
random_paper: 92
score:
  band: emerging
  composite: 18.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.2
  provenance:
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Wolf Authentication
  slug: wolf-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Wolf Domain Security
  slug: wolf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wolf
tags:
- Company
- Staffing
- Gig Economy
- Workforce Management
- Jobs
- Scheduling
- On-Demand Staffing
- Chat
website: https://fromwolf.com/
---
