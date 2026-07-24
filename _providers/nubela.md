---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nubela Agentic Access
  operation_count: 11
  slug: nubela-agentic-access
  summary_line: 11 operations
api_count: 4
apis:
- description: The Company API from Nubela — 6 operation(s) for company.
  name: Nubela Company API
  slug: nubela-company-api
- description: The Competitor API from Nubela — 1 operation(s) for competitor.
  name: Nubela Competitor API
  slug: nubela-competitor-api
- description: The Customer API from Nubela — 1 operation(s) for customer.
  name: Nubela Customer API
  slug: nubela-customer-api
- description: The Employee API from Nubela — 3 operation(s) for employee.
  name: Nubela Employee API
  slug: nubela-employee-api
artifact_total: 11
collections:
- collection_type: open
  name: Nubela Proxycurl API
  slug: open-nubela
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nubela-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nubela-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nubela-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nubela
- group: company
  title: ''
  type: Website
  url: https://nubela.co/proxycurl/
- group: docs
  title: ''
  type: Documentation
  url: https://nubela.co/proxycurl/docs
- group: agent
  title: ''
  type: LlmsText
  url: https://nubela.co/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://nubela.co/blog/feed
created: '2025-02-08'
description: Build and scale data-driven applications on people and companies with Nubela's Proxycurl API without worrying about scaling a web scraping and data-science team.
finops:
- name: Nubela Finops
  service_category: API
  slug: nubela-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nubela.png
layout: provider
modified: '2026-05-19'
name: Nubela
nav: Providers
network: true
overview: 'Nubela publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Company API, Competitor API, Customer API, and 1 more. Tagged areas include Companies, Data, People, and Scraping.


  Nubela''s developer surface includes authentication, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Nubela Plans Pricing
  plan_count: 3
  slug: nubela-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Nubela Rate Limits
  slug: nubela-rate-limits
score:
  band: thin
  composite: 33.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.8
    developer_ergonomics: 21.7
    discoverability: 42.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nubela/refs/heads/main/screenshots/nubela-2026-06-20T190506.png
security:
- kind: authentication
  name: Nubela Authentication
  slug: nubela-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nubela Domain Security
  slug: nubela-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nubela
tags:
- Companies
- Data
- People
- Scraping
website: https://nubela.co/proxycurl/
---
