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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Public REST/search API for the Brown Digital Repository, the library's platform for gathering, indexing, storing, preserving, and making available digital assets from scholarly, instructional, researc
  name: Brown Digital Repository (BDR) API
  slug: bdr-api
- description: IIIF (International Image Interoperability Framework) image and presentation service exposing IIIF manifests for objects in the Brown Digital Repository. Brown is listed as a IIIF repository case stud
  name: Brown Digital Repository IIIF Service
  slug: iiif
- description: Brown's InCommon-federated Shibboleth identity provider implementing the OASIS SAML 2.0 standard for web single sign-on across Brown web services. Used for authentication/attribute release rather than
  name: Brown Shibboleth Single Sign-On (SAML)
  slug: sso
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brown-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brown.edu
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Brown-University-Library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/brown-university/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://repository.library.brown.edu/studio/api-docs/
- group: auth
  title: ''
  type: Authentication
  url: https://sso.brown.edu/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/brown-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brown-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brown-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Brown University is a private Ivy League research university in Providence, Rhode Island, ranked #57 in the QS World University Rankings 2025. Its public developer and API footprint is centered on the Brown University Library, which operates the Brown Digital Repository (BDR) with a documented public REST/search API and a IIIF (International Image Interoperability Framework) image and presentation service. Brown also runs an InCommon-federated Shibboleth/SAML single sign-on identity service and maintains an active "Brown University Library" GitHub organization with hundreds of open-source repositories. Most institutional systems (SIS, course catalog, internal services) are gated behind Brown authentication and are not publicly documented APIs.'
finops:
- name: Brown Finops
  service_category: Education
  slug: brown-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brown.png
jsonld:
- class_count: 18
  name: Brown Context
  property_count: 7
  slug: brown-context
layout: provider
modified: '2026-06-03'
name: Brown University
nav: Providers
network: true
overview: 'Brown University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Brown University catalog on APIs.io includes 1 JSON-LD context.


  Brown University''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: Brown Plans Pricing
  plan_count: 2
  slug: brown-plans-pricing
random_paper: 105
rate_limits:
- limit_count: 1
  name: Brown Rate Limits
  slug: brown-rate-limits
score:
  band: emerging
  composite: 23.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brown/refs/heads/main/screenshots/brown-2026-06-20T173721.png
security:
- kind: domain-security
  name: Brown Domain Security
  slug: brown-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brown
tags:
- Education
- Higher Education
- University
- Research
- Library
- Digital Repository
- IIIF
- United States
website: https://www.brown.edu
---
