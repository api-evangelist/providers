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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Pipefy Agentic Access
  operation_count: 1
  slug: pipefy-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: GraphQL API for managing pipes, cards, phases, fields, organizations, users, webhooks, and AI agents on the Pipefy workflow automation platform. Authentication is performed using an OAuth2 Bearer toke
  name: Pipefy GraphQL API
  slug: graphql-api
- description: Single GraphQL entry point for all Pipefy operations.
  name: Pipefy GraphQL API
  slug: pipefy-graphql-api
artifact_total: 8
collections:
- collection_type: open
  name: Pipefy GraphQL API
  slug: open-pipefy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pipefy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pipefy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pipefy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pipefy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pipefy
- group: company
  title: ''
  type: Website
  url: https://www.pipefy.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pipefy.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pipefy.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.pipefy.com/public/registration
- group: operate
  title: ''
  type: Help Center
  url: https://help.pipefy.com
- group: operate
  title: ''
  type: Community
  url: https://community.pipefy.com
- group: company
  title: ''
  type: Blog
  url: https://www.pipefy.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pipefy.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pipefy/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.pipefy.com/llms.txt
created: '2026-05-11'
description: Pipefy is a no-code business process and workflow automation platform that lets teams build, run, and orchestrate processes such as procurement, HR onboarding, customer onboarding, and IT service requests using customizable pipes, forms, and AI agents. The platform exposes a GraphQL API at api.pipefy.com/graphql for managing pipes, cards, phases, fields, users, organizations, webhooks, and AI-driven workflow integrations, with OAuth2 Bearer token authentication via Personal Access Tokens or Service Accounts.
graphqls:
- description: GraphQL API for managing pipes, cards, phases, fields, organizations, users, webhooks, and AI agents on the Pipefy workflow automation platform. Authentication is performed using an OAuth2 Bearer toke
  name: Pipefy GraphQL API
  slug: pipefy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pipefy.png
layout: provider
modified: '2026-05-11'
name: Pipefy
nav: Providers
network: true
overview: 'Pipefy publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Workflow Automation, Business Process Management, No-Code, BPM, and GraphQL.


  Pipefy''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 10 more developer resources.'
random_paper: 79
score:
  band: thin
  composite: 34.0
  delta: -1.9
  facets:
    commercial_clarity: 18.4
    contract_quality: 61.9
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pipefy/refs/heads/main/screenshots/pipefy-2026-06-20T191727.png
security:
- kind: authentication
  name: Pipefy Authentication
  slug: pipefy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pipefy Domain Security
  slug: pipefy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pipefy Trust Center
  slug: pipefy-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018
slug: pipefy
tags:
- Workflow Automation
- Business Process Management
- No-Code
- BPM
- GraphQL
- Process Orchestration
website: https://www.pipefy.com
---
