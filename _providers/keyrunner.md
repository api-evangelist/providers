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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The KeyRunner platform provides a local-first toolset for testing, monitoring, mocking, and running APIs with secrets kept on-device. Available as desktop apps, a VS Code extension, and a CLI distribu
  name: KeyRunner Platform
  slug: keyrunner-platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keyrunner-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/launchiam
- group: company
  title: ''
  type: Website
  url: https://keyrunner.app/
- group: company
  title: ''
  type: Blog
  url: https://keyrunner.app/blog
created: '2025-01-08'
description: KeyRunner is a local-first API platform combining a desktop API client, request monitor, mock server, and secret manager. It is delivered as desktop applications (Windows, macOS Intel, macOS Apple Silicon), a VS Code extension, and a CLI, with all requests and secrets kept inside the developer environment.
finops:
- name: Keyrunner Finops
  service_category: API
  slug: keyrunner-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keyrunner.png
layout: provider
modified: '2026-04-28'
name: KeyRunner
nav: Providers
network: true
overview: 'KeyRunner publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Client, API Testing, Developer Tools, Local-First, and Mock Server.


  KeyRunner''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Keyrunner Plans Pricing
  plan_count: 3
  slug: keyrunner-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Keyrunner Rate Limits
  slug: keyrunner-rate-limits
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keyrunner/refs/heads/main/screenshots/keyrunner-2026-06-20T184014.png
security:
- kind: domain-security
  name: Keyrunner Domain Security
  slug: keyrunner-domain-security
  summary_line: TLSv1.3 · DMARC
slug: keyrunner
tags:
- API Client
- API Testing
- Developer Tools
- Local-First
- Mock Server
- Secret Management
website: https://keyrunner.app/
---
