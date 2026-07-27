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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Knit Agentic Access
  operation_count: 9
  slug: knit-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 7
apis:
- description: Operations for managing department data across connected platforms.
  name: Knit Departments API
  slug: knit-departments-api
- description: Operations for managing employee data across connected HRIS platforms.
  name: Knit Employees API
  slug: knit-employees-api
- description: Operations for managing connected integrations.
  name: Knit Integrations API
  slug: knit-integrations-api
- description: Operations for managing job postings and applications via ATS integrations.
  name: Knit Jobs API
  slug: knit-jobs-api
- description: Operations for managing location/office data.
  name: Knit Locations API
  slug: knit-locations-api
- description: Operations for monitoring sync status and triggering syncs.
  name: Knit Syncs API
  slug: knit-syncs-api
- description: Operations for managing time off and leave data.
  name: Knit Time Off API
  slug: knit-time-off-api
artifact_total: 38
collections:
- collection_type: open
  name: Knit Unified API
  slug: open-knit-unified-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knit-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knitapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getknit
- group: start
  title: ''
  type: Portal
  url: https://developers.getknit.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getknit.dev/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/knit-unified-api-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/knit-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.getknit.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.getknit.dev/blog/rss.xml
created: '2026-03-16'
description: Knit is a unified API platform for B2B products, AI agents, and MCP clients, providing integrations infrastructure for HR, recruitment, and collaboration tools. Knit manages cron jobs, rate limits, and retries out of the box for predictable data syncing at scale.
features:
- Unified API for multiple HRIS and ATS platforms
- Automatic cron job management for data syncing
- Built-in rate limiting and retry logic
- Standardized data models across providers
- MCP client and AI agent support
- Real-time webhook notifications
- Incremental sync with updated_after filtering
finops:
- name: Knit Finops
  service_category: API
  slug: knit-finops
image: /assets/icons/knit.png
integrations:
- BambooHR
- Gusto
- Workday
- ADP
- Rippling
- Greenhouse
- Lever
- Slack
- Microsoft Teams
json_schemas:
- name: Knit Unified API Resources
  property_count: 0
  slug: knit-unified-api
jsonld:
- class_count: 0
  name: Knit Context
  property_count: 5
  slug: knit-context
layout: provider
modified: '2026-05-19'
name: Knit
nav: Providers
network: true
overview: 'Knit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Departments API, Employees API, Integrations API, and 4 more. Tagged areas include B2B, HR Integrations, HRIS, and Unified API.


  The Knit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Knit''s developer surface includes authentication, developer portal, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Knit Plans Pricing
  plan_count: 3
  slug: knit-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Knit Rate Limits
  slug: knit-rate-limits
rules:
- name: Knit API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: knit-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.5
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.6
    developer_ergonomics: 30.4
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 49.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knit/refs/heads/main/screenshots/knit-2026-06-20T184110.png
security:
- kind: authentication
  name: Knit Authentication
  slug: knit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Knit Domain Security
  slug: knit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: knit
tags:
- B2B
- HR Integrations
- HRIS
- Unified API
use_cases:
- Synchronizing employee data across HR platforms
- Building B2B integrations without managing individual provider APIs
- Powering AI agents with unified HR and recruitment data
- Automating onboarding workflows across HRIS systems
- Aggregating time-off and attendance data from multiple providers
website: https://developers.getknit.dev/
---
