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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Wealthbox Agentic Access
  operation_count: 24
  slug: wealthbox-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 11
apis:
- description: REST API for managing contacts, tasks, events, opportunities, projects, notes, workflows, custom fields, teams, and activity streams in Wealthbox CRM. Supports personal Access Tokens (ACCESS_TOKEN hea
  name: Wealthbox CRM API
  slug: crm-api
- description: The Activity API from Wealthbox — 1 operation(s) for activity.
  name: Wealthbox Activity API
  slug: wealthbox-activity-api
- description: The Contacts API from Wealthbox — 2 operation(s) for contacts.
  name: Wealthbox Contacts API
  slug: wealthbox-contacts-api
- description: The Events API from Wealthbox — 1 operation(s) for events.
  name: Wealthbox Events API
  slug: wealthbox-events-api
- description: The Notes API from Wealthbox — 1 operation(s) for notes.
  name: Wealthbox Notes API
  slug: wealthbox-notes-api
- description: The Opportunities API from Wealthbox — 1 operation(s) for opportunities.
  name: Wealthbox Opportunities API
  slug: wealthbox-opportunities-api
- description: The Profile API from Wealthbox — 1 operation(s) for profile.
  name: Wealthbox Profile API
  slug: wealthbox-profile-api
- description: The Tasks API from Wealthbox — 2 operation(s) for tasks.
  name: Wealthbox Tasks API
  slug: wealthbox-tasks-api
- description: The Teams API from Wealthbox — 1 operation(s) for teams.
  name: Wealthbox Teams API
  slug: wealthbox-teams-api
- description: The Users API from Wealthbox — 1 operation(s) for users.
  name: Wealthbox Users API
  slug: wealthbox-users-api
- description: The Workflows API from Wealthbox — 2 operation(s) for workflows.
  name: Wealthbox Workflows API
  slug: wealthbox-workflows-api
artifact_total: 18
collections:
- collection_type: open
  name: Wealthbox CRM API
  slug: open-wealthbox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wealthbox-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wealthbox-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wealthbox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wealthbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wealthbox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wealthbox-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starburstlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wealthboxcrm
- group: company
  title: ''
  type: Website
  url: https://www.wealthbox.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.wealthbox.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wealthbox.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.crmworkspace.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.wealthbox.com/blog/feed/
created: '2026-05-11'
description: Wealthbox is a CRM platform built specifically for financial advisors, offering contact management, task workflows, opportunities, projects, and collaborative team features tailored to wealth management practices. The platform's REST API supports both personal Access Tokens and OAuth 2.0 for integrations, exposing CRUD endpoints for contacts, tasks, events, notes, workflows, custom fields, and activity streams under the api.crmworkspace.com base URL.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wealthbox.png
layout: provider
modified: '2026-05-11'
name: Wealthbox
nav: Providers
network: true
overview: 'Wealthbox publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Contacts API, Events API, and 7 more. Tagged areas include CRM, Financial Advisors, Wealth Management, Contact Management, and Workflow Automation.


  Wealthbox''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 70
scopes:
- name: Wealthbox Scopes
  scope_count: 2
  slug: wealthbox-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 30.5
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 57.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wealthbox/refs/heads/main/screenshots/wealthbox-2026-06-20T201306.png
security:
- kind: authentication
  name: Wealthbox Authentication
  slug: wealthbox-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Wealthbox Domain Security
  slug: wealthbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wealthbox Vulnerability Disclosure
  slug: wealthbox-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Wealthbox Trust Center
  slug: wealthbox-trust-center
  summary_line: SOC 2, GDPR
slug: wealthbox
tags:
- CRM
- Financial Advisors
- Wealth Management
- Contact Management
- Workflow Automation
- SaaS
website: https://www.wealthbox.com
---
