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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Uncapped Agentic Access
  operation_count: 14
  slug: uncapped-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 5
apis:
- description: Applicant API for external access
  name: Uncapped Applicants API
  slug: uncapped-applicants-api
- description: Application API for external access
  name: Uncapped Applications API
  slug: uncapped-applications-api
- description: Authentication API for external access
  name: Uncapped Authentication API
  slug: uncapped-authentication-api
- description: Estimations API for external access
  name: Uncapped Estimations API
  slug: uncapped-estimations-api
- description: Webhook Subscriptions API for external access
  name: Uncapped Webhook Subscriptions API
  slug: uncapped-webhook-subscriptions-api
artifact_total: 16
asyncapis:
- description: ''
  name: Uncapped Webhooks
  slug: uncapped-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: api-partners Applicants API
  slug: open-uncapped-applicants-api
- collection_type: open
  name: api-partners Applicants Applications API
  slug: open-uncapped-applications-api
- collection_type: open
  name: api-partners Applicants Authentication API
  slug: open-uncapped-authentication-api
- collection_type: open
  name: api-partners Applicants Estimations API
  slug: open-uncapped-estimations-api
- collection_type: open
  name: api-partners Applicants Webhook Subscriptions API
  slug: open-uncapped-webhook-subscriptions-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/uncapped-partners-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uncapped-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uncapped-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uncapped-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://weareuncapped.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.weareuncapped.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.weareuncapped.com/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.weareuncapped.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://developers.weareuncapped.com/api-reference
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uncapped-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.weareuncapped.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weareuncapped-com
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uncapped-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uncapped-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uncapped-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uncapped-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/uncapped-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uncapped-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uncapped-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uncapped-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uncapped-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Uncapped provides working capital to online businesses, offering revenue-based financing products including merchant cash advances (MCA), term loans, and lines of credit (LOC). Through the Uncapped Partners API, platforms and marketplaces can embed business funding directly into their product without taking on origination, compliance, or servicing - submitting anonymised applicant performance data, generating pre-offer estimations, displaying ready-to-use funding Signals in their UI, and reacting to application and estimation lifecycle events via webhooks.
image: https://developers.weareuncapped.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: uncapped-mcp.yml
  slug: uncapped-mcpyml
modified: '2026-07-21'
name: Uncapped
nav: Providers
network: true
overview: 'Uncapped publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applicants API, Applications API, Authentication API, and 2 more. Tagged areas include Company, Fintech, Lending, Embedded Finance, and Revenue-Based Financing.


  The Uncapped catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Uncapped''s developer surface includes authentication, documentation, getting-started guide, API reference, changelog, sandbox, and 16 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 35.0
  delta: -8.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 69.1
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/uncapped/refs/heads/main/screenshots/uncapped-2026-08-17T082550.png
security:
- kind: authentication
  name: Uncapped Authentication
  slug: uncapped-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uncapped Domain Security
  slug: uncapped-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uncapped
tags:
- Company
- Fintech
- Lending
- Embedded Finance
- Revenue-Based Financing
- Working Capital
- eCommerce
website: https://weareuncapped.com
---
