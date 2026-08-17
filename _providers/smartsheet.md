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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Smartsheet Agentic Access
  operation_count: 10
  slug: smartsheet-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 6
apis:
- description: 'REST API v2.0 for managing sheets, rows, columns, cells, reports, workspaces, folders, users, groups, attachments, discussions, automation rules, and webhooks. Authentication uses OAuth 2.0 or Bearer '
  name: Smartsheet REST API
  slug: rest-api
- description: Manage columns within sheets.
  name: Smartsheet Columns API
  slug: smartsheet-columns-api
- description: Retrieve report data.
  name: Smartsheet Reports API
  slug: smartsheet-reports-api
- description: Manage rows within sheets.
  name: Smartsheet Rows API
  slug: smartsheet-rows-api
- description: Manage Smartsheet sheets.
  name: Smartsheet Sheets API
  slug: smartsheet-sheets-api
- description: Manage webhook subscriptions.
  name: Smartsheet Webhooks API
  slug: smartsheet-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smartsheet Columns API
  slug: open-smartsheet-columns-api
- collection_type: open
  name: Smartsheet Columns Reports API
  slug: open-smartsheet-reports-api
- collection_type: open
  name: Smartsheet Columns Rows API
  slug: open-smartsheet-rows-api
- collection_type: open
  name: Smartsheet Columns Sheets API
  slug: open-smartsheet-sheets-api
- collection_type: open
  name: Smartsheet Columns Webhooks API
  slug: open-smartsheet-webhooks-api
- collection_type: open
  name: Smartsheet API
  slug: open-smartsheet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartsheet-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/smartsheet-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smartsheet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartsheet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartsheet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/smartsheet-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartsheet-com
- group: company
  title: ''
  type: Website
  url: https://www.smartsheet.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smartsheet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.smartsheet.com/
- group: start
  title: ''
  type: Signup
  url: https://www.smartsheet.com/try-it
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smartsheet.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smartsheet-platform
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.smartsheet.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.smartsheet.com/blog
created: '2026-05-11'
description: Smartsheet is a SaaS work management and collaboration platform that combines spreadsheet-style sheets, project plans, Gantt charts, dashboards, forms, and workflow automation for teams and enterprises. The Smartsheet REST API provides programmatic access to sheets, rows, columns, reports, workspaces, users, attachments, and webhooks using OAuth 2.0 or API access tokens.
graphqls:
- description: 'This document describes a conceptual GraphQL schema for the Smartsheet REST API. Smartsheet is a SaaS work management and collaboration platform that combines spreadsheet-style sheets, project plans, '
  name: Smartsheet GraphQL Schema
  slug: smartsheet-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartsheet.png
layout: provider
modified: '2026-05-11'
name: Smartsheet
nav: Providers
network: true
overview: 'Smartsheet publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Columns API, Reports API, Rows API, and 2 more. Tagged areas include Work Management, Project Management, Collaboration, Productivity, and Workflow Automation.


  Smartsheet''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 10 more developer resources.'
random_paper: 45
scopes:
- name: Smartsheet Scopes
  scope_count: 10
  slug: smartsheet-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 64.7
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartsheet/refs/heads/main/screenshots/smartsheet-2026-06-20T194052.png
security:
- kind: authentication
  name: Smartsheet Authentication
  slug: smartsheet-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Smartsheet Domain Security
  slug: smartsheet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Smartsheet Vulnerability Disclosure
  slug: smartsheet-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Smartsheet Trust Center
  slug: smartsheet-trust-center
  summary_line: HIPAA, FedRAMP
slug: smartsheet
tags:
- Work Management
- Project Management
- Collaboration
- Productivity
- Workflow Automation
- Spreadsheets
website: https://www.smartsheet.com
---
