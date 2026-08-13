---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 34
  human_in_the_loop: 34
  name: Yuzu Health Agentic Access
  operation_count: 76
  slug: yuzu-health-agentic-access
  summary_line: 76 operations · 34 acting · 34 human-in-the-loop
api_count: 10
apis:
- description: The Accumulator (Experimental) API from Yuzu Health — 2 operation(s) for accumulator (experimental).
  name: Yuzu Health Accumulator (Experimental) API
  slug: yuzu-health-accumulator-experimental-api
- description: The Benefits API from Yuzu Health — 2 operation(s) for benefits.
  name: Yuzu Health Benefits API
  slug: yuzu-health-benefits-api
- description: The Coverage API from Yuzu Health — 3 operation(s) for coverage.
  name: Yuzu Health Coverage API
  slug: yuzu-health-coverage-api
- description: The Enrollment API from Yuzu Health — 3 operation(s) for enrollment.
  name: Yuzu Health Enrollment API
  slug: yuzu-health-enrollment-api
- description: The EOB (Experimental) API from Yuzu Health — 1 operation(s) for eob (experimental).
  name: Yuzu Health EOB (Experimental) API
  slug: yuzu-health-eob-experimental-api
- description: The Group Policy API from Yuzu Health — 2 operation(s) for group policy.
  name: Yuzu Health Group Policy API
  slug: yuzu-health-group-policy-api
- description: The Member API from Yuzu Health — 3 operation(s) for member.
  name: Yuzu Health Member API
  slug: yuzu-health-member-api
- description: The PublicApiV1 API from Yuzu Health — 34 operation(s) for publicapiv1.
  name: Yuzu Health PublicApiV1 API
  slug: yuzu-health-publicapiv1-api
- description: The PublicApiV2 API from Yuzu Health — 14 operation(s) for publicapiv2.
  name: Yuzu Health PublicApiV2 API
  slug: yuzu-health-publicapiv2-api
- description: The Sponsor API from Yuzu Health — 1 operation(s) for sponsor.
  name: Yuzu Health Sponsor API
  slug: yuzu-health-sponsor-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://yuzu.health
- group: docs
  title: ''
  type: Documentation
  url: https://yuzu.health/docs/guides/api
- group: docs
  title: ''
  type: APIReference
  url: https://api.yuzu.health/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://yuzu.health/docs/guides/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://yuzu.health/docs/guides/api
- group: company
  title: ''
  type: Blog
  url: https://yuzu.health/blog
- group: operate
  title: ''
  type: Support
  url: https://yuzu.health/contact
- group: start
  title: ''
  type: Login
  url: https://yuzu.health/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yuzu.health/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yuzu.health/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yuzu-health
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yuzu.health
- group: operate
  title: ''
  type: Deprecation
  url: https://yuzu.health/docs/guides/api
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.yuzu.health
- group: auth
  title: ''
  type: Authentication
  url: authentication/yuzu-health-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yuzu-health-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yuzu-health-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yuzu-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yuzu-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yuzu-health-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/yuzu-health-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yuzu-health-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yuzu-health-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yuzu-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yuzu-health-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yuzu-health-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/yuzu-health-openapi-overlay.yaml
created: '2026-07-17'
description: Yuzu Health is a technology platform for building and operating custom, self-funded health plans end to end - plan design, member enrollment and eligibility, in-house medical and pharmacy claims adjudication, benefit accumulators, EOBs, ID cards, and payments - without legacy TPA systems. Its public REST API (bearer-JWT API keys, URL-prefix versioning v1/v2/v3, cursor pagination) exposes 76 operations across members, sponsors, groups/policies, coverages, claims, enrollment, benefits, care events, and accumulators, plus a white-label portal. Yuzu is backed by General Catalyst and Menlo Ventures.
image: https://cdn.yuzu.health/image.png
layout: provider
mcp_servers:
- description: ''
  name: yuzu-health-mcp.yml
  slug: yuzu-health-mcpyml
modified: '2026-07-21'
name: Yuzu Health
nav: Providers
network: true
overview: 'Yuzu Health publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accumulator (Experimental) API, Benefits API, Coverage API, and 7 more. Tagged areas include Company, Health, Healthcare, Insurance, and Health Plans.


  Yuzu Health''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 21 more developer resources.'
random_paper: 72
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 49.4
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Yuzu Health Authentication
  slug: yuzu-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yuzu Health Domain Security
  slug: yuzu-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Yuzu Health Trust Center
  slug: yuzu-health-trust-center
  summary_line: trust center published
slug: yuzu-health
tags:
- Company
- Health
- Healthcare
- Insurance
- Health Plans
- Benefits Administration
- Claims
- Enrollment
- Payers
- Self-Funded
website: https://yuzu.health
---
