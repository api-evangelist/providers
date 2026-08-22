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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Http Toolkit Agentic Access
  operation_count: 10
  slug: http-toolkit-agentic-access
  summary_line: 10 operations · 4 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: HTTP client request sending through the proxy
  name: HTTP Toolkit client API
  slug: http-toolkit-client-api
- description: Proxy configuration and network settings
  name: HTTP Toolkit config API
  slug: http-toolkit-config-api
- description: Interceptor management for various environments and applications
  name: HTTP Toolkit interceptors API
  slug: http-toolkit-interceptors-api
- description: Server lifecycle and version management
  name: HTTP Toolkit server API
  slug: http-toolkit-server-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HTTP Toolkit Server client API
  slug: open-http-toolkit-client-api
- collection_type: open
  name: HTTP Toolkit Server client config API
  slug: open-http-toolkit-config-api
- collection_type: open
  name: HTTP Toolkit Server client interceptors API
  slug: open-http-toolkit-interceptors-api
- collection_type: open
  name: HTTP Toolkit client server API
  slug: open-http-toolkit-server-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/httptoolkit/httptoolkit-server/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/httptoolkit/httptoolkit-server/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/httptoolkit/httptoolkit-server/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/http-toolkit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/http-toolkit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/http-toolkit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://httptoolkit.com
- group: docs
  title: ''
  type: Documentation
  url: https://httptoolkit.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/httptoolkit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/http-toolkit
- group: company
  title: ''
  type: Blog
  url: https://httptoolkit.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://httptoolkit.com/pricing/
- group: other
  title: ''
  type: X
  url: https://twitter.com/httptoolkit
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/httptoolkit.com
- group: company
  title: ''
  type: Mastodon
  url: https://mastodon.social/@httptoolkit
- group: commercial
  title: ''
  type: Plans
  url: plans/http-toolkit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/http-toolkit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/http-toolkit-finops.yml
created: '2026-06-13'
description: HTTP Toolkit is a beautiful, cross-platform, and open-source tool for debugging, testing, and building with HTTP(S) on Windows, Linux, and Mac. It provides a REST API for intercepting HTTP/HTTPS traffic, inspecting requests and responses, automated mocking and rewriting of API traffic, and integrations with Docker, Android, Python, Ruby, Java, Electron, and JavaScript development workflows.
examples:
- key_count: 4
  name: Activate Interceptor
  slug: activate-interceptor
- key_count: 4
  name: Get Interceptors
  slug: get-interceptors
- key_count: 4
  name: Get Version
  slug: get-version
- key_count: 4
  name: Send Request
  slug: send-request
finops:
- name: Http Toolkit Finops
  service_category: ''
  slug: http-toolkit-finops
graphqls:
- description: HTTP Toolkit GraphQL API
  name: HTTP Toolkit GraphQL Schema
  slug: http-toolkit-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/http-toolkit.png
json_schemas:
- name: HTTP Toolkit Interceptor
  property_count: 5
  slug: http-toolkit-interceptor
- name: HTTP Toolkit Proxy Configuration
  property_count: 5
  slug: http-toolkit-proxy-config
- name: HTTP Toolkit Send Request
  property_count: 2
  slug: http-toolkit-send-request
jsonld:
- class_count: 10
  name: Http Toolkit Context
  property_count: 32
  slug: http-toolkit-context
layout: provider
modified: '2026-06-13'
name: HTTP Toolkit
nav: Providers
network: true
overview: 'HTTP Toolkit publishes 4 APIs on the [APIs.io](https://apis.io/) network, including client API, config API, interceptors API, and 1 more. Tagged areas include HTTP, HTTPS, Debugging, Proxy, and Interception.


  The HTTP Toolkit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HTTP Toolkit''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Http Toolkit Plans Pricing
  plan_count: 3
  slug: http-toolkit-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Http Toolkit Rate Limits
  slug: http-toolkit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: HTTP Toolkit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: http-toolkit-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.8
  delta: -5.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 62.5
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/http-toolkit/refs/heads/main/screenshots/http-toolkit-2026-06-20T182918.png
security:
- kind: authentication
  name: Http Toolkit Authentication
  slug: http-toolkit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Http Toolkit Domain Security
  slug: http-toolkit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: http-toolkit
tags:
- HTTP
- HTTPS
- Debugging
- Proxy
- Interception
- Mocking
- Testing
- Developer Tools
- Open Source
website: https://httptoolkit.com
---
