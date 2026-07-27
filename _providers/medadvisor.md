---
access_model:
  confidence: medium
  label: Partner / integrator onboarding
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - review
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 67
  human_in_the_loop: 1
  name: Medadvisor Agentic Access
  operation_count: 112
  slug: medadvisor-agentic-access
  summary_line: 112 operations · 67 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: The publicly documented third-party integration surface of MedAdvisor's Pharmacy Unified API, enabling external widgets and eCommerce platforms to authenticate, look up pharmacy details, retrieve eScr
  name: Pharmacy Unified API - 3rd-Party Integration
  slug: pharmacy-unified-third-party-integration
- description: 'Appointment and clinical-service booking operations within the Pharmacy Unified API - listing available pharmacy services and time slots, creating and editing event bookings, managing event resources '
  name: Pharmacy Unified API - Booking Service
  slug: pharmacy-unified-booking-service
- description: Medication refill and order management operations within the Pharmacy Unified API - retrieving pending and completed orders, sending eScript tokens, adding line items and notes, processing patient-ini
  name: Pharmacy Unified API - Refill Order
  slug: pharmacy-unified-refill-order
- description: Operations for the pharmacy PlusOne inbox within the Pharmacy Unified API - retrieving the main inbox, sent, completed, scheduled, and ready-to-collect message queues, adding scripts, sending schedule
  name: Pharmacy Unified API - Inbox
  slug: pharmacy-unified-inbox
- description: Patient-communication and group-messaging operations within the Pharmacy Unified API - creating and editing patient groups, managing group membership, and supporting targeted patient outreach from the
  name: Pharmacy Unified API - Communication
  slug: pharmacy-unified-communication
- description: Head-office (banner / multi-pharmacy) operations within the Pharmacy Unified API - managing services across a group of pharmacies, listing pharmacies, and pushing services with deadlines out to indivi
  name: Pharmacy Unified API - Head Office
  slug: pharmacy-unified-head-office
- description: Pharmacy account, settings, and administration operations within the Pharmacy Unified API - retrieving pharmacy details and module/feature settings, patient search, account registration and activation
  name: Pharmacy Unified API - Pharmacy
  slug: pharmacy-unified-pharmacy
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/medadvisor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medadvisor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/medadvisor-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/medadvisor-pharmacy-unified-v2-openapi.json
- group: design
  title: ''
  type: Conventions
  url: conventions/medadvisor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/medadvisor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medadvisor-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/medadvisor-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medadvisor-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.medadvisorsolutions.com/en-au/data-and-privacy
- group: auth
  title: ''
  type: TrustCenter
  url: security/medadvisor-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/medadvisor-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/medadvisor-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medadvisor-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/medadvisor-pharmacy-unified-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/medadvisor-pharmacy-unified-v2-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/medadvisor-third-party-escript-integration.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/medadvisor-book-pharmacy-service.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/medadvisor-fulfil-refill-order.md
- group: company
  title: ''
  type: Website
  url: https://www.medadvisor.com.au
- group: company
  title: ''
  type: CompanyWebsite
  url: https://www.medadvisorsolutions.com/
- group: docs
  title: ''
  type: APIReference
  url: https://pharmacy-unified.api.medadvisor.com.au/swagger/
- group: docs
  title: ''
  type: Documentation
  url: https://support.medadvisor.com.au
- group: operate
  title: ''
  type: Support
  url: https://support.medadvisor.com.au
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medadvisor.com.au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medadvisorsolutions.com/terms-and-conditions
- group: operate
  title: ''
  type: Contact
  url: https://www.medadvisorsolutions.com/contact
created: '2026-07-24'
description: MedAdvisor (MedAdvisor Solutions) is an Australian-founded, ASX-listed medication management and patient engagement technology company whose pharmacy workflow software runs in more than 95% of Australian community pharmacies and reaches over 4 million patients. Its clinician-facing platform - the web-based "MedAdvisor for Pharmacy" that replaced the long-running PlusOne desktop software - handles dispense workflow, medication adherence, appointment and service booking (vaccinations, health checks, scope-of-practice services), e-script (eScript) token handling, refill ordering, and omnichannel patient communication, alongside a consumer medication app. On the developer side MedAdvisor exposes a real, Swagger-documented HTTP REST surface, the Pharmacy Unified API, at pharmacy-unified.api.medadvisor.com.au, including a "3rd-Party Integration" family (partner login, pharmacy lookup, eScript status, and order notification into the pharmacy PlusOne inbox) for third-party widgets and
  eCommerce integrations. Authentication is a JWT bearer token obtained via a clientId/clientSecret plus Base64-encoded pharmacy credentials exchange; the surface is HL7/HTTP REST rather than HL7 FHIR - no public FHIR CapabilityStatement or SMART-on-FHIR configuration is served. Home market is Australia, positioned as the dominant community-pharmacy engagement layer sitting between dispense systems, pharmaceutical programs, and patients.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: medadvisor-mcp.yml
  slug: medadvisor-mcpyml
modified: '2026-07-24'
name: MedAdvisor
nav: Providers
network: true
overview: 'MedAdvisor publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Pharmacy Unified API - 3rd-Party Integration, Pharmacy Unified API - Booking Service, Pharmacy Unified API - Refill Order, and 4 more. Tagged areas include Healthcare, Australia, Pharmacy, Medication Management, and Medication Adherence.


  MedAdvisor''s developer surface includes authentication, API reference, documentation, support, and 23 more developer resources.'
random_paper: 50
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 37.7
    developer_ergonomics: 45.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 40.3
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Medadvisor Authentication
  slug: medadvisor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Medadvisor Domain Security
  slug: medadvisor-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Medadvisor Trust Center
  slug: medadvisor-trust-center
  summary_line: ISO 27001, HIPAA, GDPR, Australian Privacy Principles
slug: medadvisor
tags:
- Healthcare
- Australia
- Pharmacy
- Medication Management
- Medication Adherence
- e-Prescribing
- eScript
- Patient Engagement
- Appointment Booking
- Digital Health
- Healthcare API
website: https://www.medadvisor.com.au
---
