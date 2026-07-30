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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Pylon Agentic Access
  operation_count: 68
  slug: pylon-agentic-access
  summary_line: 68 operations · 44 acting
api_count: 9
apis:
- description: Customer accounts.
  name: Pylon Accounts API
  slug: pylon-accounts-api
- description: Individual contacts (end customers).
  name: Pylon Contacts API
  slug: pylon-contacts-api
- description: Custom field definitions.
  name: Pylon Custom Fields API
  slug: pylon-custom-fields-api
- description: Support issues (tickets).
  name: Pylon Issues API
  slug: pylon-issues-api
- description: Knowledge bases, collections, and articles.
  name: Pylon Knowledge Base API
  slug: pylon-knowledge-base-api
- description: Tags used across issues, accounts, and contacts.
  name: Pylon Tags API
  slug: pylon-tags-api
- description: Tasks, projects, and milestones.
  name: Pylon Tasks API
  slug: pylon-tasks-api
- description: Support teams.
  name: Pylon Teams API
  slug: pylon-teams-api
- description: Internal Pylon users (agents).
  name: Pylon Users API
  slug: pylon-users-api
artifact_total: 17
collections:
- collection_type: open
  name: Pylon API
  slug: open-pylon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pylon-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pylon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pylon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pylon-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usepylon
- group: company
  title: ''
  type: Website
  url: https://usepylon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usepylon.com/pylon-docs/developer/api
- group: commercial
  title: ''
  type: Plans
  url: plans/pylon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pylon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pylon-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://usepylon.com/blog
created: '2026-06-20'
description: Pylon (usepylon.com) is a B2B customer support and customer operations platform that unifies shared Slack, Microsoft Teams, email, and chat support into a single ticketing system, with a knowledge base, accounts and contacts, AI agents, and a documented public REST API at https://api.usepylon.com.
finops:
- name: Pylon Finops
  service_category: Customer Support and Operations
  slug: pylon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pylon.png
layout: provider
modified: '2026-06-20'
name: Pylon
nav: Providers
network: true
overview: 'Pylon publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contacts API, Custom Fields API, and 6 more. Tagged areas include Customer Support, Customer Operations, Ticketing, Knowledge Base, and B2B.


  Pylon''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Pylon Plans Pricing
  plan_count: 4
  slug: pylon-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 3
  name: Pylon Rate Limits
  slug: pylon-rate-limits
score:
  band: thin
  composite: 38.3
  delta: -2.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pylon/refs/heads/main/screenshots/pylon-2026-06-20T192331.png
security:
- kind: authentication
  name: Pylon Authentication
  slug: pylon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pylon Domain Security
  slug: pylon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pylon Trust Center
  slug: pylon-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: pylon
tags:
- Customer Support
- Customer Operations
- Ticketing
- Knowledge Base
- B2B
- Help Desk
website: https://usepylon.com/
---
