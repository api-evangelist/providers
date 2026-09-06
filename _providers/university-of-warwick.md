---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Warwick's Shibboleth SAML 2.0 identity provider. Publishes unauthenticated, machine-readable federation metadata as a SAML EntityDescriptor with entityID https://idp.warwick.ac.uk/idp/shibboleth, a sh
  name: Warwick Shibboleth Identity Provider
  slug: identity-federation
- description: OAuth 1.0a delegated access to Warwick web services — Sitebuilder (separate read and edit scopes), Warwick Search, Files.Warwick, Warwick Blogs, Warwick Forums, Exam Timetabling, Printer Credits and W
  name: Warwick Web Sign-on OAuth Services
  slug: oauth
- description: HTTP APIs for automating tasks against Files.Warwick, the University's own file storage service. Access is protected by Warwick Web Sign-on and reachable via OAuth using the urn:files.warwick.ac.uk:fi
  name: Files.Warwick API
  slug: files
- description: Warwick runs a Moodle virtual learning environment at moodle.warwick.ac.uk. The Moodle web service endpoint is live and responds to unauthenticated requests with a well-formed Moodle exception, confir
  name: Warwick Moodle Web Services
  slug: moodle
- description: 'Warwick''s library discovery layer. encore.lib.warwick.ac.uk issues an HTTP 302 to warwick.summon.serialssolutions.com — a Warwick-specific tenancy on the Summon platform operated by Serials Solutions '
  name: Warwick Library Discovery (Summon)
  slug: library-discovery
- description: 'The Warwick Students'' Union publishes a Membership API for validating membership and retrieving member rosters. Two reasons this is not credited to the University: the Students'' Union is a separate le'
  name: Warwick SU Membership API
  slug: su-membership
- baseURL: https://tabula.warwick.ac.uk/api/v1
  baseurl_source: declared
  description: Departments and modules.
  name: University of Warwick Administration API
  slug: university-of-warwick-administration-api
- baseURL: https://tabula.warwick.ac.uk/api/v1
  baseurl_source: declared
  description: Long-running asynchronous job instances.
  name: University of Warwick Jobs API
  slug: university-of-warwick-jobs-api
- baseURL: https://tabula.warwick.ac.uk/api/v1
  baseurl_source: declared
  description: Open Archives Initiative Protocol for Metadata Harvesting, version 2.0.
  name: University of Warwick OAI PMH API
  slug: university-of-warwick-oai-pmh-api
- baseURL: https://tabula.warwick.ac.uk/api/v1
  baseurl_source: declared
  description: Term dates, term weeks, holiday dates, and module/member timetables.
  name: University of Warwick Timetabling API
  slug: university-of-warwick-timetabling-api
artifact_total: 26
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-warwick-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://warwick.ac.uk/
- group: company
  title: ''
  type: About
  url: https://warwick.ac.uk/about
- group: start
  title: ''
  type: DeveloperPortal
  url: https://warwick.ac.uk/services/idg/services-support/web/
- group: docs
  title: ''
  type: Documentation
  url: https://warwick.ac.uk/services/idg/services-support/web/tabula/api/
- group: docs
  title: ''
  type: APIReference
  url: https://warwick.ac.uk/services/idg/services-support/web/tabula/api/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/universityofwarwick
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/universityofwarwick
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/the-university-of-warwick/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://warwick.ac.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://warwick.ac.uk/privacy/
- group: company
  title: ''
  type: Blog
  url: https://warwick.ac.uk/newsandevents/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.warwick.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://wrap.warwick.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://warwick.ac.uk/services/library/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://warwick.ac.uk/study
- group: agent
  title: ''
  type: LLMsTxt
  url: https://warwick.ac.uk/llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://warwick.ac.uk/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-warwick-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-warwick-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-warwick-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-warwick-oauth-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-warwick-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-warwick-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-warwick-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-warwick-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-warwick-openapi-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-warwick-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-warwick-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-warwick-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-warwick-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Warwick is a public research university in Coventry, England, and a member of the Russell Group. Unusually for this cohort, Warwick genuinely operates its own programmable surface rather than pointing at a vendor''s: Tabula, its teaching-and-learning administration system, is built and run by Warwick''s own Information and Digital Group (IDG) software engineering team and exposes a documented, versioned REST API on tabula.warwick.ac.uk — three of whose calendar endpoints (term dates, term weeks, holiday dates) are fully public, return live JSON and iCalendar without credentials, and were verified working on 2026-08-19. Warwick also runs its own central identity infrastructure: a Shibboleth SAML 2.0 identity provider at idp.warwick.ac.uk publishing unauthenticated, machine-readable federation metadata carrying REFEDS SIRTFI and Research-and-Scholarship entity attributes, plus a Web Sign-on OAuth 1.0a service with nine documented Warwick-specific scopes. Its
  institutional repository, WRAP, is a self-hosted EPrints instance on Warwick infrastructure serving a live OAI-PMH 2.0 endpoint with seven metadata formats including RIOXX 2.0 and OpenAIRE. Warwick additionally publishes an llms.txt that documents a real agent affordance rather than merely listing links — appending `?markdown` to any warwick.ac.uk page returns that page as Markdown, which was verified. The honest limits: Warwick publishes no OpenAPI, AsyncAPI, JSON Schema or Postman collection for any of its APIs — every machine-readable contract in this repository was derived by API Evangelist from Warwick''s documentation and live probes, and is marked as such. There is no changelog, no status page, no deprecation policy and no public issue tracker. Most of the surface is gated behind Warwick Web Sign-on and is not consumable without an institutional account, sandbox access is by email request rather than self-service, and the delegated authorization standard is OAuth 1.0a rather than
  OAuth 2.0 or OIDC. Its library discovery and students'' union surfaces are vendor platforms running under Warwick-specific hostnames and are recorded here as tenant relationships, not as Warwick''s engineering.'
examples:
- key_count: 7
  name: University Of Warwick Tabula Holidaydates
  slug: university-of-warwick-tabula-holidaydates
- key_count: 7
  name: University Of Warwick Tabula Termdates
  slug: university-of-warwick-tabula-termdates
- key_count: 7
  name: University Of Warwick Tabula Unauthorized
  slug: university-of-warwick-tabula-unauthorized
finops:
- name: University Of Warwick Finops
  service_category: Education
  slug: university-of-warwick-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-warwick.png
json_schemas:
- name: Tabula Error Response
  property_count: 3
  slug: university-of-warwick-tabula-error
- name: Tabula Holiday Dates Response
  property_count: 3
  slug: university-of-warwick-tabula-holidaydates
- name: Tabula Term Dates Response
  property_count: 3
  slug: university-of-warwick-tabula-termdates
- name: Tabula Term Weeks Response
  property_count: 3
  slug: university-of-warwick-tabula-termweeks
jsonld:
- class_count: 12
  name: University Of Warwick Context
  property_count: 4
  slug: university-of-warwick-context
layout: provider
modified: '2026-08-19'
name: University of Warwick
nav: Providers
network: true
overview: 'University of Warwick publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Jobs API, OAI PMH API, and 1 more. Tagged areas include University, Higher Education, Education, Research, and United Kingdom.


  The University of Warwick catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Warwick''s developer surface includes documentation, API reference, GitHub presence, engineering blog, authentication, and 27 more developer resources.'
plans:
- name: University Of Warwick Plans Pricing
  plan_count: 2
  slug: university-of-warwick-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: University Of Warwick Rate Limits
  slug: university-of-warwick-rate-limits
rules:
- effective_rule_count: 9
  extends: []
  name: University of Warwick API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 6
  slug: university-of-warwick-openapi-spectral-rules
scopes:
- name: University Of Warwick Oauth Scopes
  scope_count: 9
  slug: university-of-warwick-oauth-scopes
  summary_line: 9 scopes · threeLegged
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 69.3
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 31.8
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 60.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 90.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-warwick/refs/heads/main/screenshots/university-of-warwick-2026-06-20T200340.png
security:
- kind: authentication
  name: University Of Warwick Authentication
  slug: university-of-warwick-authentication
  summary_line: http/oauth1/saml · 3 schemes
- kind: domain-security
  name: University Of Warwick Domain Security
  slug: university-of-warwick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Warwick Vulnerability Disclosure
  slug: university-of-warwick-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-warwick
tags:
- University
- Higher Education
- Education
- Research
- United Kingdom
- Russell Group
- Identity Federation
- Research Repository
- Course Catalog
- Timetabling
- Student Information System
- Open Data
website: https://warwick.ac.uk/
---
