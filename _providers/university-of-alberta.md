---
access_model:
  confidence: high
  label: Free · No signup, no key issuance, no developer program
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.8
  scored_at: '2026-09-03'
api_count: 6
apis:
- description: The university's own SAML 2.0 identity provider metadata document, served from its own domain. It declares entityID https://login.ualberta.ca/saml2/idp/metadata.php, an IDPSSODescriptor with SingleSig
  name: University of Alberta SAML 2.0 Identity Provider Metadata
  slug: identity-federation
- description: 'ERA is the University of Alberta''s institutional repository. It was the library''s own Samvera/Hyrax application, Jupiter, at era.library.ualberta.ca; that host now redirects to ualberta.scholaris.ca, '
  name: ERA — Education and Research Archive (on Scholaris)
  slug: era-scholaris
- description: The University of Alberta's research data collection on Borealis, the Canadian Dataverse Repository operated by Scholars Portal / Ontario Council of University Libraries. The collection is scoped by t
  name: University of Alberta Research Data Collection on Borealis
  slug: borealis-research-data
- description: The library's discovery and catalogue layer is Ex Libris. The library publishes its own Z39.50 production server details on a ualberta.ca page — host ualberta.alma.exlibrisgroup.com, port 1921, databa
  name: University of Alberta Library Catalogue (Alma Z39.50 + Primo VE)
  slug: library-catalogue
- description: The University of Alberta Library is a registered DataCite repository — client id ualberta.library, symbol UALBERTA.LIBRARY, a member since 2020 — with 90,338 DOIs registered under that client as of 2
  name: University of Alberta Library DOI Registration (DataCite)
  slug: datacite-registration
- description: The University of Alberta Library's GitHub organization, ualbertalib, holds 138 public repositories and is actively maintained. Judged by what the code says about itself rather than by the host it sit
  name: University of Alberta Library Open Source (GitHub)
  slug: library-open-source
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.ualberta.ca/
- group: start
  title: Placeholder — no portal, no catalog, no key issuance
  type: DeveloperPortal
  url: https://api.ualberta.ca/
- group: other
  title: SAML 2.0 identity provider metadata (institution-operated)
  type: IdentityFederation
  url: https://login.ualberta.ca/saml2/idp/metadata.php
- group: other
  title: ERA on Scholaris (OCUL/Scholars Portal DSpace tenancy)
  type: ResearchRepository
  url: https://ualberta.scholaris.ca/
- group: other
  title: ''
  type: OpenData
  url: https://www.ualberta.ca/en/library/research-support/open-data/index.html
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.library.ualberta.ca/
- group: learn
  title: HTML only — no JSON or API surface
  type: CourseCatalog
  url: https://apps.ualberta.ca/catalogue
- group: other
  title: Framework for the Responsible Use of AI at the University of Alberta
  type: AIPolicy
  url: https://www.ualberta.ca/en/artificial-intelligence/artificial-intelligence-framework.html
- group: build
  title: ''
  type: AITooling
  url: https://www.ualberta.ca/en/artificial-intelligence/index.html
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-alberta-conformance.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ualbertalib
- group: docs
  title: ''
  type: Documentation
  url: https://www.ualberta.ca/en/information-services-and-technology/services/application-development/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ualberta.ca/en/policies-procedures/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ualberta.ca/en/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://www.ualberta.ca/en/the-quad/index.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-alberta/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-alberta-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-alberta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-alberta-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-alberta-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Probed 2026-08-30. The University of Alberta publishes exactly one machine-readable contract it also operates: its SAML 2.0 identity provider metadata at login.ualberta.ca, which returns 200 application/samlmetadata+xml. There is no institution-operated REST API. api.ualberta.ca returns 200 but the body is a placeholder saying the university is still working out how data is cataloged, shared and governed, and offers only an email address; data.ualberta.ca serves the same byte-identical page. Every other apparent surface is a tenancy: ERA on Scholaris (OCUL DSpace), the research data collection on Borealis (Canadian Dataverse, a host five other institutions in this cohort also claim), the Alma Z39.50 server and Primo VE discovery layer from Ex Libris, and DOI registration through DataCite. The course catalogue is HTML only — apps.ualberta.ca returns 404 for /api and 410 for every .json path tried, so the third-party UAlberta course APIs in the wild are scrapers. The library''s
    Open Journal Systems installation is gone: journals.library.ualberta.ca now 302s to a library publishing page, so there is no Crossref depositing surface either. Twenty files were removed from this repository in this pass — two Borealis-derived OpenAPI documents, the pristine original and its refine report, and the sixteen collections, schemas, structures, examples, rulesets, vocabulary, JSON-LD context, authentication and agentic-access artifacts derived from them. They described the Dataverse software''s contract, not the university''s.'
  evidence:
  - status: 200
    url: https://login.ualberta.ca/saml2/idp/metadata.php
  - status: 200
    url: https://api.ualberta.ca/
  - status: 200
    url: https://data.ualberta.ca/
  - status: 200
    url: https://ualberta.scholaris.ca/server/api
  - status: 200
    url: https://ualberta.scholaris.ca/server/oai/request?verb=Identify
  - status: 200
    url: https://era.library.ualberta.ca/oai?verb=Identify
  - status: 200
    url: https://borealisdata.ca/oai?verb=Identify
  - status: 200
    url: https://borealisdata.ca/dataverse/ualberta
  - status: 200
    url: https://www.ualberta.ca/en/library/research-support/open-data/z3950.html
  - status: 200
    url: https://api.datacite.org/repositories?query=alberta
  - status: 200
    url: https://apps.ualberta.ca/catalogue
  - status: 404
    url: https://apps.ualberta.ca/api
  - status: 410
    url: https://apps.ualberta.ca/catalogue/course/cmput.json
  - status: 302
    url: https://journals.library.ualberta.ca/index.php/index/oai?verb=Identify
  - status: 200
    url: https://library.ualberta.ca/peel/api
  - status: 404
    url: https://login.ualberta.ca/idp/shibboleth
  reason: tenant_only
  state: none
created: '2026-06-03'
description: 'The University of Alberta is a public research university in Edmonton, Alberta, Canada, and a member of the U15 Group of Canadian Research Universities. It operates no public API product. Its central developer site, api.ualberta.ca, is a live placeholder that says only that the university "is currently working to improve the way data is cataloged, shared, and governed" and gives an email address; there is no portal, no key issuance and no catalog behind it. The one machine-readable contract the institution itself publishes and runs is its SAML 2.0 identity provider metadata at login.ualberta.ca, which is institution-operated by definition and is the only surface in this profile whose operator is the university. Everything else that looks like a University of Alberta API is a tenancy on someone else''s platform: ERA, the institutional repository, migrated off the library''s own Jupiter application at era.library.ualberta.ca onto Scholaris, the OCUL/Scholars Portal national DSpace
  service, and now answers as ualberta.scholaris.ca with a DSpace REST API and an OAI-PMH endpoint; research data lives in the university''s collection on Borealis, the Canadian Dataverse Repository run by the same consortium; the library catalogue is Ex Libris Alma and Primo VE, whose Z39.50 server the library documents in its own words; and its 90,338 DOIs are registered through DataCite. The course catalogue and Bear Tracks are HTML only — every JSON path probed on apps.ualberta.ca returns 404 or 410, which is why the third-party UAlberta course APIs that exist are HTML scrapers. The university''s real engineering output is open source rather than hosted: the University of Alberta Library GitHub organization is active and substantial, and includes its own OAI-PMH implementation and DSpace and DataCite client tooling.'
finops:
- name: University Of Alberta Finops
  service_category: Education
  slug: university-of-alberta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-alberta.png
layout: provider
modified: '2026-08-30'
name: University of Alberta
nav: Providers
network: true
overview: 'University of Alberta publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Canada, and U15 Group of Canadian Research Universities.


  University of Alberta''s developer surface includes documentation, engineering blog, and 19 more developer resources.'
plans:
- name: University Of Alberta Plans Pricing
  plan_count: 2
  slug: university-of-alberta-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of Alberta Rate Limits
  slug: university-of-alberta-rate-limits
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 4.4
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 29.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: University Of Alberta Domain Security
  slug: university-of-alberta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-alberta
tags:
- Education
- Higher Education
- University
- Canada
- U15 Group of Canadian Research Universities
- Research Data
- Research Repository
- Library
- Identity Federation
- OAI-PMH
website: https://www.ualberta.ca/
---
