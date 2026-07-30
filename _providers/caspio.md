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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Caspio Agentic Access
  operation_count: 22
  slug: caspio-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 8
apis:
- description: REST API for Caspio Bridge accounts providing programmatic access to tables, views, records, files, users, applications, and tasks. Uses OAuth 2.0 client credentials flow to obtain Bearer access token
  name: Caspio REST API
  slug: rest-api
- description: Caspio applications
  name: Caspio Applications API
  slug: caspio-applications-api
- description: OAuth 2.0 token endpoint
  name: Caspio Authentication API
  slug: caspio-authentication-api
- description: File management
  name: Caspio Files API
  slug: caspio-files-api
- description: Table schema and record operations
  name: Caspio Tables API
  slug: caspio-tables-api
- description: Scheduled tasks
  name: Caspio Tasks API
  slug: caspio-tasks-api
- description: Application user management
  name: Caspio Users API
  slug: caspio-users-api
- description: View record operations
  name: Caspio Views API
  slug: caspio-views-api
artifact_total: 13
collections:
- collection_type: open
  name: Caspio REST API
  slug: open-caspio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/caspio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/caspio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caspio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/caspio-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.caspio.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caspio-inc
- group: company
  title: ''
  type: Website
  url: https://www.caspio.com
- group: docs
  title: ''
  type: Documentation
  url: https://howto.caspio.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.caspio.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://pages.caspio.com/free-trial
- group: operate
  title: ''
  type: Support
  url: https://www.caspio.com/support/
created: '2026-05-11'
description: Caspio is a low-code cloud platform for building online database applications without writing code, enabling business users and developers to create multi-user data-driven web apps through a point-and-click visual builder. The platform includes automated workflows, AI integration, identity management, and compliance tooling, and exposes a REST API for managing tables, views, records, files, users, and tasks in a Caspio account.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caspio.png
layout: provider
modified: '2026-05-11'
name: Caspio
nav: Providers
network: true
overview: 'Caspio publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, Files API, and 4 more. Tagged areas include Low Code, No Code, Database, Application Platform, and Cloud Database.


  Caspio''s developer surface includes authentication, engineering blog, documentation, pricing, signup flow, support, and 5 more developer resources.'
random_paper: 65
score:
  band: thin
  composite: 29.8
  delta: -2.1
  facets:
    commercial_clarity: 18.4
    contract_quality: 53.9
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caspio/refs/heads/main/screenshots/caspio-2026-06-20T174035.png
security:
- kind: authentication
  name: Caspio Authentication
  slug: caspio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Caspio Domain Security
  slug: caspio-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: trust-center
  name: Caspio Trust Center
  slug: caspio-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR, FIPS 140
slug: caspio
tags:
- Low Code
- No Code
- Database
- Application Platform
- Cloud Database
- Online Forms
- Workflow Automation
website: https://www.caspio.com
---
