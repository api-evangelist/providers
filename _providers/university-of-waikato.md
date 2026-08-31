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
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: 'DSpace 7.6.5 REST API for the University of Waikato''s Research Commons open access institutional repository, providing programmatic access to communities, collections, items, bitstreams and discovery '
  name: Research Commons REST API
  slug: research-commons-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for Research Commons. An Identify request returns repositoryName "Research Commons" with baseURL https://researchcommons.waikato.ac.nz/server/oai/request and a
  name: Research Commons OAI-PMH
  slug: research-commons-oai
- description: REST API operated by University of Waikato IT Services for creating and managing one-time secrets that can be shared securely and retrieved only once before being deleted. All requests use JSON over H
  name: One-Time Secret (OTS) API
  slug: ots
- description: JSON REST API for the University of Waikato's User-friendly Deep Learning (UFDL) framework, developed by the Faculty of Computing and Mathematical Sciences to make deep learning more accessible to dom
  name: User-friendly Deep Learning (UFDL) API
  slug: ufdl
- description: Campus single sign-on / identity provider service hosted at api.svc.waikato.ac.nz under the uowidp path. The v1 login endpoint resolved live during review and serves a University of Waikato sign-in in
  name: University of Waikato Identity Provider (uowidp)
  slug: identity
artifact_total: 10
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Waikato/waikato-repositories/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-waikato-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.waikato.ac.nz/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Waikato
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universityofwaikato/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/waikato
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Waikato/waikato-repositories
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-waikato-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-waikato-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-waikato-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Waikato (Te Whare Wananga o Waikato) is a public research university in Hamilton, New Zealand, founded in 1964 and ranked #235 in the QS World University Rankings 2025. Its publicly observable developer/API footprint is anchored by its DSpace 7.6.5 institutional repository, Research Commons, which exposes a documented REST API and an OAI-PMH 2.0 interface, alongside operational APIs run by IT Services (a One-Time Secret API and a campus identity/SSO provider) and research-software APIs from its Computing and Mathematical Sciences faculty (notably the User-friendly Deep Learning framework). There is no single consolidated developer portal; most APIs are service-specific and several require institutional accounts.'
finops:
- name: University Of Waikato Finops
  service_category: Education
  slug: university-of-waikato-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-waikato.png
jsonld:
- class_count: 18
  name: University Of Waikato Context
  property_count: 4
  slug: university-of-waikato-context
layout: provider
modified: '2026-06-03'
name: University of Waikato
nav: Providers
network: true
overview: 'University of Waikato publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Institutional Repository.


  The University of Waikato catalog on APIs.io includes 1 JSON-LD context.


  University of Waikato''s developer surface includes GitHub presence and 10 more developer resources.'
plans:
- name: University Of Waikato Plans Pricing
  plan_count: 2
  slug: university-of-waikato-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of Waikato Rate Limits
  slug: university-of-waikato-rate-limits
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 0.0
  previous_composite: 21.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-waikato/refs/heads/main/screenshots/university-of-waikato-2026-06-20T200327.png
security:
- kind: domain-security
  name: University Of Waikato Domain Security
  slug: university-of-waikato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-waikato
tags:
- Education
- Higher Education
- University
- Research
- Institutional Repository
- Open Access
- New Zealand
website: https://www.waikato.ac.nz/
---
