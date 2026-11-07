---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 5
  name: Go1 Agentic Access
  operation_count: 20
  slug: go1-agentic-access
  summary_line: 20 operations · 10 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://gateway.go1.com
  baseurl_source: declared
  description: The Enrollments API from Go1 — 3 operation(s) for enrollments.
  name: Go1 Enrollments API
  slug: go1-enrollments-api
- baseURL: https://gateway.go1.com
  baseurl_source: declared
  description: The Learning objects API from Go1 — 5 operation(s) for learning objects.
  name: Go1 Learning objects API
  slug: go1-learning-objects-api
- baseURL: https://gateway.go1.com
  baseurl_source: declared
  description: The Portals API from Go1 — 2 operation(s) for portals.
  name: Go1 Portals API
  slug: go1-portals-api
- baseURL: https://gateway.go1.com
  baseurl_source: declared
  description: The Webhooks API from Go1 — 2 operation(s) for webhooks.
  name: Go1 Webhooks API
  slug: go1-webhooks-api
arazzos:
- description: Search the Go1 learning library, enroll a learner, and confirm the enrollment.
  name: Go1 — discover content and enroll a learner
  slug: go1-discover-and-enroll
- description: Create a customer portal and register a webhook subscription for Go1 events.
  name: Go1 — provision a portal and subscribe to events
  slug: go1-provision-portal-and-webhook
artifact_total: 21
asyncapis:
- description: ''
  name: Go1 Webhooks
  slug: go1-webhooks
collections:
- collection_type: open
  name: Go1 Enrollments API
  slug: open-go1-enrollments-api
- collection_type: open
  name: Go1 Enrollments Learning objects API
  slug: open-go1-learning-objects-api
- collection_type: open
  name: Go1 Enrollments Portals API
  slug: open-go1-portals-api
- collection_type: open
  name: Go1 Enrollments Webhooks API
  slug: open-go1-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/go1/plans/go1-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/go1-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/go1/capabilities/go1-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/go1-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/go1/security/go1-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/go1-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/go1/agentic-access/go1-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/go1-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/go1/scopes/go1-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/go1-scopes.yml
- group: auth
  href: https://artifacts.apis.io/go1/authentication/go1-authentication.yml
  title: ''
  type: Authentication
  url: authentication/go1-authentication.yml
- group: build
  href: https://artifacts.apis.io/go1/packages/go1-packages.yml
  title: ''
  type: Packages
  url: packages/go1-packages.yml
- group: build
  href: https://artifacts.apis.io/go1/packages/go1-packages.yml
  title: ''
  type: SDKs
  url: packages/go1-packages.yml
- group: build
  href: https://artifacts.apis.io/go1/cli/go1-cli.yml
  title: ''
  type: CLI
  url: cli/go1-cli.yml
- group: design
  href: https://artifacts.apis.io/go1/components/go1-components.yml
  title: ''
  type: Components
  url: components/go1-components.yml
- group: agent
  href: https://artifacts.apis.io/go1/well-known/go1-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/go1-well-known.yml
- group: agent
  href: https://artifacts.apis.io/go1/mcp/go1-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/go1-mcp.yml
- group: agent
  href: https://artifacts.apis.io/go1/llms/go1-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/go1-llms.txt
- group: other
  href: https://artifacts.apis.io/go1/overlays/go1-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/go1-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/go1/conformance/go1-conformance.yml
  title: ''
  type: Conformance
  url: conformance/go1-conformance.yml
- group: design
  href: https://artifacts.apis.io/go1/errors/go1-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/go1-problem-types.yml
- group: design
  href: https://artifacts.apis.io/go1/conventions/go1-conventions.yml
  title: ''
  type: Conventions
  url: conventions/go1-conventions.yml
- group: design
  href: https://artifacts.apis.io/go1/data-model/go1-data-model.yml
  title: ''
  type: DataModel
  url: data-model/go1-data-model.yml
- group: design
  href: https://artifacts.apis.io/go1/lifecycle/go1-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/go1-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.go1.com
- group: auth
  href: https://artifacts.apis.io/go1/security/go1-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/go1-trust-center.yml
- group: design
  href: https://artifacts.apis.io/go1/asyncapi/go1-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/go1-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/go1/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/go1/arazzo/go1-discover-and-enroll.yml
  title: ''
  type: Arazzo
  url: arazzo/go1-discover-and-enroll.yml
- group: design
  href: https://artifacts.apis.io/go1/arazzo/go1-provision-portal-and-webhook.yml
  title: ''
  type: Arazzo
  url: arazzo/go1-provision-portal-and-webhook.yml
- group: company
  title: ''
  type: Website
  url: https://www.go1.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.go1.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.go1.com/docs/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.go1.com/api/rest/2025-01-01/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.go1.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://help.go1.com/en
- group: company
  title: ''
  type: Blog
  url: https://www.go1.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/go1com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.go1.com/plans
- group: start
  title: ''
  type: SignUp
  url: https://www.go1.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.go1.com/terms/customer-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.go1.com/terms/privacy-policy
created: '2026-07-17'
description: Go1 is an AI-powered corporate learning and development (L&D) platform that consolidates employee training into a single subscription. Its content library aggregates courses from 250+ providers across 40+ languages, layered with curation, skill-based learning paths, reporting and the Morgan by Go1 learning agent, and connects to existing HR and business systems through 75+ integrations. The Go1 developer platform exposes a date-versioned REST API (gateway.go1.com, Api-Version header) for discovering learning objects, managing enrollments, provisioning customer portals and subscribing to events via webhooks, secured with OAuth 2.0, plus JavaScript/React embedding SDKs and a webhook-verifier library. Go1 is backed by SoftBank Vision Fund and Y Combinator.
finops:
- has_sources: true
  method: derived
  name: Go1 Finops
  primary_unit: ''
  service_category: ''
  slug: go1-finops
  template: true
image: https://www.go1.com/opengraph-image.png
layout: provider
modified: '2026-07-19'
name: Go1
nav: Providers
network: true
overview: 'Go1 publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Enrollments API, Learning objects API, Portals API, and 1 more. Tagged areas include Company, EdTech, Learning, E-Learning, and Corporate Training.


  The Go1 catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Go1''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, support, engineering blog, and 30 more developer resources.'
plans:
- name: Go1 Plans Pricing
  plan_count: 3
  slug: go1-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Go1 API Rules
  rule_count: 59
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 7
  slug: go1-rules
scopes:
- name: Go1 Scopes
  scope_count: 8
  slug: go1-scopes
  summary_line: 8 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 62.3
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 65.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/go1/go1-2026-07-25T220000.png
security:
- kind: authentication
  name: Go1 Authentication
  slug: go1-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Go1 Domain Security
  slug: go1-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Go1 Trust Center
  slug: go1-trust-center
  summary_line: trust center published
skill_count: 2
skills:
- name: Discover Go1 content and enroll a learner
  slug: go1-discover-and-enroll
- name: Provision a Go1 portal and subscribe to events
  slug: go1-provision-portal-and-webhook
slug: go1
tags:
- Company
- EdTech
- Learning
- E-Learning
- Corporate Training
- Content
- LMS
- Education
- Webhook
website: https://www.go1.com/
---
