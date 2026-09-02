---
access_model:
  confidence: medium
  label: No public developer programme · open protocol endpoints, otherwise affiliation-gated
  onboarding: unknown
  pricing: free
  public: false
  source:
  - probed
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
api_count: 8
apis:
- description: 'OAI-PMH 2.0 metadata harvesting interface for the UC Research Repository, a self-hosted DSpace 7 institutional repository of theses, dissertations and research outputs. Verified live 2026-08-30: verb='
  name: UC Research Repository OAI-PMH
  slug: research-repository-oai
- description: 'DSpace 7 REST API backing the UC Research Repository, providing programmatic access to communities, collections and items. Re-probed 2026-08-30 with a browser User-Agent: the API root and /server/api/'
  name: UC Research Repository DSpace REST API
  slug: research-repository-rest
- description: An institution-operated enterprise API gateway on the University of Canterbury's own registrable domain. Discovered 2026-08-30. Every probed path (/, /ping, /v1, /swagger) returns HTTP 500 with a SOAP
  name: UC API Gateway
  slug: api-gateway
- description: Three Shibboleth Service Providers run on University of Canterbury hosts and publish machine-readable SAML 2.0 metadata at the standard Shibboleth.sso/Metadata location — LEARN (learn.canterbury.ac.nz
  name: UC Shibboleth SAML 2.0 Service Provider Metadata
  slug: saml-service-providers
- description: 'LEARN, the University of Canterbury''s self-hosted Moodle learning management system, acts as an LTI 1.3 platform and serves a live JSON Web Key Set from the institution''s own host — verified HTTP 200 '
  name: LEARN LTI 1.3 Platform (Moodle)
  slug: lti-platform
- description: 'Self-hosted GitLab instance operated by the University of Canterbury College of Engineering on the institution''s own domain. Re-verified 2026-08-30: the web application redirects to /users/sign_in wit'
  name: UC Engineering GitLab API
  slug: eng-git-gitlab
- description: The University of Canterbury's SAML 2.0 Identity Provider is registered in the signed Tuakiri federation metadata aggregate with entityID https://idp.canterbury.ac.nz/idp/shibboleth and OrganizationDi
  name: Tuakiri Hosted Identity Provider for canterbury.ac.nz
  slug: tuakiri-hosted-idp
- description: canterbury.figshare.com is the University of Canterbury's institutional research data repository, a tenancy on Figshare's platform. The data, the DOIs and the curation are the institution's; the API c
  name: Canterbury Figshare Research Data Repository (tenant)
  slug: figshare-tenant
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.canterbury.ac.nz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uccser
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-canterbury/
- group: build
  title: ''
  type: SourceCode
  url: https://eng-git.canterbury.ac.nz/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canterbury.ac.nz/about-uc/corporate-information/policies/privacy-policy
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.canterbury.ac.nz/study/academic-study/courses
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.canterbury.ac.nz/library
- group: other
  title: ''
  type: ResearchRepository
  url: https://ir.canterbury.ac.nz/
- group: other
  title: ''
  type: IdentityFederation
  url: https://directory.tuakiri.ac.nz/metadata/tuakiri-metadata-signed.xml
- group: design
  title: ''
  type: x-conformance
  url: conformance/university-of-canterbury-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-canterbury-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-canterbury-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-canterbury-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-canterbury-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'University of Canterbury (Te Whare Wananga o Waitaha) is a public research university in Christchurch, Aotearoa New Zealand. It operates no public developer programme, no developer portal and no published, self-serve API: everything machine-readable it runs is infrastructure for a purpose other than being an API product. What is genuinely institution-operated and genuinely readable is narrow — the UC Research Repository (a self-hosted DSpace 7 on ir.canterbury.ac.nz) serves a live OAI-PMH 2.0 interface with thirteen metadata formats, and three Shibboleth Service Providers on canterbury.ac.nz hosts publish valid SAML 2.0 metadata as members of Tuakiri, the New Zealand Access Federation. The rest is gated rather than absent: a CA API Gateway 9.0 answers on api.canterbury.ac.nz with no routed public service, a self-hosted GitLab serves an authenticated v4 API to the College of Engineering, and the DSpace REST API sits behind a Cloudflare bot challenge. The institution''s research
  data repository and its identity provider are both tenancies on other people''s platforms — Figshare and REANNZ''s Tuakiri Hosted IdP respectively — and are recorded here as relationships, not as University of Canterbury contracts. This profile was corrected on 2026-08-30: eleven entries previously listed under this institution were a single Figshare API v2 contract, split by tag, and have been removed.'
finops:
- name: University Of Canterbury Finops
  service_category: Education
  slug: university-of-canterbury-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-canterbury.png
layout: provider
modified: '2026-08-30'
name: University of Canterbury
nav: Providers
network: true
overview: University of Canterbury publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, New Zealand, and Research.
plans:
- name: University Of Canterbury Plans Pricing
  plan_count: 2
  slug: university-of-canterbury-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: University Of Canterbury Rate Limits
  slug: university-of-canterbury-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 8.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 25.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 29.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-canterbury/refs/heads/main/screenshots/university-of-canterbury-2026-06-20T200141.png
security:
- kind: domain-security
  name: University Of Canterbury Domain Security
  slug: university-of-canterbury-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-canterbury
tags:
- Education
- Higher Education
- University
- New Zealand
- Research
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- SAML
- Learning Management
website: https://www.canterbury.ac.nz/
---
