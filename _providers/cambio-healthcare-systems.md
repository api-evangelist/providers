---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-09-05'
api_count: 19
apis:
- baseURL: https://api.openservices.cambio.se/api/open/attentionsignals
  baseurl_source: declared
  description: 'Intended Use: The intended use of this API is to retrieve attention signals for a given patient. Attention signals can be information about allergies, contagious infections and more that is relevant w'
  name: Attention signal
  slug: cambio-healthcare-systems-attention-signal
- baseURL: https://api.openservices.cambio.se/auth/realms/COS
  baseurl_source: declared
  description: OpenId Connect API for Authorizer. This is needed in between the developer portal and Keycloak since it seems the dev portals HTTP client can't speak properly directly with Keycloak for some reason. P
  name: Authorizer - OpenId Connect
  slug: cambio-healthcare-systems-authorizer-openid-connect
- baseURL: https://api.openservices.cambio.se/api/open/appointments
  baseurl_source: declared
  description: 'Intended Use: Booked appointments of all types for a patient. The intended use for reading data with this API is in first hand that the API is applied for direct access and should not be used to trans'
  name: Booked appointments
  slug: cambio-healthcare-systems-booked-appointments
- baseURL: https://api.openservices.cambio.se/api/open/contacts
  baseurl_source: declared
  description: 'Note: Deprecated All types of care contacts. Part of Cambio Open Services (COS), the business-to-business open API programme that lets third-party applications read and write data in the Cambio COSMIC'
  name: Care contacts
  slug: cambio-healthcare-systems-care-contacts
- baseURL: https://api.openservices.cambio.se/api/open/contacts
  baseurl_source: declared
  description: 'Intended Use: The Care Contacts API is intended to be used for fetching all care contacts for a given patient within a certain time frame. The intended use for reading data with this API is in first h'
  name: Care contacts (v2)
  slug: cambio-healthcare-systems-care-contacts-v2
- baseURL: https://api.openservices.cambio.se/api/open/chemistrylabreports
  baseurl_source: declared
  description: DEPRECATED All existing chemistry lab results for a given patient. Part of Cambio Open Services (COS), the business-to-business open API programme that lets third-party applications read and write dat
  name: Chemistry lab results (deprecated)
  slug: cambio-healthcare-systems-chemistry-lab-results
- baseURL: https://api.openservices.cambio.se/api/open/chemistrylabreports
  baseurl_source: declared
  description: 'Intended Use: The intended use of this API is to retrieve chemistry lab results for a given patient. The result may be filtered using a specific time interval. The intended use for reading data with t'
  name: Chemistry lab results (v2)
  slug: cambio-healthcare-systems-chemistry-lab-results-v2
- baseURL: https://api.openservices.cambio.se/api/open/diagnosis
  baseurl_source: declared
  description: 'Diagnosis API in Cambio Open Services (COS), the B2B open API programme for the Cambio COSMIC electronic health record. Part of Cambio Open Services (COS), the business-to-business open API programme '
  name: Diagnosis (deprecated)
  slug: cambio-healthcare-systems-diagnosis
- baseURL: https://api.openservices.cambio.se/api/open/diagnosis
  baseurl_source: declared
  description: 'Intended Use: The Diagnosis API is intended to be used for fetching all diagnoses for a specific patient within a specified time frame. The intended use for reading data with this API is in first hand'
  name: Diagnosis (v2)
  slug: cambio-healthcare-systems-diagnosis-v2
- baseURL: https://api.openservices.cambio.se/api/open/fhir
  baseurl_source: declared
  description: 'The Cambio FHIR R4 Public Profiles are available at Simplifier. Please look in the implementation guide for available resources: https://fhir.openservices.cambio.se/site/index.html Part of Cambio Open'
  name: FHIR R4 Public Profiles
  slug: cambio-healthcare-systems-fhir-r4-public-profiles
- baseURL: https://api.openservices.cambio.se/api/open/journalnotes
  baseurl_source: declared
  description: Journal notes API in Cambio Open Services (COS), the B2B open API programme for the Cambio COSMIC electronic health record. Part of Cambio Open Services (COS), the business-to-business open API progra
  name: Journal notes (deprecated)
  slug: cambio-healthcare-systems-journal-notes
- baseURL: https://api.openservices.cambio.se/api/open/journalnotes
  baseurl_source: declared
  description: 'Intended Use: The Journal Note API is intended to be used for fetching all journal notes for a given patient within a specified time interval. The intended use for reading data with this API is in fir'
  name: Journal notes (v2)
  slug: cambio-healthcare-systems-journal-notes-v2
- baseURL: https://api.openservices.cambio.se/open/api/medications
  baseurl_source: declared
  description: Medication prescriptions API in Cambio Open Services (COS), the B2B open API programme for the Cambio COSMIC electronic health record. Part of Cambio Open Services (COS), the business-to-business open
  name: Medication prescriptions (deprecated)
  slug: cambio-healthcare-systems-medication-prescriptions
- baseURL: https://api.openservices.cambio.se/api/open/medications
  baseurl_source: declared
  description: 'Intended use: The intended use of this API is to retrieve all prescriptions for the given patient. The result can be filtered by using a time interval. The intended use for reading data with this API '
  name: Medication prescriptions (v2)
  slug: cambio-healthcare-systems-medication-prescriptions-v2
- baseURL: https://api.openservices.cambio.se/api/open/patient
  baseurl_source: declared
  description: Demographic patient information about a given patient. Part of Cambio Open Services (COS), the business-to-business open API programme that lets third-party applications read and write data in the Cam
  name: Patient information (deprecated)
  slug: cambio-healthcare-systems-patient-information
- baseURL: https://api.openservices.cambio.se/api/open/patient
  baseurl_source: declared
  description: 'Intended Use: The intended use for reading data with this API is in first hand that the API is applied for direct access and should not be used to transfer data between caregivers. If it should be use'
  name: Patient information (v2)
  slug: cambio-healthcare-systems-patient-information-v2
- baseURL: https://api.openservices.cambio.se/api/open/paymentnotice
  baseurl_source: declared
  description: 'Intended Use: The intended use of this API is to register the payment for a given appointment for the given patient. Specific Rules and Limitations: Rule: The only status that can be set is PAID. One '
  name: Payment notice
  slug: cambio-healthcare-systems-payment-notice
- baseURL: https://api.openservices.cambio.se/api/open/referrals
  baseurl_source: declared
  description: Referral requests API in Cambio Open Services (COS), the B2B open API programme for the Cambio COSMIC electronic health record. Part of Cambio Open Services (COS), the business-to-business open API pr
  name: Referral requests
  slug: cambio-healthcare-systems-referral-requests
- baseURL: https://api.openservices.cambio.se/open/api/videomeetings
  baseurl_source: declared
  description: 'Note: Deprecated - Will be removed in COSMIC 4.1.0 Booked appointments supporting remote participation through video. Part of Cambio Open Services (COS), the business-to-business open API programme th'
  name: Video meetings
  slug: cambio-healthcare-systems-video-meetings
- description: HL7 FHIR R4 (4.0.1) server exposing Cambio COSMIC clinical data through 24 FHIR resource types — Patient, Practitioner, Organization, Encounter, Condition, Observation, MedicationRequest, MedicationDi
  name: Cambio Open Services FHIR R4 API
  slug: cambio-healthcare-systems-fhir-r4
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cambio-healthcare-systems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cambio-healthcare-systems-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cambiogroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.openservices.cambio.se/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.openservices.cambio.se/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.openservices.cambio.se/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.openservices.cambio.se/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.openservices.cambio.se/signup
- group: start
  title: ''
  type: Login
  url: https://developer.openservices.cambio.se/signin
- group: operate
  title: ''
  type: Support
  url: https://developer.openservices.cambio.se/help
- group: company
  title: ''
  type: Blog
  url: https://www.cambiogroup.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cambiogroup.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cambiogroup.com/about-us/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CambioHealthcare
- group: auth
  title: ''
  type: Compliance
  url: https://www.cambiogroup.com/compliance-eng/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.openservices.cambio.se/api-changelog
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cambio-healthcare-systems-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cambio-healthcare-systems-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://api.openservices.cambio.se/auth/realms/COS/.well-known/openid-configuration
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cambio-healthcare-systems-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cambio-healthcare-systems-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cambio-healthcare-systems-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cambio-healthcare-systems-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cambio-healthcare-systems-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cambio-healthcare-systems-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cambio-healthcare-systems-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cambio-healthcare-systems-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cambio-healthcare-systems-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/cambio-healthcare-systems-examples.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cambio-healthcare-systems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cambio-healthcare-systems-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cambio-healthcare-systems-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cambio-healthcare-systems-changelog.yml
- group: other
  title: ''
  type: CapabilityStatement
  url: fhir/cambio-healthcare-systems-fhir.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/CambioHealthcare/cp-nordic-hackathon-2025
created: '2026-09-02'
description: Cambio Healthcare Systems is a Swedish health-IT company founded in 1993 in Linkoping and headquartered in Stockholm, best known for Cambio COSMIC, an electronic health record and clinical decision support platform used across Swedish regions, Denmark and the United Kingdom by well over 100,000 clinical users. Cambio runs a public developer programme, Cambio Open Services (COS), which publishes 19 REST APIs and an HL7 FHIR R4 server on Azure API Management at api.openservices.cambio.se, together with a published FHIR Implementation Guide of COSMIC-specific profiles, a Keycloak OpenID Connect authorization server with SMART-on-FHIR style scopes, and a synthetic-data sandbox. COSMIC and its clinical decision support are CE-marked and MDR-certified (notified body BSI-2797), and the company holds ISO 9001, 13485, 14001, 20000 and 27001 certifications.
image: https://www.cambiogroup.com/wp-content/uploads/2021/03/cropped-Cambio-C-560x560px-270x270.png
layout: provider
modified: '2026-09-02'
name: Cambio Healthcare Systems
nav: Providers
network: true
overview: 'Cambio Healthcare Systems publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Attention signal, Authorizer - OpenId Connect, Booked appointments, and 16 more. Tagged areas include Healthcare, Electronic Health Records, EHR, Clinical Decision Support, and FHIR.


  Cambio Healthcare Systems'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 29 more developer resources.'
plans:
- name: Cambio Healthcare Systems Plans Pricing
  plan_count: 0
  slug: cambio-healthcare-systems-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Cambio Healthcare Systems Rate Limits
  slug: cambio-healthcare-systems-rate-limits
scopes:
- name: Cambio Healthcare Systems Scopes
  scope_count: 0
  slug: cambio-healthcare-systems-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 59.1
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 55.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 67.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Cambio Healthcare Systems Authentication
  slug: cambio-healthcare-systems-authentication
  summary_line: apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Cambio Healthcare Systems Domain Security
  slug: cambio-healthcare-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cambio-healthcare-systems
tags:
- Healthcare
- Electronic Health Records
- EHR
- Clinical Decision Support
- FHIR
- HL7
- Interoperability
- Health IT
- Sweden
- Nordics
- Patient Data
- Medical Records
- openEHR
- SMART on FHIR
- Company
website: https://www.cambiogroup.com/
---
