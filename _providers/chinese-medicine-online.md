---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chinese-medicine-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.tcmmooc.com/
- group: company
  title: ''
  type: CorporateWebsite
  url: http://www.tcmlive.com/
- group: company
  title: ''
  type: About
  url: http://www.tcmmooc.com/page/aboutus
- group: operate
  title: ''
  type: ContactUs
  url: http://www.tcmmooc.com/page/contactus
- group: operate
  title: ''
  type: Support
  url: http://www.tcmmooc.com/page/kefu
- group: start
  title: ''
  type: SignUp
  url: http://www.tcmmooc.com/register/registerForm
- group: start
  title: ''
  type: Login
  url: http://www.tcmmooc.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: http://www.tcmmooc.com/page/useragreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://www.tcmmooc.com/page/privacy
- group: company
  title: ''
  type: News
  url: http://www.tcmlive.com/pages/news.html
- group: company
  title: ''
  type: Careers
  url: http://www.tcmlive.com/pages/recruit.html
- group: other
  title: ''
  type: MobileAppiOS
  url: https://apps.apple.com/cn/app/id1032928764
- group: other
  title: ''
  type: MobileAppAndroid
  url: https://a.app.qq.com/o/simple.jsp?pkgname=com.tcmopen.tcmmooc
coverage:
  checked: '2026-08-09'
  detail: 中医在线 ships a TCM course web platform, an iOS/Android app and an AI/SaaS clinic product line, but its only backend route (http://www.tcmmooc.com/api) answers with a PHP "Whoops" error page, every spec and /.well-known/ path 404s on both tcmmooc.com and the corporate site tcmlive.com, and a POST to /mcp returns the same soft-404 error page as a nonsense control path — there is no developer portal, SDK, webhook surface or published contract anywhere on the company's public surface.
  evidence:
  - status: 404
    url: http://www.tcmmooc.com/openapi.json
  - status: 404
    url: http://www.tcmmooc.com/.well-known/agent-card.json
  - status: 500
    url: http://www.tcmmooc.com/api
  - status: 404
    url: http://www.tcmlive.com/openapi.json
  - status: 200
    url: http://www.tcmlive.com/pages/saas.html
  - status: 200
    url: https://equityzen.com/company/chinesemedicineonline/
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: Chinese Medicine Online (中医在线) is a Beijing-based traditional Chinese medicine (TCM) continuing-education and academic-exchange platform, founded in 2015 and operated by Beijing Universe In Nutshell Technology Co., Ltd. (北京果壳宇宙教育科技有限公司) on behalf of the Beijing TCM Online Education Center (北京中医在线教育中心). Through its web platform at tcmmooc.com and its iOS/Android app, it publishes recorded and live video continuing-education courses from national TCM masters and senior practitioners, runs the 经方学社 (Classical Formulas Society) learning community and 精医社 membership, livestreams academic conferences, and sells course material through a paid knowledge marketplace. The company states a catalogue of roughly 19,600 courses from 3,900+ TCM experts and around 4 million registered users, the majority of them licensed practitioners. It has since extended into AI and SaaS for grassroots clinics, including the "Yi Yin" (伊尹) TCM classical-reasoning large language model launched in Songxian,
  Henan in September 2025, and clinic workflow tooling (prescription, patient and follow-up management). The platform is delivered strictly as an end-user web and mobile product — it publishes no public API, SDK, developer portal or machine-readable contract of any kind.
image: https://is1-ssl.mzstatic.com/image/thumb/Purple112/v4/4a/e6/36/4ae6364b-437a-5d4d-ad52-9728aa9930e6/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/512x512bb.jpg
layout: provider
modified: '2026-08-09'
name: Chinese Medicine Online
nav: Providers
network: true
overview: 'Chinese Medicine Online is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Traditional Chinese Medicine, Healthcare, Medical Education, Continuing Medical Education, and Online Learning.


  Chinese Medicine Online''s developer surface includes support, signup flow, product news, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 13.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Chinese Medicine Online Domain Security
  slug: chinese-medicine-online-domain-security
  summary_line: DMARC
slug: chinese-medicine-online
tags:
- Traditional Chinese Medicine
- Healthcare
- Medical Education
- Continuing Medical Education
- Online Learning
- E-Learning
- Artificial Intelligence
- China
- SaaS
- Company
website: http://www.tcmmooc.com/
---
