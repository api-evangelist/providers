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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Ambassador Agentic Access
  operation_count: 26
  slug: ambassador-agentic-access
  summary_line: 26 operations · 13 acting
api_count: 11
apis:
- description: 'Ambassador offers a suite of products designed to deliver API developer experiences that fuel innovation. These products, Blackbird API Development Platform, Edge Stack API Gateway, and Telepresence, '
  name: Ambassador
  slug: ambassador
- description: Emissary-Ingress is an open-source, Kubernetes-native API gateway built on Envoy Proxy and a CNCF incubating project, formerly known as Ambassador API Gateway. It uses custom resource definitions (CRD
  name: Emissary-Ingress
  slug: emissary-ingress
- description: Telepresence provides a RESTful API server that runs on the local host, both on the local workstation and in a pod that contains a traffic-agent. The API includes healthz, consume-here, and intercept-
  name: Ambassador Telepresence RESTful API
  slug: telepresence-api
- description: Blackbird is an API development platform that helps developers design, build, test, and manage APIs with AI-powered code generation, mocking, and production-like test environments. It supports OpenAPI
  name: Ambassador Blackbird API Development Platform
  slug: blackbird-api-development-platform
- description: The Ambassador Edge Stack Developer Portal automatically detects and publishes API documentation, serving as a single point of reference for all microservice APIs. It supports Swagger and OpenAPI V3 s
  name: Ambassador Edge Stack Developer Portal
  slug: edge-stack-developer-portal
- description: Access diagnostic and health check endpoints for monitoring Ambassador Edge Stack operational status.
  name: Ambassador Diagnostics API
  slug: ambassador-diagnostics-api
- description: Manage Host resources that configure TLS termination, ACME certificate management, and hostname-based routing rules.
  name: Ambassador Hosts API
  slug: ambassador-hosts-api
- description: Manage Mapping resources that associate URL prefixes or paths with backend services. Mappings are the core routing mechanism in Ambassador.
  name: Ambassador Mappings API
  slug: ambassador-mappings-api
- description: Manage Ambassador Module resources for global configuration of the Ambassador gateway including diagnostics, tracing, and circuit breaking.
  name: Ambassador Modules API
  slug: ambassador-modules-api
- description: Manage rate limiting configuration for controlling request throughput to backend services using labels and descriptors.
  name: Ambassador RateLimits API
  slug: ambassador-ratelimits-api
- description: Manage TLSContext resources that configure TLS settings for Ambassador, including certificates, protocols, and cipher suites.
  name: Ambassador TLSContexts API
  slug: ambassador-tlscontexts-api
artifact_total: 152
collections:
- collection_type: open
  name: Ambassador Edge Stack API
  slug: open-ambassador
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ambassador-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ambassador-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ambassador-authentication.yml
- group: other
  title: ''
  type: Customers
  url: https://www.getambassador.io/case-studies
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getambassador.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.getambassador.io/blog
- group: operate
  title: ''
  type: FAQ
  url: https://www.getambassador.io/faq
- group: docs
  title: ''
  type: Documentation
  url: https://www.getambassador.io/docs
- group: operate
  title: ''
  type: Support
  url: https://www.getambassador.io/support
- group: company
  title: ''
  type: Partners
  url: https://www.getambassador.io/company/partnerships
- group: start
  title: ''
  type: GettingStarted
  url: https://www.getambassador.io/docs/edge-stack/latest/tutorials/getting-started/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/emissary-ingress/emissary
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/emissary-ingress/emissary/blob/master/CHANGELOG.md
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datawire.io/
- group: auth
  title: ''
  type: Authentication
  url: https://www.getambassador.io/products/edge-stack/api-gateway/security-authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://www.getambassador.io/docs/edge-stack/latest/howtos/rate-limiting-tutorial
- group: other
  title: ''
  type: X
  url: https://x.com/ambassadorlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ambassadorlabs
- group: start
  title: ''
  type: Signup
  url: https://app.getambassador.io/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/datawire/ambassador-docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datawire
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ambassador-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ambassador-mapping-schema.json
created: '2025-01-08'
description: Ambassador is a Kubernetes-native API Gateway built on Envoy Proxy, providing routing, load balancing, authentication, and observability for microservices.
examples:
- key_count: 5
  name: Ambassador Circuit Breaker Example
  slug: ambassador-circuit-breaker-example
- key_count: 6
  name: Ambassador Cors Policy Example
  slug: ambassador-cors-policy-example
- key_count: 6
  name: Ambassador Createhost Example
  slug: ambassador-createhost-example
- key_count: 6
  name: Ambassador Createmapping Example
  slug: ambassador-createmapping-example
- key_count: 6
  name: Ambassador Createratelimit Example
  slug: ambassador-createratelimit-example
- key_count: 6
  name: Ambassador Createtlscontext Example
  slug: ambassador-createtlscontext-example
- key_count: 5
  name: Ambassador Diagnostics Overview Example
  slug: ambassador-diagnostics-overview-example
- key_count: 6
  name: Ambassador Getdiagnostics Example
  slug: ambassador-getdiagnostics-example
- key_count: 6
  name: Ambassador Gethost Example
  slug: ambassador-gethost-example
- key_count: 6
  name: Ambassador Getmapping Example
  slug: ambassador-getmapping-example
- key_count: 6
  name: Ambassador Getmodule Example
  slug: ambassador-getmodule-example
- key_count: 6
  name: Ambassador Getratelimit Example
  slug: ambassador-getratelimit-example
- key_count: 6
  name: Ambassador Gettlscontext Example
  slug: ambassador-gettlscontext-example
- key_count: 2
  name: Ambassador Host Example
  slug: ambassador-host-example
- key_count: 4
  name: Ambassador Host List Example
  slug: ambassador-host-list-example
- key_count: 7
  name: Ambassador Host Spec Example
  slug: ambassador-host-spec-example
- key_count: 4
  name: Ambassador Host Status Example
  slug: ambassador-host-status-example
- key_count: 6
  name: Ambassador Listhosts Example
  slug: ambassador-listhosts-example
- key_count: 6
  name: Ambassador Listmappings Example
  slug: ambassador-listmappings-example
- key_count: 6
  name: Ambassador Listmodules Example
  slug: ambassador-listmodules-example
- key_count: 6
  name: Ambassador Listratelimits Example
  slug: ambassador-listratelimits-example
- key_count: 6
  name: Ambassador Listtlscontexts Example
  slug: ambassador-listtlscontexts-example
- key_count: 4
  name: Ambassador Load Balancer Example
  slug: ambassador-load-balancer-example
- key_count: 2
  name: Ambassador Mapping Example
  slug: ambassador-mapping-example
- key_count: 4
  name: Ambassador Mapping List Example
  slug: ambassador-mapping-list-example
- key_count: 29
  name: Ambassador Mapping Spec Example
  slug: ambassador-mapping-spec-example
- key_count: 2
  name: Ambassador Mapping Status Example
  slug: ambassador-mapping-status-example
- key_count: 2
  name: Ambassador Module Example
  slug: ambassador-module-example
- key_count: 4
  name: Ambassador Module List Example
  slug: ambassador-module-list-example
- key_count: 2
  name: Ambassador Module Spec Example
  slug: ambassador-module-spec-example
- key_count: 8
  name: Ambassador Object Meta Example
  slug: ambassador-object-meta-example
- key_count: 2
  name: Ambassador Rate Limit Example
  slug: ambassador-rate-limit-example
- key_count: 4
  name: Ambassador Rate Limit List Example
  slug: ambassador-rate-limit-list-example
- key_count: 4
  name: Ambassador Rate Limit Rule Example
  slug: ambassador-rate-limit-rule-example
- key_count: 2
  name: Ambassador Rate Limit Spec Example
  slug: ambassador-rate-limit-spec-example
- key_count: 3
  name: Ambassador Retry Policy Example
  slug: ambassador-retry-policy-example
- key_count: 2
  name: Ambassador Tls Context Example
  slug: ambassador-tls-context-example
- key_count: 4
  name: Ambassador Tls Context List Example
  slug: ambassador-tls-context-list-example
- key_count: 14
  name: Ambassador Tls Context Spec Example
  slug: ambassador-tls-context-spec-example
- key_count: 6
  name: Ambassador Updatehost Example
  slug: ambassador-updatehost-example
- key_count: 6
  name: Ambassador Updatemapping Example
  slug: ambassador-updatemapping-example
- key_count: 6
  name: Ambassador Updatemodule Example
  slug: ambassador-updatemodule-example
- key_count: 6
  name: Ambassador Updateratelimit Example
  slug: ambassador-updateratelimit-example
- key_count: 6
  name: Ambassador Updatetlscontext Example
  slug: ambassador-updatetlscontext-example
features:
- description: Purpose-built for Kubernetes with custom resource definitions (CRDs) for declarative configuration of routing, TLS, and rate limiting.
  name: Kubernetes-Native API Gateway
- description: Built on Envoy Proxy for high-performance load balancing, circuit breaking, and observability at the edge.
  name: Envoy Proxy Foundation
- description: Integrated OAuth2, API key, and JWT-based authentication filters to secure API endpoints without custom code.
  name: Authentication and Security
- description: Configurable rate limiting with labels and descriptors to control request throughput to backend services.
  name: Rate Limiting
- description: Automatic API documentation publishing from OpenAPI/Swagger specs with customizable developer portal for onboarding.
  name: Developer Portal
- description: Intercept and debug remote Kubernetes services locally using Telepresence for fast inner-loop development.
  name: Local Development with Telepresence
- description: AI-powered API development platform with mock servers and production-like test environments for rapid iteration.
  name: API Mocking with Blackbird
finops:
- name: Ambassador Finops
  service_category: API Management / Gateway
  slug: ambassador-finops
image: https://www.getambassador.io/images/ambassador-logo.png
integrations:
- description: Native integration with Kubernetes using CRDs for Mapping, Host, TLSContext, and RateLimit resources.
  name: Kubernetes
- description: Built on Envoy Proxy with full access to Envoy's load balancing, circuit breaking, and observability features.
  name: Envoy Proxy
- description: Install and manage Ambassador Edge Stack using Helm charts for Kubernetes deployments.
  name: Helm
- description: Export metrics to Prometheus and visualize API gateway performance in Grafana dashboards.
  name: Prometheus and Grafana
- description: Automatic TLS certificate management via cert-manager and ACME protocol integration.
  name: Cert-Manager
json_schemas:
- name: CircuitBreaker
  property_count: 5
  slug: ambassador-circuit-breaker
- name: CircuitBreaker
  property_count: 5
  slug: ambassador-circuitbreaker
- name: CORSPolicy
  property_count: 6
  slug: ambassador-cors-policy
- name: CORSPolicy
  property_count: 6
  slug: ambassador-corspolicy
- name: DiagnosticsOverview
  property_count: 5
  slug: ambassador-diagnostics-overview
- name: DiagnosticsOverview
  property_count: 5
  slug: ambassador-diagnosticsoverview
- name: HostList
  property_count: 4
  slug: ambassador-host-list
- name: Host
  property_count: 2
  slug: ambassador-host
- name: HostSpec
  property_count: 7
  slug: ambassador-host-spec
- name: HostStatus
  property_count: 4
  slug: ambassador-host-status
- name: HostList
  property_count: 4
  slug: ambassador-hostlist
- name: HostSpec
  property_count: 7
  slug: ambassador-hostspec
- name: HostStatus
  property_count: 4
  slug: ambassador-hoststatus
- name: LoadBalancer
  property_count: 4
  slug: ambassador-load-balancer
- name: LoadBalancer
  property_count: 4
  slug: ambassador-loadbalancer
- name: MappingList
  property_count: 4
  slug: ambassador-mapping-list
- name: Mapping
  property_count: 2
  slug: ambassador-mapping
- name: MappingSpec
  property_count: 29
  slug: ambassador-mapping-spec
- name: MappingStatus
  property_count: 2
  slug: ambassador-mapping-status
- name: MappingList
  property_count: 4
  slug: ambassador-mappinglist
- name: MappingSpec
  property_count: 32
  slug: ambassador-mappingspec
- name: MappingStatus
  property_count: 2
  slug: ambassador-mappingstatus
- name: ModuleList
  property_count: 4
  slug: ambassador-module-list
- name: Module
  property_count: 2
  slug: ambassador-module
- name: ModuleSpec
  property_count: 2
  slug: ambassador-module-spec
- name: ModuleList
  property_count: 4
  slug: ambassador-modulelist
- name: ModuleSpec
  property_count: 2
  slug: ambassador-modulespec
- name: ObjectMeta
  property_count: 8
  slug: ambassador-object-meta
- name: ObjectMeta
  property_count: 8
  slug: ambassador-objectmeta
- name: RateLimitList
  property_count: 4
  slug: ambassador-rate-limit-list
- name: RateLimitRule
  property_count: 4
  slug: ambassador-rate-limit-rule
- name: RateLimit
  property_count: 2
  slug: ambassador-rate-limit
- name: RateLimitSpec
  property_count: 2
  slug: ambassador-rate-limit-spec
- name: RateLimit
  property_count: 4
  slug: ambassador-ratelimit
- name: RateLimitList
  property_count: 4
  slug: ambassador-ratelimitlist
- name: RateLimitRule
  property_count: 4
  slug: ambassador-ratelimitrule
- name: RateLimitSpec
  property_count: 2
  slug: ambassador-ratelimitspec
- name: RetryPolicy
  property_count: 3
  slug: ambassador-retry-policy
- name: RetryPolicy
  property_count: 3
  slug: ambassador-retrypolicy
- name: TLSContextList
  property_count: 4
  slug: ambassador-tls-context-list
- name: TLSContext
  property_count: 2
  slug: ambassador-tls-context
- name: TLSContextSpec
  property_count: 14
  slug: ambassador-tls-context-spec
- name: TLSContext
  property_count: 4
  slug: ambassador-tlscontext
- name: TLSContextList
  property_count: 4
  slug: ambassador-tlscontextlist
- name: TLSContextSpec
  property_count: 14
  slug: ambassador-tlscontextspec
json_structures:
- name: Ambassador Circuit Breaker Structure
  property_count: 5
  slug: ambassador-circuit-breaker-structure
- name: Ambassador Cors Policy Structure
  property_count: 6
  slug: ambassador-cors-policy-structure
- name: Ambassador Diagnostics Overview Structure
  property_count: 5
  slug: ambassador-diagnostics-overview-structure
- name: Ambassador Host List Structure
  property_count: 4
  slug: ambassador-host-list-structure
- name: Ambassador Host Spec Structure
  property_count: 7
  slug: ambassador-host-spec-structure
- name: Ambassador Host Status Structure
  property_count: 4
  slug: ambassador-host-status-structure
- name: Ambassador Host Structure
  property_count: 2
  slug: ambassador-host-structure
- name: Ambassador Load Balancer Structure
  property_count: 4
  slug: ambassador-load-balancer-structure
- name: Ambassador Mapping List Structure
  property_count: 4
  slug: ambassador-mapping-list-structure
- name: Ambassador Mapping Spec Structure
  property_count: 29
  slug: ambassador-mapping-spec-structure
- name: Ambassador Mapping Status Structure
  property_count: 2
  slug: ambassador-mapping-status-structure
- name: Ambassador Mapping Structure
  property_count: 2
  slug: ambassador-mapping-structure
- name: Ambassador Module List Structure
  property_count: 4
  slug: ambassador-module-list-structure
- name: Ambassador Module Spec Structure
  property_count: 2
  slug: ambassador-module-spec-structure
- name: Ambassador Module Structure
  property_count: 2
  slug: ambassador-module-structure
- name: Ambassador Object Meta Structure
  property_count: 8
  slug: ambassador-object-meta-structure
- name: Ambassador Rate Limit List Structure
  property_count: 4
  slug: ambassador-rate-limit-list-structure
- name: Ambassador Rate Limit Rule Structure
  property_count: 4
  slug: ambassador-rate-limit-rule-structure
- name: Ambassador Rate Limit Spec Structure
  property_count: 2
  slug: ambassador-rate-limit-spec-structure
- name: Ambassador Rate Limit Structure
  property_count: 2
  slug: ambassador-rate-limit-structure
- name: Ambassador Retry Policy Structure
  property_count: 3
  slug: ambassador-retry-policy-structure
- name: Ambassador Structure
  property_count: 0
  slug: ambassador-structure
- name: Ambassador Tls Context List Structure
  property_count: 4
  slug: ambassador-tls-context-list-structure
- name: Ambassador Tls Context Spec Structure
  property_count: 14
  slug: ambassador-tls-context-spec-structure
- name: Ambassador Tls Context Structure
  property_count: 2
  slug: ambassador-tls-context-structure
jsonld:
- class_count: 0
  name: Ambassador Context
  property_count: 0
  slug: ambassador-context
layout: provider
modified: '2026-05-19'
name: Ambassador
nav: Providers
network: true
overview: 'Ambassador publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Diagnostics API, Hosts API, Mappings API, and 3 more. Tagged areas include API Development, Gateways, Ingress, Kubernetes, and Mock Servers.


  The Ambassador catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ambassador''s developer surface includes authentication, pricing, engineering blog, FAQ, documentation, support, getting-started guide, and 16 more developer resources.'
plans:
- name: Ambassador Plans Pricing
  plan_count: 4
  slug: ambassador-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Ambassador Rate Limits
  slug: ambassador-rate-limits
rules:
- name: Ambassador API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ambassador-jsonschema-spectral-rules
- name: Ambassador API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 5
  slug: ambassador-spectral-rules
score:
  band: developing
  composite: 53.5
  delta: -4.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.9
    developer_ergonomics: 37.0
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ambassador/refs/heads/main/screenshots/ambassador-2026-06-20T171959.png
security:
- kind: authentication
  name: Ambassador Authentication
  slug: ambassador-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ambassador Domain Security
  slug: ambassador-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ambassador
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
use_cases:
- description: Route, secure, and observe traffic to microservices running in Kubernetes clusters.
  name: Microservices API Gateway
- description: Design, mock, and test APIs locally with Blackbird before deploying to Kubernetes environments.
  name: API Development and Testing
- description: Enable multiple teams to independently manage their API routing and configuration using Kubernetes CRDs.
  name: Multi-Team API Management
- description: Serve as the edge gateway in a service mesh architecture, handling north-south traffic with TLS termination.
  name: Service Mesh Edge Gateway
- description: Provide a self-service developer portal for internal and external developers to discover and consume APIs.
  name: Developer Onboarding
---
