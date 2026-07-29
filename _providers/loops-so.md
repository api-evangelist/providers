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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Loops So Agentic Access
  operation_count: 26
  slug: loops-so-agentic-access
  summary_line: 26 operations · 12 acting
api_count: 12
apis:
- description: The API key API from Loops — 1 operation(s) for api key.
  name: Loops API key API
  slug: loops-so-api-key-api
- description: Create and manage email campaigns
  name: Loops Campaigns API
  slug: loops-so-campaigns-api
- description: View email components
  name: Loops Components API
  slug: loops-so-components-api
- description: Manage contact properties
  name: Loops Contact properties API
  slug: loops-so-contact-properties-api
- description: Manage contacts in your audience
  name: Loops Contacts API
  slug: loops-so-contacts-api
- description: View dedicated sending IP addresses
  name: Loops Dedicated sending IPs API
  slug: loops-so-dedicated-sending-ips-api
- description: Manage email message content for campaigns
  name: Loops Email messages API
  slug: loops-so-email-messages-api
- description: Trigger email sending with events
  name: Loops Events API
  slug: loops-so-events-api
- description: View mailing lists
  name: Loops Mailing lists API
  slug: loops-so-mailing-lists-api
- description: View email themes
  name: Loops Themes API
  slug: loops-so-themes-api
- description: Send and view transactional emails
  name: Loops Transactional emails API
  slug: loops-so-transactional-emails-api
- description: Upload image assets
  name: Loops Uploads API
  slug: loops-so-uploads-api
artifact_total: 65
collections:
- collection_type: open
  name: Loops OpenAPI Spec
  slug: open-loops
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loops-so-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loops-so-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loops-so-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://loops.so
- group: docs
  title: ''
  type: Documentation
  url: https://loops.so/docs
- group: docs
  title: ''
  type: Documentation
  url: https://loops.so/docs/api-reference/intro
- group: docs
  title: ''
  type: OpenAPI
  url: https://app.loops.so/openapi.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: https://app.loops.so/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://loops.so/docs/quickstart
- group: design
  title: ''
  type: Webhooks
  url: https://loops.so/docs/webhooks
- group: commercial
  title: ''
  type: Pricing
  url: https://loops.so/pricing
- group: company
  title: ''
  type: Blog
  url: https://loops.so/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://loops.so/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loops.so/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loops.so/legal/privacy
- group: auth
  title: ''
  type: Security
  url: https://loops.so/legal/security
- group: start
  title: ''
  type: Signup
  url: https://app.loops.so/register
- group: start
  title: ''
  type: Login
  url: https://app.loops.so/login
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/loops_so
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loops-so
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loops-so
- group: build
  title: ''
  type: SDKs
  url: https://github.com/loops-so/loops-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/loops-so/loops-nuxt
- group: build
  title: ''
  type: SDKs
  url: https://github.com/loops-so/loops-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/loops-so/loops-rb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/loops-so/loops-go
- group: build
  title: ''
  type: Tools
  url: https://github.com/loops-so/cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/loops-so/homebrew-tap
- group: build
  title: ''
  type: Tools
  url: https://github.com/loops-so/skills
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/loops-so/loops-nextjs
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/loops
- group: commercial
  title: ''
  type: Plans
  url: https://loops.so/pricing
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: operate
  title: ''
  type: RateLimits
  url: ''
- group: design
  title: ''
  type: Webhooks
  url: ''
created: '2026-05-25T00:00:00.000Z'
description: Loops is a modern email platform purpose-built for software companies, combining product, marketing, and transactional email behind a single REST API and a single audience. Contacts, contact properties, mailing lists, events, segments, campaigns, email messages, themes, components, uploads, transactional sends, and dedicated sending IPs are all first-class API resources, with an OpenAPI 3.1 spec published at app.loops.so/openapi.yaml. Lifecycle workflows ("loops") use the Events API as their trigger, an HMAC-SHA256-signed webhook stream broadcasts every contact and email event for real-time integrations, and official SDKs ship for JavaScript, Nuxt, PHP, Ruby, and Go alongside an official Go-based CLI. Transactional email is included on every plan, team seats are unlimited, and a generous free tier covers 1,000 contacts and 4,000 sends per month — making Loops a Tier-1 developer-first email service for SaaS teams from waitlist to IPO.
features:
- Unified platform for product, marketing, and transactional email built for software companies
- Single REST API (OpenAPI 3.1 published at app.loops.so/openapi.yaml) covering contacts, properties, mailing lists, events, campaigns, email messages, themes, components, transactional, uploads, suppressions, and dedicated sending IPs
- Bearer-token API key authentication with a GET /api-key test endpoint
- 10 requests/second per team baseline rate limit with x-ratelimit-* response headers
- Contacts API — create, update, find, delete; manage suppression status
- Contact properties API — create custom properties and list the full property catalog
- Mailing lists API — list mailing lists and manage list membership via contact updates
- Events API — POST /events/send to trigger loops (workflows) and personalize content
- Campaigns API — full CRUD plus list, with separate endpoints for the email message body
- Email message API — fetch and update the content of an individual email message inside a campaign
- Themes and components API — read reusable themes and shared components used across emails
- Transactional email API — send transactional emails with template variables, file attachments, and headers; list transactional sends
- Uploads API — create and complete file uploads for use in transactional attachments
- Dedicated sending IPs API — list dedicated IPs assigned to your account
- Webhook system with HMAC-SHA256 signing, 30 days of delivery history, contact + email + send + testing events, schema version 1.0.0
- Lifecycle workflows ("loops") with triggers, timers, branching, and conditional logic
- Saved segments built from contact properties and engagement data
- A/B testing for campaigns
- Email design editor optimized for major email clients
- Analytics for conversion, opens, clicks, bounces, and unsubscribes
- Official SDKs for JavaScript/TypeScript, Nuxt, PHP, Ruby, and Go; community SDKs for Laravel and Rails
- Official `loops` CLI (Go) with Homebrew tap distribution
- Official Claude Code Skills repository for the Loops API and CLI
- 25+ integrations across Stripe, Supabase, Clerk, Auth0, Auth.js, Better Auth, PostHog, Segment, RudderStack, Fivetran, HubSpot, Salesforce, Attio, Clay, Zapier, Make, Integrately, Bubble, Framer, Webflow, Emailify, and Email Love
- Transactional email included at no extra charge on every plan
- Unlimited team seats — never billed per seat or per send
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loops-so.png
integrations:
- description: Sync Stripe customers to your Loops audience and trigger automated emails on billing events.
  name: Stripe
- description: Send Supabase authentication emails (magic links, password reset, confirmations) through Loops.
  name: Supabase
- description: Send Clerk authentication emails through Loops.
  name: Clerk
- description: Route Auth0 authentication emails through Loops.
  name: Auth0
- description: Send Auth.js authentication emails through Loops.
  name: Auth.js
- description: Route Better Auth transactional emails through Loops.
  name: Better Auth
- description: Sync PostHog events and identified users into Loops contacts and workflows.
  name: PostHog
- description: Sync Segment events and identified users into Loops.
  name: Segment
- description: Sync RudderStack events into Loops as event triggers.
  name: RudderStack
- description: Sync data into Loops via Fivetran connectors.
  name: Fivetran
- description: Sync HubSpot contacts to Loops.
  name: HubSpot
- description: Sync Salesforce contacts to Loops.
  name: Salesforce
- description: Sync Attio CRM contacts to Loops.
  name: Attio
- description: Push contacts from Clay into Loops.
  name: Clay
- description: Connect Loops to 6,000+ apps via Zapier for contact sync, event triggers, and email sends.
  name: Zapier
- description: No-code automation flows that read from and write to Loops.
  name: Make
- description: No-code integration platform for connecting Loops to other tools.
  name: Integrately
- description: Send transactional email and sync contacts from Bubble no-code apps.
  name: Bubble
- description: Capture form submissions in Framer sites and add them to Loops.
  name: Framer
- description: Capture Webflow form submissions and add them to Loops contacts.
  name: Webflow
- description: Import custom MJML email templates from Emailify into Loops.
  name: Emailify
- description: Import MJML email templates from Email Love into Loops.
  name: Email Love
- description: Receive arbitrary HTTP payloads and turn them into Loops events.
  name: Incoming Webhooks
layout: provider
modified: '2026-05-25'
name: Loops
nav: Providers
network: true
overview: 'Loops publishes 12 APIs on the [APIs.io](https://apis.io/) network, including API key API, Campaigns API, Components API, and 9 more. Tagged areas include Email, Marketing Email, Transactional Email, Email Automation, and Email Campaigns.


  Loops'' developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, changelog, and 25 more developer resources.'
random_paper: 38
score:
  band: developing
  composite: 45.7
  delta: -2.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 55.2
    developer_ergonomics: 56.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loops-so/refs/heads/main/screenshots/loops-so-2026-06-20T184721.png
security:
- kind: authentication
  name: Loops So Authentication
  slug: loops-so-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Loops So Domain Security
  slug: loops-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loops-so
tags:
- Email
- Marketing Email
- Transactional Email
- Email Automation
- Email Campaigns
- Email Workflows
- Contacts
- Audience Management
- Events
- Webhooks
- SaaS
- Developer Tools
website: https://loops.so
---
