---
access_model:
  confidence: high
  label: Free · Institutional affiliation or federation membership required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - identity-federation
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: Monash Agentic Access
  operation_count: 157
  slug: monash-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 8
apis:
- description: Monash's federated login, published as a signed SAML 2.0 EntityDescriptor at https://idp.monash.edu.au/idp/shibboleth (HTTP 200, application/xml). Declares HTTP-POST and HTTP-Redirect SSO bindings, se
  name: Monash University Identity Provider (AAF Rapid IdP tenant)
  slug: idp
- description: A second Monash-operated SAML service provider, entityID https://hpc.erc.monash.edu.au/shibboleth, registered in the Australian Access Federation under Organization "Monash University". The entityID d
  name: Monash eResearch Center HPC ID (SAML Service Provider)
  slug: eresearch-hpc-sp
- description: 'Monash eResearch operates the Cloud Resource Allocation and Management System (CRAMS), an institutional portal for managing research cloud resource allocations. The host responds HTTP 200 with a real '
  name: CRAMS API (Cloud Resource Allocation and Management System)
  slug: crams
- description: Public documentation for the compute, storage, application and training services Monash eResearch runs, including the M3 and MonARCH HPC clusters. massive.org.au, www.massive.org.au and docs.massive.o
  name: Monash eResearch Documentation (M3 / MASSIVE)
  slug: eresearch-docs
- description: Monash's institutional research data repository, "Bridges", operating on the Figshare platform. bridges.monash.edu and monash.figshare.com both resolve as CNAMEs to figshare.com. The data, the collect
  name: Bridges — Monash Research Repository (Figshare tenant)
  slug: bridges
- description: Monash's research outputs, profiles and publication metadata portal, running on Elsevier Pure. research.monash.edu resolves as a CNAME chain to monash.elsevierpure.com and then to apac.prod.elsevierpu
  name: Monash Research Portal (Elsevier Pure tenant)
  slug: pure
- description: The official Monash course, unit and area-of-study catalog. The site is a Next.js application on Monash's own hostname, but its runtime configuration (window.__SITE_ENV_CONFIG__) points every data cal
  name: Monash University Handbook (CourseLoop tenant)
  slug: handbook
- description: 'Monash Library''s discovery layer. search.lib.monash.edu redirects to monash.primo.exlibrisgroup.com/discovery/search?vid=61MONASH_AU:MONUI — a Monash-specific view code on Ex Libris''s Primo platform. '
  name: Monash Library Discovery (Ex Libris Primo tenant)
  slug: library-discovery
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Figshare altmetric API
  slug: open-monash-altmetric-api
- collection_type: open
  name: Figshare altmetric articles API
  slug: open-monash-articles-api
- collection_type: open
  name: Figshare altmetric authors API
  slug: open-monash-authors-api
- collection_type: open
  name: Figshare altmetric collections API
  slug: open-monash-collections-api
- collection_type: open
  name: Figshare altmetric institutions API
  slug: open-monash-institutions-api
- collection_type: open
  name: Figshare altmetric oauth API
  slug: open-monash-oauth-api
- collection_type: open
  name: Figshare altmetric other API
  slug: open-monash-other-api
- collection_type: open
  name: Figshare altmetric profiles API
  slug: open-monash-profiles-api
- collection_type: open
  name: Figshare altmetric projects API
  slug: open-monash-projects-api
- collection_type: open
  name: Figshare altmetric symplectic API
  slug: open-monash-symplectic-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.monash.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/monash-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/monash-conformance.yml
- group: other
  title: ''
  type: ResearchComputing
  url: https://docs.erc.monash.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://bridges.monash.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.lib.monash.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://handbook.monash.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.monash.edu/ai/tools-training-and-resources/ai-policies-and-guidelines
- group: other
  title: ''
  type: Research
  url: https://research.monash.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/monash-university
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/MonashStudentInnovation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/monash-university/
- group: auth
  title: ''
  type: TrustCenter
  url: security/monash-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monash-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/monash-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/monash-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/monash-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Monash University is a public research university in Melbourne, Australia, and a member of the Group of Eight. Its genuinely institution-operated programmable footprint is small but real, and it is not where a company''s would be. Its three institution-operated surfaces all belong to Monash eResearch and all resolve into Monash''s own APNIC address space: the Cloud Resource Allocation and Management System (CRAMS) portal, a public documentation site for the M3/MASSIVE HPC estate, and a Shibboleth service provider federated through the Australian Access Federation. None of the three publishes an open specification, so Monash''s only evidenced domain-standard conformance (SAML, Shibboleth) rests on that one federation entry. The Monash-branded identity provider at idp.monash.edu.au looks like the strongest contract here and is not Monash''s: it CNAMEs to idp-cname.aaf.edu.au on Amazon address space, making it a tenant of AAF''s fully managed Rapid IdP. Everything else that looks
  like a Monash API is a vendor platform running under a Monash hostname: the Bridges research repository is Figshare (bridges.monash.edu is a CNAME to figshare.com), research.monash.edu is Elsevier Pure, the Handbook course catalog runs on CourseLoop, and library discovery is Ex Libris Primo. Those are recorded here as tenant relationships, not as Monash contracts. No central institutional developer portal, no open data portal, and no institution-operated OAI-PMH endpoint were found.'
finops:
- name: Monash Finops
  service_category: Education
  slug: monash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monash.png
layout: provider
modified: '2026-08-19'
name: Monash University
nav: Providers
network: true
overview: 'Monash University publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Australia.


  Monash University''s developer surface includes GitHub presence and 17 more developer resources.'
plans:
- name: Monash Plans Pricing
  plan_count: 2
  slug: monash-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Monash Rate Limits
  slug: monash-rate-limits
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 3.8
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.3
  provenance:
    agentic_access: derived
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 29.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monash/refs/heads/main/screenshots/monash-2026-06-20T185718.png
security:
- kind: domain-security
  name: Monash Domain Security
  slug: monash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Monash Trust Center
  slug: monash-trust-center
  summary_line: ISO 27001, PCI DSS
slug: monash
tags:
- Education
- Higher Education
- University
- Research
- Australia
- Group of Eight
- Identity Federation
- Research Computing
- Research Repository
- Course Catalog
website: https://www.monash.edu/
---
