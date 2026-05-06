---
aid: solo
name: Solo.io
description: Solo.io provides enterprise infrastructure for cloud-native and AI-native environments, including API gateways, service mesh, and agentic AI infrastructure built on Envoy, Istio, and Kubernetes. Products include kgateway (API gateway), Istio-based service mesh, agentgateway (AI gateway), kagent (AI agents for Kubernetes), and agentregistry (MCP registries).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Gateway
  - Agentic AI
  - API Gateway
  - Envoy
  - Istio
  - Kubernetes
  - MCP
  - Service Mesh
url: https://raw.githubusercontent.com/api-evangelist/solo/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: solo:kgateway
    name: Solo Enterprise for kgateway
    description: Kubernetes-native ingress controller and next-generation API gateway built on Envoy Proxy, supporting the Kubernetes Gateway API for traffic management, security, and transformation.
    humanURL: https://docs.solo.io/kgateway/
    tags:
      - API Gateway
      - Envoy
      - Gateway API
      - Ingress Controller
      - Kubernetes
    properties:
      - type: Documentation
        url: https://docs.solo.io/kgateway/
      - type: GettingStarted
        url: https://docs.solo.io/kgateway/latest/quickstart/
      - type: APIReference
        url: https://docs.solo.io/kgateway/latest/reference/api/
      - type: Authentication
        url: https://docs.solo.io/kgateway/latest/security/
      - type: GitHubRepository
        url: https://github.com/solo-io/gloo
        title: Gloo Gateway Repository
      - type: SDK
        url: https://github.com/solo-io/kgateway-client
        title: Go Client
      - type: KubernetesCRD
        url: crd/solo-gloo-enterprise-gloo-solo-io-v1-authconfig.yaml
        title: AuthConfig CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-gloo-solo-io-directresponses.yaml
        title: DirectResponse CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-gloo-solo-io-gatewayparameters.yaml
        title: GatewayParameters CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-solo-io-v1-gateway.yaml
        title: Gateway CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-solo-io-v1-httplisteneroption.yaml
        title: HttpListenerOption CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-solo-io-v1-listeneroption.yaml
        title: ListenerOption CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-solo-io-v1-matchablehttpgateway.yaml
        title: MatchableHttpGateway CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-solo-io-v1-matchabletcpgateway.yaml
        title: MatchableTcpGateway CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-solo-io-v1-routeoption.yaml
        title: RouteOption CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-solo-io-v1-routetable.yaml
        title: RouteTable CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-solo-io-v1-virtualhostoption.yaml
        title: VirtualHostOption CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gateway-solo-io-v1-virtualservice.yaml
        title: VirtualService CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gloo-solo-io-v1-proxy.yaml
        title: Proxy CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gloo-solo-io-v1-settings.yaml
        title: Settings CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gloo-solo-io-v1-upstream.yaml
        title: Upstream CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-gloo-solo-io-v1-upstreamgroup.yaml
        title: UpstreamGroup CRD
      - type: KubernetesCRD
        url: crd/solo-gloo-ratelimit-config.yaml
        title: RateLimitConfig CRD
      - type: KubernetesCRD
        url: crd/solo-kgateway-tcproute-crd.yaml
        title: TCPRoute CRD
      - type: JSONSchema
        url: json-schema/solo-gloo-upstream-schema.json
        title: Upstream JSON Schema
      - type: JSONSchema
        url: json-schema/solo-gloo-virtual-service-schema.json
        title: VirtualService JSON Schema
      - type: JSONStructure
        url: json-structure/solo-kgateway-structure.json
        title: kgateway CRD Structure
      - type: Example
        url: examples/solo-gloo-upstream-kube-example.json
        title: Kubernetes Upstream Example
  - aid: solo:istio
    name: Solo Enterprise for Istio
    description: Enterprise service mesh solution built on Istio for connecting, securing, and observing microservices across multiple clusters and clouds, including Istio Ambient Mesh support.
    humanURL: https://docs.solo.io/gloo-mesh/latest/
    tags:
      - Ambient Mesh
      - Istio
      - Multi-Cluster
      - Service Mesh
      - Zero Trust
    properties:
      - type: Documentation
        url: https://docs.solo.io/gloo-mesh/latest/
  - aid: solo:agentgateway
    name: Solo Enterprise for agentgateway
    description: AI connectivity and governance gateway for agents and LLMs, supporting traffic routing, load balancing, failover, guardrails, and MCP server connectivity across providers including OpenAI, Anthropic, Amazon Bedrock, Azure OpenAI, Gemini, Vertex AI, Ollama, and vLLM.
    humanURL: https://docs.solo.io/agentgateway
    tags:
      - Agentic AI
      - AI Gateway
      - Guardrails
      - LLM
      - MCP
    properties:
      - type: Documentation
        url: https://docs.solo.io/agentgateway
      - type: GettingStarted
        url: https://docs.solo.io/agentgateway/latest/quickstart/
      - type: Authentication
        url: https://docs.solo.io/agentgateway/latest/security/
      - type: GitHubRepository
        url: https://github.com/solo-io/agentgateway-new-ui
        title: Agentgateway Repository
      - type: KubernetesCRD
        url: crd/solo-agentgateway-agentgatewaybackends.yaml
        title: AgentgatewayBackend CRD
      - type: KubernetesCRD
        url: crd/solo-agentgateway-agentgatewayparameters.yaml
        title: AgentgatewayParameters CRD
      - type: KubernetesCRD
        url: crd/solo-agentgateway-agentgatewaypolicies.yaml
        title: AgentgatewayPolicy CRD
      - type: JSONSchema
        url: json-schema/solo-agentgateway-backend-schema.json
        title: AgentgatewayBackend JSON Schema
      - type: JSONStructure
        url: json-structure/solo-agentgateway-structure.json
        title: agentgateway CRD Structure
      - type: Example
        url: examples/solo-agentgateway-backend-example.json
        title: AgentgatewayBackend Example
  - aid: solo:kagent
    name: Solo Enterprise for kagent
    description: Enterprise AI agent framework for Kubernetes that enables building, managing, and scaling intelligent agents with observability, security, human-in-the-loop workflows, and support for multiple LLM providers.
    humanURL: https://docs.solo.io/kagent-enterprise/latest
    tags:
      - Agentic AI
      - AI Agents
      - Kubernetes
      - LLM
    properties:
      - type: Documentation
        url: https://docs.solo.io/kagent-enterprise/latest
      - type: GettingStarted
        url: https://docs.solo.io/kagent-enterprise/latest/quickstart/
common:
  - type: Website
    url: https://www.solo.io/
  - type: Documentation
    url: https://www.solo.io/docs
  - type: Portal
    url: https://www.solo.io/get-started
  - type: Pricing
    url: https://www.solo.io/pricing
  - type: Blog
    url: https://www.solo.io/blog
  - type: GitHubOrganization
    url: https://github.com/solo-io
  - type: Academy
    url: https://www.solo.io/academy
  - type: Training
    url: https://www.solo.io/resources/lab
  - type: Webinars
    url: https://www.solo.io/resources/webinar
  - type: Customers
    url: https://www.solo.io/customers
  - type: Security
    url: https://www.solo.io/security
  - type: PrivacyPolicy
    url: https://www.solo.io/privacy-policy/
  - type: Legal
    url: https://legal.solo.io/
  - type: Support
    url: https://support.solo.io/
  - type: LinkedIn
    url: https://www.linkedin.com/company/solo.io
  - type: X
    url: https://twitter.com/soloio_inc
  - type: YouTube
    url: https://www.youtube.com/soloio
  - type: GitHubRepository
    url: https://github.com/solo-io/solo-kit
    title: Solo-Kit Operator Framework
  - type: GitHubRepository
    url: https://github.com/solo-io/ingress2gateway
    title: Ingress to Gateway Migration Tool
  - type: GitHubRepository
    url: https://github.com/solo-io/dev-portal-starter
    title: Developer Portal Starter
  - type: GitHubRepository
    url: https://github.com/solo-io/ext-auth-plugins
    title: External Auth Plugins
  - type: CodeExamples
    url: https://github.com/solo-io/enterprise-mcp-flow
    title: MCP Flow Examples
  - type: CodeExamples
    url: https://github.com/solo-io/workshops
    title: Workshops
  - type: JSONLD
    url: json-ld/solo-context.jsonld
    title: Solo.io JSON-LD Context
  - type: Vocabulary
    url: vocabulary/solo-vocabulary.yml
    title: Solo.io Enterprise Platform Vocabulary
  - type: Features
    data:
      - name: Kubernetes Gateway API
        description: Native support for the Kubernetes Gateway API standard for traffic management.
      - name: Envoy Proxy
        description: Built on Envoy Proxy for high-performance traffic handling and extensibility.
      - name: Istio Ambient Mesh
        description: Sidecar-less service mesh using Istio Ambient mode for simplified operations.
      - name: Multi-Cluster Networking
        description: Connect and secure services across multiple Kubernetes clusters and clouds.
      - name: Zero Trust Security
        description: End-to-end mTLS, JWT validation, OAuth, OPA, and external auth for zero-trust architectures.
      - name: AI Gateway
        description: Route, load balance, and apply guardrails to LLM provider traffic.
      - name: MCP Server Connectivity
        description: Connect AI agents to MCP servers and manage agent-to-agent communication.
      - name: Rate Limiting
        description: Advanced rate limiting for API and AI traffic.
      - name: OpenTelemetry Observability
        description: Built-in tracing, metrics, and access logging via OpenTelemetry.
      - name: Traffic Transformation
        description: Request and response transformation, header manipulation, and content-based routing.
  - type: UseCases
    data:
      - name: API Gateway Modernization
        description: Replace legacy API gateways with a Kubernetes-native, Envoy-based gateway.
      - name: Service Mesh Adoption
        description: Adopt Istio service mesh for microservice security and observability.
      - name: Multi-Cloud Connectivity
        description: Connect services across AWS, GCP, Azure, and on-premises environments.
      - name: AI Agent Infrastructure
        description: Build, deploy, and manage AI agents securely in Kubernetes.
      - name: LLM Gateway
        description: Centralize LLM provider access with routing, failover, and cost controls.
  - type: Integrations
    data:
      - name: Envoy Proxy
        description: Core proxy engine powering kgateway and agentgateway.
      - name: Istio
        description: Service mesh foundation for multi-cluster networking and security.
      - name: Kubernetes
        description: Native integration with Kubernetes for deployment and configuration.
      - name: OpenAI
        description: LLM provider integration for AI gateway routing.
      - name: Anthropic
        description: Claude LLM provider integration for AI gateway routing.
      - name: Amazon Bedrock
        description: AWS Bedrock LLM provider integration.
      - name: Azure OpenAI
        description: Azure-hosted OpenAI LLM provider integration.
      - name: Google Vertex AI
        description: Google Cloud Vertex AI LLM provider integration.
      - name: OpenTelemetry
        description: Observability integration for tracing, metrics, and logging.
      - name: ArgoCD
        description: GitOps deployment support for Solo products.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
