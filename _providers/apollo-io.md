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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Apollo Io Agentic Access
  operation_count: 28
  slug: apollo-io-agentic-access
  summary_line: 28 operations · 21 acting
api_count: 35
apis:
- description: Search Apollo's organization database by industry, headcount, revenue, technology stack, location, and funding stage.
  name: Apollo Organization Search API
  slug: apollo-organization-search-api
- description: Enrich a known person record by email, LinkedIn URL, name + company, or other identifiers; returns work email, mobile, title, social profiles, and tenure.
  name: Apollo People Enrichment API
  slug: apollo-people-enrichment-api
- description: Enrich a known organization by domain or LinkedIn URL; returns headcount, industry, revenue, funding, technologies, and location.
  name: Apollo Organization Enrichment API
  slug: apollo-organization-enrichment-api
- description: Enrich up to 10 person records in a single API call to reduce round-trip and credit cost.
  name: Apollo Bulk People Enrichment API
  slug: apollo-bulk-people-enrichment-api
- description: Enrich multiple organizations in a single API call.
  name: Apollo Bulk Organization Enrichment API
  slug: apollo-bulk-organization-enrichment-api
- description: Manage contacts in your Apollo CRM workspace — create, update, delete, and bulk-import contacts with custom fields and tags.
  name: Apollo Contacts API
  slug: apollo-contacts-api
- description: Manage accounts (companies) in your Apollo CRM with stage, ownership, and custom fields.
  name: Apollo Accounts API
  slug: apollo-accounts-api
- description: Manage deals (opportunities) attached to accounts and contacts, including stage, value, probability, and custom fields.
  name: Apollo Deals API
  slug: apollo-deals-api
- description: Manage outreach sequences (cadences) and add or remove contacts as sequence subscribers; trigger sends and pause/resume schedules.
  name: Apollo Sequences API
  slug: apollo-sequences-api
- description: Manage connected email accounts (Gmail / Outlook / SMTP) used for outbound sequence sends and inbox sync.
  name: Apollo Email Accounts API
  slug: apollo-email-accounts-api
- description: Read sent / received email metadata and tracking events (open, click, reply, bounce) for sequence emails.
  name: Apollo Emails API
  slug: apollo-emails-api
- description: Log inbound and outbound calls with duration, recording URLs, transcripts, and disposition outcomes.
  name: Apollo Calls API
  slug: apollo-calls-api
- description: Manage user tasks tied to contacts and accounts.
  name: Apollo Tasks API
  slug: apollo-tasks-api
- description: Manage meetings booked via Apollo's Meetings (scheduling) feature and synced from connected calendar accounts.
  name: Apollo Meetings API
  slug: apollo-meetings-api
- description: Define and read custom field schemas across people, organizations, contacts, accounts, and deals.
  name: Apollo Custom Fields API
  slug: apollo-custom-fields-api
- description: Manage saved lists (static and dynamic) for segmenting people and accounts and feeding them into sequences and dialer queues.
  name: Apollo Lists API
  slug: apollo-lists-api
- description: Read, create, and apply tags to contacts and accounts for categorization and filtering.
  name: Apollo Tags API
  slug: apollo-tags-api
- description: Manage users (sales reps, managers) and their roles within the Apollo workspace.
  name: Apollo Users API
  slug: apollo-users-api
- description: Pull aggregated activity, sequence performance, dialer, and pipeline analytics for reporting use cases.
  name: Apollo Analytics API
  slug: apollo-analytics-api
- description: Read your workspace's API usage and remaining credit balance across hourly, daily, and monthly windows.
  name: Apollo API Usage API
  slug: apollo-api-usage-api
- description: Subscribe to Apollo events (contact.created, sequence.added, email.opened, call.completed) for downstream automation.
  name: Apollo Webhooks API
  slug: apollo-webhooks-api
- description: The Accounts API from Apollo.io — 3 operation(s) for accounts.
  name: Apollo.io Accounts API
  slug: apollo-io-accounts-api
- description: The Contacts API from Apollo.io — 3 operation(s) for contacts.
  name: Apollo.io Contacts API
  slug: apollo-io-contacts-api
- description: The Email Accounts API from Apollo.io — 1 operation(s) for email accounts.
  name: Apollo.io Email Accounts API
  slug: apollo-io-email-accounts-api
- description: The Emailer Campaigns API from Apollo.io — 3 operation(s) for emailer campaigns.
  name: Apollo.io Emailer Campaigns API
  slug: apollo-io-emailer-campaigns-api
- description: The Mixed Companies API from Apollo.io — 1 operation(s) for mixed companies.
  name: Apollo.io Mixed Companies API
  slug: apollo-io-mixed-companies-api
- description: The Mixed People API from Apollo.io — 1 operation(s) for mixed people.
  name: Apollo.io Mixed People API
  slug: apollo-io-mixed-people-api
- description: The Opportunities API from Apollo.io — 3 operation(s) for opportunities.
  name: Apollo.io Opportunities API
  slug: apollo-io-opportunities-api
- description: The Organizations API from Apollo.io — 2 operation(s) for organizations.
  name: Apollo.io Organizations API
  slug: apollo-io-organizations-api
- description: The People API from Apollo.io — 2 operation(s) for people.
  name: Apollo.io People API
  slug: apollo-io-people-api
- description: The Phone Calls API from Apollo.io — 3 operation(s) for phone calls.
  name: Apollo.io Phone Calls API
  slug: apollo-io-phone-calls-api
- description: The Sync Report API from Apollo.io — 1 operation(s) for sync report.
  name: Apollo.io Sync Report API
  slug: apollo-io-sync-report-api
- description: The Tasks API from Apollo.io — 3 operation(s) for tasks.
  name: Apollo.io Tasks API
  slug: apollo-io-tasks-api
- description: The Usage Stats API from Apollo.io — 1 operation(s) for usage stats.
  name: Apollo.io Usage Stats API
  slug: apollo-io-usage-stats-api
- description: The Users API from Apollo.io — 1 operation(s) for users.
  name: Apollo.io Users API
  slug: apollo-io-users-api
artifact_total: 54
collections:
- collection_type: open
  name: Apollo.io API
  slug: open-apollo-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apollo-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/apollo-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-io-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apolloio
- group: company
  title: ''
  type: Website
  url: https://www.apollo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apollo.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apollo.io/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apollo.io/pricing
- group: start
  title: ''
  type: Login
  url: https://app.apollo.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apollo.io/
- group: company
  title: ''
  type: Blog
  url: https://www.apollo.io/blog
- group: operate
  title: ''
  type: Support
  url: https://knowledge.apollo.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apolloio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apollo.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apollo.io/terms
- group: auth
  title: ''
  type: Authentication
  url: https://docs.apollo.io/reference/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.apollo.io/reference/rate-limits
- group: design
  title: ''
  type: Webhooks
  url: https://docs.apollo.io/reference/webhooks
- group: commercial
  title: ''
  type: Plans
  url: plans/apollo-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apollo-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/apollo-io-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/apolloio/apollo-mcp-plugin
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.apollo.io/llms.txt
created: '2026-05-08'
description: Apollo.io is a sales intelligence and engagement platform combining a 270M+ contact database with email and call sequencing. The Apollo REST API exposes people search & enrichment, organization search & enrichment, contacts, accounts, deals, sequences, email accounts, calls, tasks, meetings, lists, and webhooks.
features:
- REST API at https://api.apollo.io/api/v1/
- API key authentication via X-Api-Key header
- 270M+ person database, 60M+ companies
- Free, Basic, Professional, Organization plans
- Per-user-per-month seat pricing plus monthly credit allocations
- Search, Enrichment, and Mobile credits each tracked separately
- Bulk endpoints for batched enrichment to save credits
- Per-minute and per-hour API rate limits scaled by plan tier
- Webhooks for sequence and engagement events
- REST API access requires Basic or higher
finops:
- name: Apollo Io Finops
  service_category: Sales Intelligence
  slug: apollo-io-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Apollo.io B2B sales intelligence and engagement platform. Apollo.io does not natively expose a GraphQL endpoint; this schema is derived from the Apollo REST
  name: Apollo.io GraphQL Schema
  slug: apollo-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-io.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Apollo.io
nav: Providers
network: true
overview: 'Apollo.io publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contacts API, Email Accounts API, and 11 more. Tagged areas include Sales Intelligence, Prospecting, Engagement, B2B Data, and Enrichment.


  Apollo.io''s developer surface includes documentation, API reference, pricing, engineering blog, support, authentication, and 17 more developer resources.'
plans:
- name: Apollo Io Plans Pricing
  plan_count: 7
  slug: apollo-io-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 7
  name: Apollo Io Rate Limits
  slug: apollo-io-rate-limits
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 51.0
    developer_ergonomics: 41.3
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-io/refs/heads/main/screenshots/apollo-io-2026-06-20T172312.png
security:
- kind: domain-security
  name: Apollo Io Domain Security
  slug: apollo-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Apollo Io Trust Center
  slug: apollo-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: apollo-io
tags:
- Sales Intelligence
- Prospecting
- Engagement
- B2B Data
- Enrichment
- SaaS
website: https://www.apollo.io/
---
