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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: 'Zilla is a stateless, cloud-native multi-protocol edge and service proxy that enables seamless access to Apache Kafka through HTTP REST, gRPC, SSE, MQTT, and WebSocket protocols. Zilla eliminates the '
  name: Zilla Gateway
  slug: zilla-gateway
- description: 'The Zilla Platform adds an enterprise management layer on top of Zilla Gateway, providing API data products with versioning and rate limits, Kafka governance policies, a self-service developer portal '
  name: Zilla Platform
  slug: zilla-platform
- description: The Zilla MCP Gateway is the AI-facing face of the Zilla engine. It terminates Model Context Protocol Streamable HTTP from an agent and routes each tool call to an upstream by toolkit name, so one aut
  name: Zilla MCP Gateway
  slug: zilla-mcp-gateway
- description: ZillaBase is an event-driven backend framework for the next generation of web, mobile, and AI applications, built on top of Apache Kafka and Zilla to enable real-time, event-sourced application develo
  name: ZillaBase
  slug: zillabase
artifact_total: 27
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/aklivity/zilla/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/aklivity/zilla/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/aklivity/zilla/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/aklivity/zilla/blob/develop/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/aklivity/zilla/blob/develop/.github/CONTRIBUTING.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aklivity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aklivity-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aklivity
- group: company
  title: ''
  type: Website
  url: https://www.aklivity.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aklivity.io/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aklivity.io/latest/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aklivity
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aklivity/zilla
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aklivity.io/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aklivity.io/latest/reference/2.x/
- group: operate
  title: ''
  type: Support
  url: https://docs.aklivity.io/latest/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aklivity.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aklivity.io/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/aklivity-zilla/workspace/aklivity-zilla-quickstart/overview
- group: auth
  title: ''
  type: Security
  url: https://www.aklivity.io/security
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.aklivity.io/latest/deployment/migrating-to-2.x/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aklivity-zilla-engine.schema.json
- group: build
  title: ''
  type: Packages
  url: packages/aklivity-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aklivity-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/aklivity-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aklivity-event-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aklivity-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aklivity-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aklivity-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aklivity-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aklivity-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aklivity-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/aklivity-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aklivity-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aklivity-vocabulary.yaml
- group: design
  title: ''
  type: SpectralRules
  url: rules/aklivity-spectral-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/aklivity-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/aklivity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aklivity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aklivity-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.aklivity.io/blog
created: '2026-01-02'
description: 'Aklivity builds Zilla, a stateless, source-available multi-protocol gateway for event-driven applications and AI agents. Zilla translates HTTP, SSE, WebSocket, MQTT, gRPC and MCP Streamable HTTP to and from Apache Kafka and other backends, configured declaratively in a zilla.yaml or driven directly from an OpenAPI or AsyncAPI document, with no custom code, connectors or separate MQTT broker. The Zilla MCP Gateway compiles OpenAPI specs, Kafka topics, Kafka Connect and schema registries into governed MCP tool sets that agents call through one authenticated endpoint. The Zilla Console adds an API and data-product catalog, a self-service developer portal, governance, audit and RBAC. Aklivity is a software vendor rather than a service operator: every Zilla runs inside the customer''s own infrastructure, so there is no hosted Aklivity API and no Aklivity-issued credential.'
features:
- description: Translates HTTP REST, gRPC, MQTT, SSE, and WebSocket protocols directly to Kafka topics without custom code, connectors, or middleware.
  name: Multi-Protocol Kafka Access
- description: Define gateways and protocol mappings via YAML configuration or AsyncAPI specifications, then deploy with Docker, Helm, or native binaries.
  name: Declarative Configuration
- description: Built-in JWT token validation, TLS termination, and Kafka SASL support for securing API access to Kafka clusters.
  name: JWT Authentication and TLS
- description: SIMD-optimized runtime schema validation for JSON, Avro, and Protobuf via Confluent Schema Registry or AWS Glue Schema Registry.
  name: Schema Validation
- description: Metrics and logs exported to Prometheus and OpenTelemetry for unified visibility across Kafka API traffic.
  name: Observability
- description: Topic naming policies, runtime enforcement, schema compliance rules, and API data product versioning with rate limits via Zilla Platform.
  name: Kafka Governance
- description: API key and certificate management self-service portal for Kafka consumers and producers via Zilla Platform.
  name: Self-Service Developer Portal
- description: PII classification and field-level encryption for sensitive data in Kafka messages via Zilla Platform.
  name: Field-Level Encryption
finops:
- name: Aklivity Finops
  service_category: API
  slug: aklivity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aklivity.png
json_schemas:
- name: Namespace
  property_count: 7
  slug: aklivity-zilla-engine.schema
jsonld:
- class_count: 2
  name: Aklivity Context
  property_count: 7
  slug: aklivity-context
layout: provider
modified: '2026-08-30'
name: Aklivity
nav: Providers
network: true
overview: 'Aklivity publishes 1 API on the [APIs.io](https://apis.io/) network: Zilla Gateway. Tagged areas include AI Gateway, API Gateway, Agent Infrastructure, Apache Kafka, and AsyncAPI.


  The Aklivity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aklivity''s developer surface includes documentation, getting-started guide, pricing, API reference, support, authentication, sandbox, and 35 more developer resources.'
plans:
- name: Aklivity Plans Pricing
  plan_count: 3
  slug: aklivity-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Aklivity Rate Limits
  slug: aklivity-rate-limits
rules:
- effective_rule_count: 11
  extends: []
  name: Aklivity API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: aklivity-spectral-rules
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 79.0
    catalog_earned_first_party: 12.0
    catalog_gap: 36.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 72.7
    contract_quality: 14.7
    developer_ergonomics: 69.0
    discoverability: 64.8
    governance: 72.7
    operational_transparency: 36.8
  previous_composite: 51.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: unknown
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aklivity/refs/heads/main/screenshots/aklivity-2026-06-20T171459.png
security:
- kind: authentication
  name: Aklivity Authentication
  slug: aklivity-authentication
  summary_line: 9 schemes
- kind: domain-security
  name: Aklivity Domain Security
  slug: aklivity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aklivity Vulnerability Disclosure
  slug: aklivity-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: aklivity
tags:
- AI Gateway
- API Gateway
- Agent Infrastructure
- Apache Kafka
- AsyncAPI
- Event-Driven
- IoT
- Kafka Proxy
- MCP
- Multi-Protocol
- Open-Source
- Real-Time
use_cases:
- description: Expose Kafka topics as REST API endpoints, allowing any HTTP client to produce and consume Kafka messages without Kafka client libraries.
  name: HTTP to Kafka REST API
- description: Connect IoT devices using MQTT protocol directly to Kafka topics, eliminating the need for a separate MQTT broker.
  name: IoT MQTT to Kafka
- description: Route gRPC calls from microservices to Kafka topics for event-driven inter-service communication.
  name: gRPC to Kafka
- description: Platform teams build internal developer portals for Kafka access with governance, rate limiting, and self-service API key management.
  name: Kafka Self-Service Platform
- description: Enterprises expose Kafka event streams to external partners via secured, rate-limited REST or SSE APIs.
  name: Event-Driven Partner Integration
- description: Financial institutions distribute real-time market data and trade events via secured Kafka API gateways.
  name: Financial Services Data Distribution
website: https://www.aklivity.io/
---
