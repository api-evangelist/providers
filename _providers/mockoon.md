---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Mockoon Agentic Access
  operation_count: 3
  slug: mockoon-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- description: Mockoon ships as a desktop application, a CLI, and a serverless package for designing and running mock REST APIs. Mocks are configured in Mockoon and exposed locally as HTTP endpoints; the tool itself
  name: Mockoon
  slug: mockoon
- description: Inspect and reset data buckets defined in the mock environment.
  name: Mockoon Data Buckets API
  slug: mockoon-data-buckets-api
artifact_total: 9
collections:
- collection_type: open
  name: Mockoon Admin API
  slug: open-mockoon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mockoon-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mockoon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mockoon-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mockoon
- group: company
  title: ''
  type: Website
  url: https://mockoon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mockoon.com/docs/latest/about/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mockoon
- group: learn
  title: ''
  type: Tutorials
  url: https://mockoon.com/tutorials/
- group: company
  title: ''
  type: Blog
  url: https://mockoon.com/blog/
- group: operate
  title: ''
  type: Issues
  url: https://github.com/mockoon/mockoon/issues
- group: agent
  title: ''
  type: LlmsText
  url: https://mockoon.com/llms.txt
created: '2025-01-08'
description: Mockoon is the easiest and quickest way to design and run mock REST APIs. Available as a free, open-source desktop application and CLI, it lets developers build, share, and serve realistic mock endpoints locally, in CI, or in containers. No remote deployment, no account required.
finops:
- name: Mockoon Finops
  service_category: API
  slug: mockoon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mockoon.png
layout: provider
modified: '2026-04-28'
name: Mockoon
nav: Providers
network: true
overview: 'Mockoon publishes 1 API on the [APIs.io](https://apis.io/) network: Data Buckets API. Tagged areas include Mock Servers, Mocking, Testing, REST API, and Desktop.


  Mockoon''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Mockoon Plans Pricing
  plan_count: 3
  slug: mockoon-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Mockoon Rate Limits
  slug: mockoon-rate-limits
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 50.4
    developer_ergonomics: 10.9
    discoverability: 60.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mockoon/refs/heads/main/screenshots/mockoon-2026-06-20T185637.png
security:
- kind: domain-security
  name: Mockoon Domain Security
  slug: mockoon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Mockoon Trust Center
  slug: mockoon-trust-center
  summary_line: PCI DSS, GDPR
slug: mockoon
tags:
- Mock Servers
- Mocking
- Testing
- REST API
- Desktop
- CLI
- Platform
- Open Source
website: https://mockoon.com/
---
