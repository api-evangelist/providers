---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.3
  scored_at: '2026-08-24'
api_count: 15
apis:
- description: API key management endpoints
  name: Solo.io API Keys API
  slug: solo-io-api-keys-api
- description: API product catalog endpoints
  name: Solo.io API Products API
  slug: solo-io-api-products-api
- description: The APIs API from Solo.io — 5 operation(s) for apis.
  name: Solo.io AP Is API
  slug: solo-io-apis-api
- description: The Applications API from Solo.io — 8 operation(s) for applications.
  name: Solo.io Applications API
  slug: solo-io-applications-api
- description: Application management endpoints
  name: Solo.io Apps API
  slug: solo-io-apps-api
- description: Authentication redirect endpoints
  name: Solo.io Auth API
  slug: solo-io-auth-api
- description: Health check endpoints
  name: Solo.io Health API
  slug: solo-io-health-api
- description: The Me API from Solo.io — 1 operation(s) for me.
  name: Solo.io Me API
  slug: solo-io-me-api
- description: Internal credential metadata endpoints
  name: Solo.io Metadata API
  slug: solo-io-metadata-api
- description: OAuth credential management endpoints
  name: Solo.io OAUTH Credentials API
  slug: solo-io-oauth-credentials-api
- description: Subscription management endpoints
  name: Solo.io Subscriptions API
  slug: solo-io-subscriptions-api
- description: Team management endpoints
  name: Solo.io Teams API
  slug: solo-io-teams-api
- description: The User API from Solo.io — 1 operation(s) for user.
  name: Solo.io User API
  slug: solo-io-user-api
- description: User management endpoints
  name: Solo.io Users API
  slug: solo-io-users-api
- description: The Webhooks API from Solo.io — 2 operation(s) for webhooks.
  name: Solo.io Webhooks API
  slug: solo-io-webhooks-api
artifact_total: 74
asyncapis:
- description: ''
  name: Solo Io Webhooks
  slug: solo-io-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Portal Backend API Keys API
  slug: open-solo-io-api-keys-api
- collection_type: open
  name: Solo Io API Products API
  slug: open-solo-io-api-products-api
- collection_type: open
  name: Gloo Platform Portal AP Is API
  slug: open-solo-io-apis-api
- collection_type: open
  name: Solo Io Applications API
  slug: open-solo-io-applications-api
- collection_type: open
  name: Portal Backend Apps API
  slug: open-solo-io-apps-api
- collection_type: open
  name: Portal Backend Auth API
  slug: open-solo-io-auth-api
- collection_type: open
  name: Portal Backend Health API
  slug: open-solo-io-health-api
- collection_type: open
  name: Gloo Portal Server Me API
  slug: open-solo-io-me-api
- collection_type: open
  name: Portal Backend Metadata API
  slug: open-solo-io-metadata-api
- collection_type: open
  name: Portal Backend OAUTH Credentials API
  slug: open-solo-io-oauth-credentials-api
- collection_type: open
  name: Solo Io Subscriptions API
  slug: open-solo-io-subscriptions-api
- collection_type: open
  name: Solo Io Teams API
  slug: open-solo-io-teams-api
- collection_type: open
  name: Gloo Platform Portal User API
  slug: open-solo-io-user-api
- collection_type: open
  name: Portal Backend Users API
  slug: open-solo-io-users-api
- collection_type: open
  name: GuardRail Webhook Webhooks API
  slug: open-solo-io-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/solo-io-ai-gateway-guardrail-webhook-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/solo-io/gloo-portal-idp-connect/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.solo.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.solo.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.solo.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.solo.io/gateway/latest/portal/openapi/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.solo.io/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.solo.io/company/get-support
- group: company
  title: ''
  type: Blog
  url: https://www.solo.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.solo.io/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solo-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.solo.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.solo.io/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.solo.io/#website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.solo.io/#privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://legal.solo.io/
- group: auth
  title: ''
  type: Security
  url: https://www.solo.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.solo.io/
- group: operate
  title: ''
  type: Community
  url: https://www.solo.io/community
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.solo.io/gateway/latest/reference/changelog/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solo-io-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/solo-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/solo-io-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/solo-io-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/solo-io-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/solo-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/solo-io-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solo-io-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.solo.io/gloo-mesh-enterprise/main/reference/version/versions/
- group: design
  title: ''
  type: Conformance
  url: conformance/solo-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.solo.io/topics/security-and-compliance/fips
- group: design
  title: ''
  type: DataModel
  url: data-model/solo-io-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solo-io-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/solo-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/solo-io-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/solo-io-well-known.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/solo-io-gloo-v1-proxy.proto
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/solo-io-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/solo-io-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/solo-io-tool-crosswalk.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/solo-io-changelog.yml
- group: start
  title: ''
  type: Portal
  url: https://www.solo.io/get-started
- group: learn
  title: ''
  type: Academy
  url: https://www.solo.io/academy
- group: learn
  title: ''
  type: Training
  url: https://www.solo.io/resources/lab
- group: learn
  title: ''
  type: Webinars
  url: https://www.solo.io/resources/webinar
- group: other
  title: ''
  type: Customers
  url: https://www.solo.io/customers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/solo.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/soloio_inc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/soloio
- group: build
  title: Solo-Kit Operator Framework
  type: GitHubRepository
  url: https://github.com/solo-io/solo-kit
- group: build
  title: MCP Flow Examples
  type: CodeExamples
  url: https://github.com/solo-io/enterprise-mcp-flow
- group: design
  title: Solo.io JSON-LD Context
  type: JSONLD
  url: json-ld/solo-io-context.jsonld
- group: design
  title: Solo.io Enterprise Platform Vocabulary
  type: Vocabulary
  url: vocabulary/solo-io-vocabulary.yml
crds:
- name: solo io agentgateway agentgatewaybackends
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-agentgateway-agentgatewaybackends.yaml
- name: solo io agentgateway agentgatewayparameters
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-agentgateway-agentgatewayparameters.yaml
- name: solo io agentgateway agentgatewaypolicies
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-agentgateway-agentgatewaypolicies.yaml
- name: solo io gloo enterprise gloo solo io v1 authconfig
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-enterprise-gloo-solo-io-v1-authconfig.yaml
- name: solo io gloo gateway gloo solo io directresponses
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-gloo-solo-io-directresponses.yaml
- name: solo io gloo gateway gloo solo io gatewayparameters
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-gloo-solo-io-gatewayparameters.yaml
- name: solo io gloo gateway solo io v1 gateway
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-solo-io-v1-gateway.yaml
- name: solo io gloo gateway solo io v1 httplisteneroption
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-solo-io-v1-httplisteneroption.yaml
- name: solo io gloo gateway solo io v1 listeneroption
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-solo-io-v1-listeneroption.yaml
- name: solo io gloo gateway solo io v1 matchablehttpgateway
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-solo-io-v1-matchablehttpgateway.yaml
- name: solo io gloo gateway solo io v1 matchabletcpgateway
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-solo-io-v1-matchabletcpgateway.yaml
- name: solo io gloo gateway solo io v1 routeoption
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-solo-io-v1-routeoption.yaml
- name: solo io gloo gateway solo io v1 routetable
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-solo-io-v1-routetable.yaml
- name: solo io gloo gateway solo io v1 virtualhostoption
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-solo-io-v1-virtualhostoption.yaml
- name: solo io gloo gateway solo io v1 virtualservice
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gateway-solo-io-v1-virtualservice.yaml
- name: solo io gloo gloo solo io v1 proxy
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gloo-solo-io-v1-proxy.yaml
- name: solo io gloo gloo solo io v1 settings
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gloo-solo-io-v1-settings.yaml
- name: solo io gloo gloo solo io v1 upstream
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gloo-solo-io-v1-upstream.yaml
- name: solo io gloo gloo solo io v1 upstreamgroup
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-gloo-solo-io-v1-upstreamgroup.yaml
- name: solo io gloo ratelimit config
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-gloo-ratelimit-config.yaml
- name: solo io kgateway tcproute crd
  url: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/crd/solo-io-kgateway-tcproute-crd.yaml
created: '2026-08-02'
description: Solo.io is a cloud-native application-networking company founded in 2017 that builds enterprise and open-source API gateways, service mesh, and agentic-AI infrastructure. Its products include Kgateway Enterprise (formerly Gloo Gateway), an Envoy-powered Kubernetes Gateway API ingress and API gateway; Solo Enterprise for Istio (formerly Gloo Mesh), a hardened Istio service mesh with ambient mode; Agentgateway Enterprise, a Rust-based AI-native gateway for LLM, MCP, and A2A traffic; Kagent Enterprise, a Kubernetes-native agent runtime; and Agentregistry Enterprise, a registry for agents, MCP servers, and AI tools. Solo.io also ships Gloo Portal, a developer portal whose Portal Server REST API manages API products, teams, apps, subscriptions, API keys, and OAuth credentials, and contributes the kgateway, agentgateway, kagent, and Istio ambient-mesh open-source projects.
examples:
- key_count: 5
  name: Solo Io Agentgateway Backend Example
  slug: solo-io-agentgateway-backend-example
- key_count: 5
  name: Solo Io Gloo Upstream Kube Example
  slug: solo-io-gloo-upstream-kube-example
features:
- description: Native support for the Kubernetes Gateway API standard for traffic management.
  name: Kubernetes Gateway API
- description: Built on Envoy Proxy for high-performance traffic handling and extensibility.
  name: Envoy Proxy
- description: Sidecar-less service mesh using Istio Ambient mode for simplified operations.
  name: Istio Ambient Mesh
- description: Connect and secure services across multiple Kubernetes clusters and clouds.
  name: Multi-Cluster Networking
- description: End-to-end mTLS, JWT validation, OAuth, OPA, and external auth for zero-trust architectures.
  name: Zero Trust Security
- description: Route, load balance, and apply guardrails to LLM provider traffic.
  name: AI Gateway
- description: Connect AI agents to MCP servers and manage agent-to-agent communication.
  name: MCP Server Connectivity
- description: Advanced rate limiting for API and AI traffic.
  name: Rate Limiting
- description: Built-in tracing, metrics, and access logging via OpenTelemetry.
  name: OpenTelemetry Observability
- description: Request and response transformation, header manipulation, and content-based routing.
  name: Traffic Transformation
finops:
- name: Solo Io Finops
  service_category: API
  slug: solo-io-finops
image: https://cdn.prod.website-files.com/66dba20a96c0aa281999f399/6704540db9215a5c14c38c6c_Webclip.png
integrations:
- description: Core proxy engine powering kgateway and agentgateway.
  name: Envoy Proxy
- description: Service mesh foundation for multi-cluster networking and security.
  name: Istio
- description: Native integration with Kubernetes for deployment and configuration.
  name: Kubernetes
- description: LLM provider integration for AI gateway routing.
  name: OpenAI
- description: Claude LLM provider integration for AI gateway routing.
  name: Anthropic
- description: AWS Bedrock LLM provider integration.
  name: Amazon Bedrock
- description: Azure-hosted OpenAI LLM provider integration.
  name: Azure OpenAI
- description: Google Cloud Vertex AI LLM provider integration.
  name: Google Vertex AI
- description: Observability integration for tracing, metrics, and logging.
  name: OpenTelemetry
- description: GitOps deployment support for Solo products.
  name: ArgoCD
json_schemas:
- name: AgentgatewayBackend
  property_count: 5
  slug: solo-io-agentgateway-backend
- name: Upstream
  property_count: 5
  slug: solo-io-gloo-upstream
- name: VirtualService
  property_count: 5
  slug: solo-io-gloo-virtual-service
json_structures:
- name: Solo Io Agentgateway Structure
  property_count: 0
  slug: solo-io-agentgateway-structure
- name: Solo Io Kgateway Structure
  property_count: 0
  slug: solo-io-kgateway-structure
jsonld:
- class_count: 0
  name: Solo Io Context
  property_count: 9
  slug: solo-io-context
layout: provider
mcp_servers:
- description: First-party Solo.io MCP server that analyzes `istioctl bug-report` archives, identifies common Istio problems, and suggests remediation steps. It ships with a packaged agent skill (`/istio-report-asse
  name: Solo.io MCP Server
  slug: soloio-mcp-server
modified: '2026-08-08'
name: Solo.io
nav: Providers
network: true
overview: 'Solo.io publishes 15 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, API Products API, AP Is API, and 12 more. Tagged areas include Company, API Gateway, Service Mesh, Kubernetes, and Istio.


  The Solo.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Solo.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 47 more developer resources.'
plans:
- name: Solo Io Plans Pricing
  plan_count: 3
  slug: solo-io-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Solo Io Rate Limits
  slug: solo-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Solo.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: solo-io-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 68.2
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 41.7
    contract_quality: 68.8
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 41.7
    operational_transparency: 52.6
  previous_composite: 68.2
  provenance:
    conformance: derived
    contracts:
      callable: 20.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solo-io/refs/heads/main/screenshots/solo-io-2026-06-20T194151.png
security:
- kind: authentication
  name: Solo Io Authentication
  slug: solo-io-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Solo Io Domain Security
  slug: solo-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Solo Io Vulnerability Disclosure
  slug: solo-io-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Solo Io Trust Center
  slug: solo-io-trust-center
  summary_line: trust center published
slug: solo-io
tags:
- Company
- API Gateway
- Service Mesh
- Kubernetes
- Istio
- Envoy
- AI Gateway
- Agentic AI
- MCP
- Developer Portal
- Cloud-Native
- Open-Source
use_cases:
- description: Replace legacy API gateways with a Kubernetes-native, Envoy-based gateway.
  name: API Gateway Modernization
- description: Adopt Istio service mesh for microservice security and observability.
  name: Service Mesh Adoption
- description: Connect services across AWS, GCP, Azure, and on-premises environments.
  name: Multi-Cloud Connectivity
- description: Build, deploy, and manage AI agents securely in Kubernetes.
  name: AI Agent Infrastructure
- description: Centralize LLM provider access with routing, failover, and cost controls.
  name: LLM Gateway
website: https://www.solo.io/
---
