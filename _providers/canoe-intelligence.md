---
access_model:
  confidence: high
  label: Enterprise sales gate
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://canoeintelligence.com/api-terms-of-use/
  - https://canoeintelligence.com/demo-request/
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
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Canoe Intelligence Agentic Access
  operation_count: 50
  slug: canoe-intelligence-agentic-access
  summary_line: 50 operations · 26 acting
api_count: 9
apis:
- description: The Allocations API from Canoe Intelligence — 2 operation(s) for allocations.
  name: Canoe Intelligence Allocations API
  slug: canoe-intelligence-allocations-api
- description: The Authentication API from Canoe Intelligence — 4 operation(s) for authentication.
  name: Canoe Intelligence Authentication API
  slug: canoe-intelligence-authentication-api
- description: The Custom Fields API from Canoe Intelligence — 1 operation(s) for custom fields.
  name: Canoe Intelligence Custom Fields API
  slug: canoe-intelligence-custom-fields-api
- description: The Documents API from Canoe Intelligence — 10 operation(s) for documents.
  name: Canoe Intelligence Documents API
  slug: canoe-intelligence-documents-api
- description: The Funds API from Canoe Intelligence — 6 operation(s) for funds.
  name: Canoe Intelligence Funds API
  slug: canoe-intelligence-funds-api
- description: The Organizations API from Canoe Intelligence — 9 operation(s) for organizations.
  name: Canoe Intelligence Organizations API
  slug: canoe-intelligence-organizations-api
- description: The Password Grant Tokens API from Canoe Intelligence — 1 operation(s) for password grant tokens.
  name: Canoe Intelligence Password Grant Tokens API
  slug: canoe-intelligence-password-grant-tokens-api
- description: The Terms API from Canoe Intelligence — 2 operation(s) for terms.
  name: Canoe Intelligence Terms API
  slug: canoe-intelligence-terms-api
- description: The User API from Canoe Intelligence — 4 operation(s) for user.
  name: Canoe Intelligence User API
  slug: canoe-intelligence-user-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canoe-intelligence-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canoe-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canoeintelligence.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.canoesoftware.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.canoesoftware.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.canoesoftware.com/docs
- group: start
  title: ''
  type: Login
  url: https://client.canoesoftware.com/auth/login
- group: operate
  title: ''
  type: Support
  url: https://canoeintelligence.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://canoeintelligence.com/category/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://canoeintelligence.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canoeintelligence.com/api-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canoeintelligence.com/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.canoeintelligence.com/
- group: auth
  title: ''
  type: Compliance
  url: https://canoeintelligence.com/implementation-data-security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canoe-intelligence-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://canoeintelligence.com/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/canoe-intelligence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/canoe-intelligence-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/canoe-intelligence-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canoe-intelligence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canoe-intelligence-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canoe-intelligence-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/canoe-intelligence-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canoe-intelligence-well-known.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/canoe-intelligence-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/canoe-intelligence-api-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/canoe-intelligence-examples.yml
created: '2026-08-09'
description: Canoe Intelligence is an alternative-investment data infrastructure platform that automates the collection, extraction, and validation of private-markets documents for institutional allocators, fund-of-funds, family offices, RIAs, fund administrators, and asset servicers. The platform retrieves capital call notices, distribution notices, capital account statements, K-1 tax documents, and related fund communications from GP portals and email, applies AI-based extraction across 50+ document types and a 2,586-field data library, validates the results against fund and LP records, and delivers structured data downstream. Canoe publishes a public REST API (Canoe API v1) at api.canoesoftware.com covering documents, funds, terms, organizations, entities, accounts, allocations, custom fields, and user management, documented with a public OpenAPI 3.0 definition and authenticated with OAuth 2.0 bearer/JWT access tokens.
image: https://canoeintelligence.com/wp-content/uploads/2024/07/canoe-OG.jpg
layout: provider
modified: '2026-08-09'
name: Canoe Intelligence
nav: Providers
network: true
overview: 'Canoe Intelligence publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Allocations API, Authentication API, Custom Fields API, and 6 more. Tagged areas include alternative-investments, private-markets, document-automation, data-extraction, and fund-administration.


  Canoe Intelligence''s developer surface includes documentation, API reference, support, engineering blog, authentication, code examples, and 22 more developer resources.'
random_paper: 30
scopes:
- name: Canoe Intelligence Scopes
  scope_count: 0
  slug: canoe-intelligence-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.8
    developer_ergonomics: 42.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Canoe Intelligence Authentication
  slug: canoe-intelligence-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Canoe Intelligence Domain Security
  slug: canoe-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canoe Intelligence Vulnerability Disclosure
  slug: canoe-intelligence-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Canoe Intelligence Trust Center
  slug: canoe-intelligence-trust-center
  summary_line: SOC 2 Type II
slug: canoe-intelligence
tags:
- alternative-investments
- private-markets
- document-automation
- data-extraction
- fund-administration
- capital-calls
- k-1-tax-documents
- portfolio-reporting
- financial-services
- fintech
- wealth-management
- institutional-investors
website: https://canoeintelligence.com/
---
