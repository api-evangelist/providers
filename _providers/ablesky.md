---
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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.ablesky.com/
- group: operate
  title: ''
  type: Support
  url: https://www.ablesky.com/product/index/fqa
- group: operate
  title: ''
  type: HelpCenter
  url: https://xiaopu.ablesky.com/community.do?action=toHelpCenter
- group: start
  title: ''
  type: SignUp
  url: https://www.ablesky.com/org/apply/open?organizationProperty=organization
- group: start
  title: ''
  type: Login
  url: https://www.ablesky.com/login.do
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ablesky
- group: other
  title: ''
  type: x-Downloads
  url: https://www.ablesky.com/product/index/download
- group: build
  title: ''
  type: Tools
  url: https://product.ablesky.com/
- group: other
  title: ''
  type: x-OpenSearch
  url: https://www.ablesky.com/s/opensearch.xml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/ablesky
- group: design
  title: ''
  type: Conformance
  url: conformance/ablesky-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ablesky-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/ablesky-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ablesky-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ablesky-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ablesky-llms.txt
coverage:
  checked: '2026-09-06'
  detail: AbleSky's own FAQ says a school can embed the AbleSky teaching platform inside its existing system and share learners so students sign in once, but that integration is described only in prose — there is no developer host at all (open./developer./docs./openapi.ablesky.com do not answer), no spec at any probed path, and the one host that does exist, api.ablesky.com, answers a blanket nginx/1.6.0 403 on every path including "/".
  evidence:
  - status: 200
    url: https://www.ablesky.com/product/index/fqa
  - status: 404
    url: https://www.ablesky.com/openapi.json
  - status: 404
    url: https://www.ablesky.com/swagger.json
  - status: 404
    url: https://www.ablesky.com/graphql
  - status: 403
    url: https://api.ablesky.com/openapi.json
  - status: 404
    url: https://www.ablesky.com/.well-known/security.txt
  - status: 404
    url: https://www.ablesky.com/llms.txt
  - status: 200
    url: https://www.ablesky.com/s/opensearch.xml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-06'
description: 'AbleSky, Inc. (能力天空) is an online-education SaaS company incorporated in 2007 in Mountain View, California, operating in China through its wholly owned subsidiary 能力天空科技（北京）有限公司 in Beijing. Its platform lets a school, training institution or instructor stand up a branded online school — website, Android and iOS apps, WeChat micro-school and official account — with course hosting, live classes, exams, educational-administration workflow, course distribution and learner payment collection, marketed as roughly 3,000 features to training organisations across more than 2,000 Chinese cities. It also sells an independent deployment onto a customer''s own cloud or hardware. It publishes NO public API: contract discovery on 2026-09-06 found no OpenAPI, AsyncAPI, GraphQL SDL, WSDL, gRPC service, MCP server, agent card, SDK or developer portal on any AbleSky host. The one machine-readable document it does publish is a valid, auto-discoverable OpenSearch 1.1 course-search descriptor.'
image: https://img.ablesky.cn/stata/images/favicon_7ca206fd.ico
layout: provider
modified: '2026-09-06'
name: AbleSky
nav: Providers
network: true
overview: 'AbleSky is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, E-Learning, Online Courses, and Learning Management.


  AbleSky''s developer surface includes support, signup flow, tooling, and 13 more developer resources.'
plans:
- name: Ablesky Plans Pricing
  plan_count: 2
  slug: ablesky-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Ablesky Rate Limits
  slug: ablesky-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 12.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ablesky Domain Security
  slug: ablesky-domain-security
  summary_line: TLSv1.2
slug: ablesky
tags:
- Company
- Education
- E-Learning
- Online Courses
- Learning Management
- SaaS
- Training
- K-12
- Live Streaming
- Video
- China
website: https://www.ablesky.com/
---
