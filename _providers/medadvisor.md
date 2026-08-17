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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 67
  human_in_the_loop: 1
  name: Medadvisor Agentic Access
  operation_count: 112
  slug: medadvisor-agentic-access
  summary_line: 112 operations · 67 acting · 1 human-in-the-loop
api_count: 8
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
- description: MedAdvisor Pharmacy Unified API v2.0 from MedAdvisor — 44 path(s) described in OpenAPI.
  name: MedAdvisor Pharmacy Unified API v2.0
  slug: medadvisor-pharmacy-unified-v2-openapi
artifact_total: 15
collections:
- collection_type: open
  name: Pharmacy Unified API v2.0
  slug: open-medadvisor-pharmacy-unified-v2
- collection_type: open
  name: Pharmacy Unified API v1.0
  slug: open-medadvisor-pharmacy-unified
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
overview: 'MedAdvisor publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Pharmacy Unified API - 3rd-Party Integration, Pharmacy Unified API - Booking Service, Pharmacy Unified API - Refill Order, and 5 more. Tagged areas include Healthcare, Australia, Pharmacy, Medication Management, and Medication Adherence.


  MedAdvisor''s developer surface includes authentication, API reference, documentation, support, and 23 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 48.5
    developer_ergonomics: 34.2
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medadvisor/refs/heads/main/screenshots/medadvisor-2026-08-07T172313.png
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
