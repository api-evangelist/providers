---
access_model:
  confidence: high
  label: Institution-internal
  onboarding: unknown
  pricing: free
  public: false
  source:
  - probe
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Fudan's SAML 2.0 identity provider, entityID https://idpfudan.fudan.edu.cn/idp/shibboleth, asserting scope fudan.edu.cn. It is registered with CARSI, China's education federation, and interfederated i
  name: Fudan University Shibboleth Identity Provider (CARSI / eduGAIN)
  slug: identity-saml
- description: 'Fudan''s institutional research data repository, operated by the Research Center for Social Sciences. It moved off Dataverse: dvn.fudan.edu.cn now only meta-refreshes to rdr.fudan.edu.cn/datahome, whic'
  name: Fudan University Social Science Data Platform (复旦大学社会科学数据平台)
  provenance: unpublished
  slug: research-data-platform
- baseURL: https://id.fudan.edu.cn/idp
  baseurl_source: declared
  description: End-user authentication and token issuance.
  name: Fudan University Authorization API
  slug: fudan-authorization-api
- baseURL: https://id.fudan.edu.cn/idp
  baseurl_source: declared
  description: Machine-readable metadata about the provider.
  name: Fudan University Discovery API
  slug: fudan-discovery-api
- baseURL: https://id.fudan.edu.cn/idp
  baseurl_source: declared
  description: Claims about the authenticated end user.
  name: Fudan University Identity API
  slug: fudan-identity-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.fudan.edu.cn
- group: company
  title: ''
  type: Website
  url: https://www.fudan.edu.cn/en/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idpfudan.fudan.edu.cn/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://id.fudan.edu.cn/idp/.well-known/openid-configuration
- group: other
  title: ''
  type: ResearchRepository
  url: https://rdr.fudan.edu.cn/datahome/open/dataResource
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.fudan.edu.cn/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://jwc.fudan.edu.cn/
- group: other
  title: ''
  type: AIPolicy
  url: https://news.fudan.edu.cn/2024/1220/c3163a143685/page.htm
- group: operate
  title: ''
  type: Support
  url: https://xxb.fudan.edu.cn/
- group: company
  title: ''
  type: Blog
  url: https://news.fudan.edu.cn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FudanUniversity
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FudanNLP
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FudanSELab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/fudan-university/
- group: auth
  href: https://artifacts.apis.io/fudan/security/fudan-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fudan-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fudan/security/fudan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fudan-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/fudan/plans/fudan-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fudan-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fudan/rate-limits/fudan-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fudan-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fudan/finops/fudan-finops.yml
  title: ''
  type: FinOps
  url: finops/fudan-finops.yml
- group: other
  href: https://artifacts.apis.io/fudan/review.yml
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Fudan operates real, institution-owned surfaces and two of them publish machine-readable metadata anonymously — the SAML 2.0 IdP metadata at idpfudan.fudan.edu.cn/idp/shibboleth and the OpenID Connect discovery document plus JWKS at id.fudan.edu.cn/idp. Those are captured and described here in full. Everything the institution actually runs behind them is closed: the OIDC endpoints need a client_id issued by the IT Office and there is no public registration; the research data platform''s JSON backend answers every unauthenticated call with HTTP 200 and the body {"status":4000,"message":"状态锁不得为空"}. No developer portal, no API key programme and no documentation exists for any of it. This is not a bot block and not a language barrier — Chinese-language surfaces were searched and read, and the Chinese Information Technology Office pages were the source for several corrections here.'
  evidence:
  - status: 200
    url: https://idpfudan.fudan.edu.cn/idp/shibboleth
  - status: 200
    url: https://id.fudan.edu.cn/idp/.well-known/openid-configuration
  - status: 200
    url: https://id.fudan.edu.cn/idp/oidc/getPublicKey
  - status: 200
    url: https://rdr.fudan.edu.cn/datahome/open/admin/loginUserInfo.do
  - status: 404
    url: https://rdr.fudan.edu.cn/api/info/version
  - status: 404
    url: https://dvn.fudan.edu.cn/oai?verb=Identify
  - status: 200
    url: https://library.fudan.edu.cn/oai?verb=Identify
  - status: 404
    url: https://www.fudan.edu.cn/robots.txt
  - status: 404
    url: https://www.fudan.edu.cn/llms.txt
  reason: auth-required
  state: gated
created: '2026-06-03'
description: 'Fudan University is a public research university in Shanghai, China, and a member of the national C9 League and Double First-Class programme. Its programmable footprint is small and almost entirely internal, but — unusually for this cohort — none of it is a vendor''s contract wearing the university''s name: every surface catalogued here runs on a host under fudan.edu.cn and is operated by Fudan itself. The real find is identity federation. Fudan operates a Shibboleth SAML 2.0 identity provider, registered with the CARSI federation and published to eduGAIN since February 2020, and it serves its own SAML metadata live at idpfudan.fudan.edu.cn. Alongside it, id.fudan.edu.cn publishes a working OpenID Connect discovery document and JWKS with no authentication required. Both are genuinely machine-readable and neither is documented anywhere Fudan publishes. Beyond identity, the Social Science Data Platform migrated off Dataverse to a custom application at rdr.fudan.edu.cn/datahome;
  its JSON backend answers, but it is undocumented, session-bound, and returns application-level refusals with HTTP 200. There is no developer portal, no public API key programme, no OAI-PMH, no open data portal, no robots.txt and no llms.txt on the main site, and the official GitHub organisation has zero public repositories — the university''s public code lives instead in departmental lab organisations.'
examples:
- key_count: 1
  name: Fudan Idp Jwks
  slug: fudan-idp-jwks
- key_count: 13
  name: Fudan Openid Configuration
  slug: fudan-openid-configuration
finops:
- has_sources: true
  method: generated
  name: Fudan Finops
  primary_unit: ''
  service_category: Education
  slug: fudan-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fudan.png
json_schemas:
- name: Fudan University OpenID Connect discovery document
  property_count: 13
  slug: fudan-openid-configuration
jsonld:
- class_count: 15
  name: Fudan Context
  property_count: 0
  slug: fudan-context
layout: provider
modified: '2026-08-30'
name: Fudan University
nav: Providers
network: true
overview: 'Fudan University publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Authorization API, Discovery API, and Identity API. Tagged areas include University, Higher Education, Education, China, and Shanghai.


  The Fudan University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fudan University''s developer surface includes support, engineering blog, and 18 more developer resources.'
plans:
- name: Fudan Plans Pricing
  plan_count: 2
  slug: fudan-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Fudan Rate Limits
  slug: fudan-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Fudan University API Rules
  rule_count: 55
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 1
  slug: fudan-rules
scopes:
- name: Fudan Scopes
  scope_count: 1
  slug: fudan-scopes
  summary_line: 1 scope
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 17.4
    contract_quality: 25.6
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 22.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fudan/fudan-2026-06-20T181623.png
security:
- kind: authentication
  name: Fudan Authentication
  slug: fudan-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fudan Domain Security
  slug: fudan-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Fudan Vulnerability Disclosure
  slug: fudan-vulnerability-disclosure
  summary_line: no policy recorded
slug: fudan
tags:
- University
- Higher Education
- Education
- China
- Shanghai
- C9 League
- Identity Federation
- Research Data
- SSO
website: https://www.fudan.edu.cn
---
