---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: OAI-PMH 2.0 metadata-harvesting provider for IRIS, Sapienza's institutional research information system and repository, served from the university's own host iris.uniroma1.it. Verified live 2026-09-01
  name: IRIS Research Catalogue OAI-PMH
  slug: iris-oai-pmh
- description: Site-wide OAI-PMH 2.0 provider over Riviste Online SApienza, the university's open-access journal publishing platform, hosted on its own domain at rosa.uniroma1.it. Verified live 2026-09-01 — the inde
  name: Riviste Online SApienza (R.O.SA) OAI-PMH
  slug: rosa-oai-pmh
- description: Institution-operated Shibboleth SAML 2.0 identity provider, published as machine-readable metadata both directly on the institution's own host and in the IDEM GARR AAI federation aggregate. Verified l
  name: Sapienza Shibboleth Identity Provider (IDEM GARR AAI)
  slug: identity-federation
- description: Open-data and linked-data publishing project of the Sistema Bibliotecario Sapienza, on the institution's own host sbs.uniroma1.it, documenting library and digital-resource datasets under CC BY 4.0 aga
  name: Sapienza Library System Open Data & Linked Data (dormant)
  slug: library-open-data
- description: 'Sapienza is a registered DataCite member and DOI registrant — a fact about the institution, not a contract it operates. Verified live 2026-09-01 against the DataCite REST API: https://api.datacite.org'
  name: DataCite DOI registration (provider ROMAUNO / repository CRUI.UNIROMA1)
  slug: datacite-registration
- description: 'Sapienza is a Crossref member and DOI depositor. Verified live 2026-09-01 — https://api.crossref.org/members/13551 returns 200 with primary-name "Sapienza University of Rome", location "Rome, Italy", '
  name: Crossref membership (member 13551, prefix 10.53131)
  slug: crossref-membership
- description: Sapienza is registered in the Research Organization Registry with ROR ID https://ror.org/02be6w209, names "Sapienza University of Rome" / "Sapienza – Università di Roma", and website https://www.uniro
  name: ROR organization identifier 02be6w209
  slug: ror-registration
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.uniroma1.it/en
- group: other
  title: ''
  type: ResearchRepository
  url: https://iris.uniroma1.it/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.uniroma1.it/idp/shibboleth
- group: other
  title: ''
  type: OpenData
  url: https://sbs.uniroma1.it/data/opendata/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://opac.uniroma1.it/SebinaOpacRMS/.do?sysb=univ
- group: learn
  title: ''
  type: CourseCatalog
  url: https://corsidilaurea.uniroma1.it
- group: docs
  title: ''
  type: Documentation
  url: https://www.uniroma1.it/en/pagina/iris-support
- group: design
  title: ''
  type: Conformance
  url: conformance/sapienza-university-of-rome-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sapienza-university-of-rome-authentication.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uniroma1.it/it/pagina/piano-privacy-sapienza
- group: other
  title: ''
  type: Accessibility
  url: https://www.uniroma1.it/en/pagina/accessibility
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Sapienza-University-Rome
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/sapienza-universita-di-roma/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sapienza-university-of-rome-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sapienza-university-of-rome-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sapienza-university-of-rome-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sapienza-university-of-rome-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Sapienza University of Rome (Sapienza Università di Roma) is Italy''s largest university, a public research institution founded in 1303 and ranked #132 in the QS World University Rankings 2025. It runs no public developer portal, no API gateway and publishes no OpenAPI, and this profile does not pretend otherwise. What it does operate, on its own uniroma1.it hosts, are three genuinely institution-run machine surfaces: an OAI-PMH 2.0 provider on the IRIS institutional research catalogue (iris.uniroma1.it, DSpace-CRIS supplied by CINECA) whose underlying DSpace REST API is closed behind HTTP basic auth; a second, site-wide OAI-PMH 2.0 provider over the 100 open-access journals of Riviste Online SApienza (rosa.uniroma1.it, Open Journal Systems 3.3.0.13), whose OJS REST API v1 answers 403 to anonymous callers; and a Shibboleth SAML 2.0 identity provider, entityID https://idp.uniroma1.it/idp/shibboleth, published as machine-readable metadata in the IDEM GARR AAI federation aggregate.
  Its DataCite registration (provider ROMAUNO, repository CRUI.UNIROMA1, prefix 10.13133, 8,051 DOIs), its Crossref membership (member 13551, prefix 10.53131) and its ROR identifier 02be6w209 are verifiable from public registry endpoints. The Sapienza Library System open-data project at sbs.uniroma1.it documents a 5-star / DCAT-AP_IT dataset catalogue, but its one dataset download link is a hard 404 and its linked-data service still says "this website is still under development" — the project has not been updated since 2017 and it is recorded here honestly rather than credited as a live open-data API. The library OPAC runs vendor Sebina software on an institution host with no public API, the course catalogue is a Drupal site with no data interface, and there is no official institutional GitHub organization: the Sapienza-named org on GitHub carries student coursework, not platform code.'
finops:
- name: Sapienza University Of Rome Finops
  service_category: Education
  slug: sapienza-university-of-rome-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sapienza-university-of-rome.png
jsonld:
- class_count: 17
  name: Sapienza University Of Rome Context
  property_count: 7
  slug: sapienza-university-of-rome-context
layout: provider
modified: '2026-09-01'
name: Sapienza University of Rome
nav: Providers
network: true
overview: 'Sapienza University of Rome publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Italy, and Research.


  The Sapienza University of Rome catalog on APIs.io includes 1 JSON-LD context.


  Sapienza University of Rome''s developer surface includes documentation, authentication, GitHub presence, and 15 more developer resources.'
plans:
- name: Sapienza University Of Rome Plans Pricing
  plan_count: 2
  slug: sapienza-university-of-rome-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Sapienza University Of Rome Rate Limits
  slug: sapienza-university-of-rome-rate-limits
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 13.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 17.3
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 18.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 53.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/sapienza-university-of-rome/refs/heads/main/screenshots/sapienza-university-of-rome-2026-06-20T193443.png
security:
- kind: authentication
  name: Sapienza University Of Rome Authentication
  slug: sapienza-university-of-rome-authentication
  summary_line: none/http-basic/saml · 4 schemes
- kind: domain-security
  name: Sapienza University Of Rome Domain Security
  slug: sapienza-university-of-rome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sapienza-university-of-rome
tags:
- Education
- Higher Education
- University
- Italy
- Research
- Research Repository
- Open Access
- Open Data
- Library
- OAI-PMH
- Identity Federation
- Scholarly Publishing
website: https://www.uniroma1.it/en
---
