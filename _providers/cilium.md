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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Cilium Agentic Access
  operation_count: 41
  slug: cilium-agentic-access
  summary_line: 41 operations · 15 acting
api_count: 11
apis:
- description: The Hubble API is a gRPC-based observability API built on top of Cilium and eBPF that provides deep visibility into network flows, DNS queries, HTTP requests, and service communication within Kubernet
  name: Hubble API
  slug: hubble-api
- description: The Tetragon gRPC API provides access to eBPF-based security observability and runtime enforcement capabilities. It enables querying of kernel-level events including process execution, file access, an
  name: Tetragon API
  slug: tetragon-api
- description: 'The Hubble Relay API is a gRPC service that aggregates and relays network flow data from multiple Hubble agents running across Kubernetes cluster nodes. It provides a single cluster-wide endpoint for '
  name: Hubble Relay API
  slug: hubble-relay-api
- description: BGP control plane peers, routes, and route policies
  name: Cilium BGP API
  slug: cilium-bgp-api
- description: Cilium daemon configuration, health, and cluster management
  name: Cilium Daemon API
  slug: cilium-daemon-api
- description: Endpoint lifecycle management, configuration, and status
  name: Cilium Endpoint API
  slug: cilium-endpoint-api
- description: IP address management and allocation
  name: Cilium IPAM API
  slug: cilium-ipam-api
- description: The Lrp API from Cilium — 1 operation(s) for lrp.
  name: Cilium Lrp API
  slug: cilium-lrp-api
- description: Network policy, security identities, and FQDN/DNS policy
  name: Cilium Policy API
  slug: cilium-policy-api
- description: XDP prefilter CIDR management
  name: Cilium Prefilter API
  slug: cilium-prefilter-api
- description: The Service API from Cilium — 2 operation(s) for service.
  name: Cilium Service API
  slug: cilium-service-api
artifact_total: 31
asyncapis:
- description: The Hubble event streaming API provides real-time observability into network flows, DNS queries, HTTP requests, and service-to-service communication within Kubernetes clusters. Hubble exposes gRPC-bas
  name: Cilium Hubble Events
  slug: cilium-hubble-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cilium API
  slug: open-cilium-api
- collection_type: open
  name: Cilium BGP API
  slug: open-cilium-bgp-api
- collection_type: open
  name: Cilium BGP Daemon API
  slug: open-cilium-daemon-api
- collection_type: open
  name: Cilium BGP Endpoint API
  slug: open-cilium-endpoint-api
- collection_type: open
  name: Cilium BGP IPAM API
  slug: open-cilium-ipam-api
- collection_type: open
  name: Cilium BGP Lrp API
  slug: open-cilium-lrp-api
- collection_type: open
  name: Cilium BGP Policy API
  slug: open-cilium-policy-api
- collection_type: open
  name: Cilium BGP Prefilter API
  slug: open-cilium-prefilter-api
- collection_type: open
  name: Cilium BGP Service API
  slug: open-cilium-service-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cilium/cilium/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/cilium/cilium/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cilium/cilium/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cilium/cilium/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/cilium/cilium/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cilium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cilium-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cilium
- group: company
  title: ''
  type: Website
  url: https://cilium.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cilium.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cilium.io/en/stable/gettingstarted/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cilium
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cilium/cilium
- group: company
  title: ''
  type: Blog
  url: https://cilium.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://cilium.io/get-involved/
- group: operate
  title: ''
  type: Support
  url: https://cilium.io/get-help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cilium.io/privacy/
- group: operate
  title: ''
  type: Slack
  url: https://slack.cilium.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/cilium/cilium/releases
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@CiliumProject
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cilium.io/terms/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/cilium
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cilium-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cilium-endpoint-schema.json
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/cilium-hubble-asyncapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cilium-api-openapi.yml
- group: design
  title: ''
  type: Spectral
  url: spectral/cilium-spectral.yml
created: '2026-03-16'
description: Cilium is an open source, cloud native solution for providing, securing, and observing network connectivity between workloads, fueled by the revolutionary kernel technology eBPF. Cilium provides network security, load balancing, and observability for Kubernetes clusters.
finops:
- name: Cilium Finops
  service_category: Cloud Native Networking & Security
  slug: cilium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cilium.png
json_schemas:
- name: Cilium Endpoint
  property_count: 3
  slug: cilium-endpoint
jsonld:
- class_count: 0
  name: Cilium Context
  property_count: 11
  slug: cilium-context
layout: provider
modified: '2026-05-19'
name: Cilium
nav: Providers
network: true
overview: 'Cilium publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Hubble API, BGP API, Daemon API, and 6 more. Tagged areas include Cloud Native, eBPF, Kubernetes, Networking, and Security.


  The Cilium catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Cilium''s developer surface includes documentation, getting-started guide, engineering blog, support, changelog, YouTube channel, Stack Overflow tag, and 20 more developer resources.'
plans:
- name: Cilium Plans Pricing
  plan_count: 2
  slug: cilium-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Cilium Rate Limits
  slug: cilium-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Cilium API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: cilium-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Cilium API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: cilium-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.2
  delta: -9.5
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 11.4
    contract_quality: 61.0
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 11.4
    operational_transparency: 36.8
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cilium/refs/heads/main/screenshots/cilium-2026-06-20T174342.png
security:
- kind: domain-security
  name: Cilium Domain Security
  slug: cilium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cilium
tags:
- Cloud Native
- eBPF
- Kubernetes
- Networking
- Security
website: https://cilium.io/
---
