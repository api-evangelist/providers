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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Ontraport Agentic Access
  operation_count: 11
  slug: ontraport-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 4
apis:
- description: RESTful API providing CRUD access to contacts, transactions, tags, sequences, forms, landing pages, and ecommerce objects. Authentication uses two headers, Api-Key and Api-Appid, on every request, wit
  name: Ontraport REST API
  slug: rest-api
- description: Object metadata and field information.
  name: Ontraport Metadata API
  slug: ontraport-metadata-api
- description: Generic CRUD operations across Ontraport object types.
  name: Ontraport Objects API
  slug: ontraport-objects-api
- description: Ontraport's first-party, hosted, remote MCP server. A streamable-HTTP endpoint an agent POSTs to directly at https://mcp.ontraport.com — there is no package to install and no local stdio process. It i
  name: Ontraport MCP Server
  slug: mcp
artifact_total: 18
asyncapis:
- description: ''
  name: Ontraport Webhooks
  slug: ontraport-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ontraport REST Metadata API
  slug: open-ontraport-metadata-api
- collection_type: open
  name: Ontraport REST Metadata Objects API
  slug: open-ontraport-objects-api
- collection_type: open
  name: Ontraport REST API
  slug: open-ontraport
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ontraport-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ontraport-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ontraport-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ontraport-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ontraport-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/ontraport-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ontraport-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ontraport-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ontraport-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ontraport-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ontraport-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ontraport-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ontraport-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ontraport-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ontraport-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ontraportstatus.com
- group: design
  title: ''
  type: Conformance
  url: conformance/ontraport-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/ontraport-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ontraport-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ontraport-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ontraport-plans-pricing.yml
- group: build
  title: ''
  type: PostmanCollection
  url: collections/ontraport.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/ontraport.opencollection.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ontraport-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ontraport-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ontraport
- group: company
  title: ''
  type: Website
  url: https://ontraport.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.ontraport.com/doc/
- group: commercial
  title: ''
  type: Pricing
  url: https://ontraport.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://ontraport.com/freetrial
- group: operate
  title: ''
  type: Support
  url: https://support.ontraport.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ontraport
- group: company
  title: ''
  type: Blog
  url: https://ontraport.com/blog/feed/
- group: docs
  title: ''
  type: APIReference
  url: https://api.ontraport.com/doc/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ontraport.com/features/platform/api
- group: start
  title: ''
  type: GettingStarted
  url: https://api.ontraport.com/doc/#authentication
- group: start
  title: ''
  type: Login
  url: https://app.ontraport.com/login.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ontraport.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ontraport.com/legal
- group: operate
  title: ''
  type: HelpCenter
  url: https://ontraport.com/support
- group: company
  title: ''
  type: About
  url: https://ontraport.com/about
- group: company
  title: ''
  type: Careers
  url: https://ontraport.com/careers
created: '2026-05-11'
description: Ontraport is a business automation platform combining CRM, marketing automation, email marketing, landing pages, ecommerce, and membership site capabilities for small businesses and entrepreneurs. The platform unifies contact management, sales pipelines, payment processing, and visual automation campaigns in a single workspace. Ontraport's REST API exposes contacts, transactions, tags, sequences, forms, landing pages, and ecommerce objects using API-Key and Api-Appid header authentication, through a generic object interface where the record type is selected by an integer object type ID rather than by a path segment. Ontraport also runs a first-party remote MCP server at https://mcp.ontraport.com, publishing 47 tools across CRUD, query, management and commerce and authorizing them with OAuth 2.1 (PKCE, dynamic client registration) under a single mcp:tools scope.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ontraport.png
layout: provider
mcp_servers:
- description: ''
  name: ontraport-mcp.yml
  slug: ontraport-mcpyml
modified: '2026-08-13'
name: Ontraport
nav: Providers
network: true
overview: 'Ontraport publishes 2 APIs on the [APIs.io](https://apis.io/) network: Metadata API and Objects API. Tagged areas include CRM, Marketing Automation, Email Marketing, Ecommerce, and Landing Pages.


  The Ontraport catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ontraport''s developer surface includes changelog, authentication, documentation, pricing, signup flow, support, engineering blog, and 36 more developer resources.'
plans:
- name: Ontraport Plans Pricing
  plan_count: 5
  slug: ontraport-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 1
  name: Ontraport Rate Limits
  slug: ontraport-rate-limits
scopes:
- name: Ontraport Scopes
  scope_count: 0
  slug: ontraport-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.7
  delta: 36.6
  facets:
    commercial_clarity: 92.1
    contract_quality: 61.2
    developer_ergonomics: 78.3
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 65.8
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ontraport/refs/heads/main/screenshots/ontraport-2026-06-20T190730.png
security:
- kind: authentication
  name: Ontraport Authentication
  slug: ontraport-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Ontraport Domain Security
  slug: ontraport-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ontraport Vulnerability Disclosure
  slug: ontraport-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Ontraport Trust Center
  slug: ontraport-trust-center
  summary_line: PCI DSS, GDPR
slug: ontraport
tags:
- CRM
- Marketing Automation
- Email Marketing
- Ecommerce
- Landing Pages
- Membership Sites
- MCP
- AI Agents
- Payments
- Sales Automation
website: https://ontraport.com
---
