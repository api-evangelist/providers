---
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
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Nhs England Agentic Access
  operation_count: 70
  slug: nhs-england-agentic-access
  summary_line: 70 operations · 32 acting
api_count: 7
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
- description: The Booking API from NHS England — 2 operation(s) for booking.
  name: NHS England Booking API
  slug: nhs-england-booking-api
- description: The Callbacks API from NHS England — 3 operation(s) for callbacks.
  name: NHS England Callbacks API
  slug: nhs-england-callbacks-api
- description: The Channels API from NHS England — 1 operation(s) for channels.
  name: NHS England Channels API
  slug: nhs-england-channels-api
- description: The CodeSystem API from NHS England — 1 operation(s) for codesystem.
  name: NHS England Code System API
  slug: nhs-england-codesystem-api
- description: The communication API from NHS England — 4 operation(s) for communication.
  name: NHS England Communication API
  slug: nhs-england-communication-api
- description: The Immunization API from NHS England — 1 operation(s) for immunization.
  name: NHS England Immunization API
  slug: nhs-england-immunization-api
- description: The List{id} API from NHS England — 1 operation(s) for list{id}.
  name: NHS England List{id} API
  slug: nhs-england-list-id-api
- description: The Message API from NHS England — 1 operation(s) for message.
  name: NHS England Message API
  slug: nhs-england-message-api
- description: The Message Batches API from NHS England — 1 operation(s) for message batches.
  name: NHS England Message Batches API
  slug: nhs-england-message-batches-api
- description: The Messages API from NHS England — 2 operation(s) for messages.
  name: NHS England Messages API
  slug: nhs-england-messages-api
- description: The Metadata API from NHS England — 2 operation(s) for metadata.
  name: NHS England Metadata API
  slug: nhs-england-metadata-api
- description: The Organisation API from NHS England — 1 operation(s) for organisation.
  name: NHS England Organisation API
  slug: nhs-england-organisation-api
- description: The Organization API from NHS England — 2 operation(s) for organization.
  name: NHS England Organization API
  slug: nhs-england-organization-api
- description: The OrganizationAffiliation API from NHS England — 2 operation(s) for organizationaffiliation.
  name: NHS England Organization Affiliation API
  slug: nhs-england-organizationaffiliation-api
- description: The R4 API from NHS England — 6 operation(s) for r4.
  name: NHS England R4 API
  slug: nhs-england-r4-api
- description: The Referral API from NHS England — 2 operation(s) for referral.
  name: NHS England Referral API
  slug: nhs-england-referral-api
- description: The Slots API from NHS England — 1 operation(s) for slots.
  name: NHS England Slots API
  slug: nhs-england-slots-api
- description: The STU3 API from NHS England — 32 operation(s) for stu3.
  name: NHS England STU3 API
  slug: nhs-england-stu3-api
- description: The ValueSet API from NHS England — 1 operation(s) for valueset.
  name: NHS England Value Set API
  slug: nhs-england-valueset-api
artifact_total: 28
asyncapis:
- description: ''
  name: Nhs England Webhooks
  slug: nhs-england-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nhs-england-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nhs-e-referral-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nhs-booking-and-referral-fhir-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nhs-immunisation-history-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nhs-organisation-data-service-fhir-r4-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nhs-app-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nhs-communications-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nhs-service-search-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/NHSDigital/e-referrals-service-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/NHSDigital/e-referrals-service-api/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/NHSDigital/e-referrals-service-api/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/NHSDigital/e-referrals-service-api/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/NHSDigital/e-referrals-service-api/blob/develop/CONTRIBUTING.md
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
  name: NHS England MCP Server
  slug: nhs-england-mcp-server
modified: '2026-07-24'
name: NHS England
nav: Providers
network: true
overview: 'NHS England publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Booking API, Callbacks API, Channels API, and 16 more. Tagged areas include Healthcare, United Kingdom, National Health System, FHIR, and HL7.


  The NHS England catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NHS England''s developer surface includes authentication, API reference, support, sandbox, documentation, getting-started guide, engineering blog, and 34 more developer resources.'
random_paper: 11
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 59.6
    developer_ergonomics: 66.1
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 44.7
  open_source:
    applies: true
    score: 100.0
  previous_composite: 55.5
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nhs-england/refs/heads/main/screenshots/nhs-england-2026-08-07T185240.png
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
