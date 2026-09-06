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
api_count: 14
apis:
- description: OAI-PMH 2.0 metadata-harvesting interface for the University of Liverpool Repository, an EPrints 3.4.5 open-access archive of research outputs (journal articles, conference papers, theses, reports and
  name: University of Liverpool Repository OAI-PMH
  slug: repository-oai
- description: 'Keyless, read-only EPrints REST interface on the institutional repository. Verified live 2026-09-01: GET /rest/ returns 200 listing the eprint, user and subject datasets, and GET /rest/eprint/ returns'
  name: University of Liverpool Repository EPrints REST
  slug: repository-rest
- description: 'OAI-PMH 2.0 metadata-harvesting interface for DataCat, the University of Liverpool research data catalogue (EPrints 3.4.4), exposing metadata for finalised research datasets. Verified live 2026-09-01:'
  name: DataCat Research Data Catalogue OAI-PMH
  slug: datacat-oai
- description: 'Institution-operated Active Directory Federation Services authorization server on the university''s own host, with a public, keyless discovery document. Verified live 2026-09-01: https://fs.liverpool.a'
  name: University of Liverpool AD FS OAuth 2.0 / OpenID Connect
  slug: adfs-oauth-oidc
- description: Institution-operated Shibboleth SAML 2.0 identity provider, registered in the UK Access Management Federation and visible in eduGAIN. entityID urn:mace:eduserv.org.uk:athens:provider:liv.ac.uk, mdui:D
  name: University of Liverpool Shibboleth IdP (UK Access Management Federation)
  slug: identity-federation
- description: 'The institution''s own Microsoft Entra ID tenant, discoverable by its domain name. Verified live 2026-09-01: https://login.microsoftonline.com/liverpool.ac.uk/v2.0/.well-known/openid-configuration retu'
  name: University of Liverpool Microsoft Entra ID tenant
  slug: entra-tenant
- description: 'The University of Liverpool is a DataCite repository member and has been since 2015. Verified 2026-09-01: https://api.datacite.org/clients/bl.lpool returns 200 with name "University of Liverpool", sym'
  name: DataCite repository membership (BL.LPOOL)
  slug: datacite-membership
- description: The University of Liverpool Library operates an ORCID member integration through the Jisc-run UK ORCID consortium, sending affiliation invitations to research staff and PGR students via the ORCID Affi
  name: ORCID affiliation programme (UK ORCID consortium)
  slug: orcid-membership
- description: 'The institution''s entry in the Research Organization Registry. Verified 2026-09-01: https://api.ror.org/v2/organizations/04xs57h96 returns 200 with display names "University of Liverpool" and "Prifysg'
  name: ROR organisation record (04xs57h96)
  slug: ror-record
- description: 'Liverpool University Press, the University''s own publishing house, is Crossref member 2165. Verified 2026-09-01: https://api.crossref.org/members/2165 returns 200 with primary-name "Liverpool Universi'
  name: Crossref membership via Liverpool University Press (member 2165)
  slug: crossref-membership
- description: 'Library resource management and discovery on Ex Libris Alma and Primo VE, operated as a Liverpool tenant. Verified 2026-09-01: https://liverpool.primo.exlibrisgroup.com/discovery/search?vid=44LIV_INST'
  name: Library discovery (Ex Libris Alma / Primo VE tenant)
  slug: library-discovery
- description: 'Talis Aspire reading lists, operated as a Liverpool tenant at liverpool.rl.talis.com with the canonical institutional URI http://readinglists.liverpool.ac.uk/. Genuinely machine-readable: https://live'
  name: Reading lists (Talis Aspire tenant)
  slug: reading-lists
- description: 'The university''s virtual learning environment is Instructure Canvas on the institution CNAME canvas.liverpool.ac.uk, authenticating through Liverpool''s own AD FS. Verified 2026-09-01: the root URL 302'
  name: Canvas VLE and LTI 1.3 platform (Instructure tenant)
  slug: vle-lti
- description: 'Liverpool Elements, the university''s current research information system, runs at elements.liverpool.ac.uk — an institution host resolving to 138.253.242.19. Verified 2026-09-01: the landing page retu'
  name: Liverpool Elements research information system (Symplectic tenant)
  slug: research-information
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.liverpool.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://livrepository.liverpool.ac.uk/
- group: other
  title: ''
  type: OpenData
  url: https://datacat.liverpool.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://liverpool.primo.exlibrisgroup.com/discovery/search?vid=44LIV_INST:LIV
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.liverpool.ac.uk/courses/undergraduate
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.ukfederation.org.uk/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.liverpool.ac.uk/research-it/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.liverpool.ac.uk/about/the-university/reports-policies-and-governance/ai-at-liverpool/policies-and-guidance/
- group: build
  title: ''
  type: AITooling
  url: https://www.liverpool.ac.uk/about/the-university/reports-policies-and-governance/ai-at-liverpool/support-and-activities/
- group: docs
  title: ''
  type: Documentation
  url: https://www.liverpool.ac.uk/open-research/
- group: operate
  title: ''
  type: Support
  url: https://libanswers.liverpool.ac.uk/
- group: company
  title: ''
  type: Blog
  url: https://news.liverpool.ac.uk/
- group: company
  title: ''
  type: BlogRSS
  url: https://news.liverpool.ac.uk/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liverpool.ac.uk/legal/data_protection/privacy-notices/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liverpool.ac.uk/legal/
- group: other
  title: ''
  type: Accessibility
  url: https://www.liverpool.ac.uk/accessibility/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/livuni
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-liverpool/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-liverpool-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-liverpool-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-liverpool-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-liverpool-oai-error-codes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-liverpool-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-liverpool-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-liverpool-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-liverpool-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Liverpool is a public research university in Liverpool, United Kingdom, a founding member of the Russell Group and of the civic "red brick" universities. It runs no public developer portal, publishes no OpenAPI, issues no API keys, and this profile does not pretend otherwise. What it does operate, on its own liverpool.ac.uk and liv.ac.uk hosts, are five genuinely institution-run machine surfaces: two EPrints OAI-PMH 2.0 providers — the University of Liverpool Repository (EPrints 3.4.5, eight metadata formats including RIOXX and uketd_dc) and DataCat, the research data catalogue (EPrints 3.4.4) — a keyless EPrints REST read interface on the repository, an Active Directory Federation Services OAuth 2.0 / OpenID Connect authorization server at fs.liverpool.ac.uk whose discovery document and JWKS are public, and a Shibboleth SAML 2.0 identity provider registered in the UK Access Management Federation and visible in eduGAIN. Its DataCite membership (BL.LPOOL, prefix
  10.17638, 16,405 DOIs resolving into its own repository), its ORCID affiliation programme, its ROR record and its Crossref presence through Liverpool University Press are all verifiable from public endpoints. Alongside these it is a tenant on four vendor platforms — Ex Libris Alma/Primo VE, Talis Aspire reading lists, Instructure Canvas and Symplectic Elements — whose contracts belong to those vendors, not to Liverpool. Student records, timetabling, module enrolment and the VLE sit behind SSO and are not publicly documented APIs. One trap worth recording: livrepository.liverpool.ac.uk returns 403 to a desktop-browser User-Agent and 200 to a harvester, so a browser-only probe grades a live repository dead.'
finops:
- name: University Of Liverpool Finops
  service_category: Education
  slug: university-of-liverpool-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-liverpool.png
jsonld:
- class_count: 21
  name: University Of Liverpool Context
  property_count: 6
  slug: university-of-liverpool-context
layout: provider
modified: '2026-09-01'
name: University of Liverpool
nav: Providers
network: true
overview: 'University of Liverpool publishes 14 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Russell Group, and United Kingdom.


  The University of Liverpool catalog on APIs.io includes 1 JSON-LD context.


  University of Liverpool''s developer surface includes documentation, support, engineering blog, authentication, and 23 more developer resources.'
plans:
- name: University Of Liverpool Plans Pricing
  plan_count: 2
  slug: university-of-liverpool-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: University Of Liverpool Rate Limits
  slug: university-of-liverpool-rate-limits
scopes:
- name: University Of Liverpool Scopes
  scope_count: 0
  slug: university-of-liverpool-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 39.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 79.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-liverpool/refs/heads/main/screenshots/university-of-liverpool-2026-06-20T200201.png
security:
- kind: authentication
  name: University Of Liverpool Authentication
  slug: university-of-liverpool-authentication
  summary_line: none/oauth2/openIdConnect/saml2 · 5 schemes
- kind: domain-security
  name: University Of Liverpool Domain Security
  slug: university-of-liverpool-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-liverpool
tags:
- Education
- Higher Education
- University
- Russell Group
- United Kingdom
- Research
- Research Repository
- Research Data
- Open Access
- OAI-PMH
- EPrints
- Identity Federation
- Library
- Metadata
website: https://www.liverpool.ac.uk/
---
