---
access_model:
  confidence: high
  label: Free and keyless — no account required
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-07'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Asyncapi Agentic Access
  operation_count: 7
  slug: asyncapi-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- description: The AsyncAPI Specification is an open standard for describing asynchronous and event-driven APIs. It provides a machine-readable format for defining messaging interfaces across protocols like Kafka, M
  name: AsyncAPI Specification
  slug: asyncapi-spec
- baseURL: https://api.asyncapi.com/v1
  baseurl_source: declared
  description: 'The AsyncAPI Server API is the only callable HTTP API the AsyncAPI Initiative operates. It exposes the official AsyncAPI toolchain — validate, parse, convert, generate, bundle and diff — over HTTP at '
  name: AsyncAPI Server API
  slug: asyncapi-server-api
- baseURL: https://api.asyncapi.com/v1
  baseurl_source: declared
  description: The Bundle API from AsyncAPI — 1 operation(s) for bundle.
  name: AsyncAPI Bundle API
  slug: asyncapi-bundle-api
- baseURL: https://api.asyncapi.com/v1
  baseurl_source: declared
  description: The Convert API from AsyncAPI — 1 operation(s) for convert.
  name: AsyncAPI Convert API
  slug: asyncapi-convert-api
- baseURL: https://api.asyncapi.com/v1
  baseurl_source: declared
  description: The Diff API from AsyncAPI — 1 operation(s) for diff.
  name: AsyncAPI Diff API
  slug: asyncapi-diff-api
- baseURL: https://api.asyncapi.com/v1
  baseurl_source: declared
  description: The Generate API from AsyncAPI — 1 operation(s) for generate.
  name: AsyncAPI Generate API
  slug: asyncapi-generate-api
- baseURL: https://api.asyncapi.com/v1
  baseurl_source: declared
  description: The Help API from AsyncAPI — 1 operation(s) for help.
  name: AsyncAPI Help API
  slug: asyncapi-help-api
- baseURL: https://api.asyncapi.com/v1
  baseurl_source: declared
  description: The Parse API from AsyncAPI — 1 operation(s) for parse.
  name: AsyncAPI Parse API
  slug: asyncapi-parse-api
- baseURL: https://api.asyncapi.com/v1
  baseurl_source: declared
  description: The Validate API from AsyncAPI — 1 operation(s) for validate.
  name: AsyncAPI Validate API
  slug: asyncapi-validate-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AsyncAPI Server Bundle API
  slug: open-asyncapi-bundle-api
- collection_type: open
  name: AsyncAPI Server Bundle Convert API
  slug: open-asyncapi-convert-api
- collection_type: open
  name: AsyncAPI Server Bundle Diff API
  slug: open-asyncapi-diff-api
- collection_type: open
  name: AsyncAPI Server Bundle Generate API
  slug: open-asyncapi-generate-api
- collection_type: open
  name: AsyncAPI Server Bundle Help API
  slug: open-asyncapi-help-api
- collection_type: open
  name: AsyncAPI Server Bundle Parse API
  slug: open-asyncapi-parse-api
- collection_type: open
  name: AsyncAPI Server Bundle Validate API
  slug: open-asyncapi-validate-api
- collection_type: open
  name: AsyncAPI Server API
  slug: open-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.asyncapi.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/asyncapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asyncapi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/asyncapi
- group: start
  title: AsyncAPI Website
  type: Portal
  url: https://www.asyncapi.com/
- group: docs
  title: Documentation
  type: Documentation
  url: https://www.asyncapi.com/docs
- group: build
  title: AsyncAPI GitHub Organization
  type: GitHubOrganization
  url: https://github.com/asyncapi
- group: company
  title: Blog
  type: Blog
  url: https://www.asyncapi.com/blog
- group: build
  title: First-party packages and SDKs
  type: Packages
  url: packages/asyncapi-packages.yml
- group: build
  title: AsyncAPI client libraries and tooling packages
  type: SDKs
  url: packages/asyncapi-packages.yml
- group: build
  title: AsyncAPI CLI command surface
  type: CLI
  url: cli/asyncapi-cli.yml
- group: design
  title: Embeddable AsyncAPI document renderers
  type: Components
  url: components/asyncapi-components.yml
- group: auth
  title: Authentication profile (keyless public API)
  type: Authentication
  url: authentication/asyncapi-authentication.yml
- group: design
  title: API conventions and runtime semantics
  type: Conventions
  url: conventions/asyncapi-conventions.yml
- group: design
  title: Problem-details error catalog
  type: ErrorCatalog
  url: errors/asyncapi-problem-types.yml
- group: design
  title: Versioning and lifecycle
  type: Lifecycle
  url: lifecycle/asyncapi-lifecycle.yml
- group: operate
  title: Specification and CLI release history
  type: ChangeLog
  url: changelog/asyncapi-changelog.yml
- group: design
  title: Standards conformance
  type: Conformance
  url: conformance/asyncapi-conformance.yml
- group: design
  title: Server API data model
  type: DataModel
  url: data-model/asyncapi-data-model.yml
- group: commercial
  title: Plans and pricing (none — open source, no commercial tiers)
  type: Plans
  url: plans/asyncapi-plans-pricing.yml
- group: operate
  title: Rate limits (none published)
  type: RateLimits
  url: rate-limits/asyncapi-rate-limits.yml
- group: start
  title: AsyncAPI Studio and self-hosted API
  type: Sandbox
  url: sandbox/asyncapi-sandbox.yml
- group: start
  title: AsyncAPI Studio
  type: Console
  url: https://studio.asyncapi.com
- group: other
  title: API Evangelist enhancements overlay
  type: Overlay
  url: overlays/asyncapi-server-api-overlay.yaml
- group: agent
  title: llms.txt
  type: LLMsTxt
  url: llms/asyncapi-llms.txt
- group: agent
  title: Packaged agent skills for the AsyncAPI Server API
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: Coordinated vulnerability disclosure
  type: VulnerabilityDisclosure
  url: security/asyncapi-vulnerability-disclosure.yml
- group: auth
  title: AsyncAPI Security Policy
  type: Security
  url: https://github.com/asyncapi/.github/blob/master/SECURITY.md
- group: docs
  title: AsyncAPI Server API reference
  type: APIReference
  url: https://api.asyncapi.com/v1/docs
- group: start
  title: Getting Started
  type: GettingStarted
  url: https://www.asyncapi.com/docs/tutorials/getting-started
- group: operate
  title: Community
  type: Support
  url: https://www.asyncapi.com/community
- group: commercial
  title: LF Projects Terms of Use
  type: TermsOfService
  url: https://lfprojects.org/policies/terms-of-use/
- group: commercial
  title: LF Projects Privacy Policy
  type: PrivacyPolicy
  url: https://lfprojects.org/policies/privacy-policy/
created: '2026-03-16'
description: AsyncAPI is a Linux Foundation project that improves the state of event-driven architectures by providing an open specification and tooling ecosystem for defining asynchronous and event-driven APIs. It enables developers to document, validate, generate code, and manage message-driven APIs across protocols including Kafka, MQTT, WebSocket, AMQP, and others. The AsyncAPI specification serves as the industry standard for describing asynchronous messaging interfaces, similar to how OpenAPI serves REST APIs.
features:
- description: An open specification standard for describing asynchronous and event-driven APIs, supporting multiple messaging protocols including Kafka, MQTT, WebSocket, AMQP, and more.
  name: AsyncAPI Specification
- description: Code and documentation generation tool that uses AsyncAPI definitions to produce boilerplate code, documentation, and other artifacts in multiple programming languages.
  name: AsyncAPI Generator
- description: Command-line interface tool for working with AsyncAPI files including validation, generation, and conversion operations from the terminal.
  name: AsyncAPI CLI
- description: Web-based editor and visualization tool for creating, editing, and previewing AsyncAPI specification documents with real-time validation.
  name: AsyncAPI Studio
- description: Broad protocol support covering Kafka, MQTT, WebSocket, AMQP, NATS, JMS, and other messaging protocols through a unified specification format.
  name: Protocol Support
finops:
- name: Asyncapi Finops
  service_category: API
  slug: asyncapi-finops
- name: Asyncapi Funding
  service_category: ''
  slug: asyncapi-funding
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/asyncapi.png
integrations:
- description: AsyncAPI supports defining Kafka-based event-driven APIs with topic, message schema, and broker configuration documentation.
  name: Apache Kafka
- description: IoT and messaging platforms using MQTT can document their pub/sub interfaces using AsyncAPI specifications for device and service integration.
  name: MQTT Brokers
- description: AsyncAPI CLI integrates into continuous integration pipelines for automated validation and linting of AsyncAPI specification files.
  name: CI/CD Pipelines
layout: provider
modified: '2026-09-06'
name: AsyncAPI
nav: Providers
network: true
overview: 'AsyncAPI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Specification, Server API, Bundle API, and 6 more. Tagged areas include Event-Driven, Linux Foundation, Messaging, Standards, and Specification.


  AsyncAPI''s developer surface includes developer portal, documentation, engineering blog, CLI, authentication, changelog, sandbox, and 26 more developer resources.'
plans:
- name: Asyncapi Plans Pricing
  plan_count: 0
  slug: asyncapi-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Asyncapi Rate Limits
  slug: asyncapi-rate-limits
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 34
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 51.9
    developer_ergonomics: 80.4
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/asyncapi/refs/heads/main/screenshots/asyncapi-2026-06-20T172514.png
security:
- kind: authentication
  name: Asyncapi Authentication
  slug: asyncapi-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Asyncapi Domain Security
  slug: asyncapi-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Asyncapi Vulnerability Disclosure
  slug: asyncapi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: asyncapi
tags:
- Event-Driven
- Linux Foundation
- Messaging
- Standards
- Specification
use_cases:
- description: Development teams use AsyncAPI to create machine-readable documentation for their message-driven APIs, making it easier for consumers to understand and integrate with event streams.
  name: Event-Driven API Documentation
- description: Engineers generate boilerplate code for Kafka consumers, MQTT publishers, and other messaging clients directly from AsyncAPI specifications to accelerate development.
  name: Code Generation for Messaging
- description: Platform teams apply AsyncAPI specifications to enforce standards and governance across microservices architectures using event-driven communication.
  name: API Governance for Event-Driven Systems
website: https://www.asyncapi.com/
---
