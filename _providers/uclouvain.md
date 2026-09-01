---
access_model:
  confidence: high
  label: Free and keyless - no developer portal, no API keys; gated services use SAML federation
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Orthanc is a free and open-source, vendor-neutral DICOM server and medical-imaging ecosystem. UCLouvain describes itself as "the innovation engine behind Orthanc": the project is led by its author Seb'
  name: Orthanc API
  slug: orthanc-api
- description: 'Open Data @ UCLouvain is the institution''s research-data repository, running Dataverse 6.8 on UCLouvain infrastructure at dataverse.uclouvain.be and minting DOIs under UCLouvain''s own Crossref prefix '
  name: Open Data @ UCLouvain -- Dataverse deployment (Native + Search API)
  slug: dataverse-native-api
- description: OAI-PMH 2.0 metadata-harvesting endpoint for the UCLouvain research-data repository. Identify returns repositoryName "Open Data @ UCLouvain Dataverse OAI Archive", adminEmail cism-support@uclouvain.be
  name: Open Data @ UCLouvain Dataverse OAI-PMH
  slug: dataverse-oai
- description: DIAL.pr, branded BOREAL, is UCLouvain's institutional repository for the research publications of its professors and staff. It runs DSpace-CRIS 8.1 (cris-2025.01.00) on the UCLouvain host research.dia
  name: DIAL.pr (BOREAL) -- DSpace-CRIS REST API
  slug: dial-pr-rest
- description: 'OAI-PMH 2.0 harvesting endpoint for DIAL.pr, UCLouvain''s research-publications repository. Identify returns repositoryName "Dial.pr", adminEmail bibsys@uclouvain.be, earliestDatestamp 2026-04-07 (the '
  name: DIAL.pr OAI-PMH
  slug: dial-pr-oai
- description: DIAL.mem is UCLouvain's institutional repository for master's theses, part of the DIAL (Digital Access to Libraries) family. It runs the same DSpace-CRIS 8.1 stack as DIAL.pr, on the UCLouvain host th
  name: DIAL.mem -- DSpace-CRIS REST API
  slug: dial-mem-rest
- description: OAI-PMH 2.0 harvesting endpoint for DIAL.mem, UCLouvain's master's-thesis repository. Identify returns repositoryName "Dial.mem", adminEmail bibsys@uclouvain.be, earliestDatestamp 2025-05-14. Institut
  name: DIAL.mem OAI-PMH
  slug: dial-mem-oai
- description: OER-UCLouvain is the institution's open educational resources repository, running DSpace JSPUI on oer.uclouvain.be (CNAME dspace.sipr.ucl.ac.be, UCLouvain's own SIPR infrastructure). Its OAI-PMH 2.0 e
  name: OER-UCLouvain OAI-PMH
  slug: oer-oai
- description: UCLouvain runs its own Shibboleth identity provider and publishes signed SAML 2.0 entity metadata at a stable, unauthenticated URL. entityID https://idp.uclouvain.be/idp/shibboleth, shibmd:Scope uclou
  name: UCLouvain Shibboleth Identity Provider -- SAML 2.0 metadata
  slug: identity-federation
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://uclouvain.be/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uclouvain
- group: company
  title: ''
  type: LinkedIn
  url: https://be.linkedin.com/school/uclouvain/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uclouvain.be/en/privacy
- group: other
  title: ''
  type: OpenData
  url: https://dataverse.uclouvain.be/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research.dial.uclouvain.be/home
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.uclouvain.be/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://uclouvain.be/en/cism/cism-platform
- group: learn
  title: ''
  type: CourseCatalog
  url: https://uclouvain.be/en/study-programme
- group: other
  title: ''
  type: AIPolicy
  url: https://uclouvain.be/en/ai/documents
- group: build
  title: ''
  type: AITooling
  url: https://uclouvain.be/en/ai
- group: docs
  title: ''
  type: Documentation
  url: https://orthanc.uclouvain.be/book/
- group: docs
  title: ''
  type: APIReference
  url: https://orthanc.uclouvain.be/api/index.html
- group: design
  title: ''
  type: Conformance
  url: conformance/uclouvain-education-standards.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uclouvain-identity-federation.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uclouvain-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uclouvain-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uclouvain-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uclouvain-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uclouvain-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'UCLouvain (Universite catholique de Louvain) is Belgium''s largest French-speaking university -- a private institution subsidised by public authorities, Catholic in identity, based in Louvain-la-Neuve with campuses in Brussels, Mons, Tournai, Charleroi and Namur, and ranked #203 in the QS World University Rankings 2025. Its programmable footprint is small, real, and mostly NOT its own engineering. UCLouvain operates no public developer portal, issues no API keys, and api.uclouvain.be answers 503 with no backend behind it. What it does operate, verified live on 2026-08-30: the Orthanc medical-imaging ecosystem -- a genuinely UCLouvain-authored open-source project run out of ICTEAM''s Health Informatics Lab, publishing a 239-path OpenAPI 3.0 contract and a public demo server; four OAI-PMH 2.0 repositories (Dataverse open data, DIAL.pr research publications, DIAL.mem master''s theses, OER-UCLouvain open educational resources); a SAML 2.0 / Shibboleth identity provider registered
  with the Belnet federation and exported to eduGAIN; and Crossref membership in its own right, minting DOIs under prefix 10.14428. Everything else that looks like a UCLouvain API is a product''s contract running on a UCLouvain host: the Dataverse 6.8 Native API and the DSpace-CRIS 8.1 REST API behind DIAL are recorded here as tenant deployments, not as UCLouvain''s contracts. An earlier profile of this repository credited UCLouvain with 36 OpenAPI definitions that were in fact one Dataverse product spec split by tag -- a contract eight institutions in this catalog ship identically. Those have been removed.'
examples:
- key_count: 7
  name: Uclouvain Orthanc System Example
  slug: uclouvain-orthanc-system-example
finops:
- name: Uclouvain Finops
  service_category: Education
  slug: uclouvain-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uclouvain.png
layout: provider
modified: '2026-08-30'
name: UCLouvain
nav: Providers
network: true
overview: 'UCLouvain publishes 1 API on the [APIs.io](https://apis.io/) network: Orthanc API. Tagged areas include University, Higher Education, Education, Belgium, and Private Research University.


  UCLouvain''s developer surface includes documentation, API reference, authentication, and 18 more developer resources.'
plans:
- name: Uclouvain Plans Pricing
  plan_count: 2
  slug: uclouvain-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Uclouvain Rate Limits
  slug: uclouvain-rate-limits
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 46.3
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uclouvain/refs/heads/main/screenshots/uclouvain-2026-06-20T195945.png
security:
- kind: domain-security
  name: Uclouvain Domain Security
  slug: uclouvain-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Uclouvain Vulnerability Disclosure
  slug: uclouvain-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: uclouvain
tags:
- University
- Higher Education
- Education
- Belgium
- Private Research University
- Open Data
- Research Data
- Open Science
- Institutional Repository
- OAI-PMH
- Identity Federation
- Open-Source
- Medical Imaging
- Library
website: https://uclouvain.be/en
---
