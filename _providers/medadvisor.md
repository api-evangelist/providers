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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 67
  human_in_the_loop: 1
  name: Medadvisor Agentic Access
  operation_count: 112
  slug: medadvisor-agentic-access
  summary_line: 112 operations · 67 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The 3rd-Party Integration API from MedAdvisor — 4 operation(s) for 3rd-party integration.
  name: MedAdvisor 3rd-Party Integration API
  slug: medadvisor-3rd-party-integration-api
- description: The Account API from MedAdvisor — 1 operation(s) for account.
  name: MedAdvisor Account API
  slug: medadvisor-account-api
- description: The Booking API from MedAdvisor — 27 operation(s) for booking.
  name: MedAdvisor Booking API
  slug: medadvisor-booking-api
- description: The BookingService API from MedAdvisor — 34 operation(s) for bookingservice.
  name: MedAdvisor Booking Service API
  slug: medadvisor-bookingservice-api
- description: The CalendarSetting API from MedAdvisor — 6 operation(s) for calendarsetting.
  name: MedAdvisor Calendar Setting API
  slug: medadvisor-calendarsetting-api
- description: The Clinic API from MedAdvisor — 8 operation(s) for clinic.
  name: MedAdvisor Clinic API
  slug: medadvisor-clinic-api
- description: The Communication API from MedAdvisor — 6 operation(s) for communication.
  name: MedAdvisor Communication API
  slug: medadvisor-communication-api
- description: The Config API from MedAdvisor — 2 operation(s) for config.
  name: MedAdvisor Config API
  slug: medadvisor-config-api
- description: The HeadOffice API from MedAdvisor — 6 operation(s) for headoffice.
  name: MedAdvisor Head Office API
  slug: medadvisor-headoffice-api
- description: The Inbox API from MedAdvisor — 8 operation(s) for inbox.
  name: MedAdvisor Inbox API
  slug: medadvisor-inbox-api
- description: The Logging API from MedAdvisor — 1 operation(s) for logging.
  name: MedAdvisor Logging API
  slug: medadvisor-logging-api
- description: The Pharmacist API from MedAdvisor — 3 operation(s) for pharmacist.
  name: MedAdvisor Pharmacist API
  slug: medadvisor-pharmacist-api
- description: The Pharmacy API from MedAdvisor — 31 operation(s) for pharmacy.
  name: MedAdvisor Pharmacy API
  slug: medadvisor-pharmacy-api
- description: The RefillOrder API from MedAdvisor — 14 operation(s) for refillorder.
  name: MedAdvisor Refill Order API
  slug: medadvisor-refillorder-api
artifact_total: 21
collections:
- collection_type: open
  name: Pharmacy Unified API v2.0
  slug: open-medadvisor-pharmacy-unified-v2
- collection_type: open
  name: Pharmacy Unified API v1.0
  slug: open-medadvisor-pharmacy-unified
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/medadvisor-capability-edges.yml
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
  name: MedAdvisor MCP Server
  slug: medadvisor-mcp-server
modified: '2026-07-24'
name: MedAdvisor
nav: Providers
network: true
overview: 'MedAdvisor publishes 14 APIs on the [APIs.io](https://apis.io/) network, including 3rd-Party Integration API, Account API, Booking API, and 11 more. Tagged areas include Healthcare, Australia, Pharmacy, Medication Management, and Medication Adherence.


  MedAdvisor''s developer surface includes authentication, API reference, documentation, support, and 24 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 44.6
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 40.2
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
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 51.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
