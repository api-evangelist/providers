---
access_model:
  confidence: high
  label: Free · no registration
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 27.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Birmingham Agentic Access
  operation_count: 2
  slug: university-of-birmingham-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: UBIRA eData is the University of Birmingham's own EPrints research-data repository, running on Birmingham infrastructure (edata.bham.ac.uk resolves to 147.188.217.239, the University's own address spa
  name: UBIRA eData (EPrints OAI-PMH + REST)
  slug: edata
- description: OAI-PMH 2.0 metadata harvesting interface for the University of Birmingham eTheses EPrints repository, holding full-text electronic theses produced by research postgraduates. Identify returns reposito
  name: UBIRA eTheses (EPrints OAI-PMH)
  slug: etheses
- description: OAI-PMH 2.0 metadata harvesting interface for the University of Birmingham ePapers EPrints repository, holding open-access working papers, technical reports and other grey literature. Identify returns
  name: ePapers Repository (EPrints OAI-PMH)
  slug: epapers
- description: The University's own Shibboleth SAML 2.0 Identity Provider. The entity descriptor is served directly by IT Services and carries their maintenance history in XML comments; it declares SingleSignOnServi
  name: University of Birmingham Identity Provider (SAML 2.0 / Shibboleth)
  slug: identity-provider
- description: A GitLab instance the University runs itself on the BEAR (Birmingham Environment for Academic Research) estate — gitlab.bham.ac.uk resolves through proxy-vrrp-1.bear.bham.ac.uk to 147.188.x, Birmingha
  name: BEAR GitLab (self-hosted, /api/v4)
  slug: gitlab
- baseURL: https://englishconstructicon.bham.ac.uk/database/api
  baseurl_source: declared
  description: An open research API from the English Constructicon project, a construction-grammar database built in the College of Arts and Law with the University's Research Software Group and hosted on the instit
  name: English Constructicon API
  slug: english-constructicon
- description: 'research.birmingham.ac.uk is the University''s research information portal. It is an Elsevier Pure tenancy — the hostname CNAMEs to birmingham-live.elsevierpure.com and on to eu.prod.elsevierpure.com, '
  name: Elsevier Pure research portal (Birmingham tenancy)
  slug: pure-research-portal
- description: FindIt@Bham is the University's library discovery layer, running on Ex Libris Primo — findit.bham.ac.uk CNAMEs to birmingham.primo.exlibrisgroup.com and on to eu00.primo.exlibrisgroup.com, and the ser
  name: FindIt@Bham library discovery (Ex Libris Primo tenancy)
  slug: findit-primo
- description: canvas.bham.ac.uk is the University's virtual learning environment, an Instructure Canvas tenancy — the hostname CNAMEs to birmingham-vanity.instructure.com. Canvas ships an LTI platform and an LMS RE
  name: Canvas virtual learning environment (Instructure tenancy)
  slug: canvas-vle
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: English Constructicon Constructions API
  slug: open-university-of-birmingham-constructions-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.birmingham.ac.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://englishconstructicon.bham.ac.uk/database/api/
- group: docs
  title: ''
  type: APIReference
  url: https://edata.bham.ac.uk/rest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/University-of-Birmingham
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-birmingham/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/unibirmingham
- group: company
  title: ''
  type: Blog
  url: https://blog.bham.ac.uk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.birmingham.ac.uk/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.birmingham.ac.uk/legal
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp2.bham.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://edata.bham.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://findit.bham.ac.uk/
- group: other
  title: ''
  type: ResearchComputing
  url: https://bear-apps.bham.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.birmingham.ac.uk/libraries/education-excellence/gai
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-birmingham-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-birmingham-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-birmingham-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/university-of-birmingham-errors.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-birmingham-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-birmingham-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/university-of-birmingham-jsonschema-spectral-rules.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-birmingham-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-birmingham-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-birmingham-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-birmingham-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-birmingham-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Birmingham is a public research university in Birmingham, United Kingdom, a founding member of the Russell Group and of the Universitas 21 network. It operates no central developer portal, publishes no API programme, issues no API keys, and a subdomain sweep of birmingham.ac.uk and bham.ac.uk found nothing at api., data., developer., opendata., open., dev., portal. or git. The programmable footprint it does have is real but decentralised and departmental, and it sits on the institution''s second registrable domain, bham.ac.uk: three EPrints repositories (UBIRA eData, UBIRA eTheses and ePapers) each exposing an OAI-PMH 2.0 provider plus an EPrints REST interface; a Shibboleth SAML 2.0 identity provider registered in the UK Access Management Federation; a self-hosted GitLab on the BEAR research-computing estate whose /api/v4 project listing answers keyless; and one small open research API from the English Constructicon construction-grammar project in the College
  of Arts and Law — the only surface here with an OpenAPI description, and that description is ours, not theirs. Three further surfaces that carry the University''s name are vendor platforms the institution is a tenant on, recorded as tenancies and not as Birmingham engineering: an Elsevier Pure research portal, an Ex Libris Primo library discovery layer, and an Instructure Canvas VLE.'
examples:
- key_count: 9
  name: University Of Birmingham Getconstruction Example
  slug: university-of-birmingham-getConstruction-example
finops:
- name: University Of Birmingham Finops
  service_category: Education
  slug: university-of-birmingham-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-birmingham.png
json_schemas:
- name: Construction
  property_count: 9
  slug: university-of-birmingham-construction
json_structures:
- name: University Of Birmingham Construction Structure
  property_count: 9
  slug: university-of-birmingham-construction-structure
jsonld:
- class_count: 12
  name: University Of Birmingham Context
  property_count: 1
  slug: university-of-birmingham-context
layout: provider
modified: '2026-08-30'
name: University of Birmingham
nav: Providers
network: true
overview: 'University of Birmingham publishes 1 API on the [APIs.io](https://apis.io/) network: English Constructicon API. Tagged areas include Education, Higher Education, University, United Kingdom, and Russell Group.


  The University of Birmingham catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Birmingham''s developer surface includes documentation, API reference, engineering blog, authentication, and 23 more developer resources.'
plans:
- name: University Of Birmingham Plans Pricing
  plan_count: 2
  slug: university-of-birmingham-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: University Of Birmingham Rate Limits
  slug: university-of-birmingham-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Birmingham API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-birmingham-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: University of Birmingham API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 2
  slug: university-of-birmingham-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 53.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 25.0
    contract_quality: 26.5
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 33.4
  provenance:
    agentic_access: derived
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-birmingham/refs/heads/main/screenshots/university-of-birmingham-2026-06-20T200137.png
security:
- kind: authentication
  name: University Of Birmingham Authentication
  slug: university-of-birmingham-authentication
  summary_line: none/saml/bearer · 5 schemes
- kind: domain-security
  name: University Of Birmingham Domain Security
  slug: university-of-birmingham-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-birmingham
tags:
- Education
- Higher Education
- University
- United Kingdom
- Russell Group
- Research
- Research Data
- Open Access
- Repository
- OAI-PMH
- Identity Federation
- Library
- Research Computing
website: https://www.birmingham.ac.uk/
---
