---
access_model:
  confidence: high
  label: Free and keyless where public; institutional affiliation where not
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'The JSON backend behind Ocasys, the University''s own course and degree-programme catalog. Verified live 2026-08-30 with no credentials: course search, full course records, the catalog page projection,'
  name: University of Groningen Ocasys Course Catalog API
  slug: ocasys-course-catalog
- description: 'Keyless OAI-PMH 2.0 metadata-harvesting endpoint operated by the University on its own domain. Verified live 2026-08-30: Identify reports protocolVersion 2.0, repositoryName "University of Groningen R'
  name: University of Groningen Research Database OAI-PMH
  slug: pure-oai-pmh
- description: 'The University runs its own SAML 2.0 identity provider and publishes signed federation metadata at signon.rug.nl for entityID https://signon.rug.nl/nidp/saml2/metadata. Verified live 2026-08-30: 25KB '
  name: University of Groningen Identity Provider (SURFconext / eduGAIN)
  slug: identity-provider
- description: 'The Elsevier Pure web service deployed on the University''s CRIS host. Probed 2026-08-30: pure.rug.nl/ws/api redirects to /ws/api/documentation/index.html, whose rel=canonical is https://api.elsevierpu'
  name: University of Groningen Research Portal (Pure) REST API
  slug: pure-ws-api
- description: The University's default repository for research data and software is a collection inside DataverseNL, the shared national Dataverse installation that DANS and SURF operate at dataverse.nl — a host th
  name: University of Groningen research data collection on DataverseNL
  slug: dataversenl-collection
- description: Library discovery runs on OCLC WorldCat Discovery at rug.on.worldcat.org, a tenant instance on OCLC's platform rather than a catalog interface the University operates. Verified live 2026-08-30. Any Wo
  name: University of Groningen Library discovery (OCLC WorldCat)
  slug: worldcat-discovery
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.rug.nl/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://ocasys.rug.nl/
- group: other
  title: ''
  type: IdentityFederation
  url: https://signon.rug.nl/nidp/saml2/metadata
- group: other
  title: ''
  type: ResearchRepository
  url: https://research.rug.nl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.rug.nl/digital-competence-centre/research-data/archive-and-publish/dataversenl
- group: build
  title: ''
  type: LibraryCatalog
  url: https://rug.on.worldcat.org/discovery
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.rug.nl/society-business/center-for-information-technology/research/services/hpc/habrok
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.hpc.rug.nl/
- group: other
  title: ''
  type: OpenData
  url: https://www.rug.nl/digital-competence-centre/research-data/archive-and-publish/open-data
- group: other
  title: ''
  type: AIPolicy
  url: https://www.rug.nl/cit/services/ai-office/beleid-en-regelgeving/
- group: build
  title: ''
  type: AITooling
  url: https://www.rug.nl/cit/services/ai-office/ai-oplossingen/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rijksuniversiteit-groningen
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rug-cit-hpc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/rijksuniversiteit-groningen/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/univgroningen
- group: company
  title: ''
  type: Blog
  url: https://www.rug.nl/about-ug/latest-news/news/latest-rug-news!rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rug.nl/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rug.nl/info/disclaimer-copyright
- group: operate
  title: ''
  type: Support
  url: https://www.rug.nl/society-business/center-for-information-technology/support/
- group: auth
  title: ''
  type: SecurityDisclosure
  url: https://www.rug.nl/.well-known/security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-groningen-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-groningen-education-standards-conformance.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-groningen-errors.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-groningen-course-catalog-vocabulary.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-groningen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-groningen-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-groningen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-groningen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-groningen-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Groningen (Rijksuniversiteit Groningen, RUG/UG) is a public research university in Groningen, the Netherlands, founded in 1614. Measured honestly, it runs no API programme: there is no developer portal, no api.rug.nl, no status page, no published versioning or deprecation policy, and no first-party OpenAPI anywhere on its estate — api.rug.nl, data.rug.nl, developer.rug.nl and status.rug.nl do not resolve at all. What it does operate, on its own domain, is a small set of real programmable surfaces: the Ocasys course and degree-programme catalog, whose JSON backend at ocasys.rug.nl/api answers unauthenticated course search, full course records, programme search, faculties and controlled option lists, and emits RFC 9457 problem details on error; a keyless OAI-PMH 2.0 endpoint at pure.rug.nl/ws/oai serving 1,521,703 identifiers across six metadata profiles including OpenAIRE CERIF 1.2 with resolvable ORCID iDs; and its own SAML 2.0 identity provider at signon.rug.nl,
  registered in eduGAIN through SURFconext. Everything else that looks like a University of Groningen API is a purchase. The CRIS is Elsevier Pure, research data lives in a collection inside the shared national DataverseNL installation that DANS and SURF operate, and library discovery is OCLC WorldCat. Those are recorded here as tenant relationships, not as the University''s engineering.'
examples:
- key_count: 7
  name: University Of Groningen Ocasys Course Search Example
  slug: university-of-groningen-ocasys-course-search-example
- key_count: 7
  name: University Of Groningen Ocasys Faculties Example
  slug: university-of-groningen-ocasys-faculties-example
- key_count: 7
  name: University Of Groningen Ocasys Get Course Example
  slug: university-of-groningen-ocasys-get-course-example
- key_count: 7
  name: University Of Groningen Ocasys Problem Detail Example
  slug: university-of-groningen-ocasys-problem-detail-example
- key_count: 7
  name: University Of Groningen Ocasys Program Search Example
  slug: university-of-groningen-ocasys-program-search-example
finops:
- name: University Of Groningen Finops
  service_category: Education
  slug: university-of-groningen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-groningen.png
json_schemas:
- name: Ocasys Course
  property_count: 30
  slug: university-of-groningen-ocasys-course
- name: Ocasys Degree Programme
  property_count: 14
  slug: university-of-groningen-ocasys-program
jsonld:
- class_count: 17
  name: University Of Groningen Course Context
  property_count: 4
  slug: university-of-groningen-course-context
layout: provider
modified: '2026-08-30'
name: University of Groningen
nav: Providers
network: true
overview: 'University of Groningen publishes 2 APIs on the [APIs.io](https://apis.io/) network: Ocasys Course Catalog API and Research Database OAI-PMH. Tagged areas include Education, Higher Education, University, Netherlands, and Europe.


  The University of Groningen catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Groningen''s developer surface includes documentation, GitHub presence, engineering blog, support, authentication, and 25 more developer resources.'
plans:
- name: University Of Groningen Plans Pricing
  plan_count: 2
  slug: university-of-groningen-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: University Of Groningen Rate Limits
  slug: university-of-groningen-rate-limits
rules:
- effective_rule_count: 9
  extends: []
  name: University of Groningen API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: university-of-groningen-course-catalog-rules
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 22.7
    contract_quality: 54.6
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 22.7
    operational_transparency: 26.3
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 73
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-groningen/refs/heads/main/screenshots/university-of-groningen-2026-06-20T200155.png
security:
- kind: authentication
  name: University Of Groningen Authentication
  slug: university-of-groningen-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: University Of Groningen Domain Security
  slug: university-of-groningen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: University Of Groningen Vulnerability Disclosure
  slug: university-of-groningen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-groningen
tags:
- Education
- Higher Education
- University
- Netherlands
- Europe
- Research
- Research Data
- Course Catalog
- Identity Federation
- OAI-PMH
- Library
- Metadata
- Open Data
website: https://www.rug.nl/
---
