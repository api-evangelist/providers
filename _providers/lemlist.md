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
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Lemlist Agentic Access
  operation_count: 7
  slug: lemlist-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 4
apis:
- description: REST API for managing campaigns, leads, sequences, teams, and outreach activities in lemlist. Authentication is via API key passed using HTTP Basic auth. The API supports integrating lemlist with CRMs
  name: lemlist REST API
  slug: rest-api
- description: Campaign CRUD and lifecycle
  name: lemlist Campaigns API
  slug: lemlist-campaigns-api
- description: Team-level endpoints (info, senders, credits)
  name: lemlist Team API
  slug: lemlist-team-api
- description: User endpoints
  name: lemlist Users API
  slug: lemlist-users-api
artifact_total: 9
collections:
- collection_type: open
  name: lemlist API
  slug: open-lemlist
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lemlist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemlist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lemlist-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lemlist
- group: company
  title: ''
  type: Website
  url: https://www.lemlist.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lemlist.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lemlist.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.lemlist.com/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://api.lemlist.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.lemlist.com/blog
created: '2026-05-11'
description: lemlist is a cold email outreach and sales engagement platform that helps sales teams build prospect lists, personalize multichannel campaigns across email and LinkedIn, and automate follow-ups to book more meetings. It includes a built-in B2B lead database, AI-generated personalization, and warm-up tools to keep deliverability healthy. The lemlist API enables developers to integrate lemlist with other tools and automate outreach workflows using API key authentication.
graphqls:
- description: Conceptual GraphQL schema for the [lemlist](https://www.lemlist.com) sales engagement and email outreach automation platform. lemlist enables sales teams to build prospect lists, run personalized mult
  name: lemlist GraphQL Schema
  slug: lemlist-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lemlist.png
layout: provider
modified: '2026-05-11'
name: lemlist
nav: Providers
network: true
overview: 'lemlist publishes 3 APIs on the [APIs.io](https://apis.io/) network: Campaigns API, Team API, and Users API. Tagged areas include Email Outreach, Sales Engagement, Cold Email, Sales Automation, and LinkedIn Outreach.


  lemlist''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 24
score:
  band: emerging
  composite: 27.4
  delta: -1.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 54.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lemlist/refs/heads/main/screenshots/lemlist-2026-06-20T184417.png
security:
- kind: authentication
  name: Lemlist Authentication
  slug: lemlist-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lemlist Domain Security
  slug: lemlist-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lemlist
tags:
- Email Outreach
- Sales Engagement
- Cold Email
- Sales Automation
- LinkedIn Outreach
- Lead Generation
website: https://www.lemlist.com
---
