---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Apollo Agentic Access
  operation_count: 28
  slug: apollo-agentic-access
  summary_line: 28 operations · 21 acting
api_count: 15
apis:
- description: Apollo Client provides libraries and integrations for connecting to Apollo.io's sales platform from external applications and CRM systems.
  name: Apollo Client
  slug: apollo-client
- description: The Accounts API from Apollo — 3 operation(s) for accounts.
  name: Apollo Accounts API
  slug: apollo-accounts-api
- description: The Contacts API from Apollo — 3 operation(s) for contacts.
  name: Apollo Contacts API
  slug: apollo-contacts-api
- description: The Email Accounts API from Apollo — 1 operation(s) for email accounts.
  name: Apollo Email Accounts API
  slug: apollo-email-accounts-api
- description: The Emailer Campaigns API from Apollo — 3 operation(s) for emailer campaigns.
  name: Apollo Emailer Campaigns API
  slug: apollo-emailer-campaigns-api
- description: The Mixed Companies API from Apollo — 1 operation(s) for mixed companies.
  name: Apollo Mixed Companies API
  slug: apollo-mixed-companies-api
- description: The Mixed People API from Apollo — 1 operation(s) for mixed people.
  name: Apollo Mixed People API
  slug: apollo-mixed-people-api
- description: The Opportunities API from Apollo — 3 operation(s) for opportunities.
  name: Apollo Opportunities API
  slug: apollo-opportunities-api
- description: The Organizations API from Apollo — 2 operation(s) for organizations.
  name: Apollo Organizations API
  slug: apollo-organizations-api
- description: The People API from Apollo — 2 operation(s) for people.
  name: Apollo People API
  slug: apollo-people-api
- description: The Phone Calls API from Apollo — 3 operation(s) for phone calls.
  name: Apollo Phone Calls API
  slug: apollo-phone-calls-api
- description: The Sync Report API from Apollo — 1 operation(s) for sync report.
  name: Apollo Sync Report API
  slug: apollo-sync-report-api
- description: The Tasks API from Apollo — 3 operation(s) for tasks.
  name: Apollo Tasks API
  slug: apollo-tasks-api
- description: The Usage Stats API from Apollo — 1 operation(s) for usage stats.
  name: Apollo Usage Stats API
  slug: apollo-usage-stats-api
- description: The Users API from Apollo — 1 operation(s) for users.
  name: Apollo Users API
  slug: apollo-users-api
artifact_total: 45
collections:
- collection_type: open
  name: Apollo.io API
  slug: open-apollo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apollo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/apollo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-domain-security.yml
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
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apollo.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.apollo.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.apollo.io/support
- group: learn
  title: ''
  type: Training
  url: https://academy.apollo.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apollo.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apollo.io/terms-of-service
- group: auth
  title: ''
  type: Compliance
  url: https://www.apollo.io/security
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.apollo.io/llms.txt
created: '2026-03-25'
description: Apollo.io is an AI-powered B2B sales intelligence and engagement platform combining a database of 230M+ verified contacts and 30M+ companies with prospecting, outreach, and deal execution tools. The platform helps sales teams build pipeline, qualify inbound leads, enrich data, and close deals faster with AI-powered workflows and conversation intelligence.
features:
- description: AI-powered multichannel outbound campaigns with email deliverability guardrails and workflow automations.
  name: Outbound Prospecting
- description: Anonymous visitor identification, real-time form enrichment, instant routing, and automated follow-ups.
  name: Inbound Lead Qualification
- description: Enrich contact and company records with always-fresh data from 230M+ verified contacts and 30M+ companies.
  name: Data Enrichment
- description: Pre-meeting insights, AI call summaries, pipeline boards, and coaching dashboards.
  name: Deal Execution
- description: AI-powered assistant for automating sales research, writing, and workflow tasks.
  name: AI Assistant
- description: Call recording, AI call summaries, and conversation analytics for sales coaching.
  name: Conversation Intelligence
- description: Browser extension for accessing Apollo data and workflows directly from any website.
  name: Chrome Extension
- description: No-code workflow automation engine for sales process automation.
  name: Workflow Automation
- description: Email deliverability guardrails to protect sender reputation and maximize inbox placement.
  name: Email Deliverability
- description: Integrated meeting scheduling functionality linked to sales workflows.
  name: Meeting Scheduler
finops:
- name: Apollo Finops
  service_category: API
  slug: apollo-finops
graphqls:
- description: Apollo.io provides a GraphQL API alongside its REST API, accessible at `https://api.apollo.io/api/v1/`. The GraphQL interface exposes the full breadth of Apollo's B2B sales intelligence platform — con
  name: Apollo.io GraphQL API
  slug: apollo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo.png
integrations:
- description: Bi-directional Salesforce CRM integration syncing contacts, accounts, activities, and sequences.
  name: Salesforce
- description: HubSpot CRM integration for syncing contact data and outreach activity.
  name: HubSpot
- description: Gmail integration for email tracking and outreach directly from inbox.
  name: Gmail
- description: Microsoft Outlook integration for email tracking and outreach.
  name: Outlook
- description: LinkedIn integration via Chrome extension for prospecting and data enrichment.
  name: LinkedIn
- description: Zapier integration for connecting Apollo to hundreds of other applications.
  name: Zapier
- description: Slack integration for deal alerts and notifications.
  name: Slack
layout: provider
modified: '2026-05-19'
name: Apollo
nav: Providers
network: true
overview: 'Apollo publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contacts API, Email Accounts API, and 11 more. Tagged areas include AI, B2B Sales, CRM, Data Enrichment, and Lead Generation.


  Apollo''s developer surface includes documentation, getting-started guide, pricing, engineering blog, support, training material, and 8 more developer resources.'
plans:
- name: Apollo Plans Pricing
  plan_count: 3
  slug: apollo-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Apollo Rate Limits
  slug: apollo-rate-limits
score:
  band: developing
  composite: 46.8
  delta: 0.3
  facets:
    commercial_clarity: 86.8
    contract_quality: 51.8
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo/refs/heads/main/screenshots/apollo-2026-06-20T172305.png
security:
- kind: domain-security
  name: Apollo Domain Security
  slug: apollo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Apollo Trust Center
  slug: apollo-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: apollo
tags:
- AI
- B2B Sales
- CRM
- Data Enrichment
- Lead Generation
- Sales Intelligence
- Sales Platform
use_cases:
- description: Find and engage ideal prospects at scale using Apollo's contact database and multichannel outreach.
  name: Outbound Sales Prospecting
- description: Automatically qualify, route, and follow up on inbound leads in real time.
  name: Inbound Lead Management
- description: Enrich Salesforce, HubSpot, and other CRM records with verified contact and company data.
  name: CRM Data Enrichment
- description: Build and manage sales pipeline with AI-assisted prospecting and deal execution tools.
  name: Sales Pipeline Building
- description: Build third-party integrations using OAuth 2.0 to access Apollo data on behalf of customers.
  name: Partner API Integration
---
