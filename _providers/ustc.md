---
access_model:
  confidence: high
  label: Affiliation-gated
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: USTC's institution-operated authorization server, run by the Network Information Center and the hub every other campus system authenticates against. It speaks CAS 3.0, OAuth 2.0 authorization code (re
  name: USTC Unified Identity Authentication (id.ustc.edu.cn, formerly Passport SSO)
  slug: passport
- description: A small, precise, institution-authored REST API that resolves a person's campus enrollment status code by global person identifier or identity number, singly or in batches of up to 100. USTC publishes
  name: USTC Campus Enrollment Status Query API (在校状态查询接口)
  slug: campus-status
- description: USTC's self-hosted Shibboleth IdP 5.2.2, publishing a 15KB SAML 2.0 EntityDescriptor for entityID https://idp.ustc.edu.cn/idp/shibboleth with a shibmd:Scope of ustc.edu.cn, SSO and SLO endpoints acros
  name: USTC Shibboleth Identity Provider (跨校资源认证中心)
  slug: idp
- description: The JSON API behind USTC's public course catalog application — semesters, the college tree, program trees, course search, course and lesson detail, exam lists, major lists and public timetables, acros
  name: USTC Course Catalog API (catalog.ustc.edu.cn)
  slug: catalog
- description: The USTC Open Source Software Mirror, operated by the campus Linux User Group (LUG @ USTC), is one of the largest open source mirror services among universities in mainland China, carrying Debian, Ubu
  name: USTC Open Source Software Mirror
  slug: mirrors
- description: A GitLab instance USTC runs on its own domain at git.ustc.edu.cn, with a second LUG-operated instance at git.lug.ustc.edu.cn. GitLab exposes a well-documented REST and GraphQL API, but that contract i
  name: USTC Campus GitLab
  slug: gitlab
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://en.ustc.edu.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://id.ustc.edu.cn/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://id.ustc.edu.cn/doc/status-api/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://id.ustc.edu.cn/doc/developer/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/ustc-identity-federation.yml
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.ustc.edu.cn/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://opac.lib.ustc.edu.cn/
- group: other
  title: ''
  type: ResearchComputing
  url: https://scc.ustc.edu.cn/
- group: build
  title: ''
  type: AITooling
  url: https://chat.ustc.edu.cn/
- group: other
  title: ''
  type: AIPolicy
  url: https://chat.ustc.edu.cn/ustchat/policies/ustchat-terms-of-use.html
- group: design
  title: ''
  type: Conformance
  url: conformance/ustc-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ustc-identity-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ustc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ustc-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ustc-lifecycle.yml
- group: operate
  title: ''
  type: Support
  url: https://ustcnet.ustc.edu.cn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ustclug
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-science-and-technology-of-china/
- group: operate
  title: ''
  type: StatusPage
  url: https://mirrors.ustc.edu.cn/status/
- group: company
  title: ''
  type: Blog
  url: https://news.ustc.edu.cn/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ustc-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ustc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ustc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ustc-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ustc-context.jsonld
coverage:
  detail: 'USTC operates real, institution-owned API surfaces and documents some of them well, but an unaffiliated caller cannot consume any of them. The unified identity authorization server at id.ustc.edu.cn publishes an anonymously readable OIDC discovery document and JWKS, yet a client_id exists only after a manual registration and filing process, and USTC states explicitly that applications not deployed on campus and not on a ustc.edu.cn domain are not supported at all — the clearest such statement found in this cohort. The enrollment status API returns 200 on its public health check and 401 on every business path, and requires both an administrator-issued bearer token and a registered source IP. The course catalog''s eighteen /api/teach/ routes answer 401 and the application declares itself restricted at /api/restricted. The library OPAC returns 200 with a prose refusal naming the caller''s off-campus IP address. The one fully public machine-readable contract is the SAML 2.0 metadata
    of the Shibboleth IdP at idp.ustc.edu.cn, which is why it is the centrepiece of this profile.

    This is a re-profile, and it moves in the opposite direction to the rest of this cohort. The June 2026 pass recorded two surfaces and no artifacts and concluded USTC had no documented API program; probing found a documented one that was simply never looked for. Nothing was removed for vendor misattribution because nothing vendor-attributed was ever here — no Figshare, Pure, Ex Libris, Dataverse or Canvas contract. The single vendor-product API found (GitLab at git.ustc.edu.cn) is recorded as a deployment with x-contract-operator: vendor and no specification saved.

    Not found, after probing: any OAI-PMH endpoint (lib.ustc.edu.cn/oai 404s, ir.lib.ustc.edu.cn does not resolve), any institutional repository under USTC''s own domain, any open-data portal (data.ustc.edu.cn does not resolve), any llms.txt, and any /.well-known catalog other than the OIDC discovery document. USTC''s own AI assistant is real and institution-operated — the Network Information Center runs it on DeepSeek — and its user agreement mentions API delivery, but no API documentation for it is published, so it is recorded as a pointer rather than a surface.'
  evidence:
  - status: 200
    url: https://idp.ustc.edu.cn/idp/shibboleth
  - status: 200
    url: https://id.ustc.edu.cn/cas/oidc/.well-known/openid-configuration
  - status: 200
    url: https://id.ustc.edu.cn/cas/oidc/jwks
  - status: 200
    url: https://id.ustc.edu.cn/doc/api/health
  - status: 200
    url: https://id.ustc.edu.cn/doc/status-api/
  - status: 200
    url: https://id.ustc.edu.cn/doc/developer/
  - status: 200
    url: https://id.ustc.edu.cn/doc/notice/
  - status: 200
    url: https://passport.ustc.edu.cn/serviceValidate
  - status: 200
    url: https://passport.ustc.edu.cn/healthcheck
  - status: 401
    url: https://id.ustc.edu.cn/doc/api/status/by-zjhm/P0529
  - status: 401
    url: https://id.ustc.edu.cn/cas/oauth2.0/profile
  - status: 200
    url: https://catalog.ustc.edu.cn/api/restricted
  - status: 401
    url: https://catalog.ustc.edu.cn/api/teach/semester/list
  - status: 200
    url: https://mirrors.ustc.edu.cn/status/
  - status: 200
    url: https://opac.lib.ustc.edu.cn/
  - status: 200
    url: https://chat.ustc.edu.cn/ustchat/policies/ustchat-terms-of-use.html
  - status: 200
    url: https://git.ustc.edu.cn/
  - status: 200
    url: https://scc.ustc.edu.cn/
  - status: 404
    url: https://lib.ustc.edu.cn/oai?verb=Identify
  - status: 404
    url: https://id.ustc.edu.cn/cas/oidc/register
  - status: 404
    url: https://mirrors.ustc.edu.cn/mirrorz.json
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'The University of Science and Technology of China (USTC, 中国科学技术大学) is a public research university in Hefei, Anhui, founded in 1958 under the Chinese Academy of Sciences, a member of the C9 League and ranked #63 in the QS World University Rankings 2025. USTC publishes no developer portal, no open-data platform and no institutional API program — but it is not the empty profile an earlier pass recorded. Its Network Information Center runs and DOCUMENTS a genuine identity platform: a first-party CAS 3.0 / OAuth 2.0 / OpenID Connect authorization server at id.ustc.edu.cn with an anonymously readable discovery document and JWKS, a developer manual with parameter tables and worked examples at id.ustc.edu.cn/doc/developer/, an enrollment-status query API with a published error table and a public health check, and a self-hosted Shibboleth 5.2.2 identity provider at idp.ustc.edu.cn whose SAML 2.0 metadata is the strongest machine-readable contract in this profile — federating into CARSI,
  the CAS Science Cloud AAI and eduGAIN. Beyond identity, USTC operates a course catalog with a live JSON API at catalog.ustc.edu.cn (401 to the public, and self-declaring restricted mode), the USTC Open Source Software Mirror on the university''s own APNIC allocation, a campus GitLab, a supercomputing centre, and its own DeepSeek-based AI assistant with a published user agreement. Every one of those surfaces is institution-operated; almost every one is gated to campus members, and USTC states plainly that applications outside the ustc.edu.cn domain are not supported. No vendor contract is attributed to USTC in this profile — no Figshare, Pure, Ex Libris, Dataverse or Canvas surface was found under its name.'
examples:
- key_count: 1
  name: Ustc Jwks Example
  slug: ustc-jwks-example
- key_count: 17
  name: Ustc Openid Configuration Example
  slug: ustc-openid-configuration-example
finops:
- name: Ustc Finops
  service_category: Education
  slug: ustc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ustc.png
json_schemas:
- name: USTC Campus Enrollment Status API schemas
  property_count: 0
  slug: ustc-campus-status-schemas
jsonld:
- class_count: 13
  name: Ustc Context
  property_count: 2
  slug: ustc-context
layout: provider
modified: '2026-08-30'
name: University of Science and Technology of China
nav: Providers
network: true
overview: 'University of Science and Technology of China publishes 1 API on the [APIs.io](https://apis.io/) network: USTC Campus Enrollment Status Query API (在校状态查询接口). Tagged areas include University, Higher Education, Education, China, and C9 League.


  The University of Science and Technology of China catalog on APIs.io includes 1 JSON-LD context.


  University of Science and Technology of China''s developer surface includes documentation, API reference, code examples, authentication, support, engineering blog, and 21 more developer resources.'
plans:
- name: Ustc Plans Pricing
  plan_count: 2
  slug: ustc-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Ustc Rate Limits
  slug: ustc-rate-limits
scopes:
- name: Ustc Scopes
  scope_count: 0
  slug: ustc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -11.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 3.8
    contract_quality: 30.6
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 3.8
    operational_transparency: 39.5
  previous_composite: 49.7
  provenance:
    conformance: first-party
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
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ustc/refs/heads/main/screenshots/ustc-2026-06-20T200827.png
security:
- kind: authentication
  name: Ustc Authentication
  slug: ustc-authentication
  summary_line: 7 schemes
- kind: domain-security
  name: Ustc Domain Security
  slug: ustc-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ustc
tags:
- University
- Higher Education
- Education
- China
- C9 League
- Chinese Academy of Sciences
- Research
- Identity Federation
- Single Sign-On
- Course Catalog
- Research Computing
- Open Source Mirror
website: https://en.ustc.edu.cn/
---
