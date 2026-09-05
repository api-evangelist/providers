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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Wealthbox Agentic Access
  operation_count: 24
  slug: wealthbox-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 1
apis:
- description: REST API for managing contacts, tasks, events, opportunities, projects, notes, workflows, custom fields, teams, and activity streams in Wealthbox CRM. Supports personal Access Tokens (ACCESS_TOKEN hea
  name: Wealthbox CRM API
  slug: crm-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Activity API from Wealthbox — 1 operation(s) for activity.
  name: Wealthbox Activity API
  slug: wealthbox-activity-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Contacts API from Wealthbox — 2 operation(s) for contacts.
  name: Wealthbox Contacts API
  slug: wealthbox-contacts-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Events API from Wealthbox — 1 operation(s) for events.
  name: Wealthbox Events API
  slug: wealthbox-events-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Notes API from Wealthbox — 1 operation(s) for notes.
  name: Wealthbox Notes API
  slug: wealthbox-notes-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Opportunities API from Wealthbox — 1 operation(s) for opportunities.
  name: Wealthbox Opportunities API
  slug: wealthbox-opportunities-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Profile API from Wealthbox — 1 operation(s) for profile.
  name: Wealthbox Profile API
  slug: wealthbox-profile-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Tasks API from Wealthbox — 2 operation(s) for tasks.
  name: Wealthbox Tasks API
  slug: wealthbox-tasks-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Teams API from Wealthbox — 1 operation(s) for teams.
  name: Wealthbox Teams API
  slug: wealthbox-teams-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Users API from Wealthbox — 1 operation(s) for users.
  name: Wealthbox Users API
  slug: wealthbox-users-api
- baseURL: https://api.crmworkspace.com
  baseurl_source: declared
  description: The Workflows API from Wealthbox — 2 operation(s) for workflows.
  name: Wealthbox Workflows API
  slug: wealthbox-workflows-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wealthbox CRM Activity API
  slug: open-wealthbox-activity-api
- collection_type: open
  name: Wealthbox CRM Activity Contacts API
  slug: open-wealthbox-contacts-api
- collection_type: open
  name: Wealthbox CRM Activity Events API
  slug: open-wealthbox-events-api
- collection_type: open
  name: Wealthbox CRM Activity Notes API
  slug: open-wealthbox-notes-api
- collection_type: open
  name: Wealthbox CRM Activity Opportunities API
  slug: open-wealthbox-opportunities-api
- collection_type: open
  name: Wealthbox CRM Activity Profile API
  slug: open-wealthbox-profile-api
- collection_type: open
  name: Wealthbox CRM Activity Tasks API
  slug: open-wealthbox-tasks-api
- collection_type: open
  name: Wealthbox CRM Activity Teams API
  slug: open-wealthbox-teams-api
- collection_type: open
  name: Wealthbox CRM Activity Users API
  slug: open-wealthbox-users-api
- collection_type: open
  name: Wealthbox CRM Activity Workflows API
  slug: open-wealthbox-workflows-api
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
overview: 'Wealthbox publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Contacts API, Events API, and 7 more. Tagged areas include CRM, Financial Advisors, Wealth Management, Contact Management, and Workflow-Automation.


  Wealthbox''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 8
scopes:
- name: Wealthbox Scopes
  scope_count: 2
  slug: wealthbox-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 17.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Workflow-Automation
- Software-as-a-Service
website: https://www.wealthbox.com
---
