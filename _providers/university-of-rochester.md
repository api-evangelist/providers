---
access_model:
  confidence: high
  label: Free · Open, no registration
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
    auth_clarity: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://urresearch.rochester.edu/oai2
  baseurl_source: declared
  description: 'OAI-PMH 2.0 metadata harvesting interface for UR Research, the University of Rochester''s legacy institutional repository, served from the university''s own domain and running IR+ — repository software '
  name: UR Research OAI-PMH Interface
  slug: urresearch-oai-pmh
- description: SAML 2.0 / Shibboleth identity provider metadata for the University of Rochester, published machine-readably at its own entityID. The EntityDescriptor carries an IDPSSODescriptor supporting SAML 1.1 a
  name: University of Rochester Shibboleth Identity Provider
  slug: shibboleth-idp
- description: 'URRR is the University of Rochester''s current research data repository. It is a Figshare tenancy: Rochester''s data, Rochester''s DOIs, and Rochester''s curation, on a platform Figshare operates and whos'
  name: University of Rochester Research Repository (URRR) — Figshare tenancy
  slug: urrr-figshare-tenancy
- description: River Campus Libraries discovery runs on Ex Libris Primo VE under the institution-specific view identifier 01ROCH_INST:UR01, hosted at rochester.primo.exlibrisgroup.com. The catalogue and its holdings
  name: University of Rochester Library Discovery — Ex Libris Primo VE tenancy
  slug: primo-discovery-tenancy
artifact_total: 8
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/rochester-rcl/irplus/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.rochester.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://urresearch.rochester.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://rochester.figshare.com/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.rochester.edu/idp/shibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://rochester.primo.exlibrisgroup.com/discovery/search?vid=01ROCH_INST:UR01
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.rochester.edu/registrar/
- group: other
  title: ''
  type: ResearchComputing
  url: https://circ.rochester.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.rochester.edu/ai/
- group: build
  title: ''
  type: AITooling
  url: https://tech.rochester.edu/services/artificial-intelligence/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rochester-rcl
- group: operate
  title: ''
  type: Support
  url: https://tech.rochester.edu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rochester.edu/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rochester.edu/policies/
- group: other
  title: ''
  type: Accessibility
  url: https://www.rochester.edu/accessibility.html
- group: company
  title: ''
  type: Blog
  url: https://www.rochester.edu/newscenter/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.rochester.edu/newscenter/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-rochester/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-rochester-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-rochester-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-rochester-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-rochester-finops.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-rochester-conformance.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Rochester is a private research university in Rochester, New York, and an AAU member, ranked #236 in the QS World University Rankings 2025. It operates no central public developer portal and no public API programme, and its programmable footprint is small, decentralised, and concentrated in the libraries. Two surfaces are genuinely institution-operated and were verified live in August 2026: an OAI-PMH 2.0 metadata harvesting interface at urresearch.rochester.edu/oai2 for UR Research, the legacy institutional repository, which runs on IR+ — repository software the River Campus Libraries themselves wrote and released under Apache 2.0 — and a Shibboleth SAML 2.0 identity provider at idp.rochester.edu publishing scoped federation metadata at its own entityID. Everything else the institution appears to publish is a vendor''s contract running under its name: the University of Rochester Research Repository (URRR) is a Figshare tenancy at rochester.figshare.com and
  library discovery is an Ex Libris Primo VE tenancy at rochester.primo.exlibrisgroup.com. Those tenancies are real institutional facts and are recorded as such, but the contracts describing them belong to Figshare and Ex Libris, not to Rochester. Administrative systems — the student information system, HR, finance, and course/registrar data — are gated behind institutional identity and are not publicly documented. The River Campus Libraries maintain an active public GitHub organisation (rochester-rcl, 112 repositories) of digital-library and preservation tooling, which is the clearest evidence of the institution''s own engineering output.'
finops:
- name: University Of Rochester Finops
  service_category: Education
  slug: university-of-rochester-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-rochester.png
layout: provider
modified: '2026-08-30'
name: University of Rochester
nav: Providers
network: true
overview: 'University of Rochester publishes 1 API on the [APIs.io](https://apis.io/) network: UR Research OAI-PMH Interface. Tagged areas include University, Higher Education, Education, United States, and New York.


  University of Rochester''s developer surface includes GitHub presence, support, engineering blog, and 21 more developer resources.'
plans:
- name: University Of Rochester Plans Pricing
  plan_count: 2
  slug: university-of-rochester-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: University Of Rochester Rate Limits
  slug: university-of-rochester-rate-limits
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 30.7
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
    score: 35.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-rochester/refs/heads/main/screenshots/university-of-rochester-2026-06-20T200223.png
security:
- kind: domain-security
  name: University Of Rochester Domain Security
  slug: university-of-rochester-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-rochester
tags:
- University
- Higher Education
- Education
- United States
- New York
- Private Research University
- Association of American Universities
- Research Repository
- Institutional Repository
- OAI-PMH
- Identity Federation
- Library
- Research Computing
website: https://www.rochester.edu/
---
