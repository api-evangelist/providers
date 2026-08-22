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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 62
  human_in_the_loop: 0
  name: Kuma Agentic Access
  operation_count: 141
  slug: kuma-agentic-access
  summary_line: 141 operations · 62 acting
api_count: 38
apis:
- description: Kuma extends the Kubernetes API server with Custom Resource Definitions (CRDs) for defining and managing service mesh policies. These resources include MeshTrafficPermission, MeshRetry, MeshTimeout, M
  name: Kuma Kubernetes Policy API
  slug: kuma-kubernetes-policy-api
- description: Kuma's Multizone deployment API enables managing service meshes across multiple Kubernetes clusters and Universal zones from a single global control plane. It provides resources for zone management, c
  name: Kuma Multizone API
  slug: kuma-multizone-api
- description: The Dataplane API from Kuma — 2 operation(s) for dataplane.
  name: Kuma Dataplane API
  slug: kuma-dataplane-api
- description: The GlobalInsight API from Kuma — 1 operation(s) for globalinsight.
  name: Kuma GlobalInsight API
  slug: kuma-globalinsight-api
- description: The HostnameGenerator API from Kuma — 2 operation(s) for hostnamegenerator.
  name: Kuma HostnameGenerator API
  slug: kuma-hostnamegenerator-api
- description: The Inspect API from Kuma — 4 operation(s) for inspect.
  name: Kuma Inspect API
  slug: kuma-inspect-api
- description: The KRI API from Kuma — 1 operation(s) for kri.
  name: Kuma KRI API
  slug: kuma-kri-api
- description: The Mesh API from Kuma — 2 operation(s) for mesh.
  name: Kuma Mesh API
  slug: kuma-mesh-api
- description: The MeshAccessLog API from Kuma — 2 operation(s) for meshaccesslog.
  name: Kuma MeshAccessLog API
  slug: kuma-meshaccesslog-api
- description: The MeshCircuitBreaker API from Kuma — 2 operation(s) for meshcircuitbreaker.
  name: Kuma MeshCircuitBreaker API
  slug: kuma-meshcircuitbreaker-api
- description: The Meshes API from Kuma — 9 operation(s) for meshes.
  name: Kuma Meshes API
  slug: kuma-meshes-api
- description: The MeshExternalService API from Kuma — 2 operation(s) for meshexternalservice.
  name: Kuma MeshExternalService API
  slug: kuma-meshexternalservice-api
- description: The MeshFaultInjection API from Kuma — 2 operation(s) for meshfaultinjection.
  name: Kuma MeshFaultInjection API
  slug: kuma-meshfaultinjection-api
- description: The MeshGateway API from Kuma — 2 operation(s) for meshgateway.
  name: Kuma MeshGateway API
  slug: kuma-meshgateway-api
- description: The MeshHealthCheck API from Kuma — 2 operation(s) for meshhealthcheck.
  name: Kuma MeshHealthCheck API
  slug: kuma-meshhealthcheck-api
- description: The MeshHTTPRoute API from Kuma — 2 operation(s) for meshhttproute.
  name: Kuma MeshHTTPRoute API
  slug: kuma-meshhttproute-api
- description: The MeshIdentity API from Kuma — 2 operation(s) for meshidentity.
  name: Kuma MeshIdentity API
  slug: kuma-meshidentity-api
- description: The MeshLoadBalancingStrategy API from Kuma — 2 operation(s) for meshloadbalancingstrategy.
  name: Kuma MeshLoadBalancingStrategy API
  slug: kuma-meshloadbalancingstrategy-api
- description: The MeshMetric API from Kuma — 2 operation(s) for meshmetric.
  name: Kuma MeshMetric API
  slug: kuma-meshmetric-api
- description: The MeshMultiZoneService API from Kuma — 2 operation(s) for meshmultizoneservice.
  name: Kuma MeshMultiZoneService API
  slug: kuma-meshmultizoneservice-api
- description: The MeshOpenTelemetryBackend API from Kuma — 2 operation(s) for meshopentelemetrybackend.
  name: Kuma MeshOpenTelemetryBackend API
  slug: kuma-meshopentelemetrybackend-api
- description: The MeshPassthrough API from Kuma — 2 operation(s) for meshpassthrough.
  name: Kuma MeshPassthrough API
  slug: kuma-meshpassthrough-api
- description: The MeshProxyPatch API from Kuma — 2 operation(s) for meshproxypatch.
  name: Kuma MeshProxyPatch API
  slug: kuma-meshproxypatch-api
- description: The MeshRateLimit API from Kuma — 2 operation(s) for meshratelimit.
  name: Kuma MeshRateLimit API
  slug: kuma-meshratelimit-api
- description: The MeshRetry API from Kuma — 2 operation(s) for meshretry.
  name: Kuma MeshRetry API
  slug: kuma-meshretry-api
- description: The MeshService API from Kuma — 2 operation(s) for meshservice.
  name: Kuma MeshService API
  slug: kuma-meshservice-api
- description: The MeshTCPRoute API from Kuma — 2 operation(s) for meshtcproute.
  name: Kuma MeshTCPRoute API
  slug: kuma-meshtcproute-api
- description: The MeshTimeout API from Kuma — 2 operation(s) for meshtimeout.
  name: Kuma MeshTimeout API
  slug: kuma-meshtimeout-api
- description: The MeshTLS API from Kuma — 2 operation(s) for meshtls.
  name: Kuma MeshTLS API
  slug: kuma-meshtls-api
- description: The MeshTrace API from Kuma — 2 operation(s) for meshtrace.
  name: Kuma MeshTrace API
  slug: kuma-meshtrace-api
- description: The MeshTrafficPermission API from Kuma — 2 operation(s) for meshtrafficpermission.
  name: Kuma MeshTrafficPermission API
  slug: kuma-meshtrafficpermission-api
- description: The MeshTrust API from Kuma — 2 operation(s) for meshtrust.
  name: Kuma MeshTrust API
  slug: kuma-meshtrust-api
- description: The MeshZoneAddress API from Kuma — 2 operation(s) for meshzoneaddress.
  name: Kuma MeshZoneAddress API
  slug: kuma-meshzoneaddress-api
- description: The Secret API from Kuma — 2 operation(s) for secret.
  name: Kuma Secret API
  slug: kuma-secret-api
- description: The System API from Kuma — 2 operation(s) for system.
  name: Kuma System API
  slug: kuma-system-api
- description: The Workload API from Kuma — 2 operation(s) for workload.
  name: Kuma Workload API
  slug: kuma-workload-api
- description: The ZoneEgress API from Kuma — 2 operation(s) for zoneegress.
  name: Kuma ZoneEgress API
  slug: kuma-zoneegress-api
- description: The ZoneIngress API from Kuma — 2 operation(s) for zoneingress.
  name: Kuma ZoneIngress API
  slug: kuma-zoneingress-api
artifact_total: 85
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kuma API
  slug: open-kuma-api
- collection_type: open
  name: Kuma Dataplane API
  slug: open-kuma-dataplane-api
- collection_type: open
  name: Kuma Dataplane GlobalInsight API
  slug: open-kuma-globalinsight-api
- collection_type: open
  name: Kuma Dataplane HostnameGenerator API
  slug: open-kuma-hostnamegenerator-api
- collection_type: open
  name: Kuma Dataplane Inspect API
  slug: open-kuma-inspect-api
- collection_type: open
  name: Kuma Dataplane KRI API
  slug: open-kuma-kri-api
- collection_type: open
  name: Kuma Dataplane Mesh API
  slug: open-kuma-mesh-api
- collection_type: open
  name: Kuma Dataplane MeshAccessLog API
  slug: open-kuma-meshaccesslog-api
- collection_type: open
  name: Kuma Dataplane MeshCircuitBreaker API
  slug: open-kuma-meshcircuitbreaker-api
- collection_type: open
  name: Kuma Dataplane Meshes API
  slug: open-kuma-meshes-api
- collection_type: open
  name: Kuma Dataplane MeshExternalService API
  slug: open-kuma-meshexternalservice-api
- collection_type: open
  name: Kuma Dataplane MeshFaultInjection API
  slug: open-kuma-meshfaultinjection-api
- collection_type: open
  name: Kuma Dataplane MeshGateway API
  slug: open-kuma-meshgateway-api
- collection_type: open
  name: Kuma Dataplane MeshHealthCheck API
  slug: open-kuma-meshhealthcheck-api
- collection_type: open
  name: Kuma Dataplane MeshHTTPRoute API
  slug: open-kuma-meshhttproute-api
- collection_type: open
  name: Kuma Dataplane MeshIdentity API
  slug: open-kuma-meshidentity-api
- collection_type: open
  name: Kuma Dataplane MeshLoadBalancingStrategy API
  slug: open-kuma-meshloadbalancingstrategy-api
- collection_type: open
  name: Kuma Dataplane MeshMetric API
  slug: open-kuma-meshmetric-api
- collection_type: open
  name: Kuma Dataplane MeshMultiZoneService API
  slug: open-kuma-meshmultizoneservice-api
- collection_type: open
  name: Kuma Dataplane MeshOpenTelemetryBackend API
  slug: open-kuma-meshopentelemetrybackend-api
- collection_type: open
  name: Kuma Dataplane MeshPassthrough API
  slug: open-kuma-meshpassthrough-api
- collection_type: open
  name: Kuma Dataplane MeshProxyPatch API
  slug: open-kuma-meshproxypatch-api
- collection_type: open
  name: Kuma Dataplane MeshRateLimit API
  slug: open-kuma-meshratelimit-api
- collection_type: open
  name: Kuma Dataplane MeshRetry API
  slug: open-kuma-meshretry-api
- collection_type: open
  name: Kuma Dataplane MeshService API
  slug: open-kuma-meshservice-api
- collection_type: open
  name: Kuma Dataplane MeshTCPRoute API
  slug: open-kuma-meshtcproute-api
- collection_type: open
  name: Kuma Dataplane MeshTimeout API
  slug: open-kuma-meshtimeout-api
- collection_type: open
  name: Kuma Dataplane MeshTLS API
  slug: open-kuma-meshtls-api
- collection_type: open
  name: Kuma Dataplane MeshTrace API
  slug: open-kuma-meshtrace-api
- collection_type: open
  name: Kuma Dataplane MeshTrafficPermission API
  slug: open-kuma-meshtrafficpermission-api
- collection_type: open
  name: Kuma Dataplane MeshTrust API
  slug: open-kuma-meshtrust-api
- collection_type: open
  name: Kuma Dataplane MeshZoneAddress API
  slug: open-kuma-meshzoneaddress-api
- collection_type: open
  name: Kuma Dataplane Secret API
  slug: open-kuma-secret-api
- collection_type: open
  name: Kuma Dataplane System API
  slug: open-kuma-system-api
- collection_type: open
  name: Kuma Dataplane Workload API
  slug: open-kuma-workload-api
- collection_type: open
  name: Kuma Dataplane ZoneEgress API
  slug: open-kuma-zoneegress-api
- collection_type: open
  name: Kuma Dataplane ZoneIngress API
  slug: open-kuma-zoneingress-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kumahq/kuma/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/kumahq/kuma/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/kumahq/kuma/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/kumahq/kuma/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kuma-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kuma-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kuma-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://kuma.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kuma.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://kuma.io/docs/latest/installation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kumahq
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kumahq/kuma
- group: operate
  title: ''
  type: Community
  url: https://kuma.io/community/
- group: company
  title: ''
  type: Blog
  url: https://kuma.io/blog/
- group: operate
  title: ''
  type: Slack
  url: https://kuma-mesh.slack.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/kumahq/kuma/releases
- group: operate
  title: ''
  type: Support
  url: https://kuma.io/community/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/kuma
- group: auth
  title: ''
  type: Security
  url: https://github.com/kumahq/kuma/blob/master/SECURITY.md
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@KumaMesh
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/kuma-mesh-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kuma-context.jsonld
created: '2026-03-16'
description: Kuma is a platform-agnostic open-source service mesh built on top of Envoy proxy. It provides universal connectivity, security, and observability for services and microservices running on any infrastructure including Kubernetes and VMs.
finops:
- name: Kuma Finops
  service_category: Service Mesh / Networking
  slug: kuma-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kuma.png
json_schemas:
- name: Kuma Mesh Resource Schema
  property_count: 10
  slug: kuma-mesh
jsonld:
- class_count: 20
  name: Kuma Context
  property_count: 0
  slug: kuma-context
layout: provider
modified: '2026-05-19'
name: Kuma
nav: Providers
network: true
overview: 'Kuma publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Dataplane API, GlobalInsight API, HostnameGenerator API, and 33 more. Tagged areas include Envoy, Kubernetes, Microservices, Security, and Service Mesh.


  The Kuma catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kuma''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, support, Stack Overflow tag, and 15 more developer resources.'
plans:
- name: Kuma Plans Pricing
  plan_count: 2
  slug: kuma-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Kuma Rate Limits
  slug: kuma-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Kuma API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kuma-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.2
  delta: -6.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 57.3
    developer_ergonomics: 40.5
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/kuma/refs/heads/main/screenshots/kuma-2026-06-20T184214.png
security:
- kind: authentication
  name: Kuma Authentication
  slug: kuma-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Kuma Domain Security
  slug: kuma-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kuma
tags:
- Envoy
- Kubernetes
- Microservices
- Security
- Service Mesh
website: https://kuma.io/
---
