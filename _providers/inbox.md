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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Mailgun provides a programmable email API for sending, receiving, tracking, and validating email at scale. Endpoints cover messages, domains, suppressions, mailing lists, webhooks, inbound routes, eve
  name: Mailgun Email API
  slug: mailgun-email-api
- description: 'Nylas exposes a unified REST API for email, calendar, contacts, and scheduling across Google, Microsoft, iCloud, and IMAP providers. Developers can read, send, and thread messages, manage folders and '
  name: Nylas Email API
  slug: nylas-email-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/inbox-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inbox-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inbox-llms.txt
- group: company
  title: ''
  type: Website
  url: https://apievangelist.com/
coverage:
  checked: '2026-08-13'
  detail: Inbox is an API Evangelist editorial index of email API platforms, not a company — it owns no domain and ships no API, and the two APIs it lists (Mailgun, Nylas) are published by third parties whose own profiles already hold their specs, so nothing discoverable here belongs to this entry.
  evidence:
  - status: 200
    url: https://developer.nylas.com/.well-known/api-catalog
  - status: 200
    url: https://documentation.mailgun.com/llms.txt
  - status: 404
    url: https://api.mailgun.net/openapi.json
  - status: 404
    url: https://api.us.nylas.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2024-12-25'
description: Inbox is an API Evangelist index of email and inbox-oriented API platforms that developers use to send, receive, parse, route, schedule, and verify email messages. The index focuses on transactional and conversational email providers exposing programmatic access to message lifecycle, deliverability, and inbox automation primitives.
finops:
- name: Inbox Finops
  service_category: API
  slug: inbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inbox.png
layout: provider
modified: '2026-08-13'
name: Inbox
nav: Providers
network: true
overview: Inbox publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Inbox, Messaging, Deliverability, and Transactional Email.
plans:
- name: Inbox Plans Pricing
  plan_count: 3
  slug: inbox-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Inbox Rate Limits
  slug: inbox-rate-limits
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 21.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inbox/refs/heads/main/screenshots/inbox-2026-06-20T183305.png
security:
- kind: domain-security
  name: Inbox Domain Security
  slug: inbox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Inbox Trust Center
  slug: inbox-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: inbox
tags:
- Email
- Inbox
- Messaging
- Deliverability
- Transactional Email
website: https://apievangelist.com/
---
