---
access_model:
  confidence: high
  label: Free · Open repository, Matrix, WordPress and GitLab reads; FAU API and CRIS are credentialed
  onboarding: unknown
  pricing: free
  public: true
  source:
  - conformance/friedrich-alexander-universitat-erlangen-nurnberg-conformance.yml
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
  scored_at: '2026-09-05'
api_count: 9
apis:
- description: 'Open Archives Initiative Protocol for Metadata Harvesting 2.0 service for OPEN FAU, the university''s open-access publication repository. Verified live on 2026-08-30: Identify returns repositoryName "O'
  name: OPEN FAU OAI-PMH Metadata Service
  slug: open-fau-oai
- description: 'The REST/HAL API of OPEN FAU, FAU''s DSpace 7.4 institutional repository, run by the University Library on FAU''s own host. Verified live on 2026-08-30: the API root at /server/api returns dspaceName "O'
  name: OPEN FAU DSpace REST API
  slug: open-fau-rest
- description: 'FAU operates a Matrix homeserver — Synapse 1.159.0 at matrix.fau.de — with a hosted Element web client at chat.fau.de. It is properly delegated: both https://fau.de/.well-known/matrix/client and https'
  name: FAU Matrix Homeserver
  slug: matrix-homeserver
- description: FAU's central web single sign-on, operated by RRZE, publishes SAML 2.0 identity provider metadata as a machine-readable document at https://www.sso.uni-erlangen.de/simplesaml/saml2/idp/metadata.php, m
  name: FAU WebSSO SAML 2.0 Identity Provider
  slug: websso-saml
- description: 'FAU''s central web platform is a WordPress estate run by the RRZE Webteam, and its REST API is partly open to anonymous callers. Verified live on 2026-08-30: https://www.fau.de/wp-json/wp/v2/posts retu'
  name: FAU Web Platform WordPress REST API
  slug: wordpress-rest
- description: 'RRZE runs FAU''s self-hosted GitLab at gitlab.rrze.fau.de, and its v4 REST API answers anonymous reads. Verified live on 2026-08-30: /api/v4/projects?per_page=1 returns HTTP 200 with real project JSON '
  name: RRZE GitLab REST API (FAU self-hosted)
  slug: gitlab-api
- description: api.fau.de is an FAU-operated API portal — the browser title is "FAU API", the single-page application is served from FAU's own network, and its footer links to rrze.fau.de and www.fau.de. It is gated
  name: FAU API Gateway (api.fau.de)
  slug: fau-api-gateway
- description: NHR@FAU — the Erlangen National High Performance Computing Center, hosted by FAU — runs ClusterCockpit at monitoring.nhr.fau.de as the job-specific performance monitoring service for its clusters, alo
  name: NHR@FAU ClusterCockpit Job Monitoring API
  slug: clustercockpit-nhr
- description: FAU CRIS is the university's research information system, holding 146,000+ publications and 5,200+ projects and syndicating data to more than a thousand FAU websites. The data is FAU's; the CONTRACT i
  name: Clarivate Converis Web Service — FAU CRIS deployment
  slug: cris-converis-ws
artifact_total: 15
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/ClusterCockpit/cc-backend/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.fau.de/
- group: company
  title: ''
  type: Website
  url: https://www.fau.eu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://ub.fau.de/en/research/open-fau/
- group: other
  title: ''
  type: ResearchRepository
  url: https://cris.fau.de/
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.sso.uni-erlangen.de/simplesaml/saml2/idp/metadata.php
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.fau.de/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.nhr.fau.de/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.campo.fau.de/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ub.fau.de/
- group: other
  title: ''
  type: OpenData
  url: https://open.fau.de/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RRZE-Webteam
- group: build
  title: ''
  type: GitHub
  url: https://github.com/FAU-CDI
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RRZE-HPC
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.rrze.fau.de/
- group: auth
  title: ''
  type: Authentication
  url: https://sso.fau.de/
- group: start
  title: ''
  type: Portal
  url: https://www.sso.uni-erlangen.de/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.fau.de/.well-known/security.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fau.de/datenschutz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fau.de/impressum/
- group: operate
  title: ''
  type: Support
  url: https://www.rrze.fau.de/
- group: design
  title: ''
  type: x-conformance
  url: conformance/friedrich-alexander-universitat-erlangen-nurnberg-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/friedrich-alexander-universitat-erlangen-nurnberg-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/friedrich-alexander-universitat-erlangen-nurnberg-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/friedrich-alexander-universitat-erlangen-nurnberg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/friedrich-alexander-universitat-erlangen-nurnberg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/friedrich-alexander-universitat-erlangen-nurnberg-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU) is a public research university in Erlangen and Nuremberg, Bavaria, Germany, founded in 1743 and one of Germany''s largest, with around 39,000 students across five faculties. FAU operates no central developer portal and publishes no OpenAPI definition of its own — but unlike most of this cohort its programmable footprint is real, and every surface in it runs on FAU''s own infrastructure: every host recorded below resolves inside FAU''s own 131.188.0.0/16 network, and not one of them CNAMEs to a vendor. The institution-operated, publicly readable surfaces verified live on 2026-08-30 are the OPEN FAU institutional repository on DSpace 7.4, which serves both a REST/HAL API and a fully functional OAI-PMH 2.0 harvesting endpoint with eight metadata crosswalks; a Matrix (Synapse 1.159.0) homeserver at matrix.fau.de, correctly delegated from .well-known/matrix/server and .well-known/matrix/client on fau.de, which makes FAU''s
  chat service reachable by any standards-conformant Matrix client; the WordPress REST API behind the RRZE-operated FAU web platform, where the /wp-json index and search route are restricted but the wp/v2 content collections return real JSON on www.fau.de and a complete route index on ub.fau.de; and anonymous read access to the GitLab v4 REST API on FAU''s self-hosted GitLab at gitlab.rrze.fau.de, which reports 132 public projects. Three further surfaces are live but gated: the FAU API gateway at api.fau.de, which fronts an authenticated API router behind SSO; the ClusterCockpit HPC job-monitoring REST API at monitoring.nhr.fau.de, run by NHR@FAU, the national high-performance computing centre FAU hosts; and the Clarivate Converis web service on cris.fau.de, which is FAU''s research information system and returns HTTP 403 on its public web-service paths. FAU also operates a SAML 2.0 identity provider registered in the DFN-AAI federation, mints DOIs under its own DataCite prefix 10.25593,
  and maintains three active public GitHub organisations plus a self-hosted GitLab. No vendor contract is saved in this repository under FAU''s name: where the software beneath a surface is someone else''s product, the profile says so and keeps no copy of that product''s specification.'
finops:
- name: Friedrich Alexander Universitat Erlangen Nurnberg Finops
  service_category: Education
  slug: friedrich-alexander-universitat-erlangen-nurnberg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/friedrich-alexander-universitat-erlangen-nurnberg.png
jsonld:
- class_count: 15
  name: Friedrich Alexander Universitat Erlangen Nurnberg Context
  property_count: 7
  slug: friedrich-alexander-universitat-erlangen-nurnberg-context
layout: provider
modified: '2026-08-30'
name: Friedrich-Alexander-Universität Erlangen-Nürnberg
nav: Providers
network: true
overview: 'Friedrich-Alexander-Universität Erlangen-Nürnberg publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and Research Repository.


  The Friedrich-Alexander-Universität Erlangen-Nürnberg catalog on APIs.io includes 1 JSON-LD context.


  Friedrich-Alexander-Universität Erlangen-Nürnberg''s developer surface includes documentation, GitHub presence, authentication, developer portal, support, and 23 more developer resources.'
plans:
- name: Friedrich Alexander Universitat Erlangen Nurnberg Plans Pricing
  plan_count: 2
  slug: friedrich-alexander-universitat-erlangen-nurnberg-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Friedrich Alexander Universitat Erlangen Nurnberg Rate Limits
  slug: friedrich-alexander-universitat-erlangen-nurnberg-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 35.7
    discoverability: 85.2
    governance: 0.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 37.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/friedrich-alexander-universitat-erlangen-nurnberg/refs/heads/main/screenshots/friedrich-alexander-universitat-erlangen-nurnberg-2026-06-20T181545.png
security:
- kind: domain-security
  name: Friedrich Alexander Universitat Erlangen Nurnberg Domain Security
  slug: friedrich-alexander-universitat-erlangen-nurnberg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Friedrich Alexander Universitat Erlangen Nurnberg Vulnerability Disclosure
  slug: friedrich-alexander-universitat-erlangen-nurnberg-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: friedrich-alexander-universitat-erlangen-nurnberg
tags:
- University
- Higher Education
- Education
- Research
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Research Computing
- Matrix
- Germany
- Bavaria
- Europe
website: https://www.fau.de/
---
