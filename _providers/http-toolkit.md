---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Http Toolkit Agentic Access
  operation_count: 10
  slug: http-toolkit-agentic-access
  summary_line: 10 operations · 4 acting · 1 human-in-the-loop
api_count: 4
apis:
- baseURL: http://localhost:45456
  baseurl_source: declared
  description: HTTP client request sending through the proxy
  name: HTTP Toolkit client API
  slug: http-toolkit-client-api
- baseURL: http://localhost:45456
  baseurl_source: declared
  description: Proxy configuration and network settings
  name: HTTP Toolkit config API
  slug: http-toolkit-config-api
- baseURL: http://localhost:45456
  baseurl_source: declared
  description: Interceptor management for various environments and applications
  name: HTTP Toolkit interceptors API
  slug: http-toolkit-interceptors-api
- baseURL: http://localhost:45456
  baseurl_source: declared
  description: Server lifecycle and version management
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
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 64.3
    catalog_earned_first_party: 0.0
    catalog_gap: 50.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 62.2
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
- Open-Source
website: https://httptoolkit.com
---
