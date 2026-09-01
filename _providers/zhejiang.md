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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Zhejiang University operates a Shibboleth SAML 2.0 Identity Provider, entityID https://idp.zju.edu.cn/idp/shibboleth, registered in CARSI (the CERNET Authentication and Resource Sharing Infrastructure
  name: Shibboleth Identity Provider (SAML 2.0)
  slug: shibboleth
- description: ZJU's unified identity authentication platform — a Central Authentication Service (CAS) single sign-on login fronting campus systems. It supports username/password, QR-code scanning and third-party ha
  name: Unified Identity Authentication (CAS / SSO)
  slug: sso
- description: The machine-readable mirror service catalog.
  name: Zhejiang University Catalog API
  slug: zhejiang-catalog-api
- description: The mirrored package/distribution trees themselves.
  name: Zhejiang University Repositories API
  slug: zhejiang-repositories-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.zju.edu.cn/english/
- group: company
  title: ''
  type: WebsiteChinese
  url: https://www.zju.edu.cn/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/zhejiang-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zhejiang-education-standards.yml
- group: other
  title: ''
  type: ResearchComputing
  url: https://mirrors.zju.edu.cn/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://libweb.zju.edu.cn/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://zdbk.zju.edu.cn/jwglxt/xtgl/login_slogin.html
- group: other
  title: ''
  type: ProductPage
  url: https://mirrors.zju.edu.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://mirrors.zju.edu.cn/docs/
- group: operate
  title: ''
  type: Support
  url: https://github.com/ZJUSCT/mirror-issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZJUSCT
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zjulug
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/zhejiang-university/
- group: auth
  title: ''
  type: Authentication
  url: authentication/zhejiang-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/zhejiang-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/zhejiang-errors.yml
- group: design
  title: ''
  type: Rules
  url: rules/zhejiang-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/zhejiang-vocabulary.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zhejiang-lifecycle.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zhejiang-context.jsonld
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zhejiang-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zhejiang-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zhejiang-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zhejiang-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zhejiang-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Zhejiang University (浙江大学, ZJU) is a comprehensive public research university in Hangzhou, Zhejiang Province, China — a C9 League and Double First-Class institution, ranked in the QS World University Rankings top 50, with strengths across AI, engineering, medicine, agriculture and the sciences. ZJU operates no central developer portal, no open data portal, no institution-operated research data repository and no documented public application API. Its verified institution-operated programmable footprint is three surfaces, all under its own zju.edu.cn registrable domain: a public open source software mirror at mirrors.zju.edu.cn that publishes a genuinely machine-readable service catalog (the MirrorZ data contract, 63 mirrored repositories, anonymous read); a Shibboleth SAML 2.0 Identity Provider registered in CARSI and reachable through eduGAIN; and a CAS unified single sign-on platform. Everything else on the public estate is either vendor software running on a ZJU hostname
  — the Huiwen library catalog, the undergraduate teaching management platform, the faculty profile system — or is gated behind campus network access. The library catalog has been deliberately withdrawn from the public internet. No OpenAPI, AsyncAPI, GraphQL, MCP server, agent card, robots.txt, security.txt or llms.txt is published anywhere on the institution''s own surface.'
examples:
- key_count: 6
  name: Zhejiang Mirrorz Example
  slug: zhejiang-mirrorz-example
finops:
- name: Zhejiang Finops
  service_category: Education
  slug: zhejiang-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zhejiang.png
json_schemas:
- name: Zhejiang University MirrorZ catalog document
  property_count: 4
  slug: zhejiang-mirrorz-document
jsonld:
- class_count: 13
  name: Zhejiang Context
  property_count: 3
  slug: zhejiang-context
layout: provider
modified: '2026-08-19'
name: Zhejiang University
nav: Providers
network: true
overview: 'Zhejiang University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Catalog API and Repositories API. Tagged areas include University, Higher Education, Education, Research, and China.


  The Zhejiang University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zhejiang University''s developer surface includes documentation, support, authentication, and 23 more developer resources.'
plans:
- name: Zhejiang Plans Pricing
  plan_count: 2
  slug: zhejiang-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Zhejiang Rate Limits
  slug: zhejiang-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Zhejiang University API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: zhejiang-rules
scopes:
- name: Zhejiang Scopes
  scope_count: 0
  slug: zhejiang-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 3.8
    contract_quality: 26.0
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 3.8
    operational_transparency: 23.7
  previous_composite: 34.4
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
    score: 61.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zhejiang/refs/heads/main/screenshots/zhejiang-2026-06-20T201856.png
security:
- kind: authentication
  name: Zhejiang Authentication
  slug: zhejiang-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Zhejiang Domain Security
  slug: zhejiang-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Zhejiang Vulnerability Disclosure
  slug: zhejiang-vulnerability-disclosure
  summary_line: disclosure policy published
slug: zhejiang
tags:
- University
- Higher Education
- Education
- Research
- China
- C9 League
- Double First-Class
- Identity Federation
- Single Sign-On
- Open Source Mirror
- Library
website: https://www.zju.edu.cn/english/
---
