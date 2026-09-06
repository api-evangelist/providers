---
access_model:
  confidence: high
  label: Government · Gated onboarding (registration + NASH PKI)
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.5
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: The business-to-business FHIR Gateway for connecting conformant clinical software to the My Health Record national shared health record. Exposes FHIR-based read and upload interactions for clinical do
  name: My Health Record FHIR Gateway (B2B)
  slug: my-health-record-fhir-gateway
- description: The FHIR Mobile Gateway lets mobile and consumer applications connect to the My Health Record system to retrieve documents and health information on behalf of individuals. Registration and a developer
  name: My Health Record FHIR Mobile Gateway
  slug: my-health-record-fhir-mobile-gateway
- description: The National Clinical Terminology Service (NCTS) FHIR terminology server, operated by ADHA on CSIRO Ontoserver. A FHIR R4 (4.0.1) terminology service supporting CodeSystem, ValueSet, ConceptMap, Opera
  name: NCTS FHIR Terminology Server
  slug: ncts-fhir-terminology-server
- description: 'The NCTS National Syndication Server, an Atom Publishing Protocol profile for interrogating terminology content feeds and downloading FHIR terminology resource bundles (SNOMED CT-AU, AMT, LOINC, RCPA '
  name: NCTS National Syndication Server
  slug: ncts-syndication-server
- description: ADHA's electronic prescribing service and conformance profiles enabling electronic prescriptions, dispensing and the Active Script List across prescribing and dispensing software. Conformant integrati
  name: Electronic Prescribing
  slug: electronic-prescribing
- description: The national Healthcare Identifiers Service, providing unique identifiers for individuals (IHI), healthcare providers (HPI-I) and organisations (HPI-O) that underpin My Health Record, electronic presc
  name: Healthcare Identifiers (HI) Service
  slug: healthcare-identifiers-service
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/australian-digital-health-agency-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitalhealth.gov.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.digitalhealth.gov.au/
- group: start
  title: ''
  type: Portal
  url: https://implementer.digitalhealth.gov.au/
- group: docs
  title: ''
  type: Documentation
  url: https://implementer.digitalhealth.gov.au/resources
- group: docs
  title: ''
  type: APIReference
  url: https://implementer.digitalhealth.gov.au/fhir-resources
- group: start
  title: ''
  type: GettingStarted
  url: https://implementer.digitalhealth.gov.au/resources/guides
- group: auth
  title: ''
  type: Authentication
  url: https://implementer.digitalhealth.gov.au/resources/services/national-authentication-service-for-health-nash
- group: operate
  title: ''
  type: Support
  url: mailto:help@digitalhealth.gov.au
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AuDigitalHealth
- group: build
  title: ''
  type: Packages
  url: packages/australian-digital-health-agency-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/australian-digital-health-agency-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/australian-digital-health-agency-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/australian-digital-health-agency-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/australian-digital-health-agency-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/australian-digital-health-agency-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/australian-digital-health-agency-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/australian-digital-health-agency-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/australian-digital-health-agency-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/australian-digital-health-agency-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/australian-digital-health-agency-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/australian-digital-health-agency-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/australian-digital-health-agency-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: The Australian Digital Health Agency (ADHA) is the Australian Government statutory agency responsible for national digital health infrastructure and standards. It operates and stewards My Health Record (the national shared health record), the Healthcare Identifiers (HI) Service, the National Authentication Service for Health (NASH) PKI, electronic prescribing, and the National Clinical Terminology Service (NCTS). ADHA publishes machine-readable APIs for connecting conformant clinical software to these national systems, centred on HL7 FHIR (R4) alongside legacy HL7 CDA document exchange. Its developer surface spans the My Health Record FHIR Gateway (B2B and Mobile), the NCTS FHIR terminology server and Atom syndication feed (SNOMED CT-AU, AMT, LOINC), and conformance profiles for electronic prescribing. Home market is Australia. Authentication to the national record systems uses NASH SHA-2 PKI certificates (mutual TLS), while the NCTS terminology server uses SMART-on-FHIR OAuth2.
  Production onboarding is gated behind registration, conformance testing, and PKI issuance; ADHA aligns to the AU Base / AU Core FHIR implementation guides stewarded through HL7 Australia and the Sparked national FHIR accelerator.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Australian Digital Health Agency
nav: Providers
network: true
overview: 'Australian Digital Health Agency publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Australia, National Health System, FHIR, and HL7.


  Australian Digital Health Agency''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, support, and 18 more developer resources.'
random_paper: 14
scopes:
- name: Australian Digital Health Agency Scopes
  scope_count: 2
  slug: australian-digital-health-agency-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 34.4
    developer_ergonomics: 47.0
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 33.9
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Australian Digital Health Agency Authentication
  slug: australian-digital-health-agency-authentication
  summary_line: mutualTLS/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Australian Digital Health Agency Domain Security
  slug: australian-digital-health-agency-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: australian-digital-health-agency
tags:
- Healthcare
- Australia
- National Health System
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- Electronic Health Record
- e-Prescribing
- Terminology
- Government
website: https://www.digitalhealth.gov.au/
---
