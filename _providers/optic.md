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
- description: The Optic CLI provides OpenAPI diffing, linting, and breaking change detection from the command line, comparing two versions of an OpenAPI specification using behavior-aware diffing and applying style
  name: Optic CLI
  slug: optic-cli
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useoptic
- group: company
  title: ''
  type: Website
  url: https://www.useoptic.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.useoptic.com/docs
- group: other
  title: ''
  type: Core Concepts
  url: https://www.useoptic.com/docs/core-concepts
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/opticdev/optic
created: '2026-03-25'
description: Optic is an open source tool for OpenAPI linting, diffing, and testing that helps prevent breaking changes, publish accurate documentation, and improve API design through behavior-aware specification comparison and forwards-only governance.
finops:
- name: Optic Finops
  service_category: API
  slug: optic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optic.png
layout: provider
modified: '2026-03-26'
name: Optic
nav: Providers
network: true
overview: 'Optic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Governance, Breaking Changes, Contract Testing, Diff, and Linting.


  Optic''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Optic Plans Pricing
  plan_count: 3
  slug: optic-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Optic Rate Limits
  slug: optic-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Optic Domain Security
  slug: optic-domain-security
  summary_line: DMARC
- kind: vulnerability-disclosure
  name: Optic Vulnerability Disclosure
  slug: optic-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: optic
tags:
- API Governance
- Breaking Changes
- Contract Testing
- Diff
- Linting
- OpenAPI
- Testing
website: https://www.useoptic.com
---
