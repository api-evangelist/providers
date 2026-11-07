---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Gloo Edge is a feature-rich, Kubernetes-native ingress controller and API gateway built on Envoy Proxy, supporting advanced routing, security policies, and observability for cloud-native workloads. It
  name: Gloo Edge
  slug: gloo-edge
- baseURL: https://docs.solo.io/gloo-edge/latest/
  baseurl_source: declared
  description: The API Products API from Gloo — 3 operation(s) for api products.
  name: Gloo API Products API
  slug: gloo-api-products-api
- baseURL: https://docs.solo.io/gloo-edge/latest/
  baseurl_source: declared
  description: The Applications API from Gloo — 8 operation(s) for applications.
  name: Gloo Applications API
  slug: gloo-applications-api
- baseURL: https://docs.solo.io/gloo-edge/latest/
  baseurl_source: declared
  description: The Me API from Gloo — 1 operation(s) for me.
  name: Gloo Me API
  slug: gloo-me-api
- baseURL: https://docs.solo.io/gloo-edge/latest/
  baseurl_source: declared
  description: The Subscriptions API from Gloo — 2 operation(s) for subscriptions.
  name: Gloo Subscriptions API
  slug: gloo-subscriptions-api
- baseURL: https://docs.solo.io/gloo-edge/latest/
  baseurl_source: declared
  description: The Teams API from Gloo — 5 operation(s) for teams.
  name: Gloo Teams API
  slug: gloo-teams-api
- baseURL: https://docs.solo.io/gloo-edge/latest/
  baseurl_source: declared
  description: The User API from Gloo — 1 operation(s) for user.
  name: Gloo User API
  slug: gloo-user-api
- baseURL: https://docs.solo.io/gloo-edge/latest/
  baseurl_source: declared
  description: The Webhooks API from Gloo — 2 operation(s) for webhooks.
  name: Gloo Webhooks API
  slug: gloo-webhooks-api
- baseURL: https://docs.solo.io/gloo-edge/latest/
  baseurl_source: declared
  description: The APIs API from Gloo — 5 operation(s) for apis.
  name: Gloo APIs API
  slug: gloo-apis-api
artifact_total: 21
asyncapis:
- description: ''
  name: Gloo Webhooks
  slug: gloo-webhooks
common:
- group: other
  href: https://artifacts.apis.io/gloo/capabilities/gloo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gloo-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/gloo/authentication/gloo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gloo-authentication.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/solo-io/gloo/blob/main/LICENSE
- group: auth
  href: https://artifacts.apis.io/gloo/security/gloo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gloo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gloo/security/gloo-domain-security.yml
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
  href: https://artifacts.apis.io/gloo/packages/gloo-packages.yml
  title: ''
  type: Packages
  url: packages/gloo-packages.yml
- group: build
  href: https://artifacts.apis.io/gloo/packages/gloo-packages.yml
  title: ''
  type: SDKs
  url: packages/gloo-packages.yml
- group: build
  href: https://artifacts.apis.io/gloo/cli/gloo-cli.yml
  title: ''
  type: CLI
  url: cli/gloo-cli.yml
- group: design
  href: https://artifacts.apis.io/gloo/components/gloo-components.yml
  title: ''
  type: Components
  url: components/gloo-components.yml
- group: start
  href: https://artifacts.apis.io/gloo/sandbox/gloo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gloo-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/gloo/llms/gloo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gloo-llms.txt
- group: design
  href: https://artifacts.apis.io/gloo/conventions/gloo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gloo-conventions.yml
- group: design
  href: https://artifacts.apis.io/gloo/conformance/gloo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gloo-conformance.yml
- group: design
  href: https://artifacts.apis.io/gloo/errors/gloo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gloo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gloo/lifecycle/gloo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gloo-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/gloo/lifecycle/gloo-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/gloo-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/gloo/changelog/gloo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gloo-changelog.yml
- group: design
  href: https://artifacts.apis.io/gloo/data-model/gloo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gloo-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/gloo/plans/gloo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gloo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gloo/rate-limits/gloo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gloo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gloo/finops/gloo-finops.yml
  title: ''
  type: FinOps
  url: finops/gloo-finops.yml
- group: agent
  href: https://artifacts.apis.io/gloo/mcp/gloo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gloo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gloo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gloo/asyncapi/gloo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gloo-webhooks.yml
- group: other
  href: https://artifacts.apis.io/gloo/overlays/gloo-portal-server-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gloo-portal-server-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gloo/overlays/gloo-platform-portal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gloo-platform-portal-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gloo/overlays/gloo-idp-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gloo-idp-connect-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gloo/overlays/gloo-ai-guardrail-webhook-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gloo-ai-guardrail-webhook-overlay.yaml
created: '2026-03-18'
description: Gloo is Solo.io's family of open-source and enterprise API gateway, service mesh and developer portal products, built on Envoy Proxy and Istio and delivered as software the customer runs in their own Kubernetes clusters rather than as a hosted SaaS. Gloo Edge and Gloo Gateway provide ingress, advanced traffic management, external auth, rate limiting, WAF, GraphQL and AI/LLM traffic routing; Gloo Mesh manages multi-cluster Istio; and Gloo Portal publishes API products to internal and external consumers with teams, applications, subscriptions, API keys and OAuth credentials. Solo.io renamed its commercial line in 2026 — Gloo Gateway is now Solo Enterprise for kgateway and Gloo Mesh is now Solo Enterprise for Istio — and the upstream kgateway project is a conformant implementation of the Kubernetes Gateway API, passing 93 of 93 core and extended conformance tests against v1.6.1.
finops:
- has_sources: true
  method: derived
  name: Gloo Finops
  primary_unit: ''
  service_category: ''
  slug: gloo-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gloo.png
layout: provider
modified: '2026-09-12'
name: Gloo
nav: Providers
network: true
overview: 'Gloo publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Products API, Applications API, Me API, and 6 more. Tagged areas include API Gateway, Cloud-Native, Developer Portal, Envoy, and Istio.


  The Gloo catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Gloo''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, support, API reference, and 37 more developer resources.'
plans:
- name: Gloo Plans Pricing
  plan_count: 0
  slug: gloo-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Gloo Rate Limits
  slug: gloo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Gloo API Rules
  rule_count: 54
  severity_counts:
    error: 42
    hint: 0
    info: 3
    warn: 9
  slug: gloo-rules
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 31.8
    contract_quality: 58.5
    developer_ergonomics: 80.4
    discoverability: 78.6
    operational_transparency: 44.7
  previous_composite: 57.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/gloo/gloo-2026-06-20T181923.png
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
skill_count: 3
skills:
- name: gloo-audit-portal-access
  slug: gloo-audit-portal-access
- name: gloo-onboard-developer-to-api-product
  slug: gloo-onboard-developer-to-api-product
- name: gloo-rotate-portal-credentials
  slug: gloo-rotate-portal-credentials
slug: gloo
tags:
- API Gateway
- Cloud-Native
- Developer Portal
- Envoy
- Istio
- Kubernetes
- Kubernetes Gateway API
- Open Source
- Service Mesh
website: https://www.solo.io/
---
