---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Contour Agentic Access
  operation_count: 23
  slug: contour-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 9
apis:
- description: 'Contour''s support for the standard Kubernetes Ingress v1 resource, enabling basic ingress use cases such as host-based and path-based routing to backend services. Contour watches Ingress v1 resources '
  name: Contour Kubernetes Ingress API
  slug: contour-kubernetes-ingress-api
- description: Kubernetes Custom Resource Definition for binding gRPC-based extension services to the Contour API. ExtensionService resources allow external components to implement Contour API features such as exter
  name: Contour ExtensionService API
  slug: contour-extensionservice-api
- description: Contour's ContourConfiguration Custom Resource Definition (v1alpha1) that provides cluster-scoped configuration of a Contour instance, including ingress settings, TLS defaults, timeouts, and feature g
  name: Contour Configuration API
  slug: contour-configuration-api
- description: Namespace-scoped resources that describe network infrastructure instances that route traffic. Each Gateway is associated with a GatewayClass and defines listeners for inbound traffic.
  name: Contour Gateway API
  slug: contour-gateway-api
- description: Cluster-scoped resources that define the controller responsible for managing Gateways of a particular class. GatewayClass is analogous to IngressClass in the legacy Ingress API.
  name: Contour GatewayClass API
  slug: contour-gatewayclass-api
- description: Operations for managing Contour HTTPProxy custom resources in a Kubernetes cluster. HTTPProxy resources define ingress routing rules for HTTP and HTTPS traffic.
  name: Contour HTTPProxy API
  slug: contour-httpproxy-api
- description: Namespace-scoped resources that define HTTP routing rules, mapping HTTP/HTTPS requests to backend Kubernetes services based on host, path, headers, and other criteria.
  name: Contour HTTPRoute API
  slug: contour-httproute-api
- description: Operations for managing TLSCertificateDelegation resources that allow certificates in one namespace to be used by HTTPProxy resources in other namespaces.
  name: Contour TLSCertificateDelegation API
  slug: contour-tlscertificatedelegation-api
- description: Namespace-scoped resources that define TLS routing rules for routing TLS connections based on SNI hostname to backend services.
  name: Contour TLSRoute API
  slug: contour-tlsroute-api
artifact_total: 64
collections:
- collection_type: open
  name: Contour Gateway API
  slug: open-contour-gateway
- collection_type: open
  name: Contour HTTPProxy API
  slug: open-contour-httpproxy
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/projectcontour/contour/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/projectcontour/contour/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/projectcontour/contour/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/projectcontour/contour/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contour-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contour-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://projectcontour.io/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/contour-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/contour-httpproxy-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/contour-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/contour-httpproxy-rules.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/contour-gateway-rules.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://projectcontour.io/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://projectcontour.io/docs/main/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/projectcontour
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/projectcontour/contour
- group: operate
  title: ''
  type: Support
  url: https://projectcontour.io/resources/support/
- group: operate
  title: ''
  type: Community
  url: https://projectcontour.io/community/
- group: other
  title: ''
  type: Resources
  url: https://projectcontour.io/resources/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/projectcontour/contour/releases
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/projectcontour/contour/issues
- group: other
  title: ''
  type: Upgrading
  url: https://projectcontour.io/resources/upgrading/
created: '2025-01-01'
description: A Kubernetes ingress controller using Envoy proxy that provides dynamic configuration updates and advanced routing capabilities for managing external access to services in a cluster.
finops:
- name: Contour Finops
  service_category: Open Source Networking
  slug: contour-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contour.png
json_schemas:
- name: AuthorizationServer
  property_count: 2
  slug: contour-authorizationserver
- name: Condition
  property_count: 6
  slug: contour-condition
- name: CORSPolicy
  property_count: 6
  slug: contour-corspolicy
- name: DetailedCondition
  property_count: 8
  slug: contour-detailedcondition
- name: Gateway
  property_count: 5
  slug: contour-gateway
- name: GatewayClass
  property_count: 5
  slug: contour-gatewayclass
- name: GatewayClassList
  property_count: 3
  slug: contour-gatewayclasslist
- name: GatewayList
  property_count: 3
  slug: contour-gatewaylist
- name: HeaderMatchCondition
  property_count: 6
  slug: contour-headermatchcondition
- name: HeadersPolicy
  property_count: 2
  slug: contour-headerspolicy
- name: HeaderValue
  property_count: 2
  slug: contour-headervalue
- name: HTTPBackendRef
  property_count: 5
  slug: contour-httpbackendref
- name: Contour HTTPProxy
  property_count: 5
  slug: contour-httpproxy
- name: HTTPProxyList
  property_count: 4
  slug: contour-httpproxylist
- name: HTTPProxySpec
  property_count: 5
  slug: contour-httpproxyspec
- name: HTTPProxyStatus
  property_count: 4
  slug: contour-httpproxystatus
- name: HTTPRoute
  property_count: 5
  slug: contour-httproute
- name: HTTPRouteFilter
  property_count: 3
  slug: contour-httproutefilter
- name: HTTPRouteList
  property_count: 3
  slug: contour-httproutelist
- name: HTTPRouteMatch
  property_count: 4
  slug: contour-httproutematch
- name: HTTPRouteRule
  property_count: 4
  slug: contour-httprouterule
- name: Include
  property_count: 3
  slug: contour-include
- name: Listener
  property_count: 6
  slug: contour-listener
- name: ListenerStatus
  property_count: 4
  slug: contour-listenerstatus
- name: MatchCondition
  property_count: 3
  slug: contour-matchcondition
- name: ObjectMeta
  property_count: 8
  slug: contour-objectmeta
- name: ParentReference
  property_count: 6
  slug: contour-parentreference
- name: QueryParameterMatchCondition
  property_count: 6
  slug: contour-queryparametermatchcondition
- name: RateLimitPolicy
  property_count: 2
  slug: contour-ratelimitpolicy
- name: RetryPolicy
  property_count: 3
  slug: contour-retrypolicy
- name: Route
  property_count: 9
  slug: contour-route
- name: SecretObjectReference
  property_count: 4
  slug: contour-secretobjectreference
- name: Service
  property_count: 5
  slug: contour-service
- name: Status
  property_count: 5
  slug: contour-status
- name: SubCondition
  property_count: 4
  slug: contour-subcondition
- name: TCPProxy
  property_count: 2
  slug: contour-tcpproxy
- name: TimeoutPolicy
  property_count: 3
  slug: contour-timeoutpolicy
- name: TLS
  property_count: 4
  slug: contour-tls
- name: TLSCertificateDelegation
  property_count: 4
  slug: contour-tlscertificatedelegation
- name: TLSCertificateDelegationList
  property_count: 4
  slug: contour-tlscertificatedelegationlist
- name: TLSRoute
  property_count: 5
  slug: contour-tlsroute
- name: TLSRouteList
  property_count: 3
  slug: contour-tlsroutelist
- name: VirtualHost
  property_count: 5
  slug: contour-virtualhost
json_structures:
- name: Contour Structure
  property_count: 0
  slug: contour-structure
jsonld:
- class_count: 0
  name: Contour Context
  property_count: 12
  slug: contour-context
layout: provider
modified: '2026-05-19'
name: Contour
nav: Providers
network: true
overview: 'Contour publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Gateway API, GatewayClass API, HTTPProxy API, and 3 more. Tagged areas include Envoy, Ingress Controller, Kubernetes, Networking, and Proxy.


  The Contour catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Contour''s developer surface includes getting-started guide, documentation, support, changelog, and 18 more developer resources.'
plans:
- name: Contour Plans Pricing
  plan_count: 1
  slug: contour-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 3
  name: Contour Rate Limits
  slug: contour-rate-limits
rules:
- name: Contour API Rules
  rule_count: 5
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 1
  slug: contour-gateway-rules
- name: Contour API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: contour-httpproxy-rules
- name: Contour API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: contour-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.6
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 64.2
    developer_ergonomics: 23.9
    discoverability: 72.2
    governance: 31.3
    operational_transparency: 39.5
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contour/refs/heads/main/screenshots/contour-2026-06-20T174944.png
security:
- kind: domain-security
  name: Contour Domain Security
  slug: contour-domain-security
  summary_line: TLSv1.3 · HSTS
slug: contour
tags:
- Envoy
- Ingress Controller
- Kubernetes
- Networking
- Proxy
website: https://projectcontour.io/
---
