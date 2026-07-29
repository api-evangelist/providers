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
- acting_count: 10
  human_in_the_loop: 0
  name: Oracle Eloqua Agentic Access
  operation_count: 19
  slug: oracle-eloqua-agentic-access
  summary_line: 19 operations · 10 acting
api_count: 8
apis:
- description: REST API for managing Eloqua marketing assets, contacts, accounts, campaigns, emails, forms, landing pages, and custom data objects. Base URL is pod-specific and resolved from the /id endpoint; suppor
  name: Oracle Eloqua Application REST API
  slug: application-api
- description: High-volume import/export REST API for moving large datasets of contacts, accounts, custom objects, and activities in and out of Eloqua. Uses the same OAuth 2.0 and HTTP Basic Authentication as the Ap
  name: Oracle Eloqua Bulk API
  slug: bulk-api
- description: Manage account records.
  name: Oracle Eloqua Accounts API
  slug: oracle-eloqua-accounts-api
- description: Bulk import/export and sync operations.
  name: Oracle Eloqua Bulk API
  slug: oracle-eloqua-bulk-api
- description: Manage marketing campaign assets.
  name: Oracle Eloqua Campaigns API
  slug: oracle-eloqua-campaigns-api
- description: Manage contact records and list membership.
  name: Oracle Eloqua Contacts API
  slug: oracle-eloqua-contacts-api
- description: Manage email assets and deployments.
  name: Oracle Eloqua Emails API
  slug: oracle-eloqua-emails-api
- description: Manage forms and form submission data.
  name: Oracle Eloqua Forms API
  slug: oracle-eloqua-forms-api
artifact_total: 12
collections:
- collection_type: open
  name: Oracle Eloqua REST API
  slug: open-oracle-eloqua
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-eloqua-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-eloqua-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-eloqua-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/cx/marketing/automation/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/cx/marketing/automation/
- group: start
  title: ''
  type: Signup
  url: https://login.eloqua.com/
created: '2026-05-11'
description: Oracle Eloqua is a B2B marketing automation platform within Oracle Marketing Cloud that enables marketers to plan and execute multi-channel campaigns, manage leads, and personalize customer engagement across email, web, mobile, and social channels. The platform provides campaign design, lead scoring, segmentation, landing pages, and form processing for B2B demand generation teams. Oracle Eloqua exposes pod-specific REST APIs (Application API and Bulk API) authenticated via OAuth 2.0 or HTTP Basic Authentication, with base URLs resolved per-customer from the login.eloqua.com /id endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-eloqua.png
layout: provider
modified: '2026-05-11'
name: Oracle Eloqua
nav: Providers
network: true
overview: 'Oracle Eloqua publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Bulk API, Campaigns API, and 3 more. Tagged areas include Marketing Automation, B2B Marketing, Email Marketing, Campaign Management, and Lead Management.


  Oracle Eloqua''s developer surface includes authentication, documentation, pricing, signup flow, and 4 more developer resources.'
random_paper: 58
score:
  band: emerging
  composite: 27.6
  delta: -2.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 54.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-eloqua/refs/heads/main/screenshots/oracle-eloqua-2026-06-20T191129.png
security:
- kind: authentication
  name: Oracle Eloqua Authentication
  slug: oracle-eloqua-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Oracle Eloqua Domain Security
  slug: oracle-eloqua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-eloqua
tags:
- Marketing Automation
- B2B Marketing
- Email Marketing
- Campaign Management
- Lead Management
- Oracle
website: https://www.oracle.com/cx/marketing/automation/
---
