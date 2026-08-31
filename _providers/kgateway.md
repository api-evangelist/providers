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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Kgateway Agentic Access
  operation_count: 35
  slug: kgateway-agentic-access
  summary_line: 35 operations · 21 acting
api_count: 1
apis:
- description: Configure AI backend providers with support for LLM providers such as OpenAI, Azure OpenAI, and Gemini. Specify provider configuration and priority groups for AI routing.
  name: Kgateway AIBackend API
  slug: kgateway-aibackend-api
- description: Define routable backends such as AI providers (OpenAI, Azure, Gemini), AWS Lambda functions, or static servers for use by Gateways. Reference Backend resources in HTTPRoute to route traffic to externa
  name: Kgateway Backend API
  slug: kgateway-backend-api
- description: Configure Gateways to directly respond to incoming requests with a custom HTTP response code and body without forwarding to a backend service.
  name: Kgateway DirectResponse API
  slug: kgateway-directresponse-api
- description: Integrate external services with a Gateway such as external auth, rate limiting, and external processing. Serves as a configuration bridge between kgateway and external services that extend Gateway fu
  name: Kgateway GatewayExtension API
  slug: kgateway-gatewayextension-api
- description: Customize gateway infrastructure deployment settings including replicas, container configuration, pod templates, and proxy provisioning parameters.
  name: Kgateway GatewayParameters API
  slug: kgateway-gatewayparameters-api
- description: Apply policies to all HTTP and HTTPS listeners defined on a Gateway. Configure listener-level settings that affect all traffic passing through the specified listeners.
  name: Kgateway HTTPListenerPolicy API
  slug: kgateway-httplistenerpolicy-api
- description: Attach traffic management policies to routes in an HTTPRoute resource or all routes served by a Gateway. Supports CORS, external auth, external processing, rate limiting, timeouts, retries, transforma
  name: Kgateway TrafficPolicy API
  slug: kgateway-trafficpolicy-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: kgateway Kubernetes Gateway AIBackend API
  slug: open-kgateway-aibackend-api
- collection_type: open
  name: kgateway Kubernetes Gateway AIBackend Backend API
  slug: open-kgateway-backend-api
- collection_type: open
  name: kgateway Kubernetes Gateway AIBackend DirectResponse API
  slug: open-kgateway-directresponse-api
- collection_type: open
  name: kgateway Kubernetes Gateway AIBackend GatewayExtension API
  slug: open-kgateway-gatewayextension-api
- collection_type: open
  name: kgateway Kubernetes Gateway AIBackend GatewayParameters API
  slug: open-kgateway-gatewayparameters-api
- collection_type: open
  name: kgateway Kubernetes Gateway AIBackend HTTPListenerPolicy API
  slug: open-kgateway-httplistenerpolicy-api
- collection_type: open
  name: kgateway Kubernetes Gateway API
  slug: open-kgateway-kubernetes-gateway-api
- collection_type: open
  name: kgateway Kubernetes Gateway AIBackend TrafficPolicy API
  slug: open-kgateway-trafficpolicy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kgateway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kgateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kgateway-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kgateway
- group: company
  title: ''
  type: Website
  url: https://kgateway.dev/
- group: learn
  title: ''
  type: Videos
  url: https://kgateway.dev/resources/videos/
- group: company
  title: ''
  type: Blog
  url: https://kgateway.dev/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://kgateway.dev/docs/envoy/latest/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kgateway-dev/kgateway
created: '2026-01-02'
description: kgateway is the most widely deployed gateway in Kubernetes for microservices and AI agents. It is a feature-rich, fast, and flexible Kubernetes-native ingress controller and next-generation API gateway built on top of Envoy proxy and the Kubernetes Gateway API.
finops:
- name: Kgateway Finops
  service_category: API
  slug: kgateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kgateway.png
json_schemas:
- name: kgateway AIBackend
  property_count: 4
  slug: ai-backend
- name: kgateway Backend
  property_count: 4
  slug: backend
- name: kgateway DirectResponse
  property_count: 4
  slug: direct-response
- name: kgateway GatewayExtension
  property_count: 4
  slug: gateway-extension
- name: kgateway GatewayParameters
  property_count: 4
  slug: gateway-parameters
- name: kgateway HTTPListenerPolicy
  property_count: 4
  slug: http-listener-policy
- name: kgateway TrafficPolicy
  property_count: 4
  slug: traffic-policy
jsonld:
- class_count: 0
  name: Kgateway Context
  property_count: 7
  slug: kgateway-context
layout: provider
modified: '2026-05-19'
name: Kgateway
nav: Providers
network: true
overview: 'Kgateway publishes 7 APIs on the [APIs.io](https://apis.io/) network, including AIBackend API, Backend API, DirectResponse API, and 4 more. Tagged areas include Gateways.


  The Kgateway catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kgateway''s developer surface includes authentication, engineering blog, documentation, GitHub presence, and 5 more developer resources.'
plans:
- name: Kgateway Plans Pricing
  plan_count: 3
  slug: kgateway-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Kgateway Rate Limits
  slug: kgateway-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Kgateway API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: kgateway-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 13
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 63.9
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kgateway/refs/heads/main/screenshots/kgateway-2026-06-20T184018.png
security:
- kind: authentication
  name: Kgateway Authentication
  slug: kgateway-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kgateway Domain Security
  slug: kgateway-domain-security
  summary_line: TLSv1.3
slug: kgateway
tags:
- Gateways
website: https://kgateway.dev/
---
