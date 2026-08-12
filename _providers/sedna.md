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
  band_gated_from: agent-native
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
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 81
  human_in_the_loop: 4
  name: Sedna Agentic Access
  operation_count: 162
  slug: sedna-agentic-access
  summary_line: 162 operations · 81 acting · 4 human-in-the-loop
api_count: 17
apis:
- description: The Authentication API from SEDNA — 1 operation(s) for authentication.
  name: SEDNA Authentication API
  slug: sedna-authentication-api
- description: The Category Tag API API from SEDNA — 7 operation(s) for category tag api.
  name: SEDNA Category Tag API API
  slug: sedna-category-tag-api-api
- description: The Comment API API from SEDNA — 1 operation(s) for comment api.
  name: SEDNA Comment API API
  slug: sedna-comment-api-api
- description: The Company API API from SEDNA — 1 operation(s) for company api.
  name: SEDNA Company API API
  slug: sedna-company-api-api
- description: The Contact API API from SEDNA — 8 operation(s) for contact api.
  name: SEDNA Contact API API
  slug: sedna-contact-api-api
- description: The Document API API from SEDNA — 1 operation(s) for document api.
  name: SEDNA Document API API
  slug: sedna-document-api-api
- description: The Download API API from SEDNA — 4 operation(s) for download api.
  name: SEDNA Download API API
  slug: sedna-download-api-api
- description: The Event API API from SEDNA — 9 operation(s) for event api.
  name: SEDNA Event API API
  slug: sedna-event-api-api
- description: The Job Reference API API from SEDNA — 7 operation(s) for job reference api.
  name: SEDNA Job Reference API API
  slug: sedna-job-reference-api-api
- description: The Keyword API API from SEDNA — 3 operation(s) for keyword api.
  name: SEDNA Keyword API API
  slug: sedna-keyword-api-api
- description: The Message API API from SEDNA — 19 operation(s) for message api.
  name: SEDNA Message API API
  slug: sedna-message-api-api
- description: The Saved Search API API from SEDNA — 2 operation(s) for saved search api.
  name: SEDNA Saved Search API API
  slug: sedna-saved-search-api-api
- description: The Team API API from SEDNA — 9 operation(s) for team api.
  name: SEDNA Team API API
  slug: sedna-team-api-api
- description: The Template API API from SEDNA — 2 operation(s) for template api.
  name: SEDNA Template API API
  slug: sedna-template-api-api
- description: The User API API from SEDNA — 16 operation(s) for user api.
  name: SEDNA User API API
  slug: sedna-user-api-api
- description: The Vessel API API from SEDNA — 1 operation(s) for vessel api.
  name: SEDNA Vessel API API
  slug: sedna-vessel-api-api
- description: The Workflow API API from SEDNA — 2 operation(s) for workflow api.
  name: SEDNA Workflow API API
  slug: sedna-workflow-api-api
artifact_total: 22
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sedna-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.sedna.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.sedna.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.sedna.com/reference
- group: operate
  title: ''
  type: Support
  url: https://support.sedna.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://sedna.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sedna.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sedna.com/legal
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sedna.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/sedna-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sedna-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sedna-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sedna-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sedna-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sedna-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sedna-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sedna-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sedna-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sedna-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sedna-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sedna-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sedna-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sedna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sedna.com/
created: '2026-07-17'
description: SEDNA is the operating system for shipping — a communications and workflow platform that unifies email, voyage and trade operations, and document handling for maritime, commodity trading and logistics teams. Its API (version 2019-01-01) exposes messages, contacts, teams, users, job references, category tags, events and workflows over a JSON:API-style REST interface secured with OAuth 2.0 client-credentials, letting developers automate inbox routing, tagging, subscriptions and third-party integrations. Backed by Insight Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sedna.png
layout: provider
mcp_servers:
- description: ''
  name: sedna-mcp.yml
  slug: sedna-mcpyml
modified: '2026-07-21'
name: SEDNA
nav: Providers
network: true
overview: 'SEDNA publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Category Tag API API, Comment API API, and 14 more. Tagged areas include Company, Shipping, Maritime, Email, and Communications.


  SEDNA''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 20 more developer resources.'
random_paper: 59
scopes:
- name: Sedna Scopes
  scope_count: 53
  slug: sedna-scopes
  summary_line: 53 scopes · clientCredentials
score:
  band: thin
  composite: 41.6
  delta: -4.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 47.2
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Sedna Authentication
  slug: sedna-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sedna Domain Security
  slug: sedna-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sedna
tags:
- Company
- Shipping
- Maritime
- Email
- Communications
- Workflow
- Commodity Trading
- Logistics
- Messaging
website: https://sedna.com/
---
