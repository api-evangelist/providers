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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Primary GraphQL API for companies, tests, test sessions, live interviews, and interview templates. Authenticated with an API key.
  name: CodeSignal GraphQL API
  slug: codesignal-graphql-api
- description: Outbound webhook events across assessment, candidate, auditor, and live-interview workflows. Deliveries are signed with HMAC-SHA256.
  name: CodeSignal Webhook API
  slug: codesignal-webhook-api
- description: The Organization API from Codesignal — 5 operation(s) for organization.
  name: Codesignal Organization API
  slug: codesignal-organization-api
artifact_total: 12
asyncapis:
- description: ''
  name: Codesignal Webhooks
  slug: codesignal-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Codesignal Learn Public Organization API
  slug: open-codesignal-organization-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/codesignal-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/codesignal-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codesignal-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/codesignal-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/codesignal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/codesignal-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/codesignal-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codesignal-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/codesignal-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codesignal.com/
- group: other
  title: ''
  type: Overlay
  url: overlays/codesignal-learn-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codesignal-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/codesignal-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/codesignal-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/codesignal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://codesignal.com/security/disclosure-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.codesignal.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codesignal-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.codesignal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.codesignal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://codesignal.github.io/developer-docs/graphql/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codesignal
- group: operate
  title: ''
  type: Support
  url: https://support.codesignal.com/
- group: company
  title: ''
  type: Blog
  url: https://codesignal.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://codesignal.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.codesignal.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codesignal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codesignal.com/privacy
- group: company
  title: ''
  type: Website
  url: https://codesignal.com
created: '2026-07-17'
description: CodeSignal is a technical interview and skills-assessment platform used by companies to screen, interview, and upskill software engineers. Its developer surface includes a GraphQL API (companies, tests, test sessions, interviews, and interview templates), a versioned Learn REST API (OpenAPI 3.1) for organization members, skill sets, and learning progress, a webhook event API covering assessment, candidate, auditor, and live-interview workflows with HMAC-SHA256 signed deliveries, and an official remote MCP server that lets AI agents work with assessments, candidate sessions, and interviews. CodeSignal is backed by Menlo Ventures.
image: https://codesignal.com/wp-content/uploads/2022/12/codesignal-fallbck.jpg
layout: provider
mcp_servers:
- description: ''
  name: codesignal-mcp.yml
  slug: codesignal-mcpyml
modified: '2026-07-18'
name: Codesignal
nav: Providers
network: true
overview: 'Codesignal publishes 1 API on the [APIs.io](https://apis.io/) network: Organization API. Tagged areas include Company, Technical Interview, Skills Assessment, Hiring, and Recruiting.


  The Codesignal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Codesignal''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 20
scopes:
- name: Codesignal Scopes
  scope_count: 1
  slug: codesignal-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 54.9
  delta: 4.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 16.7
    contract_quality: 55.9
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 50.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 85.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codesignal/refs/heads/main/screenshots/codesignal-2026-07-25T205933.png
security:
- kind: authentication
  name: Codesignal Authentication
  slug: codesignal-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Codesignal Domain Security
  slug: codesignal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Codesignal Vulnerability Disclosure
  slug: codesignal-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Codesignal Trust Center
  slug: codesignal-trust-center
  summary_line: trust center published
slug: codesignal
tags:
- Company
- Technical Interview
- Skills Assessment
- Hiring
- Recruiting
- Developer Skills
- Assessment
- Education
- GraphQL
- Webhooks
website: https://codesignal.com
---
