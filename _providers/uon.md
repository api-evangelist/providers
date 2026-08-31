---
access_model:
  confidence: high
  label: Free · Affiliation-gated, no self-serve signup
  onboarding: approval
  pricing: free
  public: false
  source:
  - conformance
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
  score: 2.5
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: UON's institutional identity provider, publishing machine-readable SAML 2.0 metadata at a stable URL. entityID https://idp.newcastle.edu.au/idp/shibboleth, shibmd:Scope newcastle.edu.au, SingleSignOnS
  name: University of Newcastle Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: identity-federation
- description: A self-hosted XNAT 1.9.1.1 imaging-informatics platform operated by the university with the Hunter Medical Research Institute, running on UON's own AWS estate in ap-southeast-2 behind the prod-xnat-hm
  name: University of Newcastle XNAT Imaging Informatics Platform
  slug: xnat-imaging
- description: The university's open-access institutional repository and research-data store, running on the Figshare platform at openresearch.newcastle.edu.au. This is a genuine institutional fact and one of the fe
  name: Open Research Newcastle (Figshare) — TENANT
  slug: open-research-figshare
- description: 'The university''s program and course handbook, served from handbook.newcastle.edu.au on the CourseLoop platform. Machine-readable to the extent that it publishes a sitemap index whose child enumerates '
  name: University of Newcastle Course Handbook (CourseLoop) — TENANT
  slug: course-handbook-courseloop
- description: UON's learning management system, an Instructure Canvas tenancy reachable both at canvas.newcastle.edu.au and at newcastle.instructure.com, which return the same page byte for byte. Canvas ships a wel
  name: University of Newcastle Canvas LMS (Instructure) — TENANT
  slug: canvas-lms
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.newcastle.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.newcastle.edu.au/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://xnat.newcastle.edu.au/
- group: other
  title: ''
  type: ResearchRepository
  url: https://openresearch.newcastle.edu.au/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://handbook.newcastle.edu.au/
- group: other
  title: ''
  type: Policies
  url: https://policies.newcastle.edu.au/
- group: docs
  title: ''
  type: Documentation
  url: https://libguides.newcastle.edu.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/university-of-newcastle-research
- group: design
  title: ''
  type: Conformance
  url: conformance/uon-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uon-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uon-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Newcastle (UON) is a public research university in Callaghan and Newcastle, New South Wales, ranked #179 in the QS World University Rankings order used by this cohort. It is a federation of buyers rather than an API producer: there is no central developer portal and no institutional API gateway — api.newcastle.edu.au, apis.newcastle.edu.au, developer.newcastle.edu.au, data.newcastle.edu.au and status.newcastle.edu.au all fail to resolve — and UON publishes no OpenAPI description for anything. What it genuinely operates is small and specific: a Shibboleth identity provider at idp.newcastle.edu.au serving live SAML 2.0 metadata under its own entityID and scope, registered in the Australian Access Federation; and a self-hosted XNAT 1.9.1.1 imaging-informatics platform at xnat.newcastle.edu.au, run with the Hunter Medical Research Institute on the university''s own AWS estate, whose REST API answers on UON''s host and is registered as a SAML service provider in
  the same federation. UON also holds two DataCite repository clients in its own name, ARDCX.UON and UONAU.FIGSHARE. Everything else that looks programmable is a tenancy on someone else''s platform and is recorded as such, never as UON engineering: Open Research Newcastle is a Figshare tenancy, the course handbook is a CourseLoop tenancy, the learning management system is an Instructure Canvas tenancy, library guides are Springshare, site search is Squiz Funnelback, the student portal is PeopleSoft behind Okta, and the service desk is Oracle B2C Service. This profile was corrected on 2026-08-30: ten OpenAPI documents previously held here were Figshare''s generic api.figshare.com/v2 contract, not the university''s, and were removed along with everything derived from them.'
finops:
- name: Uon Finops
  service_category: Education
  slug: uon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uon.png
layout: provider
modified: '2026-08-30'
name: University of Newcastle Australia
nav: Providers
network: true
overview: 'University of Newcastle Australia publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and Australia.


  University of Newcastle Australia''s developer surface includes documentation and 13 more developer resources.'
plans:
- name: Uon Plans Pricing
  plan_count: 2
  slug: uon-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Uon Rate Limits
  slug: uon-rate-limits
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -20.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.5
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/uon/refs/heads/main/screenshots/uon-2026-06-20T200428.png
security:
- kind: domain-security
  name: Uon Domain Security
  slug: uon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uon
tags:
- University
- Higher Education
- Education
- Research
- Australia
- New South Wales
- Identity Federation
- SAML
- Shibboleth
- Research Computing
- Medical Imaging
- Research Repository
- Course Catalog
- DataCite
- Tenant
website: https://www.newcastle.edu.au/
---
