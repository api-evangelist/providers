---
access_model:
  confidence: high
  label: Free · no registration for the public read-only endpoints; every substantive surface needs an NJU institutional account, which outsiders cannot obtain
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probed
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
  scored_at: '2026-09-01'
api_count: 14
apis:
- description: Nanjing University's own Shibboleth Identity Provider. It publishes SAML 2.0 metadata at the canonical /idp/shibboleth location — an EntityDescriptor with an IDPSSODescriptor and an AttributeAuthority
  name: Nanjing University Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: idp-shibboleth
- description: NJU's entry in CARSI (CERNET Authentication and Resource Sharing Infrastructure), China's national research and education identity federation, republished into eduGAIN. Entity id 671521, entityID http
  name: Nanjing University CARSI / eduGAIN Federation Registration
  slug: carsi-edugain
- description: NJU's central single sign-on, a CAS deployment supporting password, verification-code, biometric and QR-code login. It is not a developer API and there is no public service registration — a relying ap
  name: Nanjing University Unified Identity Authentication (CAS SSO)
  slug: cas-sso
- description: The university's public open-source mirror, run by the NJU e-Science Center and open to anyone on the internet. Beyond the package trees themselves, the site serves JSON configuration endpoints that a
  name: NJU Mirror (open-source software mirror)
  slug: mirrors
- description: An institution-operated GitLab instance for NJU staff and students. Its REST API v4 is real and in production — the university's own mirror site fetches /api/v4/projects/2412/issues to render announce
  name: NJU e-Science Code Hosting (GitLab REST API v4)
  slug: gitlab
- description: The e-Science Center's documentation platform (a BookStack deployment) publishes a complete public REST API reference at /api/docs — 79 endpoints across books, chapters, pages, shelves, attachments, i
  name: NJU e-Science Document Service API
  slug: doc-bookstack
- description: The university's cloud storage service for staff and students, a self-hosted Seafile 13.0.25 instance branded "南大云盘 NJU Box". Service discovery is anonymous — /api2/ping/ returns "pong" and /api2/serv
  name: NJU Box (南大云盘) — Seafile deployment
  slug: box
- description: An institution-hosted SeaTable 6.1.9 enterprise-edition deployment offering collaborative tables to NJU users. /api2/ping/ and /server-info/ answer anonymously; the rest of the SeaTable API requires a
  name: NJU Table (南大表格) — SeaTable deployment
  slug: table
- description: 'A self-hosted Vaultwarden 2026.6.0 instance offering a Bitwarden-protocol password vault to NJU users. /alive returns a server timestamp and /api/config returns server identity, version, git hash and '
  name: NJU Password Manager (Vaultwarden deployment)
  slug: pass
- description: Nanjing University's supercomputing service, operated by the e-Science Center under the Collaborative Innovation Center of Advanced Microstructures. It publishes hardware and software resource invento
  name: NJU e-Science High Performance Computing Center
  slug: hpc
- description: '"小蓝鲸" — the university''s own AI assistant platform for NJU users, a single-page application backed by an astron-agent deployment with Casdoor as its identity provider and an iFlytek Spark application '
  name: NJU Intelligent Assistant Platform (小蓝鲸)
  slug: chat-assistant
- description: 'The library''s catalog host. It is live but restricted to the campus network: every route, including an OAI-PMH probe, returns HTTP 403 with the body "请使用南大VPN访问!" ("please access via the NJU VPN"). Re'
  name: Nanjing University Library Catalog (OPAC)
  slug: opac
- description: 'Nanjing University''s registration in ROR, the open registry of research organizations: ROR ID 01rxvg760, domain nju.edu.cn, established 1902, with cross-references to ISNI 0000 0001 2314 964X, GRID gr'
  name: Nanjing University in the Research Organization Registry (ROR)
  slug: ror
- description: Nanjing University's entry in the Crossref Open Funder Registry as funder 501100008048, with 3,401 works recording it as a funder and two descendant funder identifiers — the Jiangsu Collaborative Inno
  name: Nanjing University in the Crossref Open Funder Registry
  slug: crossref-funder
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.nju.edu.cn/en/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.nju.edu.cn/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.nju.edu.cn/api/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MCG-NJU
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nju-websoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/nanjing-university/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.nju.edu.cn/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/nanjing-identity-federation.yml
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.nju.edu.cn/zh/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.nju.edu.cn/
- group: build
  title: ''
  type: AITooling
  url: https://chat.nju.edu.cn/
- group: operate
  title: ''
  type: Support
  url: https://itsc.nju.edu.cn/
- group: auth
  title: ''
  type: Authentication
  url: https://authserver.nju.edu.cn/authserver/login
- group: auth
  title: ''
  type: Authentication
  url: authentication/nanjing-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nanjing-education-standards-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nanjing-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nanjing-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nanjing-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nanjing-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Nanjing University (NJU, 南京大学), founded in 1902 in Nanjing, Jiangsu, is one of China''s oldest research universities and a member of the C9 League. It publishes no developer portal, no API gateway, no API programme and no OpenAPI of its own, and this profile records that plainly. What it does operate — directly, on its own hosts, inside CERNET address space — is a genuine estate of institution-run machine-readable surfaces, almost all of it built and run by the university''s e-Science Center: its own Shibboleth identity provider at idp.nju.edu.cn, registered in CARSI and republished to eduGAIN; a CAS single sign-on service whose ticket-validation endpoints answer the CAS 2.0 and 3.0 protocol to anonymous callers; a public open-source mirror at mirrors.nju.edu.cn serving JSON configuration endpoints; a GitLab instance at git.nju.edu.cn whose REST API v4 the mirror site itself consumes; a BookStack documentation service at doc.nju.edu.cn that publishes a complete 79-endpoint
  REST API reference publicly and gates the API on an NJU token; and Seafile, SeaTable and Vaultwarden deployments that answer unauthenticated service-discovery JSON. None of this is an API product, none of it is registerable by an outsider, and the contracts behind the service deployments are the upstream products'', not NJU''s engineering — so no vendor specification is saved here under NJU''s name. The June 2026 profile of this institution saw none of it and recorded only a login page.'
finops:
- name: Nanjing Finops
  service_category: Education
  slug: nanjing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nanjing.png
jsonld:
- class_count: 13
  name: Nanjing Context
  property_count: 0
  slug: nanjing-context
layout: provider
modified: '2026-09-01'
name: Nanjing University
nav: Providers
network: true
overview: 'Nanjing University publishes 14 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, China, and C9 League.


  The Nanjing University catalog on APIs.io includes 1 JSON-LD context.


  Nanjing University''s developer surface includes documentation, API reference, support, authentication, and 16 more developer resources.'
plans:
- name: Nanjing Plans Pricing
  plan_count: 2
  slug: nanjing-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Nanjing Rate Limits
  slug: nanjing-rate-limits
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 9.3
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 17.3
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/nanjing/refs/heads/main/screenshots/nanjing-2026-06-20T190003.png
security:
- kind: authentication
  name: Nanjing Authentication
  slug: nanjing-authentication
  summary_line: none/saml/cas/bearer/challenge · 9 schemes
- kind: domain-security
  name: Nanjing Domain Security
  slug: nanjing-domain-security
  summary_line: TLSv1.2 · DMARC
slug: nanjing
tags:
- University
- Higher Education
- Education
- China
- C9 League
- Research
- Identity Federation
- Authentication
- Single Sign-On
- Research Computing
- Open Source Mirror
- Version Control
- Library
website: https://www.nju.edu.cn/en/
---
