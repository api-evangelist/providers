---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Synapse Agentic Access
  operation_count: 18
  slug: synapse-agentic-access
  summary_line: 18 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: API for integrating application services (bridges and bots) with the Matrix homeserver. Allows third-party applications to handle namespaced user IDs and room aliases, enabling Matrix bridges for IRC,
  name: Synapse Application Service API
  slug: synapse-application-service-api
- baseURL: https://matrix.example.com/_matrix/client
  baseurl_source: declared
  description: Federation management
  name: Synapse Federation API
  slug: synapse-federation-api
- baseURL: https://matrix.example.com/_matrix/client
  baseurl_source: declared
  description: Media file administration
  name: Synapse Media API
  slug: synapse-media-api
- baseURL: https://matrix.example.com/_matrix/client
  baseurl_source: declared
  description: User registration and tokens
  name: Synapse Registration API
  slug: synapse-registration-api
- baseURL: https://matrix.example.com/_matrix/client
  baseurl_source: declared
  description: Event and user reports
  name: Synapse Reports API
  slug: synapse-reports-api
- baseURL: https://matrix.example.com/_matrix/client
  baseurl_source: declared
  description: Room administration and membership
  name: Synapse Rooms API
  slug: synapse-rooms-api
- baseURL: https://matrix.example.com/_matrix/client
  baseurl_source: declared
  description: Server information and background updates
  name: Synapse Server API
  slug: synapse-server-api
- baseURL: https://matrix.example.com/_matrix/client
  baseurl_source: declared
  description: Server usage statistics
  name: Synapse Statistics API
  slug: synapse-statistics-api
- baseURL: https://matrix.example.com/_matrix/client
  baseurl_source: declared
  description: User account management
  name: Synapse Users API
  slug: synapse-users-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Synapse Admin API
  slug: open-synapse-admin-api
- collection_type: open
  name: Synapse Admin Federation API
  slug: open-synapse-federation-api
- collection_type: open
  name: Synapse Admin Federation Media API
  slug: open-synapse-media-api
- collection_type: open
  name: Synapse Admin Federation Registration API
  slug: open-synapse-registration-api
- collection_type: open
  name: Synapse Admin Federation Reports API
  slug: open-synapse-reports-api
- collection_type: open
  name: Synapse Admin Federation Rooms API
  slug: open-synapse-rooms-api
- collection_type: open
  name: Synapse Admin Federation Server API
  slug: open-synapse-server-api
- collection_type: open
  name: Synapse Admin Federation Statistics API
  slug: open-synapse-statistics-api
- collection_type: open
  name: Synapse Admin Federation Users API
  slug: open-synapse-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/synapse-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/synapse-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/synapse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synapse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synapse-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synapsepay
- group: build
  title: ''
  type: GitHub
  url: https://github.com/matrix-org/synapse
- group: build
  title: ''
  type: GitHub
  url: https://github.com/element-hq/synapse
- group: docs
  title: ''
  type: Documentation
  url: https://matrix-org.github.io/synapse/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://matrix-org.github.io/synapse/latest/setup/installation.html
- group: auth
  title: ''
  type: Authentication
  url: https://matrix-org.github.io/synapse/latest/usage/configuration/config_documentation.html#authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://matrix-org.github.io/synapse/latest/usage/configuration/config_documentation.html#ratelimiting
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/matrix-org/synapse/blob/develop/CHANGES.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/matrix-org/synapse/blob/develop/LICENSE
- group: other
  title: ''
  type: Docker
  url: https://hub.docker.com/r/matrixdotorg/synapse
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/matrix-synapse/
- group: other
  title: ''
  type: Matrix Spec
  url: https://spec.matrix.org/latest/
- group: company
  title: ''
  type: Blog
  url: https://www.matrix.org/blog/feed/
created: '2026-05-03'
description: Synapse is the reference Matrix homeserver implementation maintained by Element (formerly by the Matrix.org Foundation). Written in Python and Rust, it implements the Matrix open standard for secure, decentralized real-time communication. Synapse powers thousands of deployments worldwide and provides Client-Server, Server-Server (federation), Application Service, Identity Service, and Admin APIs. Since version 1.99, maintained by Element under AGPL-3.0.
examples:
- key_count: 5
  name: Synapse List Users Example
  slug: synapse-list-users-example
finops:
- name: Synapse Finops
  service_category: Open-Source Messaging Infrastructure
  slug: synapse-finops
image: https://matrix.org/images/matrix-logo.svg
json_schemas:
- name: Synapse User
  property_count: 12
  slug: synapse-user
json_structures:
- name: Synapse Room Structure
  property_count: 0
  slug: synapse-room-structure
jsonld:
- class_count: 0
  name: Synapse Context
  property_count: 31
  slug: synapse-context
layout: provider
modified: '2026-05-19'
name: Synapse
nav: Providers
network: true
overview: 'Synapse publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Federation API, Media API, Registration API, and 5 more. Tagged areas include Chat, Collaboration, Decentralized, Federation, and Matrix.


  The Synapse catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Synapse''s developer surface includes authentication, GitHub presence, documentation, getting-started guide, changelog, engineering blog, and 12 more developer resources.'
plans:
- name: Synapse Plans Pricing
  plan_count: 2
  slug: synapse-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 11
  name: Synapse Rate Limits
  slug: synapse-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Synapse API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: synapse-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Synapse API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 4
  slug: synapse-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 57.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 58.3
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 28.9
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synapse/refs/heads/main/screenshots/synapse-2026-06-20T194821.png
security:
- kind: authentication
  name: Synapse Authentication
  slug: synapse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Synapse Domain Security
  slug: synapse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Synapse Vulnerability Disclosure
  slug: synapse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: synapse
tags:
- Chat
- Collaboration
- Decentralized
- Federation
- Matrix
- Messaging
- Open-Source
- Real-Time
---
