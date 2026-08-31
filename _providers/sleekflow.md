---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Sleekflow Agentic Access
  operation_count: 27
  slug: sleekflow-agentic-access
  summary_line: 27 operations · 14 acting
api_count: 1
apis:
- description: Manage company records.
  name: SleekFlow Companies API
  slug: sleekflow-companies-api
- description: Create, read, search, update, and delete contacts.
  name: SleekFlow Contacts API
  slug: sleekflow-contacts-api
- description: Read conversations and update conversation assignment.
  name: SleekFlow Conversations API
  slug: sleekflow-conversations-api
- description: Manage contact lists and list membership.
  name: SleekFlow Lists API
  slug: sleekflow-lists-api
- description: Send messages, files, and internal notes; check conversation windows.
  name: SleekFlow Messaging API
  slug: sleekflow-messaging-api
- description: Manage staff and teams.
  name: SleekFlow Staff and Teams API
  slug: sleekflow-staff-and-teams-api
- description: Register webhook subscriptions for platform events.
  name: SleekFlow Webhooks API
  slug: sleekflow-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SleekFlow Platform Companies API
  slug: open-sleekflow-companies-api
- collection_type: open
  name: SleekFlow Platform Companies Contacts API
  slug: open-sleekflow-contacts-api
- collection_type: open
  name: SleekFlow Platform Companies Conversations API
  slug: open-sleekflow-conversations-api
- collection_type: open
  name: SleekFlow Platform Companies Lists API
  slug: open-sleekflow-lists-api
- collection_type: open
  name: SleekFlow Platform Companies Messaging API
  slug: open-sleekflow-messaging-api
- collection_type: open
  name: SleekFlow Platform Companies Staff and Teams API
  slug: open-sleekflow-staff-and-teams-api
- collection_type: open
  name: SleekFlow Platform Companies Webhooks API
  slug: open-sleekflow-webhooks-api
- collection_type: open
  name: SleekFlow Platform API
  slug: open-sleekflow
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sleekflow-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sleekflow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sleekflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sleekflow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sleekflow
- group: company
  title: ''
  type: Website
  url: https://sleekflow.io
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.sleekflow.io/docs/platform-api/nijbjgxrs4s50-sleek-flow-platform-api
- group: commercial
  title: ''
  type: Plans
  url: plans/sleekflow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sleekflow-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sleekflow-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sleekflow.io/blog
created: '2026-06-20'
description: SleekFlow is an omnichannel social-commerce and customer-engagement platform that unifies WhatsApp, Facebook Messenger, Instagram, WeChat, LINE, SMS, and live chat into a single inbox with automation, broadcast, and AI. The SleekFlow Platform API exposes contacts, conversations, messaging, companies, lists, staff and teams, and webhooks for building custom integrations on top of the platform.
finops:
- name: Sleekflow Finops
  service_category: Business Application Services
  slug: sleekflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sleekflow.png
layout: provider
modified: '2026-06-20'
name: SleekFlow
nav: Providers
network: true
overview: 'SleekFlow publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Contacts API, Conversations API, and 4 more. Tagged areas include Messaging, Omnichannel, WhatsApp, Customer Engagement, and Social Commerce.


  SleekFlow''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sleekflow Plans Pricing
  plan_count: 5
  slug: sleekflow-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Sleekflow Rate Limits
  slug: sleekflow-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sleekflow/refs/heads/main/screenshots/sleekflow-2026-06-20T194028.png
security:
- kind: authentication
  name: Sleekflow Authentication
  slug: sleekflow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sleekflow Domain Security
  slug: sleekflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sleekflow
tags:
- Messaging
- Omnichannel
- WhatsApp
- Customer Engagement
- Social Commerce
- Automation
website: https://sleekflow.io
---
