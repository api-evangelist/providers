---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: REST API for programmatically managing Quip threads, documents, spreadsheets, messages, folders, and users. Supports OAuth 2.0 access tokens passed as a Bearer token in the Authorization header.
  name: Quip Automation API
  slug: automation-api
- description: Administrative REST API for managing organization-level Quip resources including company configuration, audit events, and user provisioning.
  name: Quip Admin API
  slug: admin-api
- description: SCIM 2.0 API for automated user provisioning, deprovisioning, and group management from identity providers into Quip.
  name: Quip SCIM API
  slug: scim-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quip-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/salesforce-quip
- group: company
  title: ''
  type: Website
  url: https://quip.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://quip.com/dev/
- group: docs
  title: ''
  type: Documentation
  url: https://quip.com/dev/automation/documentation
- group: start
  title: ''
  type: Console
  url: https://quip.com/dev/console/
- group: company
  title: ''
  type: Blog
  url: https://quip.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quip
- group: other
  title: ''
  type: Parent Company
  url: https://www.salesforce.com/
created: '2026-05-11'
description: Quip is a Salesforce-owned collaborative productivity platform that combines documents, spreadsheets, chat, and tasks into a single workspace tightly integrated with the Salesforce CRM. It enables teams to embed live data, collaborate in real time, and automate workflows across deal collaboration, account planning, and sales operations. The Quip Automation API is a REST interface for creating and managing threads, documents, messages, folders, and users with OAuth 2.0 Bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quip.png
layout: provider
modified: '2026-05-11'
name: Quip
nav: Providers
network: true
overview: 'Quip publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Productivity, Documents, Spreadsheets, and Team Chat.


  Quip''s developer surface includes documentation, developer console, engineering blog, and 6 more developer resources.'
random_paper: 52
score:
  band: emerging
  composite: 13.3
  delta: -2.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quip/refs/heads/main/screenshots/quip-2026-06-20T192438.png
security:
- kind: domain-security
  name: Quip Domain Security
  slug: quip-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quip
tags:
- Collaboration
- Productivity
- Documents
- Spreadsheets
- Team Chat
- Salesforce
website: https://quip.com
---
