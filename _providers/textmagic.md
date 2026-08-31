---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Textmagic Agentic Access
  operation_count: 49
  slug: textmagic-agentic-access
  summary_line: 49 operations · 20 acting
api_count: 1
apis:
- description: Track bulk send sessions.
  name: Textmagic Bulk API
  slug: textmagic-bulk-api
- description: Manage two-way conversations.
  name: Textmagic Chats API
  slug: textmagic-chats-api
- description: Manage contacts in the address book.
  name: Textmagic Contacts API
  slug: textmagic-contacts-api
- description: Manage contact lists.
  name: Textmagic Lists API
  slug: textmagic-lists-api
- description: Send and manage outbound SMS messages.
  name: Textmagic Messages API
  slug: textmagic-messages-api
- description: Find and manage dedicated virtual numbers.
  name: Textmagic Numbers API
  slug: textmagic-numbers-api
- description: Retrieve and manage inbound messages.
  name: Textmagic Replies API
  slug: textmagic-replies-api
- description: Manage scheduled (future-dated) messages.
  name: Textmagic Schedules API
  slug: textmagic-schedules-api
- description: Apply for and manage alphanumeric sender IDs.
  name: Textmagic Sender IDs API
  slug: textmagic-sender-ids-api
- description: Account, usage, and spending statistics.
  name: Textmagic Stats API
  slug: textmagic-stats-api
- description: Manage reusable message templates.
  name: Textmagic Templates API
  slug: textmagic-templates-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Textmagic REST Bulk API
  slug: open-textmagic-bulk-api
- collection_type: open
  name: Textmagic REST Bulk Chats API
  slug: open-textmagic-chats-api
- collection_type: open
  name: Textmagic REST Bulk Contacts API
  slug: open-textmagic-contacts-api
- collection_type: open
  name: Textmagic REST Bulk Lists API
  slug: open-textmagic-lists-api
- collection_type: open
  name: Textmagic REST Bulk Messages API
  slug: open-textmagic-messages-api
- collection_type: open
  name: Textmagic REST Bulk Numbers API
  slug: open-textmagic-numbers-api
- collection_type: open
  name: Textmagic REST Bulk Replies API
  slug: open-textmagic-replies-api
- collection_type: open
  name: Textmagic REST Bulk Schedules API
  slug: open-textmagic-schedules-api
- collection_type: open
  name: Textmagic REST Bulk Sender IDs API
  slug: open-textmagic-sender-ids-api
- collection_type: open
  name: Textmagic REST Bulk Stats API
  slug: open-textmagic-stats-api
- collection_type: open
  name: Textmagic REST Bulk Templates API
  slug: open-textmagic-templates-api
- collection_type: open
  name: Textmagic REST API
  slug: open-textmagic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/textmagic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/textmagic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/textmagic-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.textmagic.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/textmagic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/textmagic
- group: company
  title: ''
  type: Website
  url: https://www.textmagic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.textmagic.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/textmagic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/textmagic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/textmagic-finops.yml
created: '2026-06-20'
description: Textmagic is a business text-messaging platform offering two-way SMS, bulk messaging, SMS marketing, and team inboxes. Its REST API (v2) lets developers send and receive messages, manage contacts and lists, schedule and template messages, and administer sender IDs and dedicated numbers programmatically over HTTPS.
finops:
- name: Textmagic Finops
  service_category: Communications
  slug: textmagic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/textmagic.png
layout: provider
modified: '2026-06-20'
name: Textmagic
nav: Providers
network: true
overview: 'Textmagic publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Bulk API, Chats API, Contacts API, and 8 more. Tagged areas include SMS, Text Messaging, Messaging, Communications, and CPaaS.


  Textmagic''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Textmagic Plans Pricing
  plan_count: 4
  slug: textmagic-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Textmagic Rate Limits
  slug: textmagic-rate-limits
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/textmagic/refs/heads/main/screenshots/textmagic-2026-06-20T195211.png
security:
- kind: authentication
  name: Textmagic Authentication
  slug: textmagic-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Textmagic Domain Security
  slug: textmagic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: textmagic
tags:
- SMS
- Text Messaging
- Messaging
- Communications
- CPaaS
website: https://www.textmagic.com
---
