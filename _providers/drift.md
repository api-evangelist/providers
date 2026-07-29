---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Drift Agentic Access
  operation_count: 41
  slug: drift-agentic-access
  summary_line: 41 operations · 19 acting
api_count: 9
apis:
- description: The Accounts API from Drift — 4 operation(s) for accounts.
  name: Drift Accounts API
  slug: drift-accounts-api
- description: '[https://devdocs.drift.com/docs/app-uninstall](https://devdocs.drift.com/docs/app-uninstall)'
  name: Drift App Admin API
  slug: drift-app-admin-api
- description: '[https://devdocs.drift.com/docs/contact-model](https://devdocs.drift.com/docs/contact-model)'
  name: Drift Contacts API
  slug: drift-contacts-api
- description: '[https://devdocs.drift.com/docs/conversation-model](https://devdocs.drift.com/docs/conversation-model)'
  name: Drift Conversations and Messages API
  slug: drift-conversations-and-messages-api
- description: '[https://devdocs.drift.com/docs/automating-gdpr-retrieval-and-deletion](https://devdocs.drift.com/docs/automating-gdpr-retrieval-and-deletion)'
  name: Drift Data Privacy API
  slug: drift-data-privacy-api
- description: '[https://devdocs.drift.com/docs/playbook-model-1](https://devdocs.drift.com/docs/playbook-model-1)'
  name: Drift Playbooks API
  slug: drift-playbooks-api
- description: The SCIM API API from Drift — 2 operation(s) for scim api.
  name: Drift SCIM API API
  slug: drift-scim-api-api
- description: '[https://devdocs.drift.com/docs/team-model](https://devdocs.drift.com/docs/team-model)'
  name: Drift Teams API
  slug: drift-teams-api
- description: '[https://devdocs.drift.com/docs/user-model](https://devdocs.drift.com/docs/user-model)'
  name: Drift Users API
  slug: drift-users-api
artifact_total: 17
collections:
- collection_type: open
  name: Drift
  slug: open-drift
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drift-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drift-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drift
- group: company
  title: ''
  type: Website
  url: https://www.drift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.drift.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/drift-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drift-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/drift-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://devdocs.drift.com/llms.txt
created: '2026-05-08'
description: Drift (now part of Salesloft) is a conversational marketing and sales platform delivering chatbots, live chat, video, and account-based engagement on websites.
finops:
- name: Drift Finops
  service_category: Customer Support
  slug: drift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drift.png
json_structures:
- name: Drift Structure
  property_count: 0
  slug: drift-structure
layout: provider
modified: '2026-05-19'
name: Drift
nav: Providers
network: true
overview: 'Drift publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, App Admin API, Contacts API, and 6 more. Tagged areas include Conversational Marketing, Chatbots, Sales, Messaging, and Customer Engagement.


  Drift''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Drift Plans Pricing
  plan_count: 1
  slug: drift-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Drift Rate Limits
  slug: drift-rate-limits
score:
  band: thin
  composite: 28.4
  delta: -4.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 46.4
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drift/refs/heads/main/screenshots/drift-2026-06-20T180240.png
security:
- kind: authentication
  name: Drift Authentication
  slug: drift-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Drift Domain Security
  slug: drift-domain-security
  summary_line: TLSv1.3 · DMARC
slug: drift
tags:
- Conversational Marketing
- Chatbots
- Sales
- Messaging
- Customer Engagement
website: https://www.drift.com/
---
