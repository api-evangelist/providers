---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Apollo Api Documentation Agentic Access
  operation_count: 28
  slug: apollo-api-documentation-agentic-access
  summary_line: 28 operations · 21 acting
api_count: 14
apis:
- description: The Accounts API from Apollo API Documentation — 3 operation(s) for accounts.
  name: Apollo API Documentation Accounts API
  slug: apollo-api-documentation-accounts-api
- description: The Contacts API from Apollo API Documentation — 3 operation(s) for contacts.
  name: Apollo API Documentation Contacts API
  slug: apollo-api-documentation-contacts-api
- description: The Email Accounts API from Apollo API Documentation — 1 operation(s) for email accounts.
  name: Apollo API Documentation Email Accounts API
  slug: apollo-api-documentation-email-accounts-api
- description: The Emailer Campaigns API from Apollo API Documentation — 3 operation(s) for emailer campaigns.
  name: Apollo API Documentation Emailer Campaigns API
  slug: apollo-api-documentation-emailer-campaigns-api
- description: The Mixed Companies API from Apollo API Documentation — 1 operation(s) for mixed companies.
  name: Apollo API Documentation Mixed Companies API
  slug: apollo-api-documentation-mixed-companies-api
- description: The Mixed People API from Apollo API Documentation — 1 operation(s) for mixed people.
  name: Apollo API Documentation Mixed People API
  slug: apollo-api-documentation-mixed-people-api
- description: The Opportunities API from Apollo API Documentation — 3 operation(s) for opportunities.
  name: Apollo API Documentation Opportunities API
  slug: apollo-api-documentation-opportunities-api
- description: The Organizations API from Apollo API Documentation — 2 operation(s) for organizations.
  name: Apollo API Documentation Organizations API
  slug: apollo-api-documentation-organizations-api
- description: The People API from Apollo API Documentation — 2 operation(s) for people.
  name: Apollo API Documentation People API
  slug: apollo-api-documentation-people-api
- description: The Phone Calls API from Apollo API Documentation — 3 operation(s) for phone calls.
  name: Apollo API Documentation Phone Calls API
  slug: apollo-api-documentation-phone-calls-api
- description: The Sync Report API from Apollo API Documentation — 1 operation(s) for sync report.
  name: Apollo API Documentation Sync Report API
  slug: apollo-api-documentation-sync-report-api
- description: The Tasks API from Apollo API Documentation — 3 operation(s) for tasks.
  name: Apollo API Documentation Tasks API
  slug: apollo-api-documentation-tasks-api
- description: The Usage Stats API from Apollo API Documentation — 1 operation(s) for usage stats.
  name: Apollo API Documentation Usage Stats API
  slug: apollo-api-documentation-usage-stats-api
- description: The Users API from Apollo API Documentation — 1 operation(s) for users.
  name: Apollo API Documentation Users API
  slug: apollo-api-documentation-users-api
artifact_total: 35
collections:
- collection_type: open
  name: Apollo.io API
  slug: open-apollo-api-documentation
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apollo-api-documentation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/apollo-api-documentation-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-api-documentation-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.apollo.io/magazine
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apolloio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apollo.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apollo.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apollo.io/reference
- group: auth
  title: ''
  type: Authentication
  url: https://docs.apollo.io/reference/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.apollo.io/reference/rate-limits
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.apollo.io/llms.txt
created: '2025-07-10'
description: Apollo.io provides a comprehensive REST API for sales intelligence with over 210 million contacts and 35 million companies. The Apollo API enables data enrichment, people and organization search, CRM management, sequences, deals, analytics, and integrations. Authentication is via API keys or OAuth 2.0 for partner integrations. This repository profiles Apollo.io's API documentation as an example of API documentation best practices.
features:
- description: Enrich contact records with data from Apollo's 210M+ contact database.
  name: People Enrichment
- description: Enrich company records with data from Apollo's 35M+ company database.
  name: Organization Enrichment
- description: Search Apollo's contact database to find and identify sales prospects.
  name: People Search
- description: Search Apollo's company database for target accounts and job postings.
  name: Organization Search
- description: Manage accounts, contacts, deals, and sequences via the REST API.
  name: CRM Integration
- description: Partners use OAuth 2.0 to build integrations accessing Apollo data on behalf of customers.
  name: OAuth 2.0 Partner Integration
- description: Interactive API testing capability built directly into the documentation.
  name: Interactive Try It
- description: Query analytics reports for performance metrics via the API.
  name: Analytics Reporting
finops:
- name: Apollo Api Documentation Finops
  service_category: API
  slug: apollo-api-documentation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-api-documentation.png
integrations:
- description: Partner integration protocol for accessing Apollo data on behalf of customers.
  name: OAuth 2.0
- description: Direct API key access for customers building internal integrations.
  name: API Key Authentication
layout: provider
modified: '2026-05-19'
name: Apollo API Documentation
nav: Providers
network: true
overview: 'Apollo API Documentation publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contacts API, Email Accounts API, and 11 more. Tagged areas include API Documentation, Best Practices, Data Enrichment, People Search, and Sales Intelligence.


  Apollo API Documentation''s developer surface includes engineering blog, documentation, getting-started guide, API reference, authentication, and 6 more developer resources.'
plans:
- name: Apollo Api Documentation Plans Pricing
  plan_count: 3
  slug: apollo-api-documentation-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Apollo Api Documentation Rate Limits
  slug: apollo-api-documentation-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 41.6
    developer_ergonomics: 39.1
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-api-documentation/refs/heads/main/screenshots/apollo-api-documentation-2026-06-20T172307.png
security:
- kind: domain-security
  name: Apollo Api Documentation Domain Security
  slug: apollo-api-documentation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Apollo Api Documentation Trust Center
  slug: apollo-api-documentation-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: apollo-api-documentation
tags:
- API Documentation
- Best Practices
- Data Enrichment
- People Search
- Sales Intelligence
use_cases:
- description: Access Apollo's contact and company database for prospecting and outreach.
  name: Sales Intelligence
- description: Enrich CRM records with contact and organization data at scale.
  name: Data Enrichment Pipelines
- description: Build third-party integrations using OAuth 2.0 to access Apollo data for mutual customers.
  name: Partner Integrations
- description: Automate sales workflows including sequences, tasks, and deal management.
  name: Workflow Automation
---
