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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 10
  human_in_the_loop: 5
  name: Go1 Agentic Access
  operation_count: 20
  slug: go1-agentic-access
  summary_line: 20 operations · 10 acting · 5 human-in-the-loop
api_count: 1
apis:
- description: The Enrollments API from Go1 — 3 operation(s) for enrollments.
  name: Go1 Enrollments API
  slug: go1-enrollments-api
- description: The Learning objects API from Go1 — 5 operation(s) for learning objects.
  name: Go1 Learning objects API
  slug: go1-learning-objects-api
- description: The Portals API from Go1 — 2 operation(s) for portals.
  name: Go1 Portals API
  slug: go1-portals-api
- description: The Webhooks API from Go1 — 2 operation(s) for webhooks.
  name: Go1 Webhooks API
  slug: go1-webhooks-api
arazzos:
- description: Search the Go1 learning library, enroll a learner, and confirm the enrollment.
  name: Go1 — discover content and enroll a learner
  slug: go1-discover-and-enroll
- description: Create a customer portal and register a webhook subscription for Go1 events.
  name: Go1 — provision a portal and subscribe to events
  slug: go1-provision-portal-and-webhook
artifact_total: 18
asyncapis:
- description: ''
  name: Go1 Webhooks
  slug: go1-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/go1-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/go1-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/go1-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/go1-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/go1-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/go1-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/go1-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/go1-cli.yml
- group: design
  title: ''
  type: Components
  url: components/go1-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/go1-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/go1-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/go1-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/go1-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/go1-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/go1-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/go1-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/go1-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/go1-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.go1.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/go1-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/go1-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/go1-discover-and-enroll.yml
- group: design
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
image: https://www.go1.com/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: Go1 MCP Server
  slug: go1-mcp-server
modified: '2026-07-19'
name: Go1
nav: Providers
network: true
overview: 'Go1 publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Enrollments API, Learning objects API, Portals API, and 1 more. Tagged areas include Company, Edtech, Learning, E-Learning, and Corporate Training.


  The Go1 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Go1''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, support, engineering blog, and 29 more developer resources.'
random_paper: 11
scopes:
- name: Go1 Scopes
  scope_count: 8
  slug: go1-scopes
  summary_line: 8 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 60.9
  coverage:
    artifact_dirs: 25
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 68.9
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 61.5
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
    score: 74.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/go1/refs/heads/main/screenshots/go1-2026-07-25T220000.png
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
slug: go1
tags:
- Company
- Edtech
- Learning
- E-Learning
- Corporate Training
- Content
- Learning Management
- LMS
- Education
- Webhook
website: https://www.go1.com/
---
