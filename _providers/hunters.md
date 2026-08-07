---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Authentication-gated runtime API for the Hunters SOC platform, used for data ingestion (API/webhook collection) and platform automation. No public OpenAPI is published; the developer knowledge base is
  name: Hunters SOC Platform API
  slug: hunters-soc-platform-api
artifact_total: 3
asyncapis:
- description: ''
  name: Hunters Webhooks
  slug: hunters-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.hunters.security/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hunters.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.hunters.security/en/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.hunters.ai/
- group: start
  title: ''
  type: Login
  url: https://app.hunters.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hunters.security/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hunters.security/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.hunters.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hunters-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hunters-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hunters-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hunters-domain-security.yml
created: '2026-07-17'
description: Hunters is an AI-driven, next-generation SIEM and SOC platform that helps security operations teams do more with less by automating threat detection, triage, investigation, correlation, and response across an organization's entire security stack. It ingests data from cloud, identity, endpoint, and network sources (including customer-owned Snowflake and cloud data lakes), applies built-in detectors and threat-hunting content, and surfaces the alerts that matter with automated enrichment. Hunters exposes an API/webhook data ingestion path and outbound webhook automation recipes; the runtime API at api.hunters.ai is authentication-gated and no public OpenAPI is published. This profile was surfaced as a portfolio company of Bessemer Venture Partners and enriched by the API Evangelist enrichment pipeline.
image: https://www.hunters.security/favicon.ico
layout: provider
modified: '2026-07-19'
name: Hunters
nav: Providers
network: true
overview: 'Hunters publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, SIEM, SOC, and Threat Detection.


  The Hunters catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hunters'' developer surface includes documentation, engineering blog, signup flow, changelog, and 8 more developer resources.'
random_paper: 99
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 10.9
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hunters/refs/heads/main/screenshots/hunters-2026-07-25T221736.png
security:
- kind: domain-security
  name: Hunters Domain Security
  slug: hunters-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hunters
tags:
- Company
- Cybersecurity
- SIEM
- SOC
- Threat Detection
- Security Operations
- Incident Response
- Threat Hunting
website: https://www.hunters.security/
---
