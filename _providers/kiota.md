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
api_count: 1
apis:
- description: Kiota generates strongly-typed, lightweight API clients from OpenAPI descriptions in multiple languages with minimal dependencies and idiomatic code patterns.
  name: Kiota
  slug: kiota
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kiota-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kiota-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://learn.microsoft.com/en-us/openapi/kiota/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/openapi/kiota/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/kiota
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
created: '2026-03-25'
description: Kiota is an open source API client generator from Microsoft that produces strongly-typed, lightweight clients from OpenAPI descriptions. It supports C#, Go, Java, PHP, Python, Ruby, Swift, and TypeScript, with a focus on minimal dependencies and idiomatic code patterns.
finops:
- name: Kiota Finops
  service_category: API
  slug: kiota-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kiota.png
layout: provider
modified: '2026-04-28'
name: Kiota
nav: Providers
network: true
overview: 'Kiota publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, Microsoft, OpenAPI, and SDKs.


  Kiota''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Kiota Plans Pricing
  plan_count: 3
  slug: kiota-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Kiota Rate Limits
  slug: kiota-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kiota/refs/heads/main/screenshots/kiota-2026-06-20T184046.png
security:
- kind: domain-security
  name: Kiota Domain Security
  slug: kiota-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kiota Vulnerability Disclosure
  slug: kiota-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kiota
tags:
- Code Generation
- Microsoft
- OpenAPI
- SDKs
website: https://learn.microsoft.com/en-us/openapi/kiota/
---
