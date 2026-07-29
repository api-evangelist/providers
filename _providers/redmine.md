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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Redmine Agentic Access
  operation_count: 32
  slug: redmine-agentic-access
  summary_line: 32 operations · 16 acting
api_count: 18
apis:
- description: REST API for Redmine providing JSON and XML access to issues, projects, users, time entries, wiki pages, attachments, versions, and other entities. Authentication uses HTTP Basic credentials or a per-
  name: Redmine REST API
  slug: rest-api
- description: The Attachments API from Redmine — 1 operation(s) for attachments.
  name: Redmine Attachments API
  slug: redmine-attachments-api
- description: The Custom Fields.json API from Redmine — 1 operation(s) for custom fields.json.
  name: Redmine Custom Fields.json API
  slug: redmine-custom-fields-json-api
- description: The Groups.json API from Redmine — 1 operation(s) for groups.json.
  name: Redmine Groups.json API
  slug: redmine-groups-json-api
- description: The Issue Statuses.json API from Redmine — 1 operation(s) for issue statuses.json.
  name: Redmine Issue Statuses.json API
  slug: redmine-issue-statuses-json-api
- description: The Issues API from Redmine — 1 operation(s) for issues.
  name: Redmine Issues API
  slug: redmine-issues-api
- description: The Issues.json API from Redmine — 1 operation(s) for issues.json.
  name: Redmine Issues.json API
  slug: redmine-issues-json-api
- description: The My API from Redmine — 1 operation(s) for my.
  name: Redmine My API
  slug: redmine-my-api
- description: The Projects API from Redmine — 1 operation(s) for projects.
  name: Redmine Projects API
  slug: redmine-projects-api
- description: The Projects.json API from Redmine — 1 operation(s) for projects.json.
  name: Redmine Projects.json API
  slug: redmine-projects-json-api
- description: The Roles.json API from Redmine — 1 operation(s) for roles.json.
  name: Redmine Roles.json API
  slug: redmine-roles-json-api
- description: The Time Entries API from Redmine — 1 operation(s) for time entries.
  name: Redmine Time Entries API
  slug: redmine-time-entries-api
- description: The Time Entries.json API from Redmine — 1 operation(s) for time entries.json.
  name: Redmine Time Entries.json API
  slug: redmine-time-entries-json-api
- description: The Trackers.json API from Redmine — 1 operation(s) for trackers.json.
  name: Redmine Trackers.json API
  slug: redmine-trackers-json-api
- description: The Uploads.json API from Redmine — 1 operation(s) for uploads.json.
  name: Redmine Uploads.json API
  slug: redmine-uploads-json-api
- description: The Users API from Redmine — 1 operation(s) for users.
  name: Redmine Users API
  slug: redmine-users-api
- description: The Users.json API from Redmine — 1 operation(s) for users.json.
  name: Redmine Users.json API
  slug: redmine-users-json-api
- description: The Wiki Pages.json API from Redmine — 1 operation(s) for wiki pages.json.
  name: Redmine Wiki Pages.json API
  slug: redmine-wiki-pages-json-api
artifact_total: 22
collections:
- collection_type: open
  name: Redmine REST API
  slug: open-redmine
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/redmine-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redmine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/redmine-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.redmine.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.redmine.org/guide
- group: docs
  title: ''
  type: API Documentation
  url: https://www.redmine.org/projects/redmine/wiki/rest_api
- group: other
  title: ''
  type: Download
  url: https://www.redmine.org/projects/redmine/wiki/Download
- group: build
  title: ''
  type: Source Code
  url: https://www.redmine.org/projects/redmine/repository
- group: build
  title: ''
  type: GitHub Mirror
  url: https://github.com/redmine/redmine
- group: company
  title: ''
  type: Blog
  url: https://www.redmine.org/news.atom
- group: build
  title: ''
  type: Plugins
  url: https://www.redmine.org/plugins
- group: operate
  title: ''
  type: Forums
  url: https://www.redmine.org/projects/redmine/boards
- group: operate
  title: ''
  type: Issue Tracker
  url: https://www.redmine.org/projects/redmine/issues
- group: commercial
  title: ''
  type: License
  url: https://www.redmine.org/projects/redmine/wiki/Redmine_License
created: '2026-05-11'
description: Redmine is a flexible open source project management web application written in Ruby on Rails that supports multiple projects, issue tracking, Gantt charts, wikis, forums, time tracking, and SCM integration. The Redmine REST API exposes JSON and XML endpoints for issues, projects, users, time entries, wiki pages, attachments, and more. Authentication is supported via HTTP Basic credentials or per-user API keys, with optional user impersonation for administrator accounts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redmine.png
layout: provider
modified: '2026-05-11'
name: Redmine
nav: Providers
network: true
overview: 'Redmine publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Custom Fields.json API, Groups.json API, and 14 more. Tagged areas include Project Management, Issue Tracking, Open Source, Ruby on Rails, and Bug Tracking.


  Redmine''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 23.7
  delta: -3.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 42.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redmine/refs/heads/main/screenshots/redmine-2026-06-20T192728.png
security:
- kind: authentication
  name: Redmine Authentication
  slug: redmine-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Redmine Domain Security
  slug: redmine-domain-security
  summary_line: TLSv1.3
slug: redmine
tags:
- Project Management
- Issue Tracking
- Open Source
- Ruby on Rails
- Bug Tracking
- Time Tracking
website: https://www.redmine.org
---
