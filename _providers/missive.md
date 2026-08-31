---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
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
- acting_count: 8
  human_in_the_loop: 0
  name: Missive Agentic Access
  operation_count: 19
  slug: missive-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
apis:
- description: Create and retrieve analytics reports
  name: Missive Analytics API
  slug: missive-analytics-api
- description: List available contact books
  name: Missive Contact Books API
  slug: missive-contact-books-api
- description: List contact groups and organizations
  name: Missive Contact Groups API
  slug: missive-contact-groups-api
- description: Manage contacts and contact data
  name: Missive Contacts API
  slug: missive-contacts-api
- description: Manage conversations in the inbox
  name: Missive Conversations API
  slug: missive-conversations-api
- description: Create and delete draft messages
  name: Missive Drafts API
  slug: missive-drafts-api
- description: Create messages in custom channels
  name: Missive Messages API
  slug: missive-messages-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Missive REST Analytics API
  slug: open-missive-analytics-api
- collection_type: open
  name: Missive REST Analytics Contact Books API
  slug: open-missive-contact-books-api
- collection_type: open
  name: Missive REST Analytics Contact Groups API
  slug: open-missive-contact-groups-api
- collection_type: open
  name: Missive REST Analytics Contacts API
  slug: open-missive-contacts-api
- collection_type: open
  name: Missive REST Analytics Conversations API
  slug: open-missive-conversations-api
- collection_type: open
  name: Missive REST Analytics Drafts API
  slug: open-missive-drafts-api
- collection_type: open
  name: Missive REST Analytics Messages API
  slug: open-missive-messages-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/missive-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/missive-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/missive-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/missive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/missive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/missive-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://missiveapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://missiveapp.com/docs/developers/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/missive
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/missive-app
- group: company
  title: ''
  type: Blog
  url: https://missiveapp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://missiveapp.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.missiveapp.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/missiveapp
- group: commercial
  title: ''
  type: Plans
  url: plans/missive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/missive-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/missive-finops.yml
created: '2026-06-12'
description: Missive is a team inbox and collaboration platform that brings email, SMS, WhatsApp, Instagram, Facebook Messenger, and live chat into one unified workspace. It provides a REST API for managing conversations, messages, contacts, labels, drafts, analytics, and automation rules, enabling teams to integrate Missive into business workflows. The API supports webhooks for real-time event notifications, custom channels for integrating external communication sources, and UI/iFrame integrations via JavaScript. Developers can automate drafts, sync contacts, generate analytics reports, and build custom integrations with the platform.
finops:
- name: Missive Finops
  service_category: ''
  slug: missive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/missive.png
jsonld:
- class_count: 77
  name: Missive Context
  property_count: 0
  slug: missive-context
layout: provider
modified: '2026-06-12'
name: Missive
nav: Providers
network: true
overview: 'Missive publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Contact Books API, Contact Groups API, and 4 more. Tagged areas include Team Inbox, Collaboration, Email, Messaging, and Conversations.


  The Missive catalog on APIs.io includes 1 JSON-LD context.


  Missive''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Missive Plans Pricing
  plan_count: 3
  slug: missive-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Missive Rate Limits
  slug: missive-rate-limits
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 61.2
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/missive/refs/heads/main/screenshots/missive-2026-06-20T185610.png
security:
- kind: authentication
  name: Missive Authentication
  slug: missive-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Missive Domain Security
  slug: missive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Missive Vulnerability Disclosure
  slug: missive-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Missive Trust Center
  slug: missive-trust-center
  summary_line: SOC 2, GDPR
slug: missive
tags:
- Team Inbox
- Collaboration
- Email
- Messaging
- Conversations
- Contacts
- Webhook
- Automation
- REST API
website: https://missiveapp.com
---
