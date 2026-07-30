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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Persistiq Agentic Access
  operation_count: 13
  slug: persistiq-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 7
apis:
- description: Outreach campaigns
  name: PersistIQ Campaigns API
  slug: persistiq-campaigns-api
- description: Suppressed domains
  name: PersistIQ Do Not Contact Domains API
  slug: persistiq-do-not-contact-domains-api
- description: Activity events
  name: PersistIQ Events API
  slug: persistiq-events-api
- description: Lead field definitions
  name: PersistIQ Lead Fields API
  slug: persistiq-lead-fields-api
- description: Lead status definitions
  name: PersistIQ Lead Statuses API
  slug: persistiq-lead-statuses-api
- description: Leads (prospects)
  name: PersistIQ Leads API
  slug: persistiq-leads-api
- description: Company users
  name: PersistIQ Users API
  slug: persistiq-users-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/persistiq-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/persistiq-well-known.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PersistIQ
- group: auth
  title: ''
  type: DomainSecurity
  url: security/persistiq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/persistiq-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/persistiq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/persistiq-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/persistiq-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/persistiq-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/persistiq-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/persistiq-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/persistiq-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/persistiq-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/persistiq-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.persistiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.persistiq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.persistiq.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.persistiq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.persistiq.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://persistiq.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://persistiq.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.persistiq.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.persistiq.com/privacy/
- group: company
  title: ''
  type: Website
  url: https://persistiq.com
created: '2026-07-17'
description: PersistIQ is a sales engagement platform for small teams to find new customers, start conversations, and personalize sales outreach at scale from one place. It combines prospect research (Chrome extension), multi-channel outreach (email, calls, tasks), campaign management with A/B testing, performance analytics, and CRM integrations. PersistIQ exposes a REST API (v1) for users, leads (prospects), lead statuses and fields, campaigns, activity events, and Do Not Contact domains, authenticated with a company-wide API key sent in the x-api-key header, with cursor pagination and a 100 request/minute per-key rate limit.
image: https://persistiq.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: persistiq-mcp.yml
  slug: persistiq-mcpyml
modified: '2026-07-20'
name: PersistIQ
nav: Providers
network: true
overview: 'PersistIQ publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Do Not Contact Domains API, Events API, and 4 more. Tagged areas include Company, Sales Engagement, Sales, Outbound, and Email Outreach.


  PersistIQ''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Persistiq Rate Limits
  slug: persistiq-rate-limits
score:
  band: developing
  composite: 46.1
  delta: -1.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.6
    developer_ergonomics: 40.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Persistiq Authentication
  slug: persistiq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Persistiq Domain Security
  slug: persistiq-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: persistiq
tags:
- Company
- Sales Engagement
- Sales
- Outbound
- Email Outreach
- CRM
- Lead Management
- Marketing
website: https://persistiq.com
---
