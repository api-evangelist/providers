---
access_model:
  confidence: high
  label: Free · No signup required for public metadata endpoints
  onboarding: self-serve
  pricing: free
  public: true
  source:
  - plans
  - conformance
  trial: false
  try_now: true
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
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: The Zurich Open Repository and Archive (ZORA) is UZH's institutional repository for the peer-reviewed research output of the university. Its OAI-PMH 2.0 interface serves metadata for harvesting with n
  name: ZORA Repository OAI-PMH
  slug: zora-oai
- description: ZORA runs DSpace 8.0 and exposes the standard DSpace REST API (application/hal+json) for programmatic discovery of communities, collections and items representing UZH research output. Community and co
  name: ZORA DSpace REST API
  slug: zora-rest
- description: KlickerUZH is the university's open-source audience-response and interactive-learning platform, developed and hosted by the UZH Department of Banking and Finance. Its backend is a single Apollo GraphQ
  name: KlickerUZH GraphQL API
  slug: klicker-graphql
- description: UZH self-hosts GitLab for research and teaching code. The GitLab v4 REST API is reachable without credentials for public resources — /api/v4/projects returns project metadata anonymously — while /api/
  name: UZH GitLab REST API
  slug: gitlab-api
- description: UZH's SAML 2.0 identity provider is delivered by SWITCH edu-ID as a hosted, UZH-scoped IdP and registered in the SWITCHaai federation with mdui:DisplayName "University of Zurich". The federation metad
  name: University of Zurich Identity Provider (SWITCH edu-ID, tenant)
  slug: eduid-idp
artifact_total: 9
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/uzh-bf/klicker-uzh/blob/v3/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.uzh.ch/en.html
- group: company
  title: ''
  type: About
  url: https://www.uzh.ch/en/about.html
- group: company
  title: ''
  type: Blog
  url: https://www.news.uzh.ch/en.html
- group: operate
  title: ''
  type: Support
  url: https://www.zi.uzh.ch/en/support.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uzh.ch/en/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uzh.ch/en/impressum.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uzh
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uzh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uzh
- group: company
  title: ''
  type: Twitter
  url: https://x.com/UZH_en
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.zora.uzh.ch/
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.aai.switch.ch/metadata.switchaai.xml
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.uzh.ch/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.zi.uzh.ch/en/teaching-and-research/science-it/computing/sciencecluster.html
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uzh.ch/en/explore/basics/ai/recommendations.html
- group: auth
  title: ''
  type: Authentication
  url: https://www.zi.uzh.ch/en/support/identity-access/eduid-faq.html
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-zurich-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-zurich-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-zurich-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-zurich-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-zurich-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Zurich (UZH) is Switzerland''s largest university, founded in 1833, with roughly 28,000 students across seven faculties. UZH operates no central developer portal, publishes no OpenAPI description of its own, and offers no API key or self-service onboarding of any kind. Its real programmable footprint is four institution-run endpoints that speak someone else''s contract: the ZORA repository''s OAI-PMH 2.0 interface and DSpace 8 REST API at www.zora.uzh.ch, the KlickerUZH audience-response GraphQL API at api.klicker.uzh.ch built and run by the Department of Banking and Finance, and a self-hosted GitLab at gitlab.uzh.ch whose v4 REST API answers unauthenticated reads of public projects. Federated identity is a tenancy, not an operation: the UZH SAML entity aai-idp.uzh.ch is UZH''s namespace but its SSO endpoints run on SWITCH''s hosted edu-ID platform at uzh.login.eduid.ch. The course catalogue, the OLAT learning platform and swisscovery library discovery are
  web and SSO surfaces with no documented public API.'
finops:
- name: University Of Zurich Finops
  service_category: Education
  slug: university-of-zurich-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-zurich.png
layout: provider
modified: '2026-08-30'
name: University of Zurich
nav: Providers
network: true
overview: 'University of Zurich publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Public Research University, and Switzerland.


  University of Zurich''s developer surface includes engineering blog, support, GitHub presence, authentication, and 19 more developer resources.'
plans:
- name: University Of Zurich Plans Pricing
  plan_count: 2
  slug: university-of-zurich-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: University Of Zurich Rate Limits
  slug: university-of-zurich-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 4.4
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 30.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-zurich/refs/heads/main/screenshots/university-of-zurich-2026-06-20T200336.png
security:
- kind: domain-security
  name: University Of Zurich Domain Security
  slug: university-of-zurich-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-zurich
tags:
- Education
- Higher Education
- University
- Public Research University
- Switzerland
- Europe
- League of European Research Universities
- Open Access
- Research Repository
- OAI-PMH
- Identity Federation
- GraphQL
- Research Computing
website: https://www.uzh.ch/en.html
---
