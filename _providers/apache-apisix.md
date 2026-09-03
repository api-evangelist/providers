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
- acting_count: 40
  human_in_the_loop: 0
  name: Apache Apisix Agentic Access
  operation_count: 76
  slug: apache-apisix-agentic-access
  summary_line: 76 operations · 40 acting
api_count: 2
apis:
- description: Apache APISIX provides rich traffic management features including load balancing, dynamic upstream configuration, canary releases, circuit breaking, authentication, observability plugins, and more. It
  name: Apache APISIX Gateway
  slug: apache-apisix-gateway
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage consumer groups for shared plugin configurations.
  name: Apache APISIX Consumer Groups API
  slug: apache-apisix-consumer-groups-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage API consumers and their credentials.
  name: Apache APISIX Consumers API
  slug: apache-apisix-consumers-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Runtime diagnostic operations.
  name: Apache APISIX Diagnostics API
  slug: apache-apisix-diagnostics-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage global plugin rules applied to all requests.
  name: Apache APISIX Global Rules API
  slug: apache-apisix-global-rules-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Monitor the health status of upstream nodes.
  name: Apache APISIX Health Check API
  slug: apache-apisix-health-check-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Inspect the runtime configuration of the APISIX instance.
  name: Apache APISIX Introspection API
  slug: apache-apisix-introspection-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage reusable plugin configuration sets.
  name: Apache APISIX Plugin Configs API
  slug: apache-apisix-plugin-configs-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage metadata for individual plugins.
  name: Apache APISIX Plugin Metadata API
  slug: apache-apisix-plugin-metadata-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Query available plugins and their schemas.
  name: Apache APISIX Plugins API
  slug: apache-apisix-plugins-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage Protocol Buffer definition resources.
  name: Apache APISIX Protos API
  slug: apache-apisix-protos-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage HTTP routes that define rules for matching client requests.
  name: Apache APISIX Routes API
  slug: apache-apisix-routes-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Validate resource configurations against APISIX schemas.
  name: Apache APISIX Schema API
  slug: apache-apisix-schema-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage secrets from external secret managers.
  name: Apache APISIX Secrets API
  slug: apache-apisix-secrets-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: The Services API from Apache APISIX — 2 operation(s) for services.
  name: Apache APISIX Services API
  slug: apache-apisix-services-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage SSL/TLS certificate resources.
  name: Apache APISIX SSL API
  slug: apache-apisix-ssl-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage Layer 4 TCP/UDP stream routes.
  name: Apache APISIX Stream Routes API
  slug: apache-apisix-stream-routes-api
- baseURL: http://127.0.0.1:9180/apisix/admin
  baseurl_source: spec
  description: Manage upstream backend service definitions with load balancing.
  name: Apache APISIX Upstreams API
  slug: apache-apisix-upstreams-api
artifact_total: 101
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache APISIX Admin API
  slug: open-apache-apisix-admin-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups API
  slug: open-apache-apisix-consumer-groups-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Consumers API
  slug: open-apache-apisix-consumers-api
- collection_type: open
  name: Apache APISIX Control API
  slug: open-apache-apisix-control-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Diagnostics API
  slug: open-apache-apisix-diagnostics-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Global Rules API
  slug: open-apache-apisix-global-rules-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Health Check API
  slug: open-apache-apisix-health-check-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Introspection API
  slug: open-apache-apisix-introspection-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Plugin Configs API
  slug: open-apache-apisix-plugin-configs-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Plugin Metadata API
  slug: open-apache-apisix-plugin-metadata-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Plugins API
  slug: open-apache-apisix-plugins-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Protos API
  slug: open-apache-apisix-protos-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Routes API
  slug: open-apache-apisix-routes-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Schema API
  slug: open-apache-apisix-schema-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Secrets API
  slug: open-apache-apisix-secrets-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Services API
  slug: open-apache-apisix-services-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups SSL API
  slug: open-apache-apisix-ssl-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Stream Routes API
  slug: open-apache-apisix-stream-routes-api
- collection_type: open
  name: Apache APISIX Admin Consumer Groups Upstreams API
  slug: open-apache-apisix-upstreams-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/apisix/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/apisix/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/apisix/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/apisix/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/apisix/blob/master/LICENSE
- group: auth
  title: ''
  type: Security
  url: https://www.apache.org/security/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-apisix-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-apisix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-apisix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-apisix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-apisix
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/apisix
- group: docs
  title: ''
  type: Documentation
  url: https://apisix.apache.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://apisix.apache.org/docs/apisix/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://apisix.apache.org/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/apache/apisix/releases
- group: operate
  title: ''
  type: Support
  url: https://apisix.apache.org/docs/general/community/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/apache-apisix
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/route.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/upstream.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/service.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/consumer.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ssl.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/global-rule.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/plugin-config.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/consumer-group.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stream-route.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/secret.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-apisix-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-apisix-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-apisix-vocabulary.yaml
created: '2026-03-18'
description: Apache APISIX is a dynamic, real-time, high-performance cloud-native API gateway built on NGINX and etcd, developed by the Apache Software Foundation. It supports Lua and multi-language plugins for traffic management, authentication, observability, and security. APISIX provides a RESTful Admin API for dynamic configuration of routes, upstreams, services, consumers, SSL certificates, and plugins, and a Control API for health monitoring and schema introspection.
examples:
- key_count: 5
  name: Consumer Example
  slug: consumer-example
- key_count: 3
  name: Consumer Group Example
  slug: consumer-group-example
- key_count: 1
  name: Global Rule Example
  slug: global-rule-example
- key_count: 3
  name: Plugin Config Example
  slug: plugin-config-example
- key_count: 10
  name: Route Example
  slug: route-example
- key_count: 3
  name: Secret Example
  slug: secret-example
- key_count: 8
  name: Service Example
  slug: service-example
- key_count: 9
  name: Ssl Example
  slug: ssl-example
- key_count: 8
  name: Stream Route Example
  slug: stream-route-example
- key_count: 10
  name: Upstream Example
  slug: upstream-example
features:
- description: Dynamically add, update, and delete routes without restarting via the Admin API and etcd-backed config.
  name: Dynamic Route Configuration
- description: Supports HTTP, HTTPS, HTTP/2, gRPC, TCP, UDP, and WebSocket protocols for diverse API types.
  name: Multi-Protocol Support
- description: Rich plugin ecosystem for authentication (JWT, key-auth, OAuth2), rate limiting, transformations, and observability.
  name: Plugin Ecosystem
- description: Plugins can be written in Lua, Go, Python, Java, and Node.js via the Plugin Runner architecture.
  name: Multi-Language Plugin Support
- description: Supports round-robin, consistent hashing, EWMA, and least connections load balancing strategies.
  name: Load Balancing
- description: Traffic splitting for canary deployments and A/B testing with percentage-based routing.
  name: Canary Releases
- description: Built-in circuit breaker plugin for resilience and fault tolerance in upstream communication.
  name: Circuit Breaking
- description: Native Kubernetes ingress controller (APISIX Ingress) for Kubernetes-native API gateway deployments.
  name: Kubernetes Integration
- description: Native integrations with Prometheus, Zipkin, SkyWalking, Datadog, and OpenTelemetry for metrics and tracing.
  name: Observability
- description: Dynamic service discovery via Kubernetes, Nacos, Consul, Eureka, and DNS for upstream resolution.
  name: Service Discovery
finops:
- name: Apache Apisix Finops
  service_category: API
  slug: apache-apisix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-apisix.png
integrations:
- description: Native Kubernetes Ingress controller (APISIX Ingress Controller) for cloud-native deployments.
  name: Kubernetes
- description: Native Prometheus metrics exporter for monitoring route, consumer, and upstream metrics.
  name: Prometheus
- description: Distributed tracing integration for request flow analysis across microservices.
  name: Zipkin and Jaeger
- description: OpenTelemetry plugin for standardized telemetry data export.
  name: OpenTelemetry
- description: etcd backend for distributed configuration storage and cluster synchronization.
  name: etcd
- description: Dynamic service discovery integrations for automatic upstream resolution.
  name: Nacos and Consul
- description: Secret management integration for storing API credentials and TLS certificates.
  name: HashiCorp Vault
json_schemas:
- name: Apache APISIX Consumer Group
  property_count: 3
  slug: consumer-group
- name: Apache APISIX Consumer
  property_count: 5
  slug: consumer
- name: Apache APISIX Global Rule
  property_count: 1
  slug: global-rule
- name: Apache APISIX Plugin Config
  property_count: 3
  slug: plugin-config
- name: Apache APISIX Route
  property_count: 21
  slug: route
- name: Apache APISIX Secret
  property_count: 3
  slug: secret
- name: Apache APISIX Service
  property_count: 8
  slug: service
- name: Apache APISIX SSL
  property_count: 9
  slug: ssl
- name: Apache APISIX Stream Route
  property_count: 8
  slug: stream-route
- name: Apache APISIX Upstream
  property_count: 18
  slug: upstream
json_structures:
- name: Consumer Group Structure
  property_count: 3
  slug: consumer-group-structure
- name: Consumer Structure
  property_count: 5
  slug: consumer-structure
- name: Global Rule Structure
  property_count: 1
  slug: global-rule-structure
- name: Plugin Config Structure
  property_count: 3
  slug: plugin-config-structure
- name: Route Structure
  property_count: 21
  slug: route-structure
- name: Secret Structure
  property_count: 3
  slug: secret-structure
- name: Service Structure
  property_count: 8
  slug: service-structure
- name: Ssl Structure
  property_count: 9
  slug: ssl-structure
- name: Stream Route Structure
  property_count: 8
  slug: stream-route-structure
- name: Upstream Structure
  property_count: 18
  slug: upstream-structure
jsonld:
- class_count: 0
  name: Apache Apisix Context
  property_count: 10
  slug: apache-apisix-context
layout: provider
modified: '2026-05-19'
name: Apache APISIX
nav: Providers
network: true
overview: 'Apache APISIX publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Consumer Groups API, Consumers API, Diagnostics API, and 14 more. Tagged areas include Apache, API Gateway, Cloud-Native, Kubernetes, and Lua.


  The Apache APISIX catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache APISIX''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, support, Stack Overflow tag, and 25 more developer resources.'
plans:
- name: Apache Apisix Plans Pricing
  plan_count: 3
  slug: apache-apisix-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Apache Apisix Rate Limits
  slug: apache-apisix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache APISIX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apache-apisix-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Apache APISIX API Rules
  rule_count: 24
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 14
  slug: apache-apisix-spectral-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 62.1
    developer_ergonomics: 40.5
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-apisix/refs/heads/main/screenshots/apache-apisix-2026-06-20T172044.png
security:
- kind: authentication
  name: Apache Apisix Authentication
  slug: apache-apisix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apache Apisix Domain Security
  slug: apache-apisix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Apisix Vulnerability Disclosure
  slug: apache-apisix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-apisix
tags:
- Apache
- API Gateway
- Cloud-Native
- Kubernetes
- Lua
- NGINX
- Open-Source
- Traffic Management
use_cases:
- description: Route and manage traffic to microservices with dynamic configuration and plugin-based policies.
  name: API Gateway for Microservices
- description: Apply JWT, key-auth, LDAP, OIDC, and OAuth2 plugins to protect APIs without changing upstream services.
  name: Authentication and Authorization
- description: Apply global or per-consumer rate limits to protect upstream services from traffic spikes.
  name: Rate Limiting and Throttling
- description: Use traffic splitting to gradually roll out new API versions with percentage-based routing.
  name: Canary and Blue-Green Deployments
- description: Replace traditional ingress controllers with APISIX for rich API gateway features in Kubernetes.
  name: Kubernetes Ingress Controller
- description: Collect metrics, traces, and logs via native integrations with Prometheus, Zipkin, and SkyWalking.
  name: API Observability
---
