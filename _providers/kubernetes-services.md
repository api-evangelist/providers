---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Kubernetes Services Agentic Access
  operation_count: 52
  slug: kubernetes-services-agentic-access
  summary_line: 52 operations · 29 acting
api_count: 5
apis:
- description: Kubernetes provides DNS-based service discovery for Services and Pods within a cluster. DNS records are automatically created for Services, allowing workloads to locate services by name rather than by
  name: Kubernetes DNS for Services and Pods
  slug: kubernetes-dns
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: EndpointSlice resources tracking IP addresses, ports, and readiness of pods backing a Service, with topology-aware routing support.
  name: Kubernetes Services EndpointSlices API
  slug: kubernetes-services-endpointslices-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: Gateway resources instantiating traffic-handling infrastructure such as cloud load balancers or in-cluster proxies, with listeners for each protocol.
  name: Kubernetes Services Gateway API
  slug: kubernetes-services-gateway-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: GatewayClass resources defining a class of gateway implementations. Cluster-scoped resources that link to a specific ingress or mesh controller.
  name: Kubernetes Services GatewayClass API
  slug: kubernetes-services-gatewayclass-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: GRPCRoute resources defining gRPC routing rules from Gateway listeners to backend services with service and method name matching.
  name: Kubernetes Services GRPCRoute API
  slug: kubernetes-services-grpcroute-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: HTTPRoute resources defining HTTP and HTTPS routing rules from Gateway listeners to backend services with support for path, header, and query parameter matching.
  name: Kubernetes Services HTTPRoute API
  slug: kubernetes-services-httproute-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: Ingress resources defining HTTP and HTTPS routing rules from external traffic to cluster services, with TLS termination support.
  name: Kubernetes Services Ingress API
  slug: kubernetes-services-ingress-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: IngressClass resources identifying which ingress controller should fulfill an Ingress resource.
  name: Kubernetes Services IngressClass API
  slug: kubernetes-services-ingressclass-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: Status subresource for Ingress objects, reporting load balancer IP or hostname assignments from the ingress controller.
  name: Kubernetes Services IngressStatus API
  slug: kubernetes-services-ingressstatus-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: The Namespaces API from Kubernetes Services — 2 operation(s) for namespaces.
  name: Kubernetes Services Namespaces API
  slug: kubernetes-services-namespaces-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: NetworkPolicy resources controlling Pod-level traffic ingress and egress based on label selectors, namespace selectors, and IP CIDR blocks.
  name: Kubernetes Services NetworkPolicy API
  slug: kubernetes-services-networkpolicy-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: The Services API from Kubernetes Services — 1 operation(s) for services.
  name: Kubernetes Services Services API
  slug: kubernetes-services-services-api
- baseURL: https://kubernetes.default.svc
  baseurl_source: spec
  description: Status subresource operations for Services, used to update load balancer provisioning state and conditions.
  name: Kubernetes Services ServiceStatus API
  slug: kubernetes-services-servicestatus-api
artifact_total: 90
asyncapis:
- description: The Kubernetes Services watch API provides streaming event notifications for networking resources including Services, Ingresses, EndpointSlices, NetworkPolicies, and Gateway API resources. Clients sub
  name: Kubernetes Services Watch Events
  slug: kubernetes-services-watch-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices API
  slug: open-kubernetes-endpoint-slices
- collection_type: open
  name: Kubernetes Services Kubernetes Gateway API
  slug: open-kubernetes-gateway-api
- collection_type: open
  name: Kubernetes Services Kubernetes Ingress API
  slug: open-kubernetes-ingress
- collection_type: open
  name: Kubernetes Services Kubernetes Network Policies API
  slug: open-kubernetes-network-policies
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices API
  slug: open-kubernetes-services-endpointslices-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices Gateway API
  slug: open-kubernetes-services-gateway-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices GatewayClass API
  slug: open-kubernetes-services-gatewayclass-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices GRPCRoute API
  slug: open-kubernetes-services-grpcroute-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices HTTPRoute API
  slug: open-kubernetes-services-httproute-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices Ingress API
  slug: open-kubernetes-services-ingress-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices IngressClass API
  slug: open-kubernetes-services-ingressclass-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices IngressStatus API
  slug: open-kubernetes-services-ingressstatus-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices Namespaces API
  slug: open-kubernetes-services-namespaces-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices NetworkPolicy API
  slug: open-kubernetes-services-networkpolicy-api
- collection_type: open
  name: Kubernetes Kubernetes EndpointSlices Services API
  slug: open-kubernetes-services-services-api
- collection_type: open
  name: Kubernetes Services Kubernetes EndpointSlices ServiceStatus API
  slug: open-kubernetes-services-servicestatus-api
- collection_type: open
  name: Kubernetes Services API
  slug: open-kubernetes-services
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kubernetes-services-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kubernetes/kubernetes/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/kubernetes/kubernetes/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/kubernetes/kubernetes/blob/master/.github/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/kubernetes/kubernetes/blob/master/code-of-conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/kubernetes/kubernetes/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/kubernetes/kubernetes/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kubernetes-services-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kubernetes-services-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubernetes-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kubernetes-services-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://kubernetes.io
- group: docs
  title: ''
  type: Documentation
  url: https://kubernetes.io/docs/concepts/services-networking/
- group: start
  title: ''
  type: GettingStarted
  url: https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/
- group: docs
  title: ''
  type: Reference
  url: https://kubernetes.io/docs/reference/kubernetes-api/service-resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kubernetes
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kubernetes/kubernetes
- group: company
  title: ''
  type: Blog
  url: https://kubernetes.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://kubernetes.io/community/
- group: operate
  title: ''
  type: ChangeLog
  url: https://kubernetes.io/releases/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/kubernetes-services-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kubernetes-services-context.jsonld
created: '2025-01-01'
description: Kubernetes Services provide an abstract way to expose an application running on a set of Pods as a network service. They provide stable networking endpoints and load balancing across pod replicas in a Kubernetes cluster.
finops:
- name: Kubernetes Services Finops
  service_category: Open Source / Container Networking
  slug: kubernetes-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubernetes-services.png
json_schemas:
- name: Condition
  property_count: 5
  slug: kubernetes-services-condition
- name: Endpoint
  property_count: 7
  slug: kubernetes-services-endpoint
- name: EndpointConditions
  property_count: 3
  slug: kubernetes-services-endpointconditions
- name: EndpointHints
  property_count: 2
  slug: kubernetes-services-endpointhints
- name: EndpointPort
  property_count: 4
  slug: kubernetes-services-endpointport
- name: EndpointSlice
  property_count: 6
  slug: kubernetes-services-endpointslice
- name: EndpointSliceList
  property_count: 4
  slug: kubernetes-services-endpointslicelist
- name: Gateway
  property_count: 5
  slug: kubernetes-services-gateway
- name: GatewayClass
  property_count: 5
  slug: kubernetes-services-gatewayclass
- name: GatewayClassList
  property_count: 4
  slug: kubernetes-services-gatewayclasslist
- name: GatewayList
  property_count: 4
  slug: kubernetes-services-gatewaylist
- name: GatewayListener
  property_count: 6
  slug: kubernetes-services-gatewaylistener
- name: GRPCRoute
  property_count: 4
  slug: kubernetes-services-grpcroute
- name: GRPCRouteList
  property_count: 4
  slug: kubernetes-services-grpcroutelist
- name: HTTPBackendRef
  property_count: 4
  slug: kubernetes-services-httpbackendref
- name: HTTPIngressPath
  property_count: 3
  slug: kubernetes-services-httpingresspath
- name: HTTPRoute
  property_count: 5
  slug: kubernetes-services-httproute
- name: HTTPRouteList
  property_count: 4
  slug: kubernetes-services-httproutelist
- name: HTTPRouteMatch
  property_count: 4
  slug: kubernetes-services-httproutematch
- name: Ingress
  property_count: 5
  slug: kubernetes-services-ingress
- name: IngressBackend
  property_count: 2
  slug: kubernetes-services-ingressbackend
- name: IngressClass
  property_count: 4
  slug: kubernetes-services-ingressclass
- name: IngressClassList
  property_count: 4
  slug: kubernetes-services-ingressclasslist
- name: IngressList
  property_count: 4
  slug: kubernetes-services-ingresslist
- name: IngressRule
  property_count: 2
  slug: kubernetes-services-ingressrule
- name: IngressSpec
  property_count: 4
  slug: kubernetes-services-ingressspec
- name: IngressStatus
  property_count: 1
  slug: kubernetes-services-ingressstatus
- name: IngressTLS
  property_count: 2
  slug: kubernetes-services-ingresstls
- name: IPBlock
  property_count: 2
  slug: kubernetes-services-ipblock
- name: LabelSelector
  property_count: 2
  slug: kubernetes-services-labelselector
- name: ListMeta
  property_count: 3
  slug: kubernetes-services-listmeta
- name: LoadBalancerIngress
  property_count: 3
  slug: kubernetes-services-loadbalanceringress
- name: NetworkPolicy
  property_count: 4
  slug: kubernetes-services-networkpolicy
- name: NetworkPolicyEgressRule
  property_count: 2
  slug: kubernetes-services-networkpolicyegressrule
- name: NetworkPolicyIngressRule
  property_count: 2
  slug: kubernetes-services-networkpolicyingressrule
- name: NetworkPolicyList
  property_count: 4
  slug: kubernetes-services-networkpolicylist
- name: NetworkPolicyPeer
  property_count: 3
  slug: kubernetes-services-networkpolicypeer
- name: NetworkPolicyPort
  property_count: 3
  slug: kubernetes-services-networkpolicyport
- name: NetworkPolicySpec
  property_count: 4
  slug: kubernetes-services-networkpolicyspec
- name: ObjectMeta
  property_count: 7
  slug: kubernetes-services-objectmeta
- name: Kubernetes Services Resource
  property_count: 5
  slug: kubernetes-services
- name: Service
  property_count: 5
  slug: kubernetes-services-service
- name: ServiceList
  property_count: 4
  slug: kubernetes-services-servicelist
- name: ServicePort
  property_count: 6
  slug: kubernetes-services-serviceport
- name: ServiceSpec
  property_count: 17
  slug: kubernetes-services-servicespec
- name: ServiceStatus
  property_count: 2
  slug: kubernetes-services-servicestatus
- name: Status
  property_count: 4
  slug: kubernetes-services-status
json_structures:
- name: Kubernetes Services Structure
  property_count: 0
  slug: kubernetes-services-structure
jsonld:
- class_count: 0
  name: Kubernetes Services Context
  property_count: 28
  slug: kubernetes-services-context
layout: provider
modified: '2026-05-19'
name: Kubernetes Services
nav: Providers
network: true
overview: 'Kubernetes Services publishes 12 APIs on the [APIs.io](https://apis.io/) network, including EndpointSlices API, Gateway API, GatewayClass API, and 9 more. Tagged areas include Container Orchestration, Kubernetes, Load Balancing, Networking, and Service Discovery.


  The Kubernetes Services catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Kubernetes Services'' developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, and 17 more developer resources.'
plans:
- name: Kubernetes Services Plans Pricing
  plan_count: 1
  slug: kubernetes-services-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Kubernetes Services Rate Limits
  slug: kubernetes-services-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Kubernetes Services API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: kubernetes-services-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Kubernetes Services API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: kubernetes-services-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.5
    catalog_earned_first_party: 0.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 72.5
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 65.0
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubernetes-services/refs/heads/main/screenshots/kubernetes-services-2026-06-20T184207.png
security:
- kind: authentication
  name: Kubernetes Services Authentication
  slug: kubernetes-services-authentication
  summary_line: http/mutualTLS · 2 schemes
- kind: domain-security
  name: Kubernetes Services Domain Security
  slug: kubernetes-services-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Kubernetes Services Vulnerability Disclosure
  slug: kubernetes-services-vulnerability-disclosure
  summary_line: disclosure policy published
slug: kubernetes-services
tags:
- Container Orchestration
- Kubernetes
- Load Balancing
- Networking
- Service Discovery
website: https://kubernetes.io
---
