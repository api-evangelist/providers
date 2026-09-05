---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
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
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: Yonsei University operates its own SAML 2.0 Identity Provider for KAFE, the Korean Access FEderation, on its own registrable domain. The entity is registered by kafe.kreonet.net and exported to eduGAI
  name: Yonsei University KAFE Identity Provider (SAML 2.0)
  slug: kafe-idp
- description: YUHSpace is the Yonsei University Health System / Medical Library institutional repository, running DSpace 5.5 on Yonsei's own host and built through the National Library of Korea OAK distribution pro
  name: YUHSpace Institutional Repository (DSpace)
  slug: yuhspace
- description: data.yonsei.ac.kr is an institution-operated data portal — "a collection of data resources for Yonsei University members" — on Yonsei's own registrable domain. It is a client-rendered Next.js applicat
  name: Yonsei Data Portal
  slug: data-portal
- description: Yonsei's research information system is an Elsevier Pure (CRIS) tenancy at yonsei.elsevierpure.com. The data is Yonsei's — its researchers, outputs, projects and organizational units — but the contrac
  name: Yonsei Research Information Portal (Elsevier Pure tenancy)
  slug: elsevier-pure
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.yonsei.ac.kr/
- group: company
  title: ''
  type: Website
  url: https://www.yonsei.ac.kr/en_sc/index.do
- group: other
  title: ''
  type: IdentityFederation
  url: https://kafe.yonsei.ac.kr/
- group: other
  title: ''
  type: ResearchRepository
  url: https://ir.ymlib.yonsei.ac.kr/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.yonsei.ac.kr/
- group: other
  title: ''
  type: OpenData
  url: https://data.yonsei.ac.kr/
- group: other
  title: ''
  type: AIPolicy
  url: https://yure.yonsei.ac.kr/admin/info/adminBookDetail.do?book_seq=65
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gdg-yonsei
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/yonsei/
- group: design
  title: ''
  type: Conformance
  url: conformance/yonsei-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yonsei-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/yonsei-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yonsei-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yonsei-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Yonsei publishes no institution-operated REST API and no developer portal. The only complete API contract discoverable under its name is Elsevier''s Pure API, served from the tenant host yonsei.elsevierpure.com: the specification at /ws/api/openapi.json is publicly readable (HTTP 200, ~1.7MB) but every data endpoint returns 401 and the Pure OAI-PMH feed at /ws/oai returns 401 as well. The 37 per-tag OpenAPIs previously stored in this repo were splits of that one Elsevier document and have been removed. The institution''s own machine-readable surfaces are a SAML 2.0 IdP registered in KAFE and eduGAIN, and DSpace RSS/Atom feeds reachable only after satisfying a JS bot challenge. The medical-library repository has no OAI-PMH webapp deployed (404 on /oai/request, /dspace-oai/request and /oai/driver). Yonsei''s generative-AI guideline exists only in Korean, on yure.yonsei.ac.kr, and was found by searching in the local language.'
  evidence:
  - note: Elsevier's Pure API spec, publicly readable — vendor-authored, tenant-served.
    status: 200
    url: https://yonsei.elsevierpure.com/ws/api/openapi.json
  - note: application/problem+json — "Full authentication is required to access this resource"
    status: 401
    url: https://yonsei.elsevierpure.com/ws/api/research-outputs?size=1
  - note: Pure OAI-PMH, credential-gated.
    status: 401
    url: https://yonsei.elsevierpure.com/ws/oai?verb=Identify
  - note: Yonsei-operated KAFE federated-authentication server; page states in Korean that Yonsei University operates it.
    status: 200
    url: https://kafe.yonsei.ac.kr/
  - note: eduGAIN entity https://kafe.yonsei.ac.kr/idp/simplesamlphp — IDPSSODescriptor, federation KAFE, scope yonsei.ac.kr, Sirtfi declared.
    status: 200
    url: https://technical.edugain.org/api.php?action=list_entities&format=json
  - note: JS bot challenge on first request (sets a js-challenge cookie); YUHSpace DSpace 5.5 home page served once the cookie is replayed. Live, not dead.
    status: 200
    url: https://ir.ymlib.yonsei.ac.kr/
  - note: Real RSS 2.0 XML behind the challenge cookie.
    status: 200
    url: https://ir.ymlib.yonsei.ac.kr/feed/rss_2.0/site
  - note: No OAI-PMH webapp deployed on the institution's own repository host.
    status: 404
    url: https://ir.ymlib.yonsei.ac.kr/oai/request?verb=Identify
  - note: Yonsei Data Portal, institution-operated Next.js app for Yonsei members only; /api, /openapi.json, /llms.txt all 404.
    status: 200
    url: https://data.yonsei.ac.kr/
  - note: GeoIP redirect shell that lands on /sc/index.do (KR) or /en_sc/index.do.
    status: 200
    url: https://www.yonsei.ac.kr/
  - note: Library website; robots.txt disallows all but a handful of notice-board paths. No API found.
    status: 200
    url: https://library.yonsei.ac.kr/
  reason: tenant_only
  state: gated
created: '2026-06-03'
description: 'Yonsei University (연세대학교) is a private research university in Seoul, South Korea, founded in 1885 and one of the "SKY" institutions. Its programmable footprint is small, and most of what previously appeared under its name was not its own engineering: the Yonsei Research Information portal at yonsei.elsevierpure.com is an Elsevier Pure (CRIS) tenancy whose OpenAPI is authored by Elsevier — info.title "Pure API", contact pure-support@elsevier.com — and whose data endpoints and OAI-PMH feed both return HTTP 401 to the public. That relationship is recorded here as a tenant surface; the contract itself belongs to Elsevier and has been removed from this repo. What Yonsei genuinely operates is narrower and more interesting: a SAML 2.0 Identity Provider on its own domain (kafe.yonsei.ac.kr) registered in the Korean Access FEderation and exported to eduGAIN with the scope yonsei.ac.kr and a Sirtfi declaration; a DSpace 5.5 medical-library repository (YUHSpace) at ir.ymlib.yonsei.ac.kr
  serving public RSS 2.0 and Atom 1.0 feeds from behind a JavaScript bot challenge, with no OAI-PMH deployed; and a members-only Yonsei Data Portal at data.yonsei.ac.kr that ships no public API. There is no central developer portal, no institution-operated REST API, and no official institutional GitHub organization — the only GitHub presence is GDGoC Yonsei, a student Google Developer Group. The institutional AI posture is a governance document, not an API, and it exists only on the Korean surface.'
finops:
- name: Yonsei Finops
  service_category: Education
  slug: yonsei-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yonsei.png
layout: provider
modified: '2026-08-30'
name: Yonsei University
nav: Providers
network: true
overview: Yonsei University publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Private Research University, and South Korea.
plans:
- name: Yonsei Plans Pricing
  plan_count: 2
  slug: yonsei-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Yonsei Rate Limits
  slug: yonsei-rate-limits
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 54.0
    catalog_earned_first_party: 0.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 4.4
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yonsei/refs/heads/main/screenshots/yonsei-2026-06-20T201758.png
security:
- kind: domain-security
  name: Yonsei Domain Security
  slug: yonsei-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yonsei
tags:
- University
- Higher Education
- Education
- Private Research University
- South Korea
- Seoul
- Research
- Research Repository
- Identity Federation
- Library
- Open Data
website: https://www.yonsei.ac.kr/
---
