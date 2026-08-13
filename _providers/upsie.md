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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Upsie Agentic Access
  operation_count: 22
  slug: upsie-agentic-access
  summary_line: 22 operations · 12 acting
api_count: 8
apis:
- description: The Authorization API from Upsie — 5 operation(s) for authorization.
  name: Upsie Authorization API
  slug: upsie-authorization-api
- description: The Repair Assignments (/repairassignments) API from Upsie — 1 operation(s) for repair assignments (/repairassignments).
  name: Upsie Repair Assignments (/repairassignments) API
  slug: upsie-repair-assignments-repairassignments-api
- description: The Repair Categories API from Upsie — 1 operation(s) for repair categories.
  name: Upsie Repair Categories API
  slug: upsie-repair-categories-api
- description: The Repair Item Templates API from Upsie — 1 operation(s) for repair item templates.
  name: Upsie Repair Item Templates API
  slug: upsie-repair-item-templates-api
- description: The Repair Items (/repairitems) API from Upsie — 1 operation(s) for repair items (/repairitems).
  name: Upsie Repair Items (/repairitems) API
  slug: upsie-repair-items-repairitems-api
- description: The Repair Notes API from Upsie — 1 operation(s) for repair notes.
  name: Upsie Repair Notes API
  slug: upsie-repair-notes-api
- description: The Repairs (/repairs) API from Upsie — 2 operation(s) for repairs (/repairs).
  name: Upsie Repairs (/repairs) API
  slug: upsie-repairs-repairs-api
- description: The Webhooks API from Upsie — 2 operation(s) for webhooks.
  name: Upsie Webhooks API
  slug: upsie-webhooks-api
artifact_total: 14
asyncapis:
- description: ''
  name: Upsie Webhooks
  slug: upsie-webhooks
collections:
- collection_type: postman
  name: Upsie Partner Network API
  slug: postman-upsie-partner-network-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/upsie-partner-network-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/upsie-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upsie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upsie.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documenter.getpostman.com/view/16328390/2s8ZDeUykK
- group: docs
  title: ''
  type: APIReference
  url: https://documenter.getpostman.com/view/16328390/2s8ZDeUykK
- group: build
  title: ''
  type: Postman
  url: postman/upsie-partner-network-api.postman_collection.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upsie
- group: operate
  title: ''
  type: Support
  url: https://upsie.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://upsie.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.termly.io/document/terms-of-use-for-saas/e4aa24cb-f6f6-4ebd-95bc-5e963adcacb1
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upsie.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://upsie.com/create-account
- group: auth
  title: ''
  type: Authentication
  url: authentication/upsie-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/upsie-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/upsie-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/upsie-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/upsie-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/upsie-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/upsie-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/upsie-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upsie-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Upsie is a direct-to-consumer warranty company offering affordable, transparent extended-warranty and protection plans for smartphones, laptops, TVs, appliances, and other consumer electronics, positioning itself as "the new way to warranty" against overpriced retailer protection plans. Alongside its consumer products, Upsie operates an independent repair network and publishes the Upsie Partner Network API — a JWT-authenticated REST API (api.upsie.com, documented via a public Postman collection) that lets repair-network partners create and manage repairs, repair items, notes, assignments, and categories, and subscribe to webhook events such as repair status updates.
image: https://res.cloudinary.com/upsie/image/upload/f_auto,fl_lossy,q_auto/v1635433345/Upsie_Badge.png
layout: provider
mcp_servers:
- description: ''
  name: upsie-mcp.yml
  slug: upsie-mcpyml
modified: '2026-07-21'
name: Upsie
nav: Providers
network: true
overview: 'Upsie publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Repair Assignments (/repairassignments) API, Repair Categories API, and 5 more. Tagged areas include Company, Warranties, Protection Plans, Consumer Electronics, and Repairs.


  The Upsie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Upsie''s developer surface includes documentation, API reference, support, signup flow, authentication, sandbox, and 17 more developer resources.'
random_paper: 70
score:
  band: developing
  composite: 42.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 66.8
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Upsie Authentication
  slug: upsie-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Upsie Domain Security
  slug: upsie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upsie
tags:
- Company
- Warranties
- Protection Plans
- Consumer Electronics
- Repairs
- Insurance
website: https://upsie.com/
---
