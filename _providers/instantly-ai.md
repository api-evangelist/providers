---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Instantly Ai Agentic Access
  operation_count: 13
  slug: instantly-ai-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 1
apis:
- description: The Campaigns API from Instantly — 10 operation(s) for campaigns.
  name: Instantly Campaigns API
  slug: instantly-ai-campaigns-api
artifact_total: 9
collections:
- collection_type: open
  name: Instantly.ai API v2
  slug: open-instantly-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instantly-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instantly-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instantly-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://instantly.ai
- group: other
  title: ''
  type: App
  url: https://app.instantly.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developer.instantly.ai
- group: docs
  title: ''
  type: APIReference
  url: https://developer.instantly.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.instantly.ai/getting-started/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.instantly.ai/getting-started/authorization
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.instantly.ai/openapi/api_v2.json
- group: commercial
  title: ''
  type: Pricing
  url: https://instantly.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://instantly.ai/blog
- group: operate
  title: ''
  type: Help
  url: https://help.instantly.ai
- group: start
  title: ''
  type: Signup
  url: https://app.instantly.ai/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.instantly.ai/auth/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instantly.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instantly.ai/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instantlyai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Instantlydotai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@instantly-ai
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.instantly.ai/llms.txt
- group: docs
  title: ''
  type: GraphQL
  url: graphql/instantly-ai-graphql.md
created: '2026-05-23'
description: Instantly is a cold email outbound platform that combines mailbox sending infrastructure, email warmup, a B2B lead database, deliverability tools, and a unified inbox for replies. The Instantly v2 REST API at api.instantly.ai/api/v2 covers campaigns, leads, accounts, email verification, inbox placement tests, webhooks, analytics, API keys, and workspaces, with Bearer token authentication and scoped API keys.
finops:
- name: Instantly Ai Finops
  service_category: API
  slug: instantly-ai-finops
graphqls:
- description: This conceptual GraphQL schema models the Instantly cold email outreach and sales acceleration platform. Instantly provides mailbox sending infrastructure, email warmup, a B2B lead database, deliverab
  name: Instantly GraphQL Schema
  slug: instantly-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instantly-ai.png
layout: provider
modified: '2026-05-23'
name: Instantly
nav: Providers
network: true
overview: 'Instantly publishes 1 API on the [APIs.io](https://apis.io/) network: Campaigns API. Tagged areas include Cold Email, Outbound, Sales, Deliverability, and Lead Database.


  Instantly''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Instantly Ai Plans Pricing
  plan_count: 1
  slug: instantly-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Instantly Ai Rate Limits
  slug: instantly-ai-rate-limits
score:
  band: developing
  composite: 47.9
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 62.8
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instantly-ai/refs/heads/main/screenshots/instantly-ai-2026-06-20T183518.png
security:
- kind: authentication
  name: Instantly Ai Authentication
  slug: instantly-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Instantly Ai Domain Security
  slug: instantly-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instantly-ai
tags:
- Cold Email
- Outbound
- Sales
- Deliverability
- Lead Database
- Email Verification
- Webhooks
website: https://instantly.ai
---
