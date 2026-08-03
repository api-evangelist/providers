---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: The Gloo Portal Server REST API backs the Solo.io developer portal for Kgateway Enterprise / Gloo Gateway. It lets portal users look up their session user, browse API products and product versions, cr
  name: Gloo Portal Server API
  slug: portal-server
- description: The portal backend server API for the kgateway 2.x generation of Gloo Portal. It exposes health and readiness probes, the API product catalog and product versions, user and team management, team appli
  name: Gloo Portal Backend API
  slug: portal-backend
- description: The Gloo Platform portal API covers the endpoint specifications for managing user access to the developer portal and to the resources the portal exposes — the current user session, the list of APIs an
  name: Gloo Platform Portal API
  slug: gloo-platform-portal
- description: The IdP Connect SPI that Gloo Portal calls to create and delete OAuth2 clients in the OpenID Connect identity provider protecting Portal APIs, so portal users can provision their own OAuth credentials
  name: Gloo Portal IdP Connect API
  slug: portal-idp-connect
- description: The webhook contract for the Guardrail feature in kgateway, Agentgateway Enterprise, and Gloo Gateway. Two endpoints — /request and /response — intercept prompts on the way to a large language model a
  name: AI Gateway Guardrail Webhook API
  slug: ai-guardrail-webhook
artifact_total: 11
asyncapis:
- description: ''
  name: Solo Io Webhooks
  slug: solo-io-webhooks
common:
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
created: '2026-08-02'
description: Solo.io is a cloud-native application-networking company founded in 2017 that builds enterprise and open-source API gateways, service mesh, and agentic-AI infrastructure. Its products include Kgateway Enterprise (formerly Gloo Gateway), an Envoy-powered Kubernetes Gateway API ingress and API gateway; Solo Enterprise for Istio (formerly Gloo Mesh), a hardened Istio service mesh with ambient mode; Agentgateway Enterprise, a Rust-based AI-native gateway for LLM, MCP, and A2A traffic; Kagent Enterprise, a Kubernetes-native agent runtime; and Agentregistry Enterprise, a registry for agents, MCP servers, and AI tools. Solo.io also ships Gloo Portal, a developer portal whose Portal Server REST API manages API products, teams, apps, subscriptions, API keys, and OAuth credentials, and contributes the kgateway, agentgateway, kagent, and Istio ambient-mesh open-source projects.
image: https://cdn.prod.website-files.com/66dba20a96c0aa281999f399/6704540db9215a5c14c38c6c_Webclip.png
layout: provider
mcp_servers:
- description: ''
  name: solo-io-mcp.yml
  slug: solo-io-mcpyml
modified: '2026-08-02'
name: Solo.io
nav: Providers
network: true
overview: 'Solo.io publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Gloo Portal Server API, Gloo Portal Backend API, Gloo Platform Portal API, and 2 more. Tagged areas include Company, API Gateway, Service Mesh, Kubernetes, and Istio.


  The Solo.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Solo.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
random_paper: 41
score:
  band: strong
  composite: 61.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.9
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 40.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
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
- Model Context Protocol
- Developer Portal
- Cloud Native
- Open Source
website: https://www.solo.io/
---
