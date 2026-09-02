---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Simpletexting Agentic Access
  operation_count: 38
  slug: simpletexting-agentic-access
  summary_line: 38 operations · 22 acting
api_count: 1
apis:
- description: Create and retrieve bulk campaigns to lists and segments.
  name: SimpleTexting Campaigns API
  slug: simpletexting-campaigns-api
- description: Manage contact lists and list membership.
  name: SimpleTexting Contact Lists API
  slug: simpletexting-contact-lists-api
- description: Read dynamic contact segments.
  name: SimpleTexting Contact Segments API
  slug: simpletexting-contact-segments-api
- description: Create, read, update, and delete individual contacts.
  name: SimpleTexting Contacts API
  slug: simpletexting-contacts-api
- description: Batch update and delete groups of contacts.
  name: SimpleTexting Contacts - Batch Operations API
  slug: simpletexting-contacts-batch-operations-api
- description: Read account custom fields / merge tags.
  name: SimpleTexting Custom Fields API
  slug: simpletexting-custom-fields-api
- description: Upload and manage MMS media items.
  name: SimpleTexting Media Items API
  slug: simpletexting-media-items-api
- description: Send and retrieve one-to-one SMS / MMS messages.
  name: SimpleTexting Messages API
  slug: simpletexting-messages-api
- description: Account information and sending phone numbers.
  name: SimpleTexting Tenant API
  slug: simpletexting-tenant-api
- description: Subscribe to platform events via HTTP callbacks.
  name: SimpleTexting Webhooks API
  slug: simpletexting-webhooks-api
- description: The Tenant phones API from SimpleTexting — 1 operation(s) for tenant phones.
  name: SimpleTexting Tenant phones API
  slug: simpletexting-tenant-phones-api
- description: 'Use webhooks to communicate between the SimpleTexting platform and your server. Webhooks can be used to forward messages as well as provide info about unsubscribes and message delivery. SimpleTexting '
  name: SimpleTexting Webhook Reports API
  slug: simpletexting-webhook-reports-api
artifact_total: 32
asyncapis:
- description: ''
  name: Simpletexting Webhooks
  slug: simpletexting-webhooks
collections:
- collection_type: open
  name: SimpleTexting API Documentation Campaigns API
  slug: open-simpletexting-campaigns-api
- collection_type: open
  name: SimpleTexting API Documentation Contact Lists API
  slug: open-simpletexting-contact-lists-api
- collection_type: open
  name: SimpleTexting API Documentation Contact Segments API
  slug: open-simpletexting-contact-segments-api
- collection_type: open
  name: SimpleTexting API Documentation Contacts API
  slug: open-simpletexting-contacts-api
- collection_type: open
  name: SimpleTexting API Documentation Contacts - Batch Operations API
  slug: open-simpletexting-contacts-batch-operations-api
- collection_type: open
  name: SimpleTexting API Documentation Custom Fields API
  slug: open-simpletexting-custom-fields-api
- collection_type: open
  name: SimpleTexting API Documentation Media Items API
  slug: open-simpletexting-media-items-api
- collection_type: open
  name: SimpleTexting API Documentation Messages API
  slug: open-simpletexting-messages-api
- collection_type: open
  name: SimpleTexting API Documentation Tenant API
  slug: open-simpletexting-tenant-api
- collection_type: open
  name: SimpleTexting API Documentation Tenant phones API
  slug: open-simpletexting-tenant-phones-api
- collection_type: open
  name: SimpleTexting API Documentation Webhook Reports API
  slug: open-simpletexting-webhook-reports-api
- collection_type: open
  name: SimpleTexting API Documentation Webhooks API
  slug: open-simpletexting-webhooks-api
- collection_type: open
  name: SimpleTexting API Documentation
  slug: open-simpletexting
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/simpletexting-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simpletexting-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simpletexting-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simpletexting-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://simpletexting.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simpletexting
- group: company
  title: ''
  type: Website
  url: https://simpletexting.com/
- group: docs
  title: ''
  type: Documentation
  url: https://simpletexting.com/api/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/simpletexting-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simpletexting-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/simpletexting-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/simpletexting-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simpletexting-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/simpletexting-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/simpletexting-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simpletexting-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simpletexting-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.simpletexting.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/simpletexting-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/simpletexting-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/simpletexting-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/simpletexting-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://simpletexting.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://api-doc.simpletexting.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.simpletexting.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.simpletexting.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://simpletexting.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app2.simpletexting.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app2.simpletexting.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simpletexting.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simpletexting.com/privacy-policy/
created: '2026-06-20'
description: SimpleTexting is a business SMS and MMS marketing platform. Its v2 REST API lets developers send single text messages, run bulk campaigns to lists and segments, manage contacts and contact lists, upload MMS media, provision sending numbers, and subscribe to delivery and incoming-message webhooks, all authenticated with a bearer token.
finops:
- name: Simpletexting Finops
  service_category: Communications
  slug: simpletexting-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simpletexting.png
layout: provider
modified: '2026-08-13'
name: SimpleTexting
nav: Providers
network: true
overview: 'SimpleTexting publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contact Lists API, Contact Segments API, and 9 more. Tagged areas include SMS, MMS, Messaging, Marketing, and Text Messaging.


  The SimpleTexting catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SimpleTexting''s developer surface includes authentication, engineering blog, documentation, API reference, support, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Simpletexting Plans Pricing
  plan_count: 2
  slug: simpletexting-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Simpletexting Rate Limits
  slug: simpletexting-rate-limits
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 24
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 4.5
    contract_quality: 63.0
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 51.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simpletexting/refs/heads/main/screenshots/simpletexting-2026-06-20T193933.png
security:
- kind: authentication
  name: Simpletexting Authentication
  slug: simpletexting-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Simpletexting Domain Security
  slug: simpletexting-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simpletexting
tags:
- SMS
- MMS
- Messaging
- Marketing
- Text Messaging
- SMS Marketing
- Communications
- Campaigns
- Contacts
- Webhook
- A2P 10DLC
website: https://simpletexting.com/
---
