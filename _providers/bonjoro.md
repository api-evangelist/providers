---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'REST API for the Bonjoro personal-video platform. Create and assign greets (video tasks) for one or many recipients, manage recipient profiles and campaigns/workspaces, upload recordings to presigned '
  name: Bonjoro API V2
  slug: bonjoro-api-v2
artifact_total: 7
asyncapis:
- description: ''
  name: Bonjoro Webhooks
  slug: bonjoro-webhooks
collections:
- collection_type: open
  name: Bonjoro API V2
  slug: open-bonjoro-api-v2
common:
- group: company
  title: ''
  type: Website
  url: https://bonjoro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://vimily.github.io/bonjoro-api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://vimily.github.io/bonjoro-api-docs/
- group: operate
  title: ''
  type: Support
  url: https://www.bonjoro.com/support-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.bonjoro.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bonjoro.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bonjoro.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.bonjoro.com/auth/register
- group: start
  title: ''
  type: Login
  url: https://www.bonjoro.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bonjoro.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bonjoro.com/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/bonjoro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bonjoro-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bonjoro-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bonjoro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bonjoro-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bonjoro-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bonjoro-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bonjoro-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/bonjoro-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bonjoro-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bonjoro-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bonjoro-domain-security.yml
created: '2026-08-12'
description: 'Bonjoro is a personal-video customer engagement platform operated by Vimily Pty Ltd of Sydney, Australia. Sales, marketing, customer success and education teams use it to record short one-to-one videos — "Bonjoros" — and deliver them at the moments that decide a relationship: signup, onboarding, first purchase, renewal and churn risk. Alongside the messaging product it runs a video testimonial collection surface. Bonjoro publishes a REST API (API V2, 94 paths and 123 operations) covering greets, recipient profiles, campaigns and workspaces, recordings and media, message templates, engagement results and stats, transmissions and deliverability, replies, teams and users, custom sending domains and verified signatures, and the trigger/action automation engine that wires Bonjoro into CRMs and email platforms. REST API access is published as a Company-tier entitlement; the wider integration surface runs through 18+ native connectors and a first-party Zapier app.'
image: https://www.bonjoro.com/apple-touch-icon-180x180.png
layout: provider
modified: '2026-08-12'
name: Bonjoro
nav: Providers
network: true
overview: 'Bonjoro publishes 1 API on the [APIs.io](https://apis.io/) network: API V2. Tagged areas include Video Messaging, Customer Engagement, Customer Success, Sales Engagement, and Marketing Automation.


  The Bonjoro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bonjoro''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Bonjoro Plans Pricing
  plan_count: 5
  slug: bonjoro-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Bonjoro Rate Limits
  slug: bonjoro-rate-limits
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 57.7
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 50.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bonjoro/refs/heads/main/screenshots/bonjoro-2026-08-17T080658.png
security:
- kind: authentication
  name: Bonjoro Authentication
  slug: bonjoro-authentication
  summary_line: oauth2/http-bearer · 2 schemes
- kind: domain-security
  name: Bonjoro Domain Security
  slug: bonjoro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bonjoro
tags:
- Video Messaging
- Customer Engagement
- Customer Success
- Sales Engagement
- Marketing Automation
- Video
- CRM Integration
- Testimonials
- Software-as-a-Service
- Australia
website: https://bonjoro.com/
---
