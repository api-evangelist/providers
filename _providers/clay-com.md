---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Generic HTTP request column inside Clay Tables that lets users call any external REST or GraphQL endpoint with row-level variables and write the response back into Clay. Acts as Clay's universal API c
  name: Clay HTTP API Enrichment
  slug: http-api
- description: Webhook source that pushes data from any external system into a Clay Table as new rows. Used to trigger Clay workflows from CRMs, signal providers, and product events.
  name: Clay Incoming Webhooks
  slug: webhooks-incoming
- description: Action column that POSTs enriched row data to an external webhook URL, used to deliver Clay-produced data to CRMs, sequencers, Slack, and custom backends.
  name: Clay Outgoing Webhooks
  slug: webhooks-outgoing
- description: The core spreadsheet-style workspace that combines source rows, enrichment columns, conditional logic, AI agents, and write-back destinations. Tables are the unit of automation and the data plane ever
  name: Clay Tables
  slug: tables
- description: Catalog of native connectors and 150+ data providers — Salesforce, HubSpot, Pipedrive, Apollo, Clearbit, ZoomInfo, LinkedIn Sales Navigator, Smartlead, Instantly, Apollo, OpenAI, and many more — expos
  name: Clay Integrations
  slug: integrations
- description: Browser extension for scraping LinkedIn profiles and other web pages directly into Clay Tables, used to bootstrap prospect lists from manual research.
  name: Clay Chrome Extension
  slug: chrome-extension
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clay.com
- group: other
  title: ''
  type: App
  url: https://app.clay.com
- group: docs
  title: ''
  type: Documentation
  url: https://university.clay.com/docs
- group: other
  title: ''
  type: University
  url: https://university.clay.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clay.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.clay.com/blog
- group: start
  title: ''
  type: Signup
  url: https://app.clay.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.clay.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clay.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clay.com/terms
- group: operate
  title: ''
  type: Slack
  url: https://www.clay.com/community
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clay-gtm
- group: company
  title: ''
  type: Twitter
  url: https://x.com/clay_gtm
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@clay_gtm
created: '2026-05-23'
description: 'Clay is an AI-native sales prospecting and GTM data orchestration platform built around Clay Tables — spreadsheet-like workspaces that combine 150+ data providers, AI research agents, and outbound automations. Clay''s developer surface is integration-oriented rather than a traditional public REST API: HTTP API enrichment columns, incoming and outgoing webhooks, a Chrome extension, and native connectors to CRMs, sequencers, and data providers. External systems push data into Clay Tables and consume enriched rows via webhooks or exports back to systems of record.'
finops:
- name: Clay Com Finops
  service_category: API
  slug: clay-com-finops
graphqls:
- description: ''
  name: Clay GraphQL API
  slug: clay-com-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clay-com.png
layout: provider
modified: '2026-05-23'
name: Clay
nav: Providers
network: true
overview: 'Clay publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Prospecting, GTM, Sales, Enrichment, and Automation.


  Clay''s developer surface includes documentation, pricing, engineering blog, signup flow, YouTube channel, and 10 more developer resources.'
plans:
- name: Clay Com Plans Pricing
  plan_count: 1
  slug: clay-com-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 2
  name: Clay Com Rate Limits
  slug: clay-com-rate-limits
score:
  band: emerging
  composite: 27.1
  delta: -2.6
  facets:
    commercial_clarity: 73.7
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clay-com/refs/heads/main/screenshots/clay-com-2026-06-20T174453.png
security:
- kind: domain-security
  name: Clay Com Domain Security
  slug: clay-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clay-com
tags:
- Prospecting
- GTM
- Sales
- Enrichment
- Automation
- AI
- Webhooks
website: https://www.clay.com
---
