---
access_model:
  confidence: high
  label: No developer programme — no signup, no key, no plan
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probed
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
api_count: 5
apis:
- description: Harbin Institute of Technology's own Shibboleth identity provider, self-hosted on HIT's registrable domain and asserting the scope hit.edu.cn. Publishes a SAML 2.0 EntityDescriptor anonymously at /idp
  name: HIT Shibboleth Identity Provider (SAML 2.0)
  slug: hit-shibboleth-idp
- description: 'OAI-PMH 2.0 harvesting endpoint for HIT''s research outputs, persons and datasets, on HIT''s own hostname and anonymously callable — a ListRecords over publications:all returned 358,884 bytes of oai_dc '
  name: HIT Research Portal OAI-PMH Endpoint
  slug: hit-pure-oai-pmh
- description: RSS 2.0 feeds with Dublin Core extensions emitted by HIT's Elsevier Pure research portal. The publications feed returns the latest research outputs; the persons feed lists researcher profiles. Both ve
  name: HIT Research Portal RSS Feeds
  slug: hit-pure-rss
- description: HIT's tenancy on the Elsevier Pure web services API, deployed at scholar.hit.edu.cn/ws/api. THE RELATIONSHIP IS RECORDED HERE; THE CONTRACT IS DELIBERATELY NOT SAVED IN THIS REPO. The live document at
  name: Elsevier Pure Web Services API — HIT Tenancy
  slug: elsevier-pure-tenancy
- description: HIT is registered in the Research Organization Registry with ROR ID 01yqg2h08, carrying the names Harbin Institute of Technology, 哈尔滨工业大学 and the acronym HIT, and linking to www.hit.edu.cn. A membersh
  name: ROR Registration — Harbin Institute of Technology
  slug: ror-registration
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://en.hit.edu.cn/
- group: company
  title: ''
  type: WebsiteChinese
  url: https://www.hit.edu.cn/
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholar.hit.edu.cn/en/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.hit.edu.cn/idp/shibboleth
- group: design
  title: ''
  type: Conformance
  url: conformance/harbin-institute-of-technology-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harbin-institute-of-technology-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/harbin-institute-of-technology-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harbin-institute-of-technology-domain-security.yml
- group: company
  title: ''
  type: News
  url: https://today.hit.edu.cn/
- group: build
  title: ''
  type: Library
  url: https://lib.hit.edu.cn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HITSZ-HLT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/harbin-institute-of-technology/
- group: commercial
  title: ''
  type: Plans
  url: plans/harbin-institute-of-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/harbin-institute-of-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/harbin-institute-of-technology-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: No institution-authored API contract exists to capture. Every machine-readable DATA surface HIT exposes is an Elsevier Pure tenancy on HIT's own hostname — the OAI-PMH endpoint, the RSS feeds and the Pure web services API all belong to one Pure deployment at scholar.hit.edu.cn whose Identify response names purehosted@elsevier.com as administrator and whose OpenAPI document is titled "Pure API" with contact pure-support@elsevier.com. HIT's one genuinely institution-operated machine-readable artifact is its Shibboleth SAML IdP metadata, which is identity infrastructure rather than an API and is recorded as such. Probing found no course catalog API (jwc.hit.edu.cn, the academic affairs site, is administratively DISABLED and serves a notice page), no open data portal (data.hit.edu.cn does not resolve), no library catalog API, no api./open./oapi. host, no security.txt, no robots.txt and no llms.txt. Searching was done on both the Chinese and English surfaces; this is not a language
    barrier.
  evidence:
  - detail: Served anonymously but titled "Pure API", contact pure-support@elsevier.com, 827 paths — Elsevier's contract, not HIT's.
    status: 200
    url: https://scholar.hit.edu.cn/ws/api/openapi.json
  - detail: Pure data paths are credential-gated.
    status: 401
    url: https://scholar.hit.edu.cn/ws/api/research-outputs?size=1
  - detail: 'Live OAI-PMH, but repositoryName "Pure OAI Repository", adminEmail purehosted@elsevier.com. Intermittently reachable from outside China: 200 on 5 of 9 attempts, connection timeout otherwise, never an HTTP error.'
    status: 200
    url: https://scholar.hit.edu.cn/ws/oai?verb=Identify
  - detail: HIT's own SAML 2.0 IdP metadata, scope hit.edu.cn — the one institution-operated machine-readable surface found.
    status: 200
    url: https://idp.hit.edu.cn/idp/shibboleth
  - detail: Soft-200. Academic affairs (教务处) site body reads "站点 教务处 已禁用" — site disabled. No course catalog surface.
    status: 200
    url: https://jwc.hit.edu.cn/
  - detail: DNS does not resolve. No open data portal.
    status: 0
    url: https://data.hit.edu.cn/
  - detail: No security.txt.
    status: 404
    url: https://www.hit.edu.cn/.well-known/security.txt
  - detail: 'CNAME to purealb-1397755226.cn-northwest-1.elb.amazonaws.com.cn — an Elsevier Pure AWS China load balancer. Note for the cohort detector: AWS ELB hostnames are UNIQUE PER DEPLOYMENT, so a cohort-reuse rule ("a host more than one institution points at") can never fire on them. The vendor signal is the product prefix "purealb-", not the full hostname.'
    status: 200
    url: dns:scholar.hit.edu.cn
  reason: tenant_only
  state: none
created: '2026-06-03'
description: 'Harbin Institute of Technology (HIT, 哈尔滨工业大学) is a public technical research university in Harbin, Heilongjiang, China, founded in 1920, administered by the Ministry of Industry and Information Technology, and a member of the C9 League, with additional campuses at Weihai and Shenzhen. HIT operates NO public developer programme, no API documentation, no developer portal and no API key issuance of any kind, and this profile should be read as recording that absence. Its one institution-operated machine-readable surface is a Shibboleth SAML 2.0 identity provider at idp.hit.edu.cn, scoped to hit.edu.cn — genuinely HIT''s own engineering, though the metadata document it publishes is the unedited Shibboleth template and expired in 2020. Every other machine-readable surface is a tenancy on Elsevier Pure running under HIT''s own hostname (scholar.hit.edu.cn): a live and anonymously harvestable OAI-PMH endpoint carrying the OpenAIRE CERIF 1.2 profile, RSS feeds of publications and researcher
  profiles, and a Pure web services API that is credential-gated and whose contract belongs to Elsevier, not to HIT. The data in those surfaces is HIT''s; the contracts are not.'
finops:
- name: Harbin Institute Of Technology Finops
  service_category: Education
  slug: harbin-institute-of-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harbin-institute-of-technology.png
layout: provider
modified: '2026-09-01'
name: Harbin Institute of Technology
nav: Providers
network: true
overview: 'Harbin Institute of Technology publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, China, and Technical University.


  Harbin Institute of Technology''s developer surface includes authentication, product news, and 14 more developer resources.'
plans:
- name: Harbin Institute Of Technology Plans Pricing
  plan_count: 2
  slug: harbin-institute-of-technology-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Harbin Institute Of Technology Rate Limits
  slug: harbin-institute-of-technology-rate-limits
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -17.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 4.4
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 42.0
  provenance:
    conformance: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/harbin-institute-of-technology/refs/heads/main/screenshots/harbin-institute-of-technology-2026-06-20T182524.png
security:
- kind: authentication
  name: Harbin Institute Of Technology Authentication
  slug: harbin-institute-of-technology-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Harbin Institute Of Technology Domain Security
  slug: harbin-institute-of-technology-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Harbin Institute Of Technology Vulnerability Disclosure
  slug: harbin-institute-of-technology-vulnerability-disclosure
  summary_line: disclosure policy published
slug: harbin-institute-of-technology
tags:
- University
- Higher Education
- Education
- China
- Technical University
- C9 League
- Research
- Scholarly
- Identity Federation
- Research Repository
- OAI-PMH
website: https://en.hit.edu.cn/
---
