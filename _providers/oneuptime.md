---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Oneuptime Agentic Access
  operation_count: 15
  slug: oneuptime-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 1
apis:
- description: The Projects API from OneUptime — 9 operation(s) for projects.
  name: OneUptime Projects API
  slug: oneuptime-projects-api
artifact_total: 8
collections:
- collection_type: open
  name: OneUptime API
  slug: open-oneuptime
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oneuptime-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/oneuptime-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oneuptime-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oneuptime
- group: company
  title: ''
  type: Website
  url: https://oneuptime.com
- group: docs
  title: ''
  type: Documentation
  url: https://oneuptime.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneUptime/oneuptime
- group: company
  title: ''
  type: Blog
  url: https://oneuptime.com/blog/rss.xml
created: '2026-03-25'
description: OneUptime is an open source observability platform combining monitoring, incident management, status pages, and on-call scheduling in one OpenTelemetry-native tool.
finops:
- name: Oneuptime Finops
  service_category: API
  slug: oneuptime-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oneuptime.png
layout: provider
modified: '2026-05-19'
name: OneUptime
nav: Providers
network: true
overview: 'OneUptime publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Observability and Open Source.


  OneUptime''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Oneuptime Plans Pricing
  plan_count: 3
  slug: oneuptime-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Oneuptime Rate Limits
  slug: oneuptime-rate-limits
score:
  band: thin
  composite: 32.3
  delta: 2.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 41.6
    developer_ergonomics: 10.9
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 30.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oneuptime/refs/heads/main/screenshots/oneuptime-2026-06-20T190719.png
security:
- kind: domain-security
  name: Oneuptime Domain Security
  slug: oneuptime-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Oneuptime Trust Center
  slug: oneuptime-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: oneuptime
tags:
- Observability
- Open Source
website: https://oneuptime.com
---
