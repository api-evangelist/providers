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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: 'Zilla is a stateless, cloud-native multi-protocol edge and service proxy that enables seamless access to Apache Kafka through HTTP REST, gRPC, SSE, MQTT, and WebSocket protocols. Zilla eliminates the '
  name: Zilla Gateway
  slug: zilla-gateway
- description: 'The Zilla Platform adds an enterprise management layer on top of Zilla Gateway, providing API data products with versioning and rate limits, Kafka governance policies, a self-service developer portal '
  name: Zilla Platform
  slug: zilla-platform
- description: ZillaBase is an event-driven backend framework for the next generation of web, mobile, and AI applications, built on top of Apache Kafka and Zilla to enable real-time, event-sourced application develo
  name: ZillaBase
  slug: zillabase
artifact_total: 24
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
  url: https://docs.aklivity.io/zilla/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aklivity.io/zilla/next/getting-started/quickstart/
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
- group: company
  title: ''
  type: Blog
  url: https://www.aklivity.io/blog
created: '2026-01-02'
description: Aklivity provides the Zilla multi-protocol edge and service proxy for event-driven architectures, enabling seamless integration between web apps, IoT clients, and microservices with Apache Kafka via declaratively defined, stateless APIs. Zilla supports HTTP, gRPC, MQTT, SSE, and WebSocket protocols, translating them to and from Kafka without custom code or connectors. The Zilla Platform adds enterprise governance, observability, and self-service access management for Kafka deployments.
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
jsonld:
- class_count: 2
  name: Aklivity Context
  property_count: 7
  slug: aklivity-context
layout: provider
modified: '2026-04-19'
name: Aklivity
nav: Providers
network: true
overview: 'Aklivity publishes 1 API on the [APIs.io](https://apis.io/) network: Zilla Gateway. Tagged areas include API Gateway, Apache Kafka, Event-Driven, IoT, and Kafka Proxy.


  The Aklivity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aklivity''s developer surface includes documentation, getting-started guide, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Aklivity Plans Pricing
  plan_count: 3
  slug: aklivity-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Aklivity Rate Limits
  slug: aklivity-rate-limits
rules:
- name: Aklivity API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: aklivity-spectral-rules
score:
  band: thin
  composite: 39.4
  delta: -4.4
  facets:
    commercial_clarity: 26.3
    contract_quality: 59.7
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 27.1
    operational_transparency: 39.5
  previous_composite: 43.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aklivity/refs/heads/main/screenshots/aklivity-2026-06-20T171459.png
security:
- kind: domain-security
  name: Aklivity Domain Security
  slug: aklivity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aklivity Vulnerability Disclosure
  slug: aklivity-vulnerability-disclosure
  summary_line: disclosure policy published
slug: aklivity
tags:
- API Gateway
- Apache Kafka
- Event-Driven
- IoT
- Kafka Proxy
- Multi-Protocol
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
