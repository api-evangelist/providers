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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-08-26'
api_count: 7
apis:
- description: Platform notifications API secured with OAuth 2.0 (scope NotificationService).
  name: Fourth Notifications API
  slug: fourth-notifications-api
- description: Task management API secured with OAuth 2.0.
  name: Fourth Tasks API
  slug: fourth-tasks-api
- description: SCIM 2.0 user and identity provisioning for Fourth accounts.
  name: Fourth Account SCIM API
  slug: fourth-account-scim-api
- description: Employee scheduling data for the HotSchedules workforce platform.
  name: Fourth Schedules API
  slug: fourth-schedules-api
- description: Point-of-sale transaction integration API.
  name: Fourth POS Transaction API
  slug: fourth-pos-transaction-api
- description: RME export and import APIs for recipe and menu data.
  name: Fourth Recipe & Menu Engineering API
  slug: fourth-recipe-menu-engineering-api
- description: Adaco hotel inventory (product catalogue, vendor, budget, requisitions, inventory).
  name: Fourth Adaco Web API
  slug: fourth-adaco-web-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.fourth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fourth.com/en-gb
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fourth.com/en-gb
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fourth.com/en-gb
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fourth.com/en-gb/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/fourth-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fourth-scopes.yml
- group: operate
  title: ''
  type: Support
  url: https://www.fourth.com/support/customer-support
- group: company
  title: ''
  type: Blog
  url: https://www.fourth.com/resources
- group: start
  title: ''
  type: Login
  url: https://secure.na1.fourth.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fourth.com/legal/legal-terms-and-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fourth.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fourth.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fourth-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.fourth.com/en-gb/docs/whats-new
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fourth-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developer.fourth.com/en-gb/docs/notifications-api/reference
- group: design
  title: ''
  type: Conformance
  url: conformance/fourth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.fourth.com/legal/fourth-hosting-data-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/fourth-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fourth.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fourth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fourth-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fourth-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fourth-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fourth-llms.txt
created: '2026-07-17'
description: Fourth is an AI-powered workforce management and inventory platform built for restaurants and hospitality, uniting recruiting, HR, payroll, labor scheduling, purchasing, and inventory management in a single system across 120,000+ locations globally (customers include Taco Bell, Dunkin', KFC, Pizza Hut and Culver's). Its product family includes HotSchedules for scheduling, Fourth iQ for restaurant performance, Human Capital Management for talent and payroll, and Adaco inventory for hotels. Fourth publishes a developer portal of REST APIs covering POS transactions, recipe & menu engineering, menu cycles, workforce (UK employee, labor productivity, schedules), notifications, tasks, SCIM identity provisioning, and Adaco hotel inventory. APIs authenticate with OAuth 2.0 (client_credentials and password grants) or Basic Auth; production and test host locations are provisioned per mutual customer and are not publicly disclosed.
image: https://www.fourth.com/themes/custom/fourth/logo.svg
layout: provider
modified: '2026-07-19'
name: Fourth
nav: Providers
network: true
overview: 'Fourth publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce Management, Restaurant, Hospitality, and Inventory Management.


  Fourth''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, changelog, and 19 more developer resources.'
random_paper: 13
scopes:
- name: Fourth Scopes
  scope_count: 1
  slug: fourth-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 33.7
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 83.3
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 33.7
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fourth/refs/heads/main/screenshots/fourth-2026-07-25T215048.png
security:
- kind: authentication
  name: Fourth Authentication
  slug: fourth-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Fourth Domain Security
  slug: fourth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fourth Vulnerability Disclosure
  slug: fourth-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Fourth Trust Center
  slug: fourth-trust-center
  summary_line: ISAE 3402 Type II, ISAE 3000 (SOC 2) Type II, ISO 27001, SOC 1, SOC 2, SOC 3, ISO 9001:2015
slug: fourth
tags:
- Company
- Workforce Management
- Restaurant
- Hospitality
- Inventory Management
- Payroll
- Scheduling
- HCM
- Point-of-Sale
- Food and Beverage
website: https://www.fourth.com/
---
