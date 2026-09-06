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
  scored_at: '2026-09-05'
api_count: 12
apis:
- description: Institution-operated CKAN open data portal serving the standard CKAN Action API over University of Bologna datasets. Verified live 2026-09-01 — https://dati.unibo.it/api/3/action/package_list returned
  name: University of Bologna Open Data (CKAN Action API)
  slug: opendata-ckan
- description: OAI-PMH 2.0 metadata-harvesting provider for AMS Acta, the AlmaDL institutional research repository, self-hosted on the university's own infrastructure. Verified live 2026-09-01 — verb=Identify return
  name: AMS Acta Institutional Repository OAI-PMH
  slug: amsacta-oai-pmh
- description: Second, distinct OAI-PMH 2.0 provider run by AlmaDL over AMS Tesi di Dottorato, the university's doctoral thesis repository. Verified live 2026-09-01 — verb=Identify returns 200 text/xml with reposito
  name: AMS Tesi di Dottorato (Doctoral Theses) OAI-PMH
  slug: amsdottorato-oai-pmh
- description: Third AlmaDL OAI-PMH 2.0 provider, over AMS Tesi di Laurea, the university's graduate and undergraduate thesis repository. Verified live 2026-09-01 — verb=Identify returns 200 text/xml with repository
  name: AMS Tesi di Laurea (Graduate Theses) OAI-PMH
  slug: amslaurea-oai-pmh
- description: Site-wide OAI-PMH 2.0 provider over AlmaDL Journals, the university's open-access journal publishing platform, on its own host journals.unibo.it (atrproxy4.unibo.it, 137.204.24.209). Verified live 202
  name: AlmaDL Journals OAI-PMH
  slug: almadl-journals-oai-pmh
- description: Institution-operated Shibboleth SAML 2.0 identity provider, published as machine-readable metadata both directly on the university's own host and in the IDEM GARR AAI federation aggregate. Verified li
  name: UNIBO Shibboleth Identity Provider (IDEM GARR AAI)
  slug: identity-federation
- description: Virtuale is the university's self-hosted Moodle learning management system, on its own host virtuale.unibo.it (frontend-http-azure-01.unibo.it), and it exposes a live LTI 1.3 platform surface. Verifie
  name: Virtuale (Moodle) LTI 1.3 Platform and Web Services
  slug: virtuale-lti
- description: IRIS is the university's current research information system and publication catalogue, reachable at cris.unibo.it. The host is a vanity name on the university's domain but it is NOT university-run in
  name: IRIS Research Information System (CINECA tenancy)
  slug: iris-cineca-tenancy
- description: AlmaStart is the University of Bologna library system's discovery layer. The entry point almastart.unibo.it wears the university's domain but CNAMEs to unibo.primo.exlibrisgroup.com and then eu03.prim
  name: AlmaStart Library Discovery (Ex Libris Primo VE tenancy)
  slug: almastart-primo-tenancy
- description: 'The University of Bologna is a registered DataCite member and DOI registrant — a fact about the institution, not a contract it operates. Verified live 2026-09-01 against the DataCite REST API: https:/'
  name: DataCite DOI registration (provider UYEY, 32,291 DOIs)
  slug: datacite-registration
- description: The University of Bologna is a Crossref member and DOI depositor. Verified live 2026-09-01 — https://api.crossref.org/members/32492 returns 200 with primary-name "Alma Mater Studiorum Università di Bo
  name: Crossref membership (member 32492, prefix 10.60923)
  slug: crossref-membership
- description: The University of Bologna is registered in the Research Organization Registry with ROR ID https://ror.org/01111rn36, names "University of Bologna" / "Alma Mater Studiorum - Università di Bologna", dom
  name: ROR organization identifier 01111rn36
  slug: ror-registration
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.unibo.it/en
- group: other
  title: ''
  type: OpenData
  url: https://dati.unibo.it/
- group: other
  title: ''
  type: ResearchRepository
  url: https://amsacta.unibo.it/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shib.unibo.it/idp/shibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://almastart.unibo.it/discovery/search?vid=39UBO_INST:VU
- group: learn
  title: ''
  type: CourseCatalog
  url: https://corsi.unibo.it/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.unibo.it/it/ateneo/statuto-norme-strategie-bilanci/intelligenza-artificiale
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-bologna-domain-standards.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-bologna-authentication.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-bologna-context.jsonld
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unibo.it/en/university/privacy-policy-and-legal-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unibo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/unibo/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bologna-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-bologna-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-bologna-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-bologna-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Bologna (Alma Mater Studiorum - Università di Bologna) is the oldest university in the Western world, founded in 1088, and Italy''s largest public research university, ranked #133 in the QS World University Rankings 2025. It publishes no OpenAPI, runs no developer portal and issues no API keys, and this profile does not pretend otherwise. What it does operate, on its own unibo.it hosts and its own network (137.204.24.0/24), is an unusually deep set of standards-based machine surfaces for a university: a CKAN 2.6.9 open data portal serving the CKAN Action API at dati.unibo.it; four separate live OAI-PMH 2.0 providers run by the AlmaDL digital library — AMS Acta (institutional research repository, EPrints, ten metadata formats including oai_datacite and openaire_oai_dc), AMS Tesi di Dottorato (doctoral theses), AMS Tesi di Laurea (graduate theses) and AlmaDL Journals (Open Journal Systems, 100 open-access journals); a Shibboleth SAML 2.0 identity provider, entityID
  https://shib.unibo.it/idp/shibboleth, published as machine-readable metadata both on its own host and in the IDEM GARR AAI federation aggregate; and a self-hosted Moodle at virtuale.unibo.it exposing a live LTI 1.3 platform surface (JWKS plus an OAuth2 token endpoint) alongside a token-gated Moodle Web Services REST API. Its DataCite registration (provider UYEY, five prefixes, 32,291 DOIs), its Crossref membership (member 32492, prefix 10.60923, 1,170 DOIs) and its ROR identifier 01111rn36 are verifiable from public registry endpoints. Two further surfaces are the university''s data on someone else''s platform and are recorded as tenancies, not as its contracts: the IRIS research information system at cris.unibo.it CNAMEs to unibo.prod.iris.cineca.it (CINECA), and the AlmaStart library discovery layer at almastart.unibo.it CNAMEs to unibo.primo.exlibrisgroup.com (Ex Libris Primo VE). The university''s generative-AI policy is a real governance artifact but exists only on the Italian surface.
  Administrative, student-record and course-catalogue systems are behind institutional SSO and are not openly documented.'
finops:
- name: University Of Bologna Finops
  service_category: Education
  slug: university-of-bologna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bologna.png
jsonld:
- class_count: 18
  name: University Of Bologna Context
  property_count: 7
  slug: university-of-bologna-context
layout: provider
modified: '2026-09-01'
name: University of Bologna
nav: Providers
network: true
overview: 'University of Bologna publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Italy, and Europe.


  The University of Bologna catalog on APIs.io includes 1 JSON-LD context.


  University of Bologna''s developer surface includes documentation, authentication, and 17 more developer resources.'
plans:
- name: University Of Bologna Plans Pricing
  plan_count: 2
  slug: university-of-bologna-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: University Of Bologna Rate Limits
  slug: university-of-bologna-rate-limits
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 27.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bologna/refs/heads/main/screenshots/university-of-bologna-2026-06-20T200136.png
security:
- kind: authentication
  name: University Of Bologna Authentication
  slug: university-of-bologna-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Bologna Domain Security
  slug: university-of-bologna-domain-security
  summary_line: TLSv1.2 · DMARC
slug: university-of-bologna
tags:
- Education
- Higher Education
- University
- Italy
- Europe
- Research
- Research Repository
- Open Data
- Open Access
- Library
- OAI-PMH
- Identity Federation
- Scholarly Publishing
- Learning Management
website: https://www.unibo.it/en
---
