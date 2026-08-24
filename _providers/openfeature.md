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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Openfeature Agentic Access
  operation_count: 2
  slug: openfeature-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: '**Required**: Core APIs to implement to support OFREP. *This is the minimum set of APIs required for a flag management system to be OFREP compatible.*'
  name: OpenFeature OFREP Core API
  slug: openfeature-ofrep-core-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenFeature Remote Evaluation Protocol (OFREP) OFREP Core API
  slug: open-openfeature-ofrep-core-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openfeature-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openfeature-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openfeature-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openfeature
- group: docs
  title: ''
  type: Documentation
  url: https://openfeature.dev/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/open-feature
- group: company
  title: ''
  type: Blog
  url: https://openfeature.dev/blog/rss.xml
created: '2026-03-16'
description: OpenFeature is a CNCF incubating open specification for feature flag management. It provides a vendor-agnostic API for evaluating feature flags, enabling developers to use a consistent interface regardless of the underlying feature flag provider. OpenFeature offers SDKs in multiple languages including Go, Java, JavaScript, Python, PHP, and .NET with a provider-based architecture.
finops:
- name: Openfeature Finops
  service_category: API
  slug: openfeature-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openfeature.png
layout: provider
modified: '2026-05-19'
name: OpenFeature
nav: Providers
network: true
overview: 'OpenFeature publishes 1 API on the [APIs.io](https://apis.io/) network: OFREP Core API. Tagged areas include Cloud-Native, Feature Flags, Feature Management, Incubating, and SDK.


  OpenFeature''s developer surface includes authentication, documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Openfeature Plans Pricing
  plan_count: 3
  slug: openfeature-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Openfeature Rate Limits
  slug: openfeature-rate-limits
score:
  band: thin
  composite: 31.3
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 60.1
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openfeature/refs/heads/main/screenshots/openfeature-2026-06-20T191000.png
security:
- kind: authentication
  name: Openfeature Authentication
  slug: openfeature-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Openfeature Domain Security
  slug: openfeature-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openfeature
tags:
- Cloud-Native
- Feature Flags
- Feature Management
- Incubating
- SDK
- Specification
website: https://openfeature.dev
---
