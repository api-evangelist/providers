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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 12
  name: Mockserver Agentic Access
  operation_count: 20
  slug: mockserver-agentic-access
  summary_line: 20 operations · 20 acting · 12 human-in-the-loop
api_count: 3
apis:
- description: Manage state or process (both MockServer & MockServer Proxy)
  name: MockServer control API
  slug: mockserver-control-api
- description: Create or update expectations - updates if the id matches an existing expectations (only supported by MockServer)
  name: MockServer expectation API
  slug: mockserver-expectation-api
- description: Verify requests (both MockServer & MockServer Proxy)
  name: MockServer verify API
  slug: mockserver-verify-api
artifact_total: 10
collections:
- collection_type: open
  name: MockServer API
  slug: open-mockserver-openapi-original
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mockserver-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mockserver-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mockserver-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mockserver
- group: company
  title: ''
  type: Website
  url: https://www.mock-server.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mock-server.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mock-server
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mock-server.com/mock_server/getting_started.html
- group: operate
  title: ''
  type: Issues
  url: https://github.com/mock-server/mockserver/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/mock-server/mockserver/blob/master/LICENSE.md
- group: agent
  title: ''
  type: LlmsText
  url: https://mock-server.com/llms.txt
created: '2025-01-08'
description: MockServer enables easy mocking of any system you integrate with via HTTP or HTTPS (e.g. services, web sites, etc) with clients in Java, JavaScript, and Ruby and a simple REST API. MockServer can be used to mock APIs that are not yet fully developed, isolate the system under test for reliable testing, simulate slow or faulty endpoints, and record/replay requests.
finops:
- name: Mockserver Finops
  service_category: API
  slug: mockserver-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mockserver.png
layout: provider
modified: '2026-05-19'
name: MockServer
nav: Providers
network: true
overview: 'MockServer publishes 3 APIs on the [APIs.io](https://apis.io/) network: control API, expectation API, and verify API. Tagged areas include Mocking, Mock Server, Testing, Service Virtualization, and HTTP.


  MockServer''s developer surface includes documentation, getting-started guide, and 9 more developer resources.'
plans:
- name: Mockserver Plans Pricing
  plan_count: 3
  slug: mockserver-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Mockserver Rate Limits
  slug: mockserver-rate-limits
score:
  band: thin
  composite: 32.0
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 35.6
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mockserver/refs/heads/main/screenshots/mockserver-2026-06-20T185638.png
security:
- kind: domain-security
  name: Mockserver Domain Security
  slug: mockserver-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mockserver Vulnerability Disclosure
  slug: mockserver-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mockserver
tags:
- Mocking
- Mock Server
- Testing
- Service Virtualization
- HTTP
- REST API
- Platform
website: https://www.mock-server.com/
---
