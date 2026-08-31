---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Respond Agentic Access
  operation_count: 20
  slug: respond-agentic-access
  summary_line: 20 operations · 15 acting
api_count: 1
apis:
- description: Internal collaboration comments on a contact.
  name: Respond.io Comments API
  slug: respond-comments-api
- description: Create, read, update, merge, list, and delete contacts.
  name: Respond.io Contacts API
  slug: respond-contacts-api
- description: Open, close, status, and assign conversations.
  name: Respond.io Conversations API
  slug: respond-conversations-api
- description: Structured contact metadata definitions.
  name: Respond.io Custom Fields API
  slug: respond-custom-fields-api
- description: Send messages to contacts and read message history.
  name: Respond.io Messages API
  slug: respond-messages-api
- description: Workspace tags and contact tag assignment.
  name: Respond.io Tags API
  slug: respond-tags-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Respond.io Developer Comments API
  slug: open-respond-comments-api
- collection_type: open
  name: Respond.io Developer Comments Contacts API
  slug: open-respond-contacts-api
- collection_type: open
  name: Respond.io Developer Comments Conversations API
  slug: open-respond-conversations-api
- collection_type: open
  name: Respond.io Developer Comments Custom Fields API
  slug: open-respond-custom-fields-api
- collection_type: open
  name: Respond.io Developer Comments Messages API
  slug: open-respond-messages-api
- collection_type: open
  name: Respond.io Developer Comments Tags API
  slug: open-respond-tags-api
- collection_type: open
  name: Respond.io Developer API
  slug: open-respond
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/respond-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/respond-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/respond-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/respond-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/respond-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/respond-io
- group: company
  title: ''
  type: Website
  url: https://respond.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.respond.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/respond-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/respond-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/respond-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://respond.io/blog/rss.xml
created: '2026-06-20'
description: Respond.io is an AI-powered customer-conversation management platform that unifies omnichannel messaging - WhatsApp, Messenger, Instagram, Telegram, SMS, email, and website chat - into a single inbox. Its REST Developer API lets businesses manage contacts, send and read messages across channels, manage conversations, post comments, apply tags and custom fields, and subscribe to webhooks.
finops:
- name: Respond Finops
  service_category: Customer Engagement and Messaging
  slug: respond-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/respond.png
layout: provider
modified: '2026-06-20'
name: Respond.io
nav: Providers
network: true
overview: 'Respond.io publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Contacts API, Conversations API, and 3 more. Tagged areas include Messaging, Omnichannel, Customer Conversations, WhatsApp, and Artificial Intelligence.


  Respond.io''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Respond Plans Pricing
  plan_count: 4
  slug: respond-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Respond Rate Limits
  slug: respond-rate-limits
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 59.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/respond/refs/heads/main/screenshots/respond-2026-06-20T192954.png
security:
- kind: authentication
  name: Respond Authentication
  slug: respond-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Respond Domain Security
  slug: respond-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Respond Trust Center
  slug: respond-trust-center
  summary_line: ISO 27001, GDPR
slug: respond
tags:
- Messaging
- Omnichannel
- Customer Conversations
- WhatsApp
- Artificial Intelligence
website: https://respond.io/
---
