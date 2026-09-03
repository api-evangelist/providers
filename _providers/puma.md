---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Puma Agentic Access
  operation_count: 10
  slug: puma-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- description: Puma ships with an optional control/status HTTP application that can be bound to a local port or Unix socket and queried for runtime statistics (busy threads, worker status, backlog) and lifecycle con
  name: Puma Control/Status Application
  slug: control-app
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Gc API from Puma — 1 operation(s) for gc.
  name: Puma Gc API
  slug: puma-gc-api
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Gc Stats API from Puma — 1 operation(s) for gc stats.
  name: Puma Gc Stats API
  slug: puma-gc-stats-api
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Halt API from Puma — 1 operation(s) for halt.
  name: Puma Halt API
  slug: puma-halt-api
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Phased Restart API from Puma — 1 operation(s) for phased restart.
  name: Puma Phased Restart API
  slug: puma-phased-restart-api
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Refork API from Puma — 1 operation(s) for refork.
  name: Puma Refork API
  slug: puma-refork-api
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Reload Worker Directory API from Puma — 1 operation(s) for reload worker directory.
  name: Puma Reload Worker Directory API
  slug: puma-reload-worker-directory-api
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Restart API from Puma — 1 operation(s) for restart.
  name: Puma Restart API
  slug: puma-restart-api
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Stats API from Puma — 1 operation(s) for stats.
  name: Puma Stats API
  slug: puma-stats-api
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Stop API from Puma — 1 operation(s) for stop.
  name: Puma Stop API
  slug: puma-stop-api
- baseURL: http://127.0.0.1:9293
  baseurl_source: declared
  description: The Thread Backtraces API from Puma — 1 operation(s) for thread backtraces.
  name: Puma Thread Backtraces API
  slug: puma-thread-backtraces-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Puma Control/Status Application Gc API
  slug: open-puma-gc-api
- collection_type: open
  name: Puma Control/Status Application Gc Gc Stats API
  slug: open-puma-gc-stats-api
- collection_type: open
  name: Puma Control/Status Application Gc Halt API
  slug: open-puma-halt-api
- collection_type: open
  name: Puma Control/Status Application Gc Phased Restart API
  slug: open-puma-phased-restart-api
- collection_type: open
  name: Puma Control/Status Application Gc Refork API
  slug: open-puma-refork-api
- collection_type: open
  name: Puma Control/Status Application Gc Reload Worker Directory API
  slug: open-puma-reload-worker-directory-api
- collection_type: open
  name: Puma Control/Status Application Gc Restart API
  slug: open-puma-restart-api
- collection_type: open
  name: Puma Control/Status Application Gc Stats API
  slug: open-puma-stats-api
- collection_type: open
  name: Puma Control/Status Application Gc Stop API
  slug: open-puma-stop-api
- collection_type: open
  name: Puma Control/Status Application Gc Thread Backtraces API
  slug: open-puma-thread-backtraces-api
- collection_type: open
  name: Puma Control/Status Application API
  slug: open-puma
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/puma/puma/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/puma/puma/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/puma/puma/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/puma/puma/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/puma-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/puma-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/puma-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/puma
- group: company
  title: ''
  type: Website
  url: https://puma.io
- group: docs
  title: ''
  type: Documentation
  url: https://puma.io/puma/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/puma
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/puma/puma
- group: other
  title: ''
  type: RubyGems
  url: https://rubygems.org/gems/puma
- group: operate
  title: ''
  type: Issues
  url: https://github.com/puma/puma/issues
- group: operate
  title: ''
  type: Forums
  url: https://github.com/puma/puma/discussions
- group: commercial
  title: ''
  type: License
  url: https://github.com/puma/puma/blob/master/LICENSE
created: '2026-05-11'
description: Puma is a simple, fast, multi-threaded, and highly parallel HTTP 1.1 server for Ruby/Rack applications. It is the most popular Ruby web server and the default server for Ruby on Rails, supporting SSL, zero-downtime rolling restarts, and a built-in request bufferer. Puma is an open-source application server and not a hosted service, so it does not expose a public REST API; integration is through configuration, Rack middleware, and the Puma control application server.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/puma.png
layout: provider
modified: '2026-05-11'
name: Puma
nav: Providers
network: true
overview: 'Puma publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Gc API, Gc Stats API, Halt API, and 7 more. Tagged areas include Web Server, Ruby, Rack, Application Server, and HTTP.


  Puma''s developer surface includes authentication, documentation, and 14 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/puma/refs/heads/main/screenshots/puma-2026-06-20T192302.png
security:
- kind: authentication
  name: Puma Authentication
  slug: puma-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Puma Domain Security
  slug: puma-domain-security
  summary_line: TLSv1.3
slug: puma
tags:
- Web Server
- Ruby
- Rack
- Application Server
- HTTP
- Open-Source
website: https://puma.io
---
