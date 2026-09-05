---
access_model:
  confidence: high
  label: Free · OAI-PMH and SRU harvesting are open and keyless; Primo and Pure REST are keyed
  onboarding: unknown
  pricing: free
  public: true
  source:
  - conformance/tel-aviv-university-conformance.yml
  trial: false
  try_now: true
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
api_count: 5
apis:
- description: 'Open Archives Initiative Protocol for Metadata Harvesting 2.0 service for the Tel Aviv University library record, served from TAU''s Ex Libris Alma tenant. Verified live and keyless on 2026-08-30: Iden'
  name: TAU Libraries Alma OAI-PMH Metadata Harvesting
  slug: alma-oai-pmh
- description: 'SRU (Search/Retrieve via URL) 1.2 search service over the Tel Aviv University library catalogue, served from TAU''s Ex Libris Alma tenant. Verified live and keyless on 2026-08-30: operation=explain ret'
  name: TAU Libraries Alma SRU Search
  slug: alma-sru
- description: Tel Aviv University's current research information system is Elsevier Pure, published as the TAU Research Portal at cris.tau.ac.il. The host sits on TAU's own registrable domain but CNAMEs to telaviv.
  name: TAU Research Portal (Elsevier Pure) OAI-PMH
  slug: cris-oai-pmh
- description: Tel Aviv University Libraries run Ex Libris Primo VE for catalogue discovery, branded "DaTA Search", institution code 972TAU_INST:TAU, on the TAU-specific tenant host tau.primo.exlibrisgroup.com. TAU'
  name: TAU Libraries Primo VE Discovery (DaTA Search)
  slug: primo-discovery
- description: Tel Aviv University federates through the IUCC Identity Federation (IUCCIF), the Israeli national federation operated by the Inter-University Computation Center, an eduGAIN member since 2014-07-07 and
  name: TAU SAML Identity in the IUCC Identity Federation
  slug: iucc-identity-federation
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://english.tau.ac.il/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://english.tau.ac.il/terms_of_use
- group: company
  title: ''
  type: Blog
  url: https://english.tau.ac.il/news
- group: company
  title: ''
  type: BlogRSS
  url: https://english.tau.ac.il/rss.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://cris.tau.ac.il/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://data.tau.ac.il/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.ims.tau.ac.il/Tal/KR/Search_P.aspx
- group: other
  title: ''
  type: IdentityFederation
  url: https://iif-ng.iucc.ac.il/sp/saml2/idp/metadata.php
- group: other
  title: ''
  type: AIPolicy
  url: https://innovative-learning.tau.ac.il/Responsible_use_of_AI
- group: build
  title: ''
  type: AITooling
  url: https://innovative-learning.tau.ac.il/Main_AI_tools
- group: company
  title: ''
  type: LinkedIn
  url: https://il.linkedin.com/school/tel-aviv-university/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/telavivuni
- group: design
  title: ''
  type: Conformance
  url: conformance/tel-aviv-university-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tel-aviv-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tel-aviv-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tel-aviv-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tel-aviv-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Every surface class the university pipeline hunts was probed on 2026-08-30 and Tel Aviv University operates no institution-owned public API. A 90-name DNS sweep of tau.ac.il found no api., developer., opendata., services., swagger., graphql. or rest. host; data.tau.ac.il and digital.tau.ac.il exist only as vanity redirects (data. lands on the Ex Libris Primo tenant). dspace.tau.ac.il and idp.tau.ac.il resolve to campus addresses but refuse connections on 80 and 443 from the public internet, so neither is a public surface. The library and research surfaces are all real and all tenant: Alma OAI-PMH 2.0 and SRU 1.2 on tau.alma.exlibrisgroup.com (both live, keyless, verified), Primo VE discovery on tau.primo.exlibrisgroup.com, and the Elsevier Pure CRIS at cris.tau.ac.il whose OAI-PMH Identify names "Pure OAI Repository" and purehosted@elsevier.com — an Elsevier-hosted deployment on a TAU-branded CNAME, not TAU engineering. Its Pure Web Service returns 401 without an institution key
    and cris.tau.ac.il/en/datasets/ is behind a Cloudflare interstitial (HTTP 403), while the /ws/oai path is unchallenged. Identity federation is a real find and a negative one: TAU has no eduGAIN-registered entity, only a tau.ac.il shibMD:Scope on the IUCC national proxy IdP. The only machine-readable documents TAU serves from its own hosts are two Drupal RSS 2.0 feeds (www.tau.ac.il/rss.xml, english.tau.ac.il/rss.xml, both 200 and populated); the public course search at www.ims.tau.ac.il/Tal/KR/Search_P.aspx is an HTML form that POSTs to Search_L.aspx and returns HTML. No llms.txt, no /.well-known/security.txt, no apis.json and no sitemap.xml are served. Two entries carried by the June 2026 profile were removed in this run as misattributions rather than gaps: an "Alma / OAI-PMH" entry whose only URL was Ex Libris''s own generic vendor documentation, now re-based on the real live TAU tenant endpoint; and an "Unofficial tau-tools" API entry plus a GitHubOrganization pointer at github.com/arazimproject
    — a student club''s credential-scraping Python library that badges itself "tau-unofficial" and is neither operated nor endorsed by the university. It is documented in review.yml and is deliberately not credited as a TAU surface.'
  evidence:
  - status: 200
    url: https://tau.alma.exlibrisgroup.com/view/oai/972TAU_INST/request?verb=Identify
  - status: 200
    url: https://tau.alma.exlibrisgroup.com/view/sru/972TAU_INST?version=1.2&operation=explain
  - status: 200
    url: https://cris.tau.ac.il/ws/oai?verb=Identify
  - status: 401
    url: https://cris.tau.ac.il/ws/api/524/openapi.json
  - status: 403
    url: https://cris.tau.ac.il/en/datasets/
  - status: 200
    url: https://iif-ng.iucc.ac.il/sp/saml2/idp/metadata.php
  - status: 200
    url: https://tau.primo.exlibrisgroup.com/discovery/search?vid=972TAU_INST:TAU&lang=en
  - status: 200
    url: https://english.tau.ac.il/rss.xml
  - status: 200
    url: https://www.tau.ac.il/rss.xml
  - status: 200
    url: https://www.ims.tau.ac.il/Tal/KR/Search_P.aspx
  - status: 200
    url: https://english.tau.ac.il/terms_of_use
  - status: 200
    url: https://innovative-learning.tau.ac.il/Responsible_use_of_AI
  - status: 200
    url: https://innovative-learning.tau.ac.il/Main_AI_tools
  - status: 200
    url: https://english.tau.ac.il/
  - status: 200
    url: https://data.tau.ac.il/
  - status: 403
    url: https://www.tau.ac.il/llms.txt
  - status: 403
    url: https://www.tau.ac.il/.well-known/security.txt
  - status: 404
    url: https://english.tau.ac.il/apis.json
  - status: 404
    url: https://www.tau.ac.il/sitemap.xml
  - status: 0
    url: https://api.tau.ac.il/
  reason: tenant_only
  state: none
created: '2026-06-03'
description: 'Tel Aviv University (TAU / אוניברסיטת תל אביב) is Israel''s largest university, a public research institution in Tel Aviv with roughly 30,000 students across nine faculties, and a member of the Israeli research-university group served by the Inter-University Computation Center (IUCC). Re-profiled on 2026-08-30 with operator attribution settled before any artifact was saved: TAU operates NO central developer portal, NO open-data portal and NO institution-operated public API. api.tau.ac.il, developer.tau.ac.il, opendata.tau.ac.il and services.tau.ac.il do not resolve; data.tau.ac.il and digital.tau.ac.il resolve only as vanity redirects. Every machine-readable, callable surface TAU has is a vendor product deployed under the institution''s name and is recorded here as a TENANT relationship, not as TAU engineering: the Ex Libris Alma OAI-PMH 2.0 service and SRU 1.2 search service for the library record, the Ex Libris Primo VE discovery layer (institution code 972TAU_INST:TAU, branded
  "DaTA Search"), the Elsevier Pure CRIS at cris.tau.ac.il whose OAI-PMH endpoint self-identifies as "Pure OAI Repository" administered from purehosted@elsevier.com, and TAU''s SAML identity, which is a tau.ac.il scope on the IUCC national proxy identity provider in eduGAIN rather than a TAU- registered entity of its own. The only machine-readable documents TAU itself serves from its own hosts are the Drupal RSS 2.0 news feeds at www.tau.ac.il/rss.xml and english.tau.ac.il/rss.xml, and its public timetable and course search at www.ims.tau.ac.il/Tal/KR/Search_P.aspx is an HTML form with no API behind it. TAU publishes an institutional generative-AI guidance set for students and faculty through its Deanery for Innovation in Teaching and Learning. There is no official institution-wide GitHub organisation; code lives in lab and student-club orgs.'
finops:
- name: Tel Aviv University Finops
  service_category: Education
  slug: tel-aviv-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tel-aviv-university.png
jsonld:
- class_count: 5
  name: Tel Aviv University Context
  property_count: 6
  slug: tel-aviv-university-context
layout: provider
modified: '2026-08-30'
name: Tel Aviv University
nav: Providers
network: true
overview: 'Tel Aviv University publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Israel, and Research.


  The Tel Aviv University catalog on APIs.io includes 1 JSON-LD context.


  Tel Aviv University''s developer surface includes engineering blog and 17 more developer resources.'
plans:
- name: Tel Aviv University Plans Pricing
  plan_count: 2
  slug: tel-aviv-university-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Tel Aviv University Rate Limits
  slug: tel-aviv-university-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 11.7
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 27.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tel-aviv-university/refs/heads/main/screenshots/tel-aviv-university-2026-06-20T195022.png
security:
- kind: domain-security
  name: Tel Aviv University Domain Security
  slug: tel-aviv-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tel-aviv-university
tags:
- University
- Higher Education
- Education
- Israel
- Research
- Research Repository
- Library
- Discovery
- OAI-PMH
- Identity Federation
- Course Catalog
- Middle East
website: https://english.tau.ac.il/
---
