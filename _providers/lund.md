---
access_model:
  confidence: high
  label: Free · no key required
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lund Agentic Access
  operation_count: 2
  slug: lund-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- baseURL: https://lup.lub.lu.se/search
  baseurl_source: declared
  description: Keyless REST/JSON(P) search over the Lund University Publications (LUP) research-output database, operated by Lund University Libraries on Lund's own host. Supports CQL-style queries, paging and sorti
  name: Lund University Publications Search API
  slug: lund-publication-api
- description: OAI-PMH 2.0 metadata-harvesting endpoint for the LUP research-output repository. Identify confirms repositoryName "Lund University Publications", repositoryIdentifier lup.lub.lu.se and adminEmail publ
  name: Lund University Publications OAI-PMH
  slug: lup-oai
- description: 'SRU 1.1 Search/Retrieve via URL service over the LUP research-output database, querying with CQL and returning MODS 3.3 records in the http://www.loc.gov/zing/srw/ namespace. Scan and explain are not '
  name: Lund University Publications SRU
  slug: lup-sru
- description: 'unAPI 1 discovery service returning the alternate metadata formats available for LUP records, which is how reference managers such as Zotero autodiscover Lund records. No authentication required. The '
  name: Lund University Publications unAPI
  slug: lup-unapi
- baseURL: https://lup.lub.lu.se/student-papers/search
  baseurl_source: declared
  description: Keyless REST/JSON(P) search over LUP Student Papers, a second Lund University Libraries repository holding student theses and degree projects, with its own record model — courseCode, courseTerm, stude
  name: LUP Student Papers Search API
  slug: lup-student-papers
- description: OAI-PMH 2.0 harvesting endpoint for the LUP Student Papers repository. Identify confirms repositoryName "Lund University Publications - Student Papers" and repositoryIdentifier lup-student-papers.lub.
  name: LUP Student Papers OAI-PMH
  slug: lup-student-papers-oai
- description: SRU 1.1 / CQL search service over the LUP Student Papers repository, returning MODS 3.3 records. No authentication required. Base URL is /student-papers/sru.
  name: LUP Student Papers SRU
  slug: lup-student-papers-sru
- description: Lund University's own SAML 2.0 / Shibboleth Identity Provider, serving machine-readable federation metadata at its entityID. The EntityDescriptor declares an IDPSSODescriptor, the Shibboleth scope lu.
  name: Lund University Shibboleth Identity Provider (SWAMID)
  slug: idp-saml-metadata
- description: Lund's tenant deployment of Elsevier Pure, branded LUCRIS, covering researchers, organisations, outputs, projects, datasets and activities at portal.research.lu.se. The data and the deployment are Lun
  name: Lund University Research Portal (LUCRIS / Elsevier Pure)
  slug: research-portal
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lund University Publications (LUP) Search Publication API
  slug: open-lund-publication-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.lunduniversity.lu.se/
- group: docs
  title: ''
  type: Documentation
  url: https://lup.lub.lu.se/search/doc/api
- group: docs
  title: ''
  type: APIReference
  url: https://lup.lub.lu.se/search/doc/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lup.lub.lu.se/search/doc/api
- group: other
  title: ''
  type: ResearchRepository
  url: https://lup.lub.lu.se/
- group: other
  title: ''
  type: ResearchRepository
  url: https://lup.lub.lu.se/student-papers/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idpv4.lu.se/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.lunarc.lu.se/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.lub.lu.se/en
- group: other
  title: ''
  type: AIPolicy
  url: https://www.staff.lu.se/sites/staff.lu.se/files/2025-12/policy-on-principles-for-the-use-of-generative-AI-at-LU..pdf
- group: build
  title: ''
  type: AITooling
  url: https://www.staff.lu.se/support-and-tools/it-mail-and-telephony/ai-lund-university
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.lunduniversity.lu.se/study/find-education
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lunduniversity.lu.se/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.lunduniversity.lu.se/about-lund-university/contact-us/processing-personal-data-lund-university
- group: company
  title: ''
  type: Blog
  url: https://www.lunduniversity.lu.se/news
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lunduniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/lund-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/lund-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lund-authentication.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lund-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lund-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lund-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lund-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lund-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lund-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lund-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Lund University is a public research university in Lund, Sweden, founded in 1666, with roughly 46,000 students across nine faculties and the MAX IV and ESS research infrastructures on its doorstep. Its programmable footprint is narrow, real, and almost entirely library-operated: Lund University Libraries run two self-hosted publication repositories on the university''s own host — Lund University Publications (LUP) for research output and LUP Student Papers for theses and degree projects — and each exposes the same open, keyless stack of a JSON(P) search API, an OAI-PMH 2.0 repository, an SRU 1.1/CQL search service, a unAPI 1 discovery service, RSS feeds and a bulk bibliographic export. Lund also operates its own Shibboleth Identity Provider, registered in the Swedish national federation SWAMID and interfederated through eduGAIN, which is a genuinely institution-operated machine-readable surface. Outside those, there is no central developer portal, no self-service API key, no
  open data portal at data.lu.se, and no public JSON endpoint behind the course finder — the education search at lunduniversity.lu.se is server-rendered with nothing machine-readable underneath. The research portal at portal.research.lu.se is the LUCRIS research information system running on Elsevier Pure: the data is Lund''s, the contract is Elsevier''s, and its web service refuses anonymous callers. Library discovery (LUBcat, LUBsearch) and the timetable (TimeEdit) are likewise vendor platforms carrying Lund''s name.'
examples:
- key_count: 5
  name: Lund Searchpublications Example
  slug: lund-searchpublications-example
finops:
- name: Lund Finops
  service_category: Education
  slug: lund-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lund.png
json_schemas:
- name: Publication
  property_count: 52
  slug: lund-publication
- name: SearchResult
  property_count: 5
  slug: lund-searchresult
json_structures:
- name: Lund Publication Structure
  property_count: 21
  slug: lund-publication-structure
jsonld:
- class_count: 29
  name: Lund Context
  property_count: 7
  slug: lund-context
layout: provider
modified: '2026-08-30'
name: Lund University
nav: Providers
network: true
overview: 'Lund University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Publications Search API and LUP Student Papers Search API. Tagged areas include University, Higher Education, Education, Sweden, and Europe.


  The Lund University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Lund University''s developer surface includes documentation, API reference, support, engineering blog, GitHub presence, authentication, and 21 more developer resources.'
plans:
- name: Lund Plans Pricing
  plan_count: 2
  slug: lund-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Lund Rate Limits
  slug: lund-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lund University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lund-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Lund University API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: lund-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 72.3
    catalog_earned_first_party: 0.0
    catalog_gap: 42.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.0
    contract_quality: 26.8
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 28.0
    operational_transparency: 26.3
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 50.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lund/refs/heads/main/screenshots/lund-2026-06-20T184805.png
security:
- kind: authentication
  name: Lund Authentication
  slug: lund-authentication
  summary_line: none/saml · 2 schemes
- kind: domain-security
  name: Lund Domain Security
  slug: lund-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lund Vulnerability Disclosure
  slug: lund-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lund
tags:
- University
- Higher Education
- Education
- Sweden
- Europe
- Research
- Research Repository
- Publications
- Library
- Open Metadata
- Identity Federation
- OAI-PMH
website: https://www.lunduniversity.lu.se/
---
