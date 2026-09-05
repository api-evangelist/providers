---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Upsie Agentic Access
  operation_count: 22
  slug: upsie-agentic-access
  summary_line: 22 operations · 12 acting
api_count: 8
apis:
- baseURL: https://api.upsie.com
  baseurl_source: declared
  description: The Authorization API from Upsie — 5 operation(s) for authorization.
  name: Upsie Authorization API
  slug: upsie-authorization-api
- baseURL: https://api.upsie.com
  baseurl_source: declared
  description: The Repair Assignments (/repairassignments) API from Upsie — 1 operation(s) for repair assignments (/repairassignments).
  name: Upsie Repair Assignments (/repairassignments) API
  slug: upsie-repair-assignments-repairassignments-api
- baseURL: https://api.upsie.com
  baseurl_source: declared
  description: The Repair Categories API from Upsie — 1 operation(s) for repair categories.
  name: Upsie Repair Categories API
  slug: upsie-repair-categories-api
- baseURL: https://api.upsie.com
  baseurl_source: declared
  description: The Repair Item Templates API from Upsie — 1 operation(s) for repair item templates.
  name: Upsie Repair Item Templates API
  slug: upsie-repair-item-templates-api
- baseURL: https://api.upsie.com
  baseurl_source: declared
  description: The Repair Items (/repairitems) API from Upsie — 1 operation(s) for repair items (/repairitems).
  name: Upsie Repair Items (/repairitems) API
  slug: upsie-repair-items-repairitems-api
- baseURL: https://api.upsie.com
  baseurl_source: declared
  description: The Repair Notes API from Upsie — 1 operation(s) for repair notes.
  name: Upsie Repair Notes API
  slug: upsie-repair-notes-api
- baseURL: https://api.upsie.com
  baseurl_source: declared
  description: The Repairs (/repairs) API from Upsie — 2 operation(s) for repairs (/repairs).
  name: Upsie Repairs (/repairs) API
  slug: upsie-repairs-repairs-api
- baseURL: https://api.upsie.com
  baseurl_source: declared
  description: The Webhooks API from Upsie — 2 operation(s) for webhooks.
  name: Upsie Webhooks API
  slug: upsie-webhooks-api
artifact_total: 22
asyncapis:
- description: ''
  name: Upsie Webhooks
  slug: upsie-webhooks
collections:
- collection_type: postman
  name: Upsie Partner Network API
  slug: postman-upsie-partner-network-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Upsie Partner Network Authorization API
  slug: open-upsie-authorization-api
- collection_type: open
  name: Upsie Partner Network Authorization Repair Assignments (/repairassignments) API
  slug: open-upsie-repair-assignments-repairassignments-api
- collection_type: open
  name: Upsie Partner Network Authorization Repair Categories API
  slug: open-upsie-repair-categories-api
- collection_type: open
  name: Upsie Partner Network Authorization Repair Item Templates API
  slug: open-upsie-repair-item-templates-api
- collection_type: open
  name: Upsie Partner Network Authorization Repair Items (/repairitems) API
  slug: open-upsie-repair-items-repairitems-api
- collection_type: open
  name: Upsie Partner Network Authorization Repair Notes API
  slug: open-upsie-repair-notes-api
- collection_type: open
  name: Upsie Partner Network Authorization Repairs (/repairs) API
  slug: open-upsie-repairs-repairs-api
- collection_type: open
  name: Upsie Partner Network Authorization Webhooks API
  slug: open-upsie-webhooks-api
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Upsie
nav: Providers
network: true
overview: 'Upsie publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Repair Assignments (/repairassignments) API, Repair Categories API, and 5 more. Tagged areas include Company, Warranties, Protection-Plans, Consumer Electronics, and Repairs.


  The Upsie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Upsie''s developer surface includes documentation, API reference, support, signup flow, authentication, sandbox, and 17 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 22.7
    developer_ergonomics: 43.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upsie/refs/heads/main/screenshots/upsie-2026-08-17T082639.png
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
- Protection-Plans
- Consumer Electronics
- Repairs
- Insurance
website: https://upsie.com/
---
