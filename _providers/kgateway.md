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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Kgateway Agentic Access
  operation_count: 35
  slug: kgateway-agentic-access
  summary_line: 35 operations · 21 acting
api_count: 7
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
artifact_total: 23
collections:
- collection_type: open
  name: kgateway Kubernetes Gateway API
  slug: open-kgateway-kubernetes-gateway-api
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
random_paper: 45
rate_limits:
- limit_count: 5
  name: Kgateway Rate Limits
  slug: kgateway-rate-limits
rules:
- name: Kgateway API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: kgateway-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.6
    developer_ergonomics: 21.7
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 47.5
  schema_version: 0.5
  scored_at: '2026-07-23'
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
