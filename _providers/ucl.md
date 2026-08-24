---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-24'
api_count: 6
apis:
- description: UCL Discovery is UCL's open-access institutional repository of research outputs, running EPrints on UCL's own registrable domain, and it exposes an OAI-PMH 2.0 metadata-harvesting endpoint at discover
  name: UCL Discovery — OAI-PMH
  slug: discovery-oai
- description: The UCL Research Data Repository is UCL's institutional data repository, used to deposit, archive, publish and mint DOIs for research datasets. The data, the curation policy and the DOI prefix (10.552
  name: UCL Research Data Repository (Figshare tenancy)
  slug: research-data-repository
- description: UCL Profiles is UCL's public research-information and researcher-profile directory, successor to the IRIS research portal (iris.ucl.ac.uk now redirects to it). It is a Symplectic Elements Discovery te
  name: UCL Profiles / IRIS (Symplectic Elements tenancy)
  slug: profiles
- description: 'UCL Library Services runs its catalog and discovery layer on Ex Libris Primo VE, at an institution-specific view on Ex Libris'' shared host: ucl.primo.exlibrisgroup.com with vid=44UCL_INST:UCL_VU2. The'
  name: UCL Library Discovery (Ex Libris Primo VE tenancy)
  slug: library-discovery
- description: 'UCL''s website and module-catalogue search runs on Funnelback (Squiz) at search2.ucl.ac.uk, on UCL''s own registrable domain. It is the only surface in this profile that returns a machine-readable JSON '
  name: UCL site search (Funnelback tenancy)
  slug: site-search
- description: UCL is a registered Identity Provider in the UK Access Management Federation (Jisc), and by extension in eduGAIN. Its SAML metadata is published in the federation's machine-readable aggregate under en
  name: UCL Identity Provider — UK Access Management Federation
  slug: identity-federation
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.ucl.ac.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UCL
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uclapi
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/uclapi/uclapi
- group: commercial
  title: ''
  type: License
  url: https://github.com/uclapi/uclapi/blob/master/LICENSE
- group: other
  title: ''
  type: ResearchRepository
  url: https://discovery.ucl.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://rdr.ucl.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ucl.primo.exlibrisgroup.com/discovery/search?vid=44UCL_INST:UCL_VU2
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.ucl.ac.uk/module-catalogue/
- group: other
  title: ''
  type: IdentityFederation
  url: http://metadata.ukfederation.org.uk/ukfederation-metadata.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.rc.ucl.ac.uk/docs/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.ucl.ac.uk/advanced-research-computing
- group: other
  title: ''
  type: AIPolicy
  url: https://www.ucl.ac.uk/teaching-learning/generative-ai-hub
- group: operate
  title: ''
  type: Support
  url: https://www.ucl.ac.uk/isd/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ucl.ac.uk/library/open-science-research-support/research-data-management
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ucl.ac.uk/legal-services/privacy
- group: other
  title: ''
  type: DataProtection
  url: https://www.ucl.ac.uk/data-protection/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/ucl-api
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/uclapi
- group: design
  title: ''
  type: Conformance
  url: conformance/ucl-education-standards-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucl-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ucl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucl-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucl-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'University College London (UCL) is a public research university in London, United Kingdom, and a member of the Russell Group. UCL is the clearest illustration in this cohort of why a university is a federation of buyers rather than a producer of APIs. Its flagship developer surface, UCL API (uclapi.com) — a student-built, ISD-backed, open-source, OAuth2-secured platform exposing room bookings, timetables, staff search, desktop and study-space availability and workspaces — was genuinely UCL''s own engineering, and as of 2026-08-19 its entire estate is gone: uclapi.com, api.uclapi.com, docs.uclapi.com and status.uclapi.com all fail to complete a TCP connection on either port 80 or 443. The source repository remains public and unarchived (github.com/uclapi/uclapi, last pushed 2026-05-06); the OpenAPI repository was archived in 2021. What remains is almost entirely bought, not built. UCL Discovery, the open-access institutional repository, is the one institution-operated machine-readable
  surface left standing: EPrints on UCL''s own domain with an OAI-PMH endpoint, currently behind a Cloudflare challenge. Everything else is a tenancy — the UCL Research Data Repository is Figshare (rdr.ucl.ac.uk CNAMEs to figshare.com, UCL''s data addressed as institution=549 on Figshare''s shared host), UCL Profiles is Symplectic Elements (profiles.ucl.ac.uk CNAMEs to ucl.discovery.symplectic.org), library discovery is Ex Libris Primo VE, site search is Funnelback, and even UCL''s UK Access Management Federation identity provider — the one class of surface a university is supposed to operate by definition — resolves its SAML SSO to OpenAthens rather than to a UCL host. UCL owns the entityID, the ucl.ac.uk scope and the DataCite DOI prefix 10.5522; vendors run the services underneath them. No central developer portal, no open data portal and no publicly callable institution-operated API were found in this pass.'
finops:
- name: Ucl Finops
  service_category: Education
  slug: ucl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucl.png
layout: provider
modified: '2026-08-19'
name: UCL
nav: Providers
network: true
overview: 'UCL publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, United Kingdom, and London.


  UCL''s developer surface includes GitHub presence, support, documentation, engineering blog, and 21 more developer resources.'
plans:
- name: Ucl Plans Pricing
  plan_count: 2
  slug: ucl-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Ucl Rate Limits
  slug: ucl-rate-limits
score:
  band: emerging
  composite: 20.8
  delta: -0.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 21.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 27.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucl/refs/heads/main/screenshots/ucl-2026-06-20T195940.png
security:
- kind: domain-security
  name: Ucl Domain Security
  slug: ucl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ucl
tags:
- Education
- Higher Education
- University
- United Kingdom
- London
- Russell Group
- Research
- Open Access
- Research Data
- Research Repository
- Library
- Identity Federation
- Research Computing
- Course Catalog
website: https://www.ucl.ac.uk/
---
