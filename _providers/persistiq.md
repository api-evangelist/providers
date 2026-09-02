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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Persistiq Agentic Access
  operation_count: 13
  slug: persistiq-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 2
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
- description: The Campaign Leads API from PersistIQ — 2 operation(s) for campaign leads.
  name: PersistIQ Campaign Leads API
  slug: persistiq-campaign-leads-api
- description: The DNC Domains API from PersistIQ — 1 operation(s) for dnc domains.
  name: PersistIQ DNC Domains API
  slug: persistiq-dnc-domains-api
- description: The Replies API from PersistIQ — 1 operation(s) for replies.
  name: PersistIQ Replies API
  slug: persistiq-replies-api
- description: The Tags API from PersistIQ — 1 operation(s) for tags.
  name: PersistIQ Tags API
  slug: persistiq-tags-api
- description: The Webhook Plugin API from PersistIQ — 1 operation(s) for webhook plugin.
  name: PersistIQ Webhook Plugin API
  slug: persistiq-webhook-plugin-api
artifact_total: 27
asyncapis:
- description: ''
  name: Persistiq Webhooks
  slug: persistiq-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PersistIQ Campaigns API
  slug: open-persistiq-campaigns-api
- collection_type: open
  name: PersistIQ Campaigns Do Not Contact Domains API
  slug: open-persistiq-do-not-contact-domains-api
- collection_type: open
  name: PersistIQ Campaigns Events API
  slug: open-persistiq-events-api
- collection_type: open
  name: PersistIQ Campaigns Lead Fields API
  slug: open-persistiq-lead-fields-api
- collection_type: open
  name: PersistIQ Campaigns Lead Statuses API
  slug: open-persistiq-lead-statuses-api
- collection_type: open
  name: PersistIQ Campaigns Leads API
  slug: open-persistiq-leads-api
- collection_type: open
  name: PersistIQ Campaigns Users API
  slug: open-persistiq-users-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/persistiq-handle-campaign-replies.md
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/persistiq-api-v1-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/persistiq-openapi-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/persistiq-api-v1-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/persistiq-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/persistiq-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/persistiq-changelog.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/persistiq-agentic-access.yml
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
- group: start
  title: ''
  type: GettingStarted
  url: http://help.persistiq.com/en/articles/466972-getting-started-guide
- group: operate
  title: ''
  type: Support
  url: http://help.persistiq.com/en/
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
description: PersistIQ is a sales engagement platform for small teams to find new customers, start conversations, and personalize sales outreach at scale from one place. It combines prospect research (Chrome extension), multi-channel outreach (email, calls, tasks), campaign management with A/B testing, performance analytics, and CRM integrations. PersistIQ exposes a REST API (v1) for users, leads (prospects), lead statuses and fields, tags, campaigns (including duplication and inbox replies), activity events, Do Not Contact domains, and a webhook plugin carrying five events. It is specified by PersistIQ's own OpenAPI 3.0.1 document, served from the API host at /api-docs/v1/swagger.json. Authentication is a single company-wide API key sent in the x-api-key header, with page-number pagination and a documented 100 request/minute per-key rate limit.
image: https://persistiq.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: PersistIQ MCP Server
  slug: persistiq-mcp-server
modified: '2026-08-13'
name: PersistIQ
nav: Providers
network: true
overview: 'PersistIQ publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Do Not Contact Domains API, Events API, and 9 more. Tagged areas include Company, Sales Engagement, Sales, Outbound, and Email Outreach.


  The PersistIQ catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PersistIQ''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 26 more developer resources.'
plans:
- name: Persistiq Plans Pricing
  plan_count: 0
  slug: persistiq-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Persistiq Rate Limits
  slug: persistiq-rate-limits
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 56.8
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/persistiq/refs/heads/main/screenshots/persistiq-2026-08-17T081210.png
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
- Webhook
- SEP
website: https://persistiq.com
---
