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
  scored_at: '2026-08-26'
api_count: 7
apis:
- description: LSE operates its own SAML2 Shibboleth identity provider for staff, students and library resource access, registered in the UK Access Management Federation under entityID https://lse.ac.uk/idp with the
  name: LSE Shibboleth Identity Provider (UK Access Management Federation)
  slug: identity-federation
- description: LSE runs its own Moodle virtual learning environment at moodle.lse.ac.uk on its own registrable domain, resolving directly to AWS with no vendor CNAME (managed hosting is provided by Catalyst IT, a Mo
  name: LSE Moodle LTI 1.3 Platform
  slug: moodle-lti-platform
- description: LSE Research Online is LSE's institutional repository — LSE's research outputs, LSE's metadata, LSE's registered OAI-PMH base URL and admin contact (lseresearchonline@lse.ac.uk). It is not LSE's engin
  name: LSE Research Online (EPrints, OAI-PMH)
  slug: research-online-oai
- description: LSE library discovery runs on Ex Libris Primo VE at librarysearch.lse.ac.uk, which CNAMEs to lse.primo.exlibrisgroup.com and then eu00.primo.exlibrisgroup.com, under LSE's institutional view identifie
  name: LSE Library Search (Ex Libris Primo VE / Alma)
  slug: library-search
- description: The LSE Digital Library publishes digitised and born-digital material from LSE Library collections. The host CNAMEs to lse.custom.url.quartexcollections.com, an LSE tenancy on Adam Matthew Digital's Q
  name: LSE Digital Library (Quartex — IIIF / OAI-PMH)
  slug: digital-library
- description: The LSE Library archive catalogue at archives.lse.ac.uk runs on Epexio, a hosted archival discovery platform, served from AWS behind a certificate issued to LSE's own hostname. The page markup carries
  name: LSE Archives Catalogue (Epexio)
  slug: archives-catalogue
- description: LSE is a registered DataCite provider — member identifier lcqr, "London School of Economics", memberType consortium_organization, region EMEA, registered 2020-09-01, linked to ROR https://ror.org/0090
  name: LSE DOI Registration (DataCite)
  slug: datacite-doi
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.lse.ac.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lse.ac.uk/lse-information/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lse.ac.uk/lse-information/privacy-policy
- group: other
  title: ''
  type: IdentityFederation
  url: https://gate.library.lse.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchonline.lse.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://librarysearch.lse.ac.uk/discovery/search?vid=44LSE_INST
- group: other
  title: ''
  type: AIPolicy
  url: https://info.lse.ac.uk/staff/divisions/Eden-Centre/Artificial-Intelligence-Education-and-Assessment/School-position-on-generative-AI
- group: auth
  title: ''
  type: Authentication
  url: authentication/lse-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lse-domain-standards.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lse-vocabulary.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lse-lifecycle.yml
- group: design
  title: ''
  type: Errors
  url: errors/lse-errors.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lse-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/the-london-school-of-economics-and-political-science/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LSEnews
- group: commercial
  title: ''
  type: Plans
  url: plans/lse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lse-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://blogs.lse.ac.uk/
- group: company
  title: ''
  type: BlogRSS
  url: https://blogs.lse.ac.uk/feed/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/lse-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'The London School of Economics and Political Science (LSE) is a public research university in London, United Kingdom, a member of the Russell Group and the University of London, ranked in the QS World University Rankings top 40 and specialised in the social sciences. LSE operates no public developer portal, no open data portal, no course-catalog or timetable API, and no official GitHub organisation — github.com/lse is an unrelated systems-programming lab. Re-profiled on 2026-08-19 against the operator axis, its genuinely institution-operated machine-readable footprint is two things: a SAML2 Shibboleth identity provider registered in the UK Access Management Federation under entityID https://lse.ac.uk/idp, and an IMS LTI 1.3 platform on its own Moodle VLE serving a live JWKS, OAuth 2.0 token endpoint and OIDC authorization endpoint. Everything else that appears to be an LSE API is a vendor contract running under an LSE tenancy — EPrints Services hosts the research repository,
  Ex Libris Primo VE the library discovery layer, Quartex the digital library, Epexio the archive catalogue, and DataCite the DOI registration. Those tenancies are real institutional facts and are recorded as such; the contracts behind them belong to the vendors, not to LSE.'
examples:
- key_count: 1
  name: Lse Lti Jwks Response
  slug: lse-lti-jwks-response
finops:
- name: Lse Finops
  service_category: Education
  slug: lse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lse.png
json_schemas:
- name: LSE Moodle LTI 1.3 Platform JSON Web Key Set
  property_count: 1
  slug: lse-lti-jwks
jsonld:
- class_count: 13
  name: Lse Context
  property_count: 10
  slug: lse-context
layout: provider
modified: '2026-08-19'
name: London School of Economics and Political Science
nav: Providers
network: true
overview: 'London School of Economics and Political Science publishes 1 API on the [APIs.io](https://apis.io/) network: LSE Moodle LTI 1.3 Platform. Tagged areas include University, Higher Education, Education, United Kingdom, and Russell Group.


  The London School of Economics and Political Science catalog on APIs.io includes 1 JSON-LD context.


  London School of Economics and Political Science''s developer surface includes authentication, engineering blog, and 21 more developer resources.'
plans:
- name: Lse Plans Pricing
  plan_count: 2
  slug: lse-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Lse Rate Limits
  slug: lse-rate-limits
score:
  band: thin
  composite: 36.0
  delta: 2.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 26.9
    developer_ergonomics: 22.6
    discoverability: 74.1
    governance: 15.2
    operational_transparency: 21.1
  previous_composite: 33.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lse/refs/heads/main/screenshots/lse-2026-06-20T184742.png
security:
- kind: authentication
  name: Lse Authentication
  slug: lse-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lse Domain Security
  slug: lse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lse
tags:
- University
- Higher Education
- Education
- United Kingdom
- Russell Group
- Social Sciences
- Identity Federation
- Learning Management
- Research Repository
- Library
- Open Research
- OAI-PMH
- SAML
- LTI
- IIIF
website: https://www.lse.ac.uk/
---
