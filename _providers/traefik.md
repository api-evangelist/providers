---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Traefik Agentic Access
  operation_count: 23
  slug: traefik-agentic-access
  summary_line: 23 operations
api_count: 16
apis:
- description: Traefik Proxy is the flagship open-source (MIT) cloud-native reverse proxy, ingress controller, and load balancer. It auto-discovers services from Kubernetes (Ingress, Gateway API, CRD), Docker, Docke
  name: Traefik Proxy
  slug: traefik-proxy
- description: Lightweight liveness probe at `/ping` that returns HTTP 200 with body "OK" when the Traefik process is alive. Usually mounted on a dedicated entry point for container-orchestrator liveness checks.
  name: Traefik Ping API
  slug: traefik-ping
- description: Built-in single-page web UI rendering routers, services, middlewares, entry points, providers, version, and TLS configuration in real time. Shares the API handler; exposed at `/dashboard/` (trailing s
  name: Traefik Dashboard
  slug: traefik-dashboard
- description: Commercial Kubernetes-native API gateway built on Traefik Proxy. Adds a native WAF (claimed 23x faster than alternatives), advanced authentication (LDAP, JWT, HMAC, OAuth2, OIDC, OPA), HashiCorp Vault
  name: Traefik Hub API Gateway
  slug: traefik-hub-api-gateway
- description: Kubernetes-native API management on top of the Hub API Gateway. Surfaces a declarative CRD set - API, APIVersion, APIBundle, APIPlan, APIPortal, APICatalogItem, ManagedSubscription - plus a multi-clus
  name: Traefik Hub API Management
  slug: traefik-hub-api-management
- description: 'Self-hosted Kubernetes-native gateway for LLM traffic. OpenAI-compatible unified API in front of OpenAI, Anthropic, Azure OpenAI, AWS Bedrock, Cohere, Gemini, Mistral, Ollama, and self-hosted models. '
  name: Traefik AI Gateway
  slug: traefik-ai-gateway
- description: Gateway add-on that governs how AI agents access Model Context Protocol (MCP) servers. Provides identity-aware routing, capability scoping, and audit logging for agent-to-MCP traffic.
  name: Traefik MCP Gateway
  slug: traefik-mcp-gateway
- description: Public registry of community-built Traefik middlewares. Plugins are authored in Go (loaded at runtime through Yaegi without recompiling Traefik) or in WebAssembly. Surfaces categories such as auth, ob
  name: Traefik Plugin Catalog
  slug: traefik-plugin-catalog
- description: Embeddable Go interpreter maintained by Traefik Labs. Powers the Traefik plugin system - plugins are uploaded as Go source and executed at runtime without recompiling Traefik. Also usable standalone a
  name: Yaegi (Go Interpreter)
  slug: yaegi
- description: Lightweight service mesh built on Traefik Proxy. Offers traffic management and observability for service-to-service communication inside a Kubernetes cluster.
  name: Traefik Mesh
  slug: traefik-mesh
- description: Endpoints for listing configured entry points.
  name: Traefik Labs Entrypoints API
  slug: traefik-entrypoints-api
- description: Health check and ping endpoints for liveness probes.
  name: Traefik Labs Health API
  slug: traefik-health-api
- description: Endpoints for inspecting HTTP routers, services, and middlewares.
  name: Traefik Labs HTTP API
  slug: traefik-http-api
- description: Overview and version information for the running Traefik instance.
  name: Traefik Labs Overview API
  slug: traefik-overview-api
- description: Endpoints for inspecting TCP routers, services, and middlewares.
  name: Traefik Labs TCP API
  slug: traefik-tcp-api
- description: Endpoints for inspecting UDP routers and services.
  name: Traefik Labs UDP API
  slug: traefik-udp-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Traefik Proxy REST Entrypoints API
  slug: open-traefik-entrypoints-api
- collection_type: open
  name: Traefik Proxy REST Entrypoints Health API
  slug: open-traefik-health-api
- collection_type: open
  name: Traefik Proxy REST Entrypoints HTTP API
  slug: open-traefik-http-api
- collection_type: open
  name: Traefik Proxy REST Entrypoints Overview API
  slug: open-traefik-overview-api
- collection_type: open
  name: Traefik Proxy REST API
  slug: open-traefik-proxy
- collection_type: open
  name: Traefik Proxy REST Entrypoints TCP API
  slug: open-traefik-tcp-api
- collection_type: open
  name: Traefik Proxy REST Entrypoints UDP API
  slug: open-traefik-udp-api
common:
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://doc.traefik.io/traefik/deprecation/releases/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://traefik.io/legal/privacy-and-cookie-policy
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/traefik-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/traefik-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/traefik
- group: company
  title: ''
  type: Website
  url: https://traefik.io/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.traefik.io/traefik/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.traefik.io/traefik/getting-started/quick-start/
- group: commercial
  title: ''
  type: Pricing
  url: https://traefik.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://traefik.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/traefik/traefik/blob/master/CHANGELOG.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/traefik
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/traefik/traefik
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/traefik/traefik/issues
- group: operate
  title: ''
  type: Community
  url: https://community.traefik.io/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/traefik
- group: build
  title: ''
  type: Plugin Catalog
  url: https://plugins.traefik.io/
- group: other
  title: ''
  type: Helm Chart
  url: https://github.com/traefik/traefik-helm-chart
- group: design
  title: ''
  type: JSONLD
  url: json-ld/traefik-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/traefik-router-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/traefik-service-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/traefik-middleware-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/traefik-entrypoint-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/traefik-router-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/traefik-middleware-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/traefik-vocabulary.yml
- group: design
  title: ''
  type: Spectral
  url: rules/traefik-proxy-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/traefik-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/traefik-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/traefik-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://traefik.io/llms.txt
crds:
- name: hub aiservice
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/hub-aiservice.yaml
- name: hub api
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/hub-api.yaml
- name: hub apibundle
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/hub-apibundle.yaml
- name: hub apicatalogitem
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/hub-apicatalogitem.yaml
- name: hub apiplan
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/hub-apiplan.yaml
- name: hub apiportal
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/hub-apiportal.yaml
- name: hub apiversion
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/hub-apiversion.yaml
- name: hub managedsubscription
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/hub-managedsubscription.yaml
- name: traefik ingressroute
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-ingressroute.yaml
- name: traefik ingressroutetcp
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-ingressroutetcp.yaml
- name: traefik ingressrouteudp
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-ingressrouteudp.yaml
- name: traefik middleware
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-middleware.yaml
- name: traefik middlewaretcp
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-middlewaretcp.yaml
- name: traefik serverstransport
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-serverstransport.yaml
- name: traefik serverstransporttcp
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-serverstransporttcp.yaml
- name: traefik tlsoption
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-tlsoption.yaml
- name: traefik tlsstore
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-tlsstore.yaml
- name: traefik traefikservice
  url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/crd/traefik-traefikservice.yaml
created: '2026-03-18'
description: Traefik Labs builds cloud-native traffic and API infrastructure - the open-source Traefik Proxy (an ingress controller, reverse proxy, and load balancer for Kubernetes, Docker, Nomad, ECS, Consul, and bare metal), plus the commercial Traefik Hub product line covering API Gateway, API Management, AI Gateway, and MCP Gateway. The data plane is the same Traefik binary across every tier; the Hub control plane adds GitOps-driven CRDs, a developer portal, multi-cluster dashboards, WAF, advanced auth, and AI safety / agent-governance capabilities.
examples:
- key_count: 5
  name: Traefik Get Overview Example
  slug: traefik-get-overview-example
- key_count: 3
  name: Traefik Get Version Example
  slug: traefik-get-version-example
finops:
- name: Traefik Finops
  service_category: API Gateway / API Management Software
  slug: traefik-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/traefik.png
json_schemas:
- name: Traefik Entry Point
  property_count: 5
  slug: traefik-entrypoint
- name: Traefik HTTP Middleware
  property_count: 5
  slug: traefik-middleware
- name: Traefik Router
  property_count: 12
  slug: traefik-router
- name: Traefik Service
  property_count: 7
  slug: traefik-service
json_structures:
- name: Traefik Middleware Structure
  property_count: 5
  slug: traefik-middleware-structure
- name: Traefik Router Structure
  property_count: 0
  slug: traefik-router-structure
jsonld:
- class_count: 0
  name: Traefik Context
  property_count: 9
  slug: traefik-context
layout: provider
modified: '2026-05-19'
name: Traefik Labs
nav: Providers
network: true
overview: 'Traefik Labs publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Entrypoints API, Health API, HTTP API, and 3 more. Tagged areas include AI Gateway, API Gateway, API Management, Developer Portal, and GitOps.


  The Traefik Labs catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Traefik Labs'' developer surface includes documentation, getting-started guide, pricing, engineering blog, changelog, Stack Overflow tag, and 25 more developer resources.'
plans:
- name: Traefik Plans Pricing
  plan_count: 5
  slug: traefik-plans-pricing
random_paper: 146
rate_limits:
- limit_count: 5
  name: Traefik Rate Limits
  slug: traefik-rate-limits
rules:
- name: Traefik Labs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: traefik-jsonschema-spectral-rules
- name: Traefik Labs API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: traefik-proxy-rules
score:
  band: developing
  composite: 46.5
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 54.7
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/screenshots/traefik-2026-06-20T195532.png
security:
- kind: domain-security
  name: Traefik Domain Security
  slug: traefik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: traefik
tags:
- AI Gateway
- API Gateway
- API Management
- Developer Portal
- GitOps
- Kubernetes
- Load Balancer
- MCP Gateway
- Open Source
- Reverse Proxy
- WAF
website: https://traefik.io/
---
