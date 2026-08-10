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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Private first-party HTTP API that backs the Firefly Health member web app and iOS/Android apps. Observed at https://api-prod.firefly.health with an /api/v2/ base path referenced by the members.firefly
  name: Firefly Health Member API
  slug: member-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firefly-health-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/firefly-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/firefly-health-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/firefly-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.fireflyhealth.com/
- group: other
  title: ''
  type: Forge
  url: https://forgeglobal.com/firefly-health_stock/
- group: company
  title: ''
  type: About
  url: https://www.fireflyhealth.com/about
- group: other
  title: ''
  type: HowItWorks
  url: https://www.fireflyhealth.com/how-it-works
- group: start
  title: ''
  type: SignUp
  url: https://members.firefly.health/signup/user-type
- group: start
  title: ''
  type: Login
  url: https://members.firefly.health/
- group: operate
  title: ''
  type: Support
  url: https://www.fireflyhealth.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.fireflyhealth.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.fireflyhealth.com/blog/newsroom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fireflyhealth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fireflyhealth.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.fireflyhealth.com/hipaa
- group: commercial
  title: ''
  type: PriceTransparency
  url: https://www.fireflyhealth.com/pricing-transparency
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fireflyhealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/firefly-health/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCkF9UhfHCuMvTtj8O_Jfv2Q
- group: company
  title: ''
  type: Careers
  url: https://www.fireflyhealth.com/careers
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/firefly-health-telemedicine/id1396647655
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.fireflyhealth2
created: '2026-08-01'
description: 'Firefly Health is a virtual-first primary care practice and clinically integrated health plan founded in 2016 and headquartered in Watertown, Massachusetts. Members get a dedicated care team - a primary care physician, nurse practitioner, health guide and behavioral health specialist - reachable by chat and video through the Firefly Health app, backed by the Firefly Nearby network for in-person, at-home and specialty care. Firefly sells an employer-sponsored alternative health plan alongside its virtual primary care service, and in 2025 became the first national primary care practice to earn NCQA Virtual Care Accreditation. Firefly publishes no public developer program, portal, documentation or specification: the member web and mobile apps are served by a private first-party API at api-prod.firefly.health under an /api/v2/ base path. Included Health signed an agreement to acquire Firefly Health in July 2026.'
image: https://cdn.sanity.io/images/xgbrv2vi/production/4095bfda2782d4ea0e578f21c79132dfa867ffac-1200x630.png?w=1200&h=630
layout: provider
modified: '2026-08-01'
name: Firefly Health
nav: Providers
network: true
overview: 'Firefly Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Plans, Virtual Care, and Primary Care.


  Firefly Health''s developer surface includes signup flow, support, FAQ, engineering blog, YouTube channel, and 18 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 23.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 23.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firefly-health/refs/heads/main/screenshots/firefly-health-2026-08-07T165314.png
security:
- kind: domain-security
  name: Firefly Health Domain Security
  slug: firefly-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: firefly-health
tags:
- Company
- Healthcare
- Health Plans
- Virtual Care
- Primary Care
- Telehealth
- Health Insurance
- Employee Benefits
- Digital Health
website: https://www.fireflyhealth.com/
---
