---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-24'
api_count: 7
apis:
- description: Goldmane is the Calico flow aggregation and network-observability service introduced in Calico Open Source 3.30. It exposes a gRPC API for querying aggregated flow data — List for point-in-time querie
  name: Goldmane Flows API
  slug: goldmane-flows-api
- description: 'A remote Model Context Protocol server published on the tigera.io host, advertised through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. The server fronts the '
  name: Tigera MCP Server
  slug: tigera-mcp-server
- description: A read-only REST API on the Calico Cloud SaaS management plane that returns the same vCPU usage and managed-cluster data shown on the Usage Metrics page, for capacity planning, FinOps and license-comp
  name: Calico Cloud Usage API
  slug: calico-cloud-usage-api
- description: The apis API from Tigera — 1 operation(s) for apis.
  name: Tigera APIS API
  slug: tigera-apis-api
- description: The projectcalicoOrg API from Tigera — 1 operation(s) for projectcalicoorg.
  name: Tigera Projectcalico Org API
  slug: tigera-projectcalicoorg-api
- description: The projectcalicoOrg_v3 API from Tigera — 121 operation(s) for projectcalicoorg_v3.
  name: Tigera Projectcalico Org V3 API
  slug: tigera-projectcalicoorg-v3-api
- description: The version API from Tigera — 1 operation(s) for version.
  name: Tigera Version API
  slug: tigera-version-api
artifact_total: 19
asyncapis:
- description: ''
  name: Tigera Calico Cloud Webhooks
  slug: tigera-calico-cloud-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Generic API Server APIS API
  slug: open-tigera-apis-api
- collection_type: open
  name: Generic API Server Projectcalico Org API
  slug: open-tigera-projectcalicoorg-api
- collection_type: open
  name: Generic API Server Projectcalico Org V3 API
  slug: open-tigera-projectcalicoorg-v3-api
- collection_type: open
  name: Generic API Server Version API
  slug: open-tigera-version-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/projectcalico/calico/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.tigera.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tigera.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tigera.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tigera.io/calico-cloud/reference/rest-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.tigera.io/calico-support/
- group: operate
  title: ''
  type: Community
  url: https://www.tigera.io/project-calico/community/
- group: company
  title: ''
  type: Blog
  url: https://www.tigera.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tigera
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/projectcalico/calico
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tigera.io/tigera-products/calico-cloud-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.calicocloud.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tigera.io/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tigera.io/legal/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.tigera.io/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.calicocloud.io/
- group: auth
  title: ''
  type: Security
  url: https://www.tigera.io/vulnerability-disclosure/
- group: auth
  title: ''
  type: SecurityBulletins
  url: https://www.tigera.io/security-bulletins/
- group: auth
  title: ''
  type: Compliance
  url: https://www.tigera.io/tigera-products/calico-cloud-trust-center/
- group: auth
  title: ''
  type: TrustCenter
  url: security/tigera-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tigera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tigera-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tigera-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tigera-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tigera-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tigera-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tigera-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tigera-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/tigera-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tigera-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tigera-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tigera-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tigera-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tigera-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tigera-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tigera-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tigera-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tigera-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tigera-calico-cloud-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tigera-calico-api-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/tigera-goldmane-api.proto
created: '2026-08-05'
description: 'Tigera is the creator of Project Calico, the open-source networking and network-security engine for Kubernetes, and the company behind Calico Open Source, Calico Enterprise and Calico Cloud. Its products deliver container networking (BGP, eBPF, VPP and standard Linux data planes), tiered network policy and microsegmentation, egress gateways and egress access control, cluster mesh, an Envoy-based ingress gateway, workload-based IDS/IPS/WAF and threat detection, and full-stack observability (Service Graph, flow/DNS/L7 logs, packet capture) for Kubernetes clusters. The programmable surface is Kubernetes-native: the projectcalico.org/v3 aggregated API server exposes 27 custom resources through a published Swagger 2.0 definition, the Goldmane gRPC service exposes aggregated flow observability, calicoctl and kubectl are the first-party CLIs, and Calico Cloud adds a SaaS management plane with a read-only Usage API and security-event webhooks.'
image: https://www.tigera.io/app/uploads/2026/01/generic-Tigera-1200x628-1.png
layout: provider
mcp_servers:
- description: Tigera publishes a remote Model Context Protocol server on its primary marketing host. It was not found in any MCP registry or in the Tigera documentation — it was discovered by probing /.well-known/*
  name: Tigera MCP Server
  slug: tigera-mcp-server
modified: '2026-08-05'
name: Tigera
nav: Providers
network: true
overview: 'Tigera publishes 4 APIs on the [APIs.io](https://apis.io/) network, including APIS API, Projectcalico Org API, Projectcalico Org V3 API, and 1 more. Tagged areas include Company, Kubernetes, Networking, Network Security, and Container Security.


  The Tigera catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tigera''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
random_paper: 6
scopes:
- name: Tigera Scopes
  scope_count: 1
  slug: tigera-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 51.1
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 47.4
    developer_ergonomics: 73.2
    discoverability: 83.3
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 51.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tigera/refs/heads/main/screenshots/tigera-2026-08-17T082354.png
security:
- kind: authentication
  name: Tigera Authentication
  slug: tigera-authentication
  summary_line: http/apiKey/oauth2/openIdConnect/mutualTLS · 6 schemes
- kind: domain-security
  name: Tigera Domain Security
  slug: tigera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tigera Vulnerability Disclosure
  slug: tigera-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Tigera Trust Center
  slug: tigera-trust-center
  summary_line: CSA STAR, SOC 2, PCI DSS, GDPR, CCPA
slug: tigera
tags:
- Company
- Kubernetes
- Networking
- Network Security
- Container Security
- Cloud-Native
- Observability
- Microsegmentation
- Zero Trust
- eBPF
- Open-Source
website: https://www.tigera.io/
---
