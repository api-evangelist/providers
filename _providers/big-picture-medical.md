---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.bigpicturemedical.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigpicturemedical.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bigpicturemedical.com/terms-of-service/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/big-picture-medical
- group: commercial
  title: ''
  type: Pricing
  url: https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/544327769943197
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bigpicturemedical.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/big-picture-medical-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/big-picture-medical-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/big-picture-medical-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/big-picture-medical-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/big-picture-medical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/big-picture-medical-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/big-picture-medical-packages.yml
- group: design
  title: ''
  type: Components
  url: components/big-picture-medical-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/big-picture-medical-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Big Picture Medical's own G-Cloud 14 listing says the BPM Platform exposes REST APIs and ships API documentation in PDF, but that PDF is only handed to contracted customers — docs.bigpicturemedical.com is a Google Workspace Drive alias that redirects to a bigpicturemedical.com account sign-in, and api.bigpicturemedical.com resolves to an IBM Cloud address that refuses connections on 80, 443, 8080 and 8443.
  evidence:
  - status: 200
    url: https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/544327769943197
  - status: 200
    url: http://docs.bigpicturemedical.com/
  - status: 0
    url: https://api.bigpicturemedical.com/
  - status: 404
    url: https://www.bigpicturemedical.com/developers
  - status: 404
    url: https://www.bigpicturemedical.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-09-02'
description: 'Big Picture Medical Limited is a London-based health technology company building what it calls a semantic execution layer for healthcare — a low-code platform, founded by emergency physician Dr Tom McKinnon and developed over roughly a decade inside live NHS services, that harmonises clinical data from different systems into openEHR-coded concepts, holds it with visible lineage and provenance, and turns recommendations from algorithms, agents and clinicians into governed, auditable actions in the systems a trust already runs. The product is assembled from four component types the company calls Blocks — UX, Mapping, Data and Orchestration — sold as two solutions: Care Workflow, for protocolised care pathways such as single points of access, virtual wards and chronic monitoring, and Data Workflow, a next-generation interoperability engine that connects data silos across openEHR, FHIR, HL7 and proprietary formats. It is live in the NHS at ICB level, integrates with EMIS and SystmOne,
  and connects to the NHS Network. Big Picture Medical publishes no public API contract, developer portal or SDK; its own G-Cloud 14 listing confirms a platform REST API exists and that its documentation is supplied to customers as a PDF.'
image: https://www.bigpicturemedical.com/favicon.ico
layout: provider
modified: '2026-09-02'
name: Big Picture Medical
nav: Providers
network: true
overview: 'Big Picture Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Care, Electronic Health Records, and openEHR.


  Big Picture Medical''s developer surface includes pricing and 14 more developer resources.'
plans:
- name: Big Picture Medical Plans Pricing
  plan_count: 1
  slug: big-picture-medical-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Big Picture Medical Rate Limits
  slug: big-picture-medical-rate-limits
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 24.7
  provenance:
    conformance: first-party
    mcp: derived
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
    score: 40.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Big Picture Medical Authentication
  slug: big-picture-medical-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Big Picture Medical Domain Security
  slug: big-picture-medical-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Big Picture Medical Trust Center
  slug: big-picture-medical-trust-center
  summary_line: ISO/IEC 27001:2022, Cyber Essentials, HIPAA, GDPR, WCAG 2.1 AA
slug: big-picture-medical
tags:
- Company
- Healthcare
- Health Care
- Electronic Health Records
- openEHR
- FHIR
- HL7
- Interoperability
- Clinical Data
- Care Pathways
- Workflow
- Orchestration
- No Code
- NHS
- United Kingdom
website: https://www.bigpicturemedical.com/
---
