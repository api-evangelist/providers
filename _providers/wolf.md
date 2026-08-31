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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-30'
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
- description: Candidate MCP (Model Context Protocol) server tool surface for the Wolf staffing-platform API, derived from the documented operations. No official hosted/remote Wolf MCP server was found. This is a pr
  name: Wolf MCP Server
  slug: wolf-mcp-server
modified: '2026-07-21'
name: Wolf
nav: Providers
network: true
overview: 'Wolf publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, Gig Economy, Workforce Management, and Job.


  Wolf''s developer surface includes documentation, API reference, getting-started guide, authentication, and 6 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.0
  provenance:
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Job
- Scheduling
- On-Demand Staffing
- Chat
website: https://fromwolf.com/
---
