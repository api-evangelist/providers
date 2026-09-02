---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: true
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
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: 'NTNU runs its own Open Journal Systems installation, "NTNU Open Access Journals", on its own registrable domain at www.ntnu.no/ojs, publishing sixteen journals including Nordic Journal of Science and '
  name: NTNU Open Access Journals OAI-PMH
  slug: ojs-oai
- description: api.ntnu.no is an NTNU-operated API gateway serving internal and partner integrations. It is live and institution-run — responses carry NTNU's own X-TIA-Processed-by frontend-auth header — but every r
  name: NTNU API Gateway (api.ntnu.no)
  slug: api-ntnu
- description: Cristin is Norway's national Current Research Information System, operated by Sikt (the Norwegian Agency for Shared Services in Education and Research) on behalf of every participating institution. NT
  name: Cristin Research Information API (NTNU institution 194)
  slug: cristin
- description: 'Nasjonalt vitenarkiv (NVA) is the Sikt-operated national open research archive that absorbed NTNU''s institutional repository — ntnuopen.ntnu.no now redirects to nva.sikt.no. NTNU deposits into it and '
  name: NVA National Research Archive (NTNU Open successor)
  slug: nva
- description: NTNU's research data is deposited into the "NTNU – Norwegian University of Science and Technology" collection (alias "ntnu") of DataverseNO, the Norwegian national research-data repository operated by
  name: DataverseNO — NTNU Research Data Collection
  slug: dataverseno
- description: 'TP (Timeplan) is the timetable, room-booking and course-activity system NTNU uses, hosted on the shared educloud.no platform at tp.educloud.no/ntnu. The /ntnu/ws/ web-service path is live and returns '
  name: TP Timetable Web Service (NTNU instance)
  slug: tp
- description: 'NTNU authenticates through Feide, the Norwegian national identity federation operated by Sikt, with Dataporten providing OAuth2 / OpenID Connect and SAML single sign-on. NTNU does not publish its own '
  name: Feide / Dataporten Identity Federation (NTNU membership)
  slug: feide
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.ntnu.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EECS-NTNU
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ntnu/
- group: company
  title: ''
  type: Blog
  url: https://nyheter.ntnu.no/en/feed/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.feide.no/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.ntnu.no/.well-known/security.txt
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.feide.no/feide-edugain-metadata.xml
- group: other
  title: ''
  type: OpenData
  url: https://data.ntnu.no/
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataverse.no/dataverse/ntnu
- group: other
  title: ''
  type: ResearchRepository
  url: https://nva.sikt.no/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.ntnu.no/studier/emner
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.hpc.ntnu.no/
- group: other
  title: ''
  type: AIPolicy
  url: https://i.ntnu.no/wiki/-/wiki/English/Use+of+ICT+tools+with+generative+artificial+intelligence+at+NTNU+-+policy
- group: build
  title: ''
  type: AITooling
  url: https://i.ntnu.no/en/ki-for-ansatte
- group: design
  title: ''
  type: Conformance
  url: conformance/ntnu-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ntnu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ntnu-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ntnu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ntnu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ntnu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  checked: '2026-08-30'
  detail: 'NTNU publishes no API contract of its own — no OpenAPI, AsyncAPI, GraphQL schema, llms.txt or developer portal exists on any NTNU host (www.ntnu.no/llms.txt 404, developer.ntnu.no does not resolve). It does operate a real API gateway at api.ntnu.no, but every path on it, including /docs, /openapi.json and /status, redirects to Feide OAuth and serves the same account-chooser page, so no contract, scope list or reference could be read without an institutional account. The one institution-operated surface that is openly callable is the OAI-PMH interface of NTNU Open Access Journals at www.ntnu.no/ojs, which was fully probed and is recorded as an API. All remaining programmable footprint is tenant: DataverseNO (UiT), Cristin and NVA (Sikt), TP (educloud.no) and Feide (Sikt). This profile is thin because NTNU''s own API surface is behind a national identity federation, not because it was unreachable.'
  evidence:
  - status: 200
    url: https://www.ntnu.no/ojs/index.php/index/oai?verb=Identify
  - status: 200
    url: https://www.ntnu.no/ojs/index.php/index/oai?verb=ListMetadataFormats
  - status: 200
    url: https://www.ntnu.no/ojs/index.php/index/oai?verb=ListSets
  - status: 200
    url: https://api.ntnu.no/
  - status: 200
    url: https://api.ntnu.no/openapi.json
  - status: 200
    url: https://www.ntnu.no/.well-known/security.txt
  - status: 404
    url: https://www.ntnu.no/llms.txt
  - status: 0
    url: https://developer.ntnu.no/
  - status: 200
    url: https://dataverse.no/api/dataverses/ntnu
  - status: 200
    url: https://api.cristin.no/v2/institutions/194
  - status: 403
    url: https://api.nva.unit.no/
  - status: 403
    url: https://tp.educloud.no/ntnu/ws/
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'The Norwegian University of Science and Technology (NTNU) is Norway''s largest university, headquartered in Trondheim with campuses in Gjovik and Alesund. NTNU operates no consolidated institutional developer portal and publishes no OpenAPI, AsyncAPI or other machine-readable API contract of its own. Its one openly callable, institution-operated surface is the OAI-PMH interface of NTNU Open Access Journals at www.ntnu.no/ojs, which answers Identify, ListMetadataFormats and ListSets over sixteen NTNU-published journals. NTNU also runs an institutional API gateway at api.ntnu.no, but every path on it is behind Feide OAuth and no public documentation, contract or scope list is served without an institutional account. Everything else that looks programmable under NTNU''s name is operated by somebody else and entered here as a tenant relationship, not as NTNU engineering: research data in the NTNU collection of DataverseNO (run by UiT The Arctic University of Norway on Dataverse
  software), research information in Cristin and the national research archive NVA (both run by Sikt), timetables in TP on educloud.no, identity in the Feide federation where NTNU exists as the scope ntnu.no on Sikt''s national IdP rather than as its own eduGAIN entity, and teaching in a hosted Canvas tenant. This repo previously carried 35 OpenAPI files and 87 derived artifacts that were splits of the generic Dataverse 6.6 product contract; they were the vendor''s, not NTNU''s, and have been removed.'
finops:
- name: Ntnu Finops
  service_category: Education
  slug: ntnu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ntnu.png
layout: provider
modified: '2026-08-30'
name: Norwegian University of Science and Technology
nav: Providers
network: true
overview: 'Norwegian University of Science and Technology publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Research Data.


  Norwegian University of Science and Technology''s developer surface includes engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Ntnu Plans Pricing
  plan_count: 2
  slug: ntnu-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Ntnu Rate Limits
  slug: ntnu-rate-limits
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 6.9
    developer_ergonomics: 23.8
    discoverability: 85.2
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 31.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ntnu/refs/heads/main/screenshots/ntnu-2026-06-20T190500.png
security:
- kind: domain-security
  name: Ntnu Domain Security
  slug: ntnu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Ntnu Vulnerability Disclosure
  slug: ntnu-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ntnu
tags:
- Education
- Higher Education
- University
- Research
- Research Data
- Open Access
- Open Data
- Identity
- Course Catalog
- Norway
- Scandinavia
website: https://www.ntnu.edu/
---
