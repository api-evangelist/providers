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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Hanyang University's own Open API platform, built and run by the university rather than bought from a vendor. REST endpoints under https://api.hanyang.ac.kr/rs/ return XML or JSON, selected by file ex
  name: Hanyang University Open API Developer Center
  slug: developer-center
- baseURL: https://repository.hanyang.ac.kr/oai/request
  baseurl_source: declared
  description: OAI-PMH 2.0 metadata-harvesting interface on Hanyang's institutional DSpace repository, plus an OpenSearch 1.1 descriptor and RSS/Atom feeds. Twelve metadata formats are advertised (oai_dc, qdc, mods,
  name: Repository at Hanyang University — OAI-PMH
  slug: repository-oai-pmh
- description: Software development kits published by the Hanyang University Developer Center for building against the Open APIs — Android and iOS SDKs and server-side sample integrations (ASP) that handle the OAuth
  name: Hanyang University Open API SDKs
  slug: sdk
- description: Hanyang University's current research information system and research-output portal, run as a tenancy on the Bwise ScholarWorks platform, one instance per campus. Linked from the university's own home
  name: Hanyang ScholarWorks (research-output tenancy)
  slug: scholarworks
- description: 'Online submission and access for Hanyang University theses and dissertations, hosted on the KERIS dCollection platform. Recorded as a relationship only; no public machine-readable interface was found '
  name: Hanyang dCollection (thesis and dissertation tenancy)
  slug: dcollection
- description: 'Hanyang registers DOIs through Crossref at the research-institute level rather than centrally. Members and prefixes verified on 2026-09-01: Hanyang University College of Medicine (4423, 10.7599), Musi'
  name: Crossref DOI registration (institute-level memberships)
  slug: crossref
- description: Research Organization Registry identifier for Hanyang University, the stable machine-readable identity other systems resolve the institution by.
  name: ROR registration
  slug: ror
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.hanyang.ac.kr/web/eng
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.hanyang.ac.kr/develop/start.page
- group: docs
  title: ''
  type: Documentation
  url: https://api.hanyang.ac.kr/develop/guide.page
- group: auth
  title: ''
  type: Authentication
  url: https://api.hanyang.ac.kr/develop/auths.page
- group: auth
  title: ''
  type: Authentication
  url: authentication/hanyang-open-api-authentication.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.hanyang.ac.kr/member/join_step01.page
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://portal.hanyang.ac.kr/PiopAct/piopMainDaepyoWeb.do
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.hanyang.ac.kr/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.hanyang.ac.kr/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://portal.hanyang.ac.kr/sugang/sulg.do
- group: company
  title: ''
  type: Blog
  url: https://blog.naver.com/hanyang-univ
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hanyang-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hanyang-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hanyang-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hanyang-finops.yml
- group: design
  title: ''
  type: Errors
  url: errors/hanyang-open-api-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hanyang-education-standards-conformance.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: Hanyang runs a real, institution-built Open API programme, but its API catalogue is behind a developer-center member account. /api/search.page returns HTTP 200 with the detail template rendered and no rows; /develop/console.page, /notice/list.page and /board/list.page all return the login form instead of content; app keys require manual administrator approval. The public documentation pages (getting started, authentication, error codes, app registration, Android/iOS SDKs, terms of service) are readable and were the source for the authentication, errors and rate-limit artifacts in this repo, but no endpoint, no scope name and no machine-readable contract can be enumerated from outside. The one openly callable institution-operated API found is the OAI-PMH interface on the university's own DSpace host, and it returns noRecordsMatch to every harvest request. Nothing here is blocked at our end; every probe below ran and returned.
  evidence:
  - status: 200
    url: https://api.hanyang.ac.kr/develop/start.page
  - status: 200
    url: https://api.hanyang.ac.kr/api/search.page
  - status: 200
    url: https://api.hanyang.ac.kr/develop/console.page
  - status: 200
    url: https://api.hanyang.ac.kr/develop/auths.page
  - status: 200
    url: https://api.hanyang.ac.kr/develop/errorcode.page
  - status: 404
    url: https://api.hanyang.ac.kr/openapi.json
  - status: 404
    url: https://api.hanyang.ac.kr/.well-known/oauth-authorization-server
  - status: 200
    url: https://repository.hanyang.ac.kr/oai/request?verb=Identify
  - status: 200
    url: https://repository.hanyang.ac.kr/oai/request?verb=ListIdentifiers&metadataPrefix=oai_dc
  - status: 404
    url: https://www.hanyang.ac.kr/llms.txt
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'Hanyang University is a private research university in Seoul and Ansan (ERICA), South Korea, ROR https://ror.org/046865y68. Unusually for this cohort it operates a genuine, institution-built API programme rather than a set of vendor tenancies: the HYU Open API Developer Center at api.hanyang.ac.kr publishes REST endpoints returning XML or JSON across twelve service categories (academic records, campus life, administration, research, careers, library, alumni giving, volunteering and more), backed by its own OAuth 2.0 authorization server, Android and iOS SDKs, an API console, a developer community and a full published error-code table. The catch is that the API catalogue itself is member-only: /api/search.page renders an empty template to anonymous visitors and app keys are issued only after manual administrator approval, so no endpoint list, scope list or machine-readable contract is publicly enumerable. The one openly callable institution-operated API is the OAI-PMH 2.0 interface
  on Hanyang''s own DSpace repository at repository.hanyang.ac.kr, which answers Identify, ListMetadataFormats and ListSets correctly but returned noRecordsMatch to every harvest request probed. Its research-output and thesis surfaces are vendor tenancies (ScholarWorks/Bwise, KERIS dCollection), it registers DOIs through eight institute-level Crossref memberships rather than centrally, and it publishes no SAML identity-provider metadata to KAFE or eduGAIN while eleven of its Korean peers do.'
finops:
- name: Hanyang Finops
  service_category: Education
  slug: hanyang-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hanyang.png
jsonld:
- class_count: 10
  name: Hanyang Context
  property_count: 7
  slug: hanyang-context
layout: provider
modified: '2026-09-01'
name: Hanyang University
nav: Providers
network: true
overview: 'Hanyang University publishes 1 API on the [APIs.io](https://apis.io/) network: Repository at Hanyang University — OAI-PMH. Tagged areas include Education, Higher Education, University, South Korea, and Seoul.


  The Hanyang University catalog on APIs.io includes 1 JSON-LD context.


  Hanyang University''s developer surface includes documentation, authentication, engineering blog, and 15 more developer resources.'
plans:
- name: Hanyang Plans Pricing
  plan_count: 2
  slug: hanyang-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Hanyang Rate Limits
  slug: hanyang-rate-limits
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 48.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 22.0
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.4
  provenance:
    conformance: derived
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hanyang/refs/heads/main/screenshots/hanyang-2026-06-20T182515.png
security:
- kind: authentication
  name: Hanyang Open Api Authentication
  slug: hanyang-open-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hanyang Domain Security
  slug: hanyang-domain-security
  summary_line: TLSv1.2
slug: hanyang
tags:
- Education
- Higher Education
- University
- South Korea
- Seoul
- Research Repository
- OAI-PMH
- Authentication
- OpenAPI
website: https://www.hanyang.ac.kr/web/eng
---
