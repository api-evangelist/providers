---
access_model:
  confidence: high
  label: Self-service with free trial
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://www.nimble.com/pricing/
  - https://support.nimble.com/en/articles/502755-nimble-api-access
  trial: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 70
  human_in_the_loop: 0
  name: Nimble Agentic Access
  operation_count: 96
  slug: nimble-agentic-access
  summary_line: 96 operations · 70 acting
api_count: 13
apis:
- description: The Nimble CRM REST API — 89 operations across contacts, contact custom fields, contact and deal pipelines, deals, leads, activities, tasks, messages and users. Nimble publishes a full OpenAPI 3.0.0 c
  name: Nimble REST API
  slug: rest-api
- description: Account activity stream — list activities across contacts and deals, walked with a next_tstamp timestamp cursor. 1 operation(s).
  name: Nimble Activities API
  slug: nimble-activities-api
- description: Contact records — the Nimble platform root object. Create, read, update and delete person and company contacts, search them with keyword or the advanced JSON query syntax, manage notes and tags. Conta
  name: Nimble Contacts API
  slug: nimble-contacts-api
- description: User-definable contact field schema — fields, choice option lists, field groups and tabs, plus primary-value marks on multi-valued fields. The field set differs per account and must be read before wri
  name: Nimble Contacts Fields API
  slug: nimble-contacts-fields-api
- description: Contact pipelines — the lead-progression surface for contacts, distinct from deal pipelines. 8 operation(s).
  name: Nimble Contacts Pipelines API
  slug: nimble-contacts-pipelines-api
- description: Deals on the /api/v2 surface — create, update and delete deals, attach notes and files, manage deal tags, list overdue activity and read the won-last-month rollup. 18 operation(s).
  name: Nimble Deals API
  slug: nimble-deals-api
- description: Deal field surface — the user deal field list and the column catalogue backing Nimble's deal listing views. 2 operation(s).
  name: Nimble Deals Fields API
  slug: nimble-deals-fields-api
- description: Deal pipelines and stages — create and reshape pipelines, add and archive stages, set lost reasons, and read the deal book grouped by stage or by owner. 13 operation(s).
  name: Nimble Deals Pipelines API
  slug: nimble-deals-pipelines-api
- description: Per-pipeline deal custom fields — fields, choice lists and field groups scoped to a single deal pipeline. 9 operation(s).
  name: Nimble Deals Pipelines Fields API
  slug: nimble-deals-pipelines-fields-api
- description: Lead transitions through contact pipelines — move a lead between stages, mark it exited successfully or unsuccessfully, and undo a transition. 7 operation(s).
  name: Nimble Leads API
  slug: nimble-leads-api
- description: Message drafts — list and create draft messages. 2 operation(s).
  name: Nimble Messages API
  slug: nimble-messages-api
- description: Task creation against contacts. 1 operation(s).
  name: Nimble Tasks API
  slug: nimble-tasks-api
- description: The authenticated user record — the credential-verification endpoint. 1 operation(s).
  name: Nimble Users API
  slug: nimble-users-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nimble CRM Contacts API
  slug: open-nimble-contacts-api
- collection_type: open
  name: Nimble CRM Contacts Deals API
  slug: open-nimble-deals-api
- collection_type: open
  name: Nimble CRM Contacts Fields API
  slug: open-nimble-fields-api
- collection_type: open
  name: Nimble CRM Contacts Messages API
  slug: open-nimble-messages-api
- collection_type: open
  name: Nimble CRM Contacts Notes API
  slug: open-nimble-notes-api
- collection_type: open
  name: Nimble CRM Contacts Pipelines API
  slug: open-nimble-pipelines-api
- collection_type: open
  name: Nimble CRM Contacts Users API
  slug: open-nimble-users-api
- collection_type: open
  name: Nimble CRM API
  slug: open-nimble
common:
- group: company
  title: ''
  type: Website
  url: https://www.nimble.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.nimble.com/developers/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nimble.com/developers/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.nimble.com/developers/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.nimble.com/en/articles/502755-nimble-api-access
- group: operate
  title: ''
  type: Support
  url: https://support.nimble.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.nimble.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.nimble.com/blog/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nimble.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.nimble.com/register/business_trial/
- group: start
  title: ''
  type: Login
  url: https://app.nimble.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nimble.com/company/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nimble.com/company/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nimble.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nimblecrm
- group: auth
  title: ''
  type: Authentication
  url: authentication/nimble-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nimble-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nimble-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nimble-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nimble-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nimble-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nimble-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nimble-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nimble-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/nimble-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nimble-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nimble-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nimble-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nimble-domain-security.yml
created: '2026-05-11'
description: Nimble is a relationship-focused CRM that unifies contacts, communications, social profiles, calendar and email into a single shared record for small businesses and whole-company teams. Founded in 2010 by GoldMine co-founder Jon Ferrara and headquartered in Santa Monica, California, the platform combines contact management, sales pipelines, email marketing, sequences, web forms, web chat and workflow automation, and enriches contact profiles automatically from email, calendar, social and web data. Nimble publishes a full OpenAPI 3.0.0 contract for its REST API — 89 operations over contacts, user-definable contact fields, contact and deal pipelines, deals, leads, activities, tasks and messages — authenticated with an account API key or OAuth 2.0 authorization_code.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nimble.png
layout: provider
mcp_servers:
- description: ''
  name: nimble-mcp.yml
  slug: nimble-mcpyml
modified: '2026-08-13'
name: Nimble
nav: Providers
network: true
overview: 'Nimble publishes 13 APIs on the [APIs.io](https://apis.io/) network, including REST API, Activities API, Contacts API, and 10 more. Tagged areas include CRM, Sales, Contact Management, Relationship Management, and Marketing Automation.


  Nimble''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Nimble Plans Pricing
  plan_count: 1
  slug: nimble-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 0
  name: Nimble Rate Limits
  slug: nimble-rate-limits
scopes:
- name: Nimble Scopes
  scope_count: 3
  slug: nimble-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 51.6
  delta: -1.7
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 16.7
    contract_quality: 57.8
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 53.3
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nimble/refs/heads/main/screenshots/nimble-2026-08-17T124228.png
security:
- kind: authentication
  name: Nimble Authentication
  slug: nimble-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Nimble Domain Security
  slug: nimble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nimble
tags:
- CRM
- Sales
- Contact Management
- Relationship Management
- Marketing Automation
- Pipeline Management
- Small Business
- Email Marketing
- Sales Automation
- Lead Management
website: https://www.nimble.com
---
