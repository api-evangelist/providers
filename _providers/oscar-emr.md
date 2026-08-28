---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: OSCAR's REST web-services layer, served under the /ws/services base path of a deployed OSCAR instance, covering most of the clinical record - scheduling/appointments, demographics, billing, prescripti
  name: OSCAR REST Web Services API
  slug: oscar-rest-web-services-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oscar-emr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oscar-emr.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://oscaremr.atlassian.net/wiki/spaces/OS/overview
- group: docs
  title: ''
  type: Documentation
  url: https://oscaremr.atlassian.net/wiki/spaces/OS/overview
- group: docs
  title: ''
  type: APIReference
  url: https://oscaremr.atlassian.net/wiki/spaces/OS/pages/85396074/Documenting+the+REST+API
- group: start
  title: ''
  type: GettingStarted
  url: https://oscaremr.atlassian.net/wiki/spaces/OS/pages/79855638/Connecting+to+OSCAR's+REST+API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scoophealth
- group: build
  title: ''
  type: SourceCode
  url: https://bitbucket.org/oscaremr/oscar/src/stable/
- group: other
  title: ''
  type: Marketplace
  url: https://apps.health/
- group: start
  title: ''
  type: SignUp
  url: https://share.hsforms.com/1p6l4kFOyRh6_7RfxVHpYTQcgcz4
- group: operate
  title: ''
  type: Support
  url: mailto:help@oscarprodesk.ca
- group: commercial
  title: ''
  type: Pricing
  url: https://get.oscarpro.ca/
- group: auth
  title: ''
  type: Authentication
  url: authentication/oscar-emr-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oscar-emr-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oscar-emr-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oscar-emr-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oscar-emr-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oscar-emr-llms.txt
created: '2026-07-24'
description: OSCAR EMR is an open-source electronic medical record (EMR) system created by Dr. David Chan and McMaster University's Department of Family Medicine, and one of Canada's most widely deployed primary-care EMRs. The core software is distributed under the GPL v2+ license (mirrored on GitHub as scoophealth/oscar and on Bitbucket), while the commercially supported OSCAR Pro distribution is delivered by the WELL EMR Group (a WELL Health company) to more than 2,000 clinics and 10,000 providers across Canada. OSCAR exposes a documented REST web-services API under the /ws/services path (scheduling, demographics, billing, prescriptions, documents, labs, ticklers, eForms and providers), secured with 3-legged OAuth 1.0a via /ws/oauth. Clinical data flows historically use HL7 v2 messaging, and OSCAR ships an internal HL7 FHIR integration used for Ontario public-health and immunization reporting (BORN, DHIR). Third-party integrations for OSCAR Pro are partner-gated through the apps.health
  marketplace. As self-hosted software there is no single public API host or hosted FHIR CapabilityStatement; the API surface is documented on the OSCAR EMR developer wiki and realized per clinic deployment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: OSCAR EMR
nav: Providers
network: true
overview: 'OSCAR EMR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Canada, EHR, EMR, and Primary Care.


  OSCAR EMR''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, pricing, authentication, and 11 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 27.9
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 27.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oscar-emr/refs/heads/main/screenshots/oscar-emr-2026-08-07T191006.png
security:
- kind: authentication
  name: Oscar Emr Authentication
  slug: oscar-emr-authentication
  summary_line: oauth1a/oauth2 · 2 schemes
- kind: domain-security
  name: Oscar Emr Domain Security
  slug: oscar-emr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oscar-emr
tags:
- Healthcare
- Canada
- EHR
- EMR
- Primary Care
- Open-Source
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- Authentication
website: https://oscar-emr.com/
---
