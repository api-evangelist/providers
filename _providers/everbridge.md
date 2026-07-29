---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Everbridge Agentic Access
  operation_count: 18
  slug: everbridge-agentic-access
  summary_line: 18 operations · 12 acting
api_count: 12
apis:
- description: The Everbridge Asset Management API allows organizations to manage assets, asset types, asset associations, and related templates. It supports batch operations for bulk asset management and provides l
  name: Everbridge Asset Management API
  slug: everbridge-asset-management-api
- description: The Everbridge Asset Query API provides endpoints for streaming, listing, searching, paginating, and aggregating asset data. It enables organizations to query and retrieve asset information for report
  name: Everbridge Asset Query API
  slug: everbridge-asset-query-api
- description: The Everbridge CEM Alerts API provides GraphQL-based endpoints for querying public alerts and streaming alert data from the Critical Event Management platform. It enables organizations to programmatic
  name: Everbridge CEM Alerts API
  slug: everbridge-cem-alerts-api
- description: The Everbridge SnapComms API enables targeted internal communications broadcasting through the Everbridge Engage platform. It supports authentication, group and attribute targeting, content templates,
  name: Everbridge SnapComms API
  slug: everbridge-snapcomms-api
- description: The Everbridge Digital Apps API provides integration capabilities for mobile, desktop, and web applications from the perspective of an Everbridge contact. It supports receiving and responding to notif
  name: Everbridge Digital Apps API
  slug: everbridge-digital-apps-api
- description: The Everbridge Communications API provides endpoints for managing communication templates, categories, reservations, contact builders, message builders, plans, schedules, and variables. It enables org
  name: Everbridge Communications API
  slug: everbridge-communications-api
- description: 'The Everbridge iPaaS (Integration Platform as a Service) API enables IT organizations to build integrations with monitoring and service management tools such as APM, NPM, ITOM, SIEM, DevOps, and ITSM '
  name: Everbridge iPaaS API
  slug: everbridge-ipaas-api
- description: The Everbridge Safety Devices API provides event management capabilities for safety devices integrated with the Everbridge platform. It uses OAuth 2.0 client credential grant type authentication and e
  name: Everbridge Safety Devices API
  slug: everbridge-safety-devices-api
- description: The Authentication API from Everbridge — 1 operation(s) for authentication.
  name: Everbridge Authentication API
  slug: everbridge-authentication-api
- description: The Contacts API from Everbridge — 3 operation(s) for contacts.
  name: Everbridge Contacts API
  slug: everbridge-contacts-api
- description: The Groups API from Everbridge — 3 operation(s) for groups.
  name: Everbridge Groups API
  slug: everbridge-groups-api
- description: The Notifications API from Everbridge — 2 operation(s) for notifications.
  name: Everbridge Notifications API
  slug: everbridge-notifications-api
artifact_total: 20
collections:
- collection_type: open
  name: Everbridge Suite API
  slug: open-everbridge
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/everbridge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everbridge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/everbridge-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/everbridge
- group: start
  title: ''
  type: Portal
  url: https://manager.everbridge.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.everbridge.net/home
- group: start
  title: ''
  type: Login
  url: https://manager.everbridge.net/login
- group: start
  title: ''
  type: Signup
  url: https://www.everbridge.com/free-trial/
- group: company
  title: ''
  type: Blog
  url: https://www.everbridge.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.everbridge.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.everbridge.com/contact/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.everbridge.net/home/docs/ebs-gs-guide
- group: auth
  title: ''
  type: Authentication
  url: https://developers.everbridge.net/home/docs/ebs-gs-guide-authentication-types
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.everbridge.net/home/docs/ebs-gs-guide-throttling-limits
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.everbridge.net/home/changelog
- group: operate
  title: ''
  type: Support
  url: https://www.everbridge.com/support/
- group: docs
  title: ''
  type: Documentation
  url: https://supportcenter.everbridge.com/hc/en-us/categories/18141856301339-Documentation
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.everbridge.com/company-policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.everbridge.com/about/legal/everbridge-global-privacy-notice/
- group: company
  title: ''
  type: Website
  url: https://www.everbridge.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/everbridge
- group: operate
  title: ''
  type: Community
  url: https://supportcenter.everbridge.com/hc/en-us
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.everbridge.net/
created: 2024-01-09 00:00:00+00:00
description: Everbridge is a global software company that provides enterprise software applications that automate and accelerate organizations' operational response to critical events in order to keep people safe and businesses running.
finops:
- name: Everbridge Finops
  service_category: API
  slug: everbridge-finops
graphqls:
- description: The Everbridge CEM Alerts API provides GraphQL-based endpoints for querying public alerts and streaming alert data from the Critical Event Management platform. It enables organizations to programmatic
  name: Everbridge GraphQL API
  slug: everbridge-graphql
image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
layout: provider
modified: '2026-03-16'
name: Everbridge
nav: Providers
network: true
overview: 'Everbridge publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contacts API, Groups API, and 1 more. Tagged areas include Critical Event Management, Emergency Management, Incident Management, IT Alerting, and Mass Notification.


  Everbridge''s developer surface includes authentication, developer portal, signup flow, engineering blog, getting-started guide, changelog, support, and 16 more developer resources.'
plans:
- name: Everbridge Plans Pricing
  plan_count: 3
  slug: everbridge-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Everbridge Rate Limits
  slug: everbridge-rate-limits
score:
  band: developing
  composite: 54.6
  delta: -1.3
  facets:
    commercial_clarity: 73.7
    contract_quality: 54.7
    developer_ergonomics: 45.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everbridge/refs/heads/main/screenshots/everbridge-2026-06-20T180905.png
security:
- kind: authentication
  name: Everbridge Authentication
  slug: everbridge-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Everbridge Domain Security
  slug: everbridge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: everbridge
tags:
- Critical Event Management
- Emergency Management
- Incident Management
- IT Alerting
- Mass Notification
website: https://www.everbridge.com
---
