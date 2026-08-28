---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Loopio Public API v2 is a REST API over the Loopio response management platform. It exposes the Library (entries, attachments, history, stacks, tags), Projects (entries, sections, subSections, par
  name: Loopio Public API v2
  slug: loopio-public-api-v2
artifact_total: 7
asyncapis:
- description: ''
  name: Loopio Events Webhooks
  slug: loopio-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loopio-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/loopio-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loopio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://loopio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.loopio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.loopio.com/docs/loopio-api/c56ffe1fdae3e-getting-started-with-the-loopio-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.loopio.com/docs/loopio-api/68a341c676710-loopio
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.loopio.com/docs/loopio-api/c56ffe1fdae3e-getting-started-with-the-loopio-api
- group: operate
  title: ''
  type: Support
  url: https://support.loopio.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://loopio.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://loopio.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loopio.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loopio.com/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.loopiostatus.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/loopio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loopio-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/loopio-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loopio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loopio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loopio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loopio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loopio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://loopio.com/legal/compliance-statement/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/loopio-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loopio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/loopio-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/loopio-openapi-overlay.yaml
created: '2026-08-25'
description: Loopio is a Toronto-based response management platform used by teams to answer RFPs, RFIs, DDQs, and security questionnaires from a governed, reusable content Library. It publishes a public REST API — the Loopio Public API v2 at https://api.loopio.com/data/v2 — documented on a Stoplight developer portal at developer.loopio.com, with a 96-operation OpenAPI 3.0.1 contract covering Library Entries, Projects, Project Entries, Sections and subSections, Custom Project Fields, Merge Variables, Compliance Sets, Project Templates, Stacks, Tags, Teams, Users, Roles, Files, CRM opportunity links, asynchronous task status, and webhook subscriptions. Authentication is OAuth 2.0 client credentials against https://api.loopio.com/oauth2/access_token with 22 in-spec scopes, and the authorization server publishes RFC 8414 and RFC 9728 discovery documents that advertise a wider 51-scope surface including SCIM user/group provisioning and MCP tool/prompt/resource scopes.
image: https://cdn.loopio.com/cache/8.328.b01/resources/images/favicon.png
layout: provider
modified: '2026-08-25'
name: Loopio
nav: Providers
network: true
overview: 'Loopio publishes 1 API on the [APIs.io](https://apis.io/) network: Public API v2. Tagged areas include Company, RFP, Proposals, Response Management, and Content Library.


  The Loopio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Loopio''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Loopio Plans Pricing
  plan_count: 0
  slug: loopio-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Loopio Rate Limits
  slug: loopio-rate-limits
scopes:
- name: Loopio Scopes
  scope_count: 52
  slug: loopio-scopes
  summary_line: 52 scopes
score:
  band: thin
  composite: 37.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 30.3
    contract_quality: 61.6
    developer_ergonomics: 18.5
    discoverability: 79.6
    governance: 30.3
    operational_transparency: 23.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Loopio Authentication
  slug: loopio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Loopio Domain Security
  slug: loopio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loopio
tags:
- Company
- RFP
- Proposals
- Response Management
- Content Library
- Sales Enablement
- Questionnaires
- Compliance
- Collaboration
- Documents
- Webhooks
- SaaS
website: https://loopio.com/
---
