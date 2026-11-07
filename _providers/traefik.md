---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Traefik Agentic Access
  operation_count: 23
  slug: traefik-agentic-access
  summary_line: 23 operations
api_count: 1
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
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: Health check and ping endpoints for liveness probes.
  name: Traefik Labs Health API
  slug: traefik-health-api
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: Endpoints for inspecting HTTP routers, services, and middlewares.
  name: Traefik Labs HTTP API
  slug: traefik-http-api
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: Overview and version information for the running Traefik instance.
  name: Traefik Labs Overview API
  slug: traefik-overview-api
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: Endpoints for inspecting TCP routers, services, and middlewares.
  name: Traefik Labs TCP API
  slug: traefik-tcp-api
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: Endpoints for inspecting UDP routers and services.
  name: Traefik Labs UDP API
  slug: traefik-udp-api
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: Endpoints for listing configured entry points.
  name: Traefik Labs Entry Points API
  slug: traefik-entry-points-api
artifact_total: 52
collections:
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
- group: design
  href: https://artifacts.apis.io/traefik/rules/traefik-rules.yml
  title: ''
  type: Spectral
  url: rules/traefik-rules.yml
- group: design
  href: https://artifacts.apis.io/traefik/rules/traefik-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/traefik-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/traefik/data-model/traefik-data-model.yml
  title: ''
  type: DataModel
  url: data-model/traefik-data-model.yml
- group: build
  href: https://artifacts.apis.io/traefik/cli/traefik-cli.yml
  title: ''
  type: CLI
  url: cli/traefik-cli.yml
- group: design
  href: https://artifacts.apis.io/traefik/errors/traefik-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/traefik-problem-types.yml
- group: design
  href: https://artifacts.apis.io/traefik/conformance/traefik-conformance.yml
  title: ''
  type: Conformance
  url: conformance/traefik-conformance.yml
- group: other
  href: https://artifacts.apis.io/traefik/overlays/traefik-overview-api-overlay.yml
  title: ''
  type: Overlay
  url: overlays/traefik-overview-api-overlay.yml
- group: agent
  href: https://artifacts.apis.io/traefik/llms/traefik-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/traefik-llms.txt
- group: auth
  href: https://artifacts.apis.io/traefik/well-known/traefik-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/traefik-security.txt
- group: agent
  href: https://artifacts.apis.io/traefik/well-known/traefik-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/traefik-well-known.yml
- group: other
  href: https://artifacts.apis.io/traefik/hosts/traefik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/traefik-hosts.yml
- group: other
  href: https://artifacts.apis.io/traefik/vendors/traefik-vendors.yml
  title: ''
  type: Vendors
  url: vendors/traefik-vendors.yml
- group: build
  href: https://artifacts.apis.io/traefik/packages/traefik-packages.yml
  title: ''
  type: SDKs
  url: packages/traefik-packages.yml
- group: build
  href: https://artifacts.apis.io/traefik/packages/traefik-packages.yml
  title: ''
  type: Packages
  url: packages/traefik-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://traefik.io/legal/terms-of-services-20190401
- group: operate
  title: ''
  type: StatusPage
  url: https://status.traefik.io/
- group: company
  title: ''
  type: Newsroom
  url: https://traefik.io/press
- group: docs
  title: ''
  type: APIReference
  url: https://doc.traefik.io/traefik/reference/routing-configuration/tcp/tls/
- group: auth
  href: https://artifacts.apis.io/traefik/security/traefik-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/traefik-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/traefik/traefik/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/traefik/traefik/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/traefik/traefik/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/traefik/traefik/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/traefik/traefik/blob/master/CONTRIBUTING.md
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://doc.traefik.io/traefik/deprecation/releases/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://traefik.io/legal/privacy-and-cookie-policy
- group: agent
  href: https://artifacts.apis.io/traefik/agentic-access/traefik-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/traefik-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/traefik/security/traefik-domain-security.yml
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
  href: https://artifacts.apis.io/traefik/json-ld/traefik-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/traefik-context.jsonld
- group: docs
  href: https://artifacts.apis.io/traefik/json-schema/traefik-router-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/traefik-router-schema.json
- group: docs
  href: https://artifacts.apis.io/traefik/json-schema/traefik-service-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/traefik-service-schema.json
- group: docs
  href: https://artifacts.apis.io/traefik/json-schema/traefik-middleware-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/traefik-middleware-schema.json
- group: docs
  href: https://artifacts.apis.io/traefik/json-schema/traefik-entrypoint-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/traefik-entrypoint-schema.json
- group: design
  href: https://artifacts.apis.io/traefik/json-structure/traefik-router-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/traefik-router-structure.json
- group: design
  href: https://artifacts.apis.io/traefik/json-structure/traefik-middleware-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/traefik-middleware-structure.json
- group: design
  href: https://artifacts.apis.io/traefik/vocabulary/traefik-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/traefik-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/traefik/rules/traefik-proxy-rules.yml
  title: ''
  type: Spectral
  url: rules/traefik-proxy-rules.yml
- group: commercial
  href: https://artifacts.apis.io/traefik/plans/traefik-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/traefik-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/traefik/rate-limits/traefik-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/traefik-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/traefik/finops/traefik-finops.yml
  title: ''
  type: FinOps
  url: finops/traefik-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://traefik.io/llms.txt
coverage:
  checked: '2026-10-04'
  detail: Documentation pages are rendered client‑side JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://doc.traefik.io/traefik/
  reason: js-rendered-docs
  state: unreadable
crds:
- name: hub aiservice
  url: https://artifacts.apis.io/traefik/crd/hub-aiservice.yaml
- name: hub api
  url: https://artifacts.apis.io/traefik/crd/hub-api.yaml
- name: hub apibundle
  url: https://artifacts.apis.io/traefik/crd/hub-apibundle.yaml
- name: hub apicatalogitem
  url: https://artifacts.apis.io/traefik/crd/hub-apicatalogitem.yaml
- name: hub apiplan
  url: https://artifacts.apis.io/traefik/crd/hub-apiplan.yaml
- name: hub apiportal
  url: https://artifacts.apis.io/traefik/crd/hub-apiportal.yaml
- name: hub apiversion
  url: https://artifacts.apis.io/traefik/crd/hub-apiversion.yaml
- name: hub managedsubscription
  url: https://artifacts.apis.io/traefik/crd/hub-managedsubscription.yaml
- name: traefik ingressroute
  url: https://artifacts.apis.io/traefik/crd/traefik-ingressroute.yaml
- name: traefik ingressroutetcp
  url: https://artifacts.apis.io/traefik/crd/traefik-ingressroutetcp.yaml
- name: traefik ingressrouteudp
  url: https://artifacts.apis.io/traefik/crd/traefik-ingressrouteudp.yaml
- name: traefik middleware
  url: https://artifacts.apis.io/traefik/crd/traefik-middleware.yaml
- name: traefik middlewaretcp
  url: https://artifacts.apis.io/traefik/crd/traefik-middlewaretcp.yaml
- name: traefik serverstransport
  url: https://artifacts.apis.io/traefik/crd/traefik-serverstransport.yaml
- name: traefik serverstransporttcp
  url: https://artifacts.apis.io/traefik/crd/traefik-serverstransporttcp.yaml
- name: traefik tlsoption
  url: https://artifacts.apis.io/traefik/crd/traefik-tlsoption.yaml
- name: traefik tlsstore
  url: https://artifacts.apis.io/traefik/crd/traefik-tlsstore.yaml
- name: traefik traefikservice
  url: https://artifacts.apis.io/traefik/crd/traefik-traefikservice.yaml
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
- has_sources: true
  method: derived
  name: Traefik Finops
  primary_unit: ''
  service_category: ''
  slug: traefik-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/traefik.png
json_schemas:
- name: EntryPoint
  property_count: 3
  slug: traefik-entry-point
- name: Traefik Entry Point
  property_count: 5
  slug: traefik-entrypoint
- name: HTTPMiddleware
  property_count: 5
  slug: traefik-httpmiddleware
- name: HTTPRouter
  property_count: 11
  slug: traefik-httprouter
- name: HTTPService
  property_count: 6
  slug: traefik-httpservice
- name: Traefik HTTP Middleware
  property_count: 5
  slug: traefik-middleware
- name: Overview
  property_count: 5
  slug: traefik-overview
- name: Traefik Router
  property_count: 12
  slug: traefik-router
- name: Traefik Service
  property_count: 7
  slug: traefik-service
- name: TCPMiddleware
  property_count: 4
  slug: traefik-tcpmiddleware
- name: TCPRouter
  property_count: 7
  slug: traefik-tcprouter
- name: TCPService
  property_count: 5
  slug: traefik-tcpservice
- name: UDPRouter
  property_count: 5
  slug: traefik-udprouter
- name: UDPService
  property_count: 5
  slug: traefik-udpservice
- name: Version
  property_count: 3
  slug: traefik-version
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
overview: 'Traefik Labs publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, HTTP API, Overview API, and 13 more. Tagged areas include AI Gateway, API Gateway, API Management, Developer Portal, and GitOps.


  The Traefik Labs catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Traefik Labs'' developer surface includes CLI, API reference, documentation, getting-started guide, pricing, engineering blog, changelog, and 48 more developer resources.'
plans:
- name: Traefik Plans Pricing
  plan_count: 3
  slug: traefik-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Traefik Rate Limits
  slug: traefik-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Traefik Labs — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: traefik-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 16
  extends: []
  name: Traefik Labs — proxy rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: traefik-proxy-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Traefik Labs API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: traefik-rules
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 70.0
    catalog_earned_first_party: 12.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 57.9
    contract_governance: 31.8
    contract_quality: 51.7
    developer_ergonomics: 46.4
    discoverability: 65.2
    operational_transparency: 60.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/traefik/traefik-2026-06-20T195532.png
security:
- kind: domain-security
  name: Traefik Domain Security
  slug: traefik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Traefik Vulnerability Disclosure
  slug: traefik-vulnerability-disclosure
  summary_line: security.txt · contact published
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
