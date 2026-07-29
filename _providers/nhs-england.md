---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Nhs England Agentic Access
  operation_count: 70
  slug: nhs-england-agentic-access
  summary_line: 70 operations · 32 acting
api_count: 10
apis:
- description: National electronic database of NHS patient demographic details - name, address, date of birth, related people, registered GP, nominated pharmacy and NHS number - exposed as an HL7 FHIR R4 API. Produc
  name: Personal Demographics Service (PDS) - FHIR API
  slug: nhs-personal-demographics-service-fhir
- description: Lets authorised health and social care staff retrieve a patient's GP practice record as structured HL7 FHIR resources (medications, allergies, problems, immunisations, and more) from EMIS and TPP Syst
  name: GP Connect Access Record - Structured - FHIR API
  slug: nhs-gp-connect-access-record-structured-fhir
- description: 'National service for sending electronic prescriptions from prescribers to dispensers (pharmacies), exposed as an HL7 FHIR R4 API. Sandbox FHIR endpoint confirmed live (returns a FHIR OperationOutcome '
  name: Electronic Prescription Service (EPS) - FHIR API
  slug: nhs-electronic-prescription-service-fhir
- description: Create paperless referrals from primary to secondary care and receive referrals, Clinical Referral Information (CRI) and attachments from the NHS e-Referral Service, as an HL7 FHIR API. OpenAPI harves
  name: e-Referral Service (e-RS) - FHIR API
  slug: nhs-e-referral-service-fhir
- description: Sends booking and referral information between NHS service providers using the Booking and Referral Standard as an HL7 FHIR R4 API. OpenAPI harvested verbatim (8 paths).
  name: Booking and Referral Standard (BaRS) - FHIR API
  slug: nhs-booking-and-referral-fhir
- description: Access a patient's immunisation record (including coronavirus, influenza and HPV immunisations) as an HL7 FHIR R4 API. OpenAPI harvested verbatim.
  name: Immunisation History - FHIR API
  slug: nhs-immunisation-history-fhir
- description: Reference data on NHS and healthcare organisations, roles and terminology (the Organisation Data Service), exposed as an HL7 FHIR R4 API. OpenAPI harvested verbatim (8 paths).
  name: Organisation Data Service (ODS) - FHIR API
  slug: nhs-organisation-data-service-fhir
- description: Integrate with the NHS App to deliver messages and content to citizens and to link into NHS App journeys. OpenAPI harvested verbatim (4 paths).
  name: NHS App API
  slug: nhs-app-api
- description: National service for sending messages to people about their health and care across channels (NHS App, SMS, email, letter). OpenAPI harvested verbatim (7 paths).
  name: NHS Notify (Communications Manager) API
  slug: nhs-notify-communications-manager
- description: Search the national Directory of Healthcare Services for NHS organisations, services and their attributes. OpenAPI harvested verbatim.
  name: Service Search (Directory of Healthcare Services) API
  slug: nhs-service-search
artifact_total: 16
asyncapis:
- description: ''
  name: Nhs England Webhooks
  slug: nhs-england-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nhs-england-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nhs-england-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nhs-england-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nhs-england-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://digital.nhs.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://digital.nhs.uk/developer
- group: docs
  title: ''
  type: APIReference
  url: https://digital.nhs.uk/developer/api-catalogue
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NHSDigital
- group: operate
  title: ''
  type: Support
  url: https://digital.nhs.uk/developer/help-and-support
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nhs-england-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nhs-england-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://www.england.nhs.uk/security-vulnerability-disclosure/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nhs-england-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nhs-england-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nhs-england-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/nhs-england-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.england.nhs.uk/long-read/digital-clinical-safety-assurance/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nhs-england-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nhs-england-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://digital.nhs.uk/services/e-referral-service/api/updates-and-releases/sunsetting-policy
- group: design
  title: ''
  type: Conventions
  url: conventions/nhs-england-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nhs-england-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nhs-england-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nhs-england-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://digital.nhs.uk/developer/guides-and-documentation/reference-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://digital.nhs.uk/developer/guides-and-documentation
- group: company
  title: ''
  type: Blog
  url: https://digital.nhs.uk/blog
created: '2026-07-24'
description: 'NHS England (which absorbed NHS Digital in 2023) is the national body that runs England''s public health and social care API platform at digital.nhs.uk and api.service.nhs.uk. It publishes a large catalogue of internet-facing APIs - most of them HL7 FHIR R4 built to the FHIR UK Core profile - covering the national spine services: the Personal Demographics Service (PDS), GP Connect, the e-Referral Service (e-RS), the Electronic Prescription Service (EPS), the Organisation Data Service (ODS), Booking and Referral Standard (BaRS), immunisation history, the NHS App, NHS Notify, and the Directory of Healthcare Services. Access is governed centrally: applications onboard through the NHS API platform and authenticate with OAuth 2.0 bearer tokens - application-restricted (signed-JWT client credentials / API key) or user-restricted via NHS login (OIDC) and NHS CIS2 - with production access gated behind registration, assurance, and connection agreements. Home market is the United Kingdom
  (England). Positioning: a single national health system operating public, standards-based (FHIR UK Core) interoperability APIs rather than a commercial API vendor.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: nhs-england-mcp.yml
  slug: nhs-england-mcpyml
modified: '2026-07-24'
name: NHS England
nav: Providers
network: true
overview: 'NHS England publishes 7 APIs on the [APIs.io](https://apis.io/) network, including e-Referral Service (e-RS) - FHIR API, Booking and Referral Standard (BaRS) - FHIR API, Immunisation History - FHIR API, and 4 more. Tagged areas include Healthcare, United Kingdom, National Health System, FHIR, and HL7.


  The NHS England catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NHS England''s developer surface includes authentication, API reference, support, sandbox, documentation, getting-started guide, engineering blog, and 21 more developer resources.'
random_paper: 25
score:
  band: developing
  composite: 44.2
  delta: -1.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 54.7
    developer_ergonomics: 62.5
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nhs England Authentication
  slug: nhs-england-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nhs England Domain Security
  slug: nhs-england-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Nhs England Vulnerability Disclosure
  slug: nhs-england-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: nhs-england
tags:
- Healthcare
- United Kingdom
- National Health System
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- Health Data
- e-Prescribing
- EHR
website: https://digital.nhs.uk/
---
