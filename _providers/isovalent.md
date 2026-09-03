---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Isovalent Agentic Access
  operation_count: 47
  slug: isovalent-agentic-access
  summary_line: 47 operations · 14 acting
api_count: 2
apis:
- description: The gRPC Hubble Observer, Relay, and Peer APIs that stream real-time network flow, service-map, and connectivity observability events from Cilium's eBPF dataplane.
  name: Hubble Observer API
  slug: hubble-observer-api
- baseURL: unix:///var/run/cilium/cilium.sock
  baseurl_source: declared
  description: The bgp API from Isovalent — 3 operation(s) for bgp.
  name: Isovalent bgp API
  slug: isovalent-bgp-api
- baseURL: unix:///var/run/cilium/cilium.sock
  baseurl_source: declared
  description: The connectivity API from Isovalent — 2 operation(s) for connectivity.
  name: Isovalent connectivity API
  slug: isovalent-connectivity-api
- baseURL: unix:///var/run/cilium/cilium.sock
  baseurl_source: declared
  description: The daemon API from Isovalent — 9 operation(s) for daemon.
  name: Isovalent daemon API
  slug: isovalent-daemon-api
- baseURL: unix:///var/run/cilium/cilium.sock
  baseurl_source: declared
  description: The endpoint API from Isovalent — 6 operation(s) for endpoint.
  name: Isovalent endpoint API
  slug: isovalent-endpoint-api
- baseURL: unix:///var/run/cilium/cilium.sock
  baseurl_source: declared
  description: The Healthz API from Isovalent — 1 operation(s) for healthz.
  name: Isovalent Healthz API
  slug: isovalent-healthz-api
- baseURL: unix:///var/run/cilium/cilium.sock
  baseurl_source: declared
  description: The ipam API from Isovalent — 2 operation(s) for ipam.
  name: Isovalent ipam API
  slug: isovalent-ipam-api
- baseURL: unix:///var/run/cilium/cilium.sock
  baseurl_source: declared
  description: The policy API from Isovalent — 10 operation(s) for policy.
  name: Isovalent policy API
  slug: isovalent-policy-api
- baseURL: unix:///var/run/cilium/cilium.sock
  baseurl_source: declared
  description: The prefilter API from Isovalent — 1 operation(s) for prefilter.
  name: Isovalent prefilter API
  slug: isovalent-prefilter-api
- baseURL: unix:///var/run/cilium/cilium.sock
  baseurl_source: declared
  description: The service API from Isovalent — 2 operation(s) for service.
  name: Isovalent service API
  slug: isovalent-service-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cilium bgp API
  slug: open-isovalent-bgp-api
- collection_type: open
  name: Cilium bgp connectivity API
  slug: open-isovalent-connectivity-api
- collection_type: open
  name: Cilium bgp daemon API
  slug: open-isovalent-daemon-api
- collection_type: open
  name: Cilium bgp endpoint API
  slug: open-isovalent-endpoint-api
- collection_type: open
  name: Cilium bgp Healthz API
  slug: open-isovalent-healthz-api
- collection_type: open
  name: Cilium bgp ipam API
  slug: open-isovalent-ipam-api
- collection_type: open
  name: Cilium bgp policy API
  slug: open-isovalent-policy-api
- collection_type: open
  name: Cilium bgp prefilter API
  slug: open-isovalent-prefilter-api
- collection_type: open
  name: Cilium bgp service API
  slug: open-isovalent-service-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/isovalent-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/isovalent-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/isovalent-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: security/isovalent-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/isovalent-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/isovalent-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/isovalent-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/isovalent-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/isovalent-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/isovalent-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/isovalent-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/isovalent-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/isovalent-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/isovalent-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/isovalent-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/isovalent-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/isovalent-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/isovalent-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/isovalent-cilium-agent-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/isovalent-cilium-health-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/isovalent-hubble-observer.proto
- group: company
  title: ''
  type: Website
  url: https://isovalent.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cilium.io/en/stable/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cilium.io/en/stable/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cilium.io/en/stable/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cilium.io/en/stable/gettingstarted/
- group: company
  title: ''
  type: Blog
  url: https://isovalent.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://isovalent.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cilium
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.cilium.io/en/stable/community/roadmap/
- group: operate
  title: ''
  type: Support
  url: https://isovalent.com/support/
- group: operate
  title: ''
  type: Community
  url: https://cilium.io/get-involved/
- group: commercial
  title: ''
  type: Pricing
  url: https://isovalent.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://isovalent.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://isovalent.com/privacy-policy/
created: '2026-07-17'
description: Isovalent is the company founded in 2017 by the creators of Cilium, the eBPF-based networking, security, and observability platform for Kubernetes and cloud-native infrastructure. Isovalent builds and maintains the open source Cilium project (a CNCF graduated project), the Hubble observability layer, and the Tetragon runtime security engine, and offers commercial Isovalent Enterprise for Cilium and Isovalent Enterprise for Tetragon distributions with hardened builds, support, and advanced features. Cilium replaces kube-proxy and traditional CNI plugins with identity-aware, eBPF-powered dataplane networking, network policy, service mesh, multi-cluster mesh, and deep flow-level observability. The developer surface spans the JSON REST API served by the cilium-agent, the cilium-health connectivity API, the gRPC Hubble Observer/Relay flow APIs, first-party Go client packages, and the cilium and hubble command-line tools. Isovalent was acquired by Cisco in 2024 and its technology
  now underpins Cisco's cloud-native security portfolio.
image: https://isovalent.com/favicon.ico
layout: provider
modified: '2026-08-19'
name: Isovalent
nav: Providers
network: true
overview: 'Isovalent publishes 9 APIs on the [APIs.io](https://apis.io/) network, including bgp API, connectivity API, daemon API, and 6 more. Tagged areas include Company, Networking, Kubernetes, eBPF, and Security.


  Isovalent''s developer surface includes CLI, authentication, changelog, sandbox, documentation, API reference, getting-started guide, and 30 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 9.4
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/isovalent/refs/heads/main/screenshots/isovalent-2026-07-25T222948.png
security:
- kind: authentication
  name: Isovalent Authentication
  slug: isovalent-authentication
  summary_line: none-local-socket/mutualTLS · 2 schemes
- kind: domain-security
  name: Isovalent Domain Security
  slug: isovalent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Isovalent Vulnerability Disclosure
  slug: isovalent-vulnerability-disclosure
  summary_line: contact published
slug: isovalent
tags:
- Company
- Networking
- Kubernetes
- eBPF
- Security
- Observability
- Cloud-Native
- Service Mesh
- CNI
- Container Networking
website: https://isovalent.com/
---
