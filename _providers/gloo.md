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
api_count: 4
apis:
- description: Gloo Edge is a feature-rich, Kubernetes-native ingress controller and API gateway built on Envoy Proxy, supporting advanced routing, security policies, and observability for cloud-native workloads. It
  name: Gloo Edge
  slug: gloo-edge
- baseURL: https://docs.solo.io/gateway/latest/
  baseurl_source: declared
  description: Gloo Gateway is the next-generation API gateway from Solo.io built on Envoy Proxy and implementing the Kubernetes Gateway API specification. It provides advanced traffic management, security, and exte
  name: Gloo Gateway
  slug: gloo-gateway
- baseURL: https://docs.solo.io/gloo-mesh-enterprise/latest/
  baseurl_source: declared
  description: Gloo Mesh is an enterprise service mesh management platform from Solo.io built on Istio, providing multi-cluster and multi-mesh traffic management, security policy enforcement, and observability acros
  name: Gloo Mesh
  slug: gloo-mesh
- baseURL: https://docs.solo.io/gateway/latest/portal/
  baseurl_source: declared
  description: Gloo Portal is a developer portal product from Solo.io that enables organizations to expose, document, and manage API products for internal and external consumers. It integrates with Gloo Gateway to p
  name: Gloo Portal
  slug: gloo-portal
artifact_total: 12
asyncapis:
- description: ''
  name: Gloo Webhooks
  slug: gloo-webhooks
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/gloo-authentication.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/solo-io/gloo/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gloo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gloo-domain-security.yml
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
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.solo.io/gloo-edge/latest/getting_started/
- group: company
  title: ''
  type: Blog
  url: https://www.solo.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solo-io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/solo-io/gloo
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/solo-io/gloo/releases
- group: operate
  title: ''
  type: Community
  url: https://slack.solo.io/
- group: operate
  title: ''
  type: Support
  url: https://www.solo.io/company/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.solo.io/#website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.solo.io/#privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://docs.solo.io/gateway/latest/reference/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.solo.io/pricing
- group: auth
  title: ''
  type: Security
  url: https://www.solo.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.solo.io/
- group: build
  title: ''
  type: Packages
  url: packages/gloo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gloo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/gloo-cli.yml
- group: design
  title: ''
  type: Components
  url: components/gloo-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gloo-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gloo-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/gloo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gloo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gloo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gloo-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/gloo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gloo-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gloo-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gloo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gloo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gloo-finops.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gloo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gloo-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gloo-portal-server-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/gloo-platform-portal-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/gloo-idp-connect-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/gloo-ai-guardrail-webhook-overlay.yaml
created: '2026-03-18'
description: Gloo is Solo.io's family of open-source and enterprise API gateway, service mesh and developer portal products, built on Envoy Proxy and Istio and delivered as software the customer runs in their own Kubernetes clusters rather than as a hosted SaaS. Gloo Edge and Gloo Gateway provide ingress, advanced traffic management, external auth, rate limiting, WAF, GraphQL and AI/LLM traffic routing; Gloo Mesh manages multi-cluster Istio; and Gloo Portal publishes API products to internal and external consumers with teams, applications, subscriptions, API keys and OAuth credentials. Solo.io renamed its commercial line in 2026 — Gloo Gateway is now Solo Enterprise for kgateway and Gloo Mesh is now Solo Enterprise for Istio — and the upstream kgateway project is a conformant implementation of the Kubernetes Gateway API, passing 93 of 93 core and extended conformance tests against v1.6.1.
finops:
- name: Gloo Finops
  service_category: API
  slug: gloo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gloo.png
layout: provider
modified: '2026-09-12'
name: Gloo
nav: Providers
network: true
overview: 'Gloo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Gateway, Mesh, and Portal. Tagged areas include API Gateway, Cloud-Native, Developer Portal, Developer Tools, and Envoy.


  The Gloo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gloo''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, support, API reference, and 36 more developer resources.'
plans:
- name: Gloo Plans Pricing
  plan_count: 0
  slug: gloo-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Gloo Rate Limits
  slug: gloo-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/gloo/refs/heads/main/screenshots/gloo-2026-06-20T181923.png
security:
- kind: authentication
  name: Gloo Authentication
  slug: gloo-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Gloo Domain Security
  slug: gloo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gloo Vulnerability Disclosure
  slug: gloo-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Gloo Trust Center
  slug: gloo-trust-center
  summary_line: trust center published
slug: gloo
tags:
- API Gateway
- Cloud-Native
- Developer Portal
- Developer Tools
- Envoy
- Istio
- Kubernetes
- Kubernetes Gateway API
- Open-Source
- Service Mesh
website: https://www.solo.io/
---
