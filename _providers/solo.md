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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Kubernetes-native ingress controller and next-generation API gateway built on Envoy Proxy, supporting the Kubernetes Gateway API for traffic management, security, and transformation.
  name: Solo Enterprise for kgateway
  slug: kgateway
- description: Enterprise service mesh solution built on Istio for connecting, securing, and observing microservices across multiple clusters and clouds, including Istio Ambient Mesh support.
  name: Solo Enterprise for Istio
  slug: istio
- description: 'AI connectivity and governance gateway for agents and LLMs, supporting traffic routing, load balancing, failover, guardrails, and MCP server connectivity across providers including OpenAI, Anthropic, '
  name: Solo Enterprise for agentgateway
  slug: agentgateway
- description: Enterprise AI agent framework for Kubernetes that enables building, managing, and scaling intelligent agents with observability, security, human-in-the-loop workflows, and support for multiple LLM pro
  name: Solo Enterprise for kagent
  slug: kagent
artifact_total: 33
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/solo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.solo.io/docs
- group: start
  title: ''
  type: Portal
  url: https://www.solo.io/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.solo.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.solo.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solo-io
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
- group: auth
  title: ''
  type: Security
  url: https://www.solo.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solo.io/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://legal.solo.io/
- group: operate
  title: ''
  type: Support
  url: https://support.solo.io/
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
  title: Ingress to Gateway Migration Tool
  type: GitHubRepository
  url: https://github.com/solo-io/ingress2gateway
- group: build
  title: Developer Portal Starter
  type: GitHubRepository
  url: https://github.com/solo-io/dev-portal-starter
- group: build
  title: External Auth Plugins
  type: GitHubRepository
  url: https://github.com/solo-io/ext-auth-plugins
- group: build
  title: MCP Flow Examples
  type: CodeExamples
  url: https://github.com/solo-io/enterprise-mcp-flow
- group: build
  title: Workshops
  type: CodeExamples
  url: https://github.com/solo-io/workshops
- group: design
  title: Solo.io JSON-LD Context
  type: JSONLD
  url: json-ld/solo-context.jsonld
- group: design
  title: Solo.io Enterprise Platform Vocabulary
  type: Vocabulary
  url: vocabulary/solo-vocabulary.yml
crds:
- name: solo agentgateway agentgatewaybackends
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-agentgateway-agentgatewaybackends.yaml
- name: solo agentgateway agentgatewayparameters
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-agentgateway-agentgatewayparameters.yaml
- name: solo agentgateway agentgatewaypolicies
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-agentgateway-agentgatewaypolicies.yaml
- name: solo gloo enterprise gloo solo io v1 authconfig
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-enterprise-gloo-solo-io-v1-authconfig.yaml
- name: solo gloo gateway gloo solo io directresponses
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-gloo-solo-io-directresponses.yaml
- name: solo gloo gateway gloo solo io gatewayparameters
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-gloo-solo-io-gatewayparameters.yaml
- name: solo gloo gateway solo io v1 gateway
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-solo-io-v1-gateway.yaml
- name: solo gloo gateway solo io v1 httplisteneroption
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-solo-io-v1-httplisteneroption.yaml
- name: solo gloo gateway solo io v1 listeneroption
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-solo-io-v1-listeneroption.yaml
- name: solo gloo gateway solo io v1 matchablehttpgateway
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-solo-io-v1-matchablehttpgateway.yaml
- name: solo gloo gateway solo io v1 matchabletcpgateway
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-solo-io-v1-matchabletcpgateway.yaml
- name: solo gloo gateway solo io v1 routeoption
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-solo-io-v1-routeoption.yaml
- name: solo gloo gateway solo io v1 routetable
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-solo-io-v1-routetable.yaml
- name: solo gloo gateway solo io v1 virtualhostoption
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-solo-io-v1-virtualhostoption.yaml
- name: solo gloo gateway solo io v1 virtualservice
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gateway-solo-io-v1-virtualservice.yaml
- name: solo gloo gloo solo io v1 proxy
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gloo-solo-io-v1-proxy.yaml
- name: solo gloo gloo solo io v1 settings
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gloo-solo-io-v1-settings.yaml
- name: solo gloo gloo solo io v1 upstream
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gloo-solo-io-v1-upstream.yaml
- name: solo gloo gloo solo io v1 upstreamgroup
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-gloo-solo-io-v1-upstreamgroup.yaml
- name: solo gloo ratelimit config
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-gloo-ratelimit-config.yaml
- name: solo kgateway tcproute crd
  url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/crd/solo-kgateway-tcproute-crd.yaml
created: '2026-03-27'
description: Solo.io provides enterprise infrastructure for cloud-native and AI-native environments, including API gateways, service mesh, and agentic AI infrastructure built on Envoy, Istio, and Kubernetes. Products include kgateway (API gateway), Istio-based service mesh, agentgateway (AI gateway), kagent (AI agents for Kubernetes), and agentregistry (MCP registries).
examples:
- key_count: 5
  name: Solo Agentgateway Backend Example
  slug: solo-agentgateway-backend-example
- key_count: 5
  name: Solo Gloo Upstream Kube Example
  slug: solo-gloo-upstream-kube-example
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
- name: Solo Finops
  service_category: API
  slug: solo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/solo.png
json_schemas:
- name: AgentgatewayBackend
  property_count: 5
  slug: solo-agentgateway-backend
- name: Upstream
  property_count: 5
  slug: solo-gloo-upstream
- name: VirtualService
  property_count: 5
  slug: solo-gloo-virtual-service
json_structures:
- name: Solo Agentgateway Structure
  property_count: 0
  slug: solo-agentgateway-structure
- name: Solo Kgateway Structure
  property_count: 0
  slug: solo-kgateway-structure
jsonld:
- class_count: 0
  name: Solo Context
  property_count: 9
  slug: solo-context
layout: provider
modified: '2026-05-02'
name: Solo.io
nav: Providers
network: true
overview: 'Solo.io publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Gateway, Agentic AI, API Gateway, Envoy, and Istio.


  The Solo.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Solo.io''s developer surface includes documentation, developer portal, pricing, engineering blog, academy / training, training material, legal docs, and 20 more developer resources.'
plans:
- name: Solo Plans Pricing
  plan_count: 3
  slug: solo-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Solo Rate Limits
  slug: solo-rate-limits
rules:
- name: Solo.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: solo-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.8
  delta: -5.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 24.2
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 47.4
  previous_composite: 49.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/screenshots/solo-2026-06-20T194151.png
security:
- kind: domain-security
  name: Solo Domain Security
  slug: solo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Solo Vulnerability Disclosure
  slug: solo-vulnerability-disclosure
  summary_line: disclosure policy published
slug: solo
tags:
- AI Gateway
- Agentic AI
- API Gateway
- Envoy
- Istio
- Kubernetes
- MCP
- Service Mesh
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
