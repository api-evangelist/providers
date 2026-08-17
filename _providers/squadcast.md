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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Squadcast Agentic Access
  operation_count: 13
  slug: squadcast-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 4
apis:
- description: Public REST API for managing incidents, services, on-call schedules, escalation policies, users, and teams in Squadcast. Authentication uses HTTP Bearer access tokens exchanged from a refresh token at
  name: Squadcast Public API
  slug: public-api
- description: Token exchange endpoints
  name: Squadcast Authentication API
  slug: squadcast-authentication-api
- description: Incident lifecycle and bulk operations
  name: Squadcast Incidents API
  slug: squadcast-incidents-api
- description: Incident creation request status
  name: Squadcast Requests API
  slug: squadcast-requests-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Squadcast Public Authentication API
  slug: open-squadcast-authentication-api
- collection_type: open
  name: Squadcast Public Authentication Incidents API
  slug: open-squadcast-incidents-api
- collection_type: open
  name: Squadcast Public Authentication Requests API
  slug: open-squadcast-requests-api
- collection_type: open
  name: Squadcast Public API
  slug: open-squadcast
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/squadcast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/squadcast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/squadcast-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SquadcastHub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/squadcast
- group: company
  title: ''
  type: Website
  url: https://www.squadcast.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.squadcast.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.squadcast.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.squadcast.com/signup
- group: company
  title: ''
  type: Blog
  url: https://squadcast.com/blog/rss.xml
created: '2026-05-11'
description: Squadcast (now part of SolarWinds Incidents Cloud) is an end-to-end incident response and on-call management platform that helps SRE and DevOps teams detect, respond to, and learn from incidents with on-call schedules, escalation policies, runbooks, status pages, and post-incident reviews. Squadcast's public API provides programmatic access to incidents, services, schedules, escalation policies, and users using OAuth bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/squadcast.png
layout: provider
modified: '2026-05-11'
name: Squadcast
nav: Providers
network: true
overview: 'Squadcast publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Incidents API, and Requests API. Tagged areas include Incident Response, On-Call Management, DevOps, SRE, and Alerting.


  Squadcast''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 75
score:
  band: thin
  composite: 32.4
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 60.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/squadcast/refs/heads/main/screenshots/squadcast-2026-06-20T194432.png
security:
- kind: authentication
  name: Squadcast Authentication
  slug: squadcast-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Squadcast Domain Security
  slug: squadcast-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: squadcast
tags:
- Incident Response
- On-Call Management
- DevOps
- SRE
- Alerting
- Incident Management
website: https://www.squadcast.com
---
