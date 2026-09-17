---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-09-16'
api_count: 26
apis:
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: diy材料申请信息控制层
  name: 51offer Diym API
  slug: 51offer-diym-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: 顾问控制层
  name: 51offer Ng Adviser API
  slug: 51offer-ngadviser-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: 大总管服务控制层
  name: 51offer Ng Alliance API
  slug: 51offer-ngalliance-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: 渠道限时兑换礼包相关控制层
  name: 51offer Ng Delivery Channel API
  slug: 51offer-ngdeliverychannel-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: Diy服务控制层
  name: 51offer Ng Diy API
  slug: 51offer-ngdiy-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: Diy申请支付服务控制
  name: 51offer Ngdiyapplypay API
  slug: 51offer-ngdiyapplypay-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: diy选校控制器
  name: 51offer Ngdiychoose School API
  slug: 51offer-ngdiychooseschool-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: diy定位通知服务
  name: 51offer Ngdiypositioningnotice API
  slug: 51offer-ngdiypositioningnotice-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: Diy选校控制器前置
  name: 51offer Ngdiyselectschool API
  slug: 51offer-ngdiyselectschool-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: diy单品页控制器
  name: 51offer Ngdiysinglepage API
  slug: 51offer-ngdiysinglepage-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: 双十二活动服务控制层
  name: 51offer Ng Double Twelve API
  slug: 51offer-ngdoubletwelve-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: Enroll Controller
  name: 51offer Ng Enroll API
  slug: 51offer-ngenroll-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: GPA计算器
  name: 51offer Ng Gpa Calc API
  slug: 51offer-nggpacalc-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: H5首页控制层
  name: 51offer Ng Home API
  slug: 51offer-nghome-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: 语培口语批改
  name: 51offer Ng Lan Correct API
  slug: 51offer-nglancorrect-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: 商城控制层
  name: 51offer Ng Mall API
  slug: 51offer-ngmall-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: 51品牌节支付优惠券
  name: 51offer Ng Pay Coupon API
  slug: 51offer-ngpaycoupon-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: 文章图片更新控制层
  name: 51offer Ng Pic API
  slug: 51offer-ngpic-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: 订单退款控制层
  name: 51offer Ngrefund API
  slug: 51offer-ngrefund-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: Sign Controller
  name: 51offer Ng Sign API
  slug: 51offer-ngsign-api
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: runway用户控制层
  name: 51offer Ng User Info API
  slug: 51offer-nguserinfo-api
artifact_total: 25
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/overlays/51offer-horizon-site-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/51offer-horizon-site-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/security/51offer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/51offer-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/authentication/51offer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/51offer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.51offer.com/
- group: company
  title: ''
  type: About
  url: https://www.51offer.com/aboutus/
- group: start
  title: ''
  type: SignUp
  url: https://account.51offer.com/register.html
- group: start
  title: ''
  type: Login
  url: https://account.51offer.com/login.html
- group: operate
  title: ''
  type: Support
  url: https://account.51offer.com/user/feedback.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.51offer.com/aboutus/contract.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.51offer.com/aboutus/protection.html
- group: company
  title: ''
  type: Blog
  url: https://51offer.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/51offer
- group: company
  title: ''
  type: Partners
  url: https://www.51offer.com/aboutus/cooperation.html
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/packages/51offer-packages.yml
  title: ''
  type: Packages
  url: packages/51offer-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/conventions/51offer-conventions.yml
  title: ''
  type: Conventions
  url: conventions/51offer-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/conformance/51offer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/51offer-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/lifecycle/51offer-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/51offer-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/plans/51offer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/51offer-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/rate-limits/51offer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/51offer-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/llms/51offer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/51offer-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/51offer/refs/heads/main/mcp/51offer-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/51offer-mcp.yml
created: '2026-09-05'
description: 51offer (Shanghai Huizhi Business Consulting Co., Ltd. / 上海汇紫商务咨询有限公司) is a Shanghai-based one-stop online study-abroad platform for Chinese students applying to universities in the United Kingdom, Australia, the United States, New Zealand, Japan and Singapore. Its consumer surface covers DIY application filing, AI/big-data school and course matching, personal-statement and document services, language training (IELTS/TOEFL), adviser and channel-partner services, a study-abroad mall with online contract signing, payment and refund flows, a GPA calculator and a student content and community section. 51offer publishes no developer program, but its official site www.51offer.com serves a public, unauthenticated Swagger 1.2 API listing at /api-docs ("Horizon Site APIConfig List / 51offer官网所有开放接口清单") describing 24 controllers and several hundred JSON operations, and that listing is the machine-readable contract profiled here.
image: https://static.51offer.com/skin/common/images/favicon.ico
layout: provider
modified: '2026-09-05'
name: 51offer
nav: Providers
network: true
overview: '51offer publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Diym API, Ng Adviser API, Ng Alliance API, and 18 more. Tagged areas include Company, Education, Study Abroad, Higher Education, and University Applications.


  51offer''s developer surface includes authentication, signup flow, support, engineering blog, and 18 more developer resources.'
plans:
- name: 51Offer Plans Pricing
  plan_count: 0
  slug: 51offer-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: 51Offer Rate Limits
  slug: 51offer-rate-limits
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 16.4
    developer_ergonomics: 24.4
    discoverability: 74.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 22.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 21
      marker_coverage: 100.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: 51Offer Authentication
  slug: 51offer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: 51Offer Domain Security
  slug: 51offer-domain-security
  summary_line: TLSv1.2
slug: 51offer
tags:
- Company
- Education
- Study Abroad
- Higher Education
- University Applications
- Students
- Language Training
- E-Commerce
- China
- Consulting
website: https://www.51offer.com/
---
