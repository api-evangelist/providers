---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.3
  scored_at: '2026-09-01'
api_count: 24
apis:
- description: The Appointment API from Podium — 1 operation(s) for appointment.
  name: Podium Appointment API
  slug: podium-appointment-api
- description: The Call API from Podium — 1 operation(s) for call.
  name: Podium Call API
  slug: podium-call-api
- description: The Campaign API from Podium — 2 operation(s) for campaign.
  name: Podium Campaign API
  slug: podium-campaign-api
- description: The Campaign Interaction API from Podium — 1 operation(s) for campaign interaction.
  name: Podium Campaign Interaction API
  slug: podium-campaign-interaction-api
- description: The Contact API from Podium — 6 operation(s) for contact.
  name: Podium Contact API
  slug: podium-contact-api
- description: The Contact Attribute API from Podium — 2 operation(s) for contact attribute.
  name: Podium Contact Attribute API
  slug: podium-contact-attribute-api
- description: The Contact Tag API from Podium — 2 operation(s) for contact tag.
  name: Podium Contact Tag API
  slug: podium-contact-tag-api
- description: The Conversation API from Podium — 4 operation(s) for conversation.
  name: Podium Conversation API
  slug: podium-conversation-api
- description: The Conversation Assignee API from Podium — 1 operation(s) for conversation assignee.
  name: Podium Conversation Assignee API
  slug: podium-conversation-assignee-api
- description: The Feedback API from Podium — 1 operation(s) for feedback.
  name: Podium Feedback API
  slug: podium-feedback-api
- description: The Invoice API from Podium — 6 operation(s) for invoice.
  name: Podium Invoice API
  slug: podium-invoice-api
- description: The Location API from Podium — 2 operation(s) for location.
  name: Podium Location API
  slug: podium-location-api
- description: The Message API from Podium — 6 operation(s) for message.
  name: Podium Message API
  slug: podium-message-api
- description: The Organization API from Podium — 1 operation(s) for organization.
  name: Podium Organization API
  slug: podium-organization-api
- description: The Payment API from Podium — 1 operation(s) for payment.
  name: Podium Payment API
  slug: podium-payment-api
- description: The Product API from Podium — 4 operation(s) for product.
  name: Podium Product API
  slug: podium-product-api
- description: The Reader API from Podium — 1 operation(s) for reader.
  name: Podium Reader API
  slug: podium-reader-api
- description: The Refund API from Podium — 2 operation(s) for refund.
  name: Podium Refund API
  slug: podium-refund-api
- description: The Review API from Podium — 2 operation(s) for review.
  name: Podium Review API
  slug: podium-review-api
- description: The Review Attribution API from Podium — 1 operation(s) for review attribution.
  name: Podium Review Attribution API
  slug: podium-review-attribution-api
- description: The Review Invite API from Podium — 2 operation(s) for review invite.
  name: Podium Review Invite API
  slug: podium-review-invite-api
- description: The Review Response API from Podium — 2 operation(s) for review response.
  name: Podium Review Response API
  slug: podium-review-response-api
- description: The Review Sites Summary API from Podium — 1 operation(s) for review sites summary.
  name: Podium Review Sites Summary API
  slug: podium-review-sites-summary-api
- description: The Review Summary API from Podium — 1 operation(s) for review summary.
  name: Podium Review Summary API
  slug: podium-review-summary-api
- description: The Template API from Podium — 2 operation(s) for template.
  name: Podium Template API
  slug: podium-template-api
- description: The User API from Podium — 2 operation(s) for user.
  name: Podium User API
  slug: podium-user-api
- description: The Webhook API from Podium — 2 operation(s) for webhook.
  name: Podium Webhook API
  slug: podium-webhook-api
artifact_total: 47
asyncapis:
- description: ''
  name: Podium Webhooks
  slug: podium-webhooks
collections:
- collection_type: open
  name: Accounts
  slug: open-podium-accounts
- collection_type: open
  name: Appointments
  slug: open-podium-appointments
- collection_type: open
  name: Campaigns
  slug: open-podium-campaigns
- collection_type: open
  name: Contacts
  slug: open-podium-contacts
- collection_type: open
  name: Conversations
  slug: open-podium-conversations
- collection_type: open
  name: Feedback (Surveys)
  slug: open-podium-feedback-surveys
- collection_type: open
  name: Messenger
  slug: open-podium-messenger
- collection_type: open
  name: Payments
  slug: open-podium-payments
- collection_type: open
  name: Phones
  slug: open-podium-phones
- collection_type: open
  name: Products
  slug: open-podium-products
- collection_type: open
  name: Webhooks
  slug: open-podium-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/podium-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-accounts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-appointments-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-campaigns-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-contacts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-conversations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-feedback-surveys-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-messenger-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-payments-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-phones-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-products-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-reviews-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/podium-webhooks-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.podium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.podium.com/reference/introduction
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.podium.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/podium
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podiumhq/
- group: company
  title: ''
  type: Blog
  url: https://www.podium.com/resource-center
- group: commercial
  title: ''
  type: Pricing
  url: https://www.podium.com/getpricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.podium.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/podiumhq/
- group: commercial
  title: ''
  type: Plans
  url: plans/podium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/podium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/podium-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/podium-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/podium-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/podium-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/podium-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/podium-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/podium-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/podium-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/podium-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.podium.com
- group: start
  title: ''
  type: Sandbox
  url: sandbox/podium-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/podium-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/podium-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/podium-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/podium-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/podium-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://docs.podium.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.podium.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/podium
- group: operate
  title: ''
  type: Support
  url: https://www.podium.com/knowledgebase/s
- group: start
  title: ''
  type: Login
  url: https://auth.podium.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.podium.com/#termsofservice-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.podium.com/#privacypolicy-us
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/podiumhq/podium-s-api-workspace
created: '2026-06-13'
description: Podium is a customer communication platform providing a REST API for local businesses to manage text-based conversations, reviews, payment requests, lead capture forms, webchat, and AI-driven lead conversion. The API is organized around REST with predictable resource-oriented URLs, JSON-encoded responses, and OAuth 2.0 authentication.
finops:
- name: Podium Finops
  service_category: ''
  slug: podium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podium.png
jsonld:
- class_count: 18
  name: Podium Context
  property_count: 3
  slug: podium-context
layout: provider
modified: '2026-08-14'
name: Podium
nav: Providers
network: true
overview: 'Podium publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Appointment API, Call API, Campaign API, and 24 more. Tagged areas include Customer Communication, Reviews, Messaging, Payments, and Web Chat.


  The Podium catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Podium''s developer surface includes documentation, engineering blog, pricing, authentication, changelog, sandbox, API reference, and 43 more developer resources.'
plans:
- name: Podium Plans Pricing
  plan_count: 0
  slug: podium-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Podium Rate Limits
  slug: podium-rate-limits
scopes:
- name: Podium Scopes
  scope_count: 25
  slug: podium-scopes
  summary_line: 25 scopes · authorizationCode
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 26
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 65.1
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 43.4
  previous_composite: 51.2
  provenance:
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
    score: 59.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podium/refs/heads/main/screenshots/podium-2026-06-20T191840.png
security:
- kind: authentication
  name: Podium Authentication
  slug: podium-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Podium Domain Security
  slug: podium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Podium Trust Center
  slug: podium-trust-center
  summary_line: trust center published
slug: podium
tags:
- Customer Communication
- Reviews
- Messaging
- Payments
- Web Chat
- Local Business
- SMS
- Lead Generation
website: https://www.podium.com/
---
