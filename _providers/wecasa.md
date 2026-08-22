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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.wecasa.fr/
- group: operate
  title: ''
  type: Support
  url: https://help.wecasa.fr/fr/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.wecasa.fr/en/
- group: company
  title: ''
  type: Blog
  url: https://www.wecasa.fr/mag/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wecasa
- group: start
  title: ''
  type: SignUp
  url: https://www.wecasa.fr/pro
- group: start
  title: ''
  type: Login
  url: https://www.wecasa.fr/customer-area/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wecasa.fr/page/conditions-generales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wecasa.fr/page/politique-confidentialite
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.wecasa.fr/page/mentions-legales
- group: operate
  title: ''
  type: Contact
  url: https://www.wecasa.fr/page/contact
- group: company
  title: ''
  type: Careers
  url: https://careers.wecasa.fr/
- group: build
  title: ''
  type: Packages
  url: packages/wecasa-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wecasa-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wecasa-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Wecasa ships software only as an end-user product — a consumer booking app and a separate Wecasa Pro app for professionals — and every candidate developer hostname (api., developers., developer., docs., app., admin., partners.wecasa.fr) fails to resolve in DNS at all, so there is no portal, reference or contract to read; the /pro "become a partner" funnel is a human recruitment form that hands the professional a mobile app, not a partner API.
  evidence:
  - status: 200
    url: https://www.wecasa.fr/pro
  - status: 404
    url: https://www.wecasa.fr/openapi.json
  - status: 404
    url: https://www.wecasa.fr/graphql
  - status: 404
    url: https://www.wecasa.fr/llms.txt
  - status: 404
    url: https://www.wecasa.fr/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: Wecasa is a French on-demand home-services marketplace that connects households with vetted independent professionals who deliver the service at the customer's home. Its catalogue spans household cleaning and ironing, childcare and babysitting, mobile hairdressing, at-home beauty and nail care, massage and wellness, and personal fitness coaching. Customers book, schedule and pay through the Wecasa web site or the iOS/Android app; the professionals who fulfil the work run their business through the separate Wecasa Pro app. Founded in France and backed by Serena, the company operates in France, the United Kingdom, Germany, Austria and Switzerland. Wecasa publishes no public developer program, API reference or machine-readable contract — the platform is a consumer application and a partner-onboarding funnel, not a developer product.
image: https://www.wecasa.fr/assets/wecasa-social-logo-6c1be70d86b862e2d55d6968f50c56a9b37fc182ecadbfb12e1cad6ca8206a58.jpg
layout: provider
modified: '2026-08-17'
name: Wecasa
nav: Providers
network: true
overview: 'Wecasa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Marketplace, Home Services, and Beauty and Wellness.


  Wecasa''s developer surface includes support, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Wecasa Plans Pricing
  plan_count: 0
  slug: wecasa-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Wecasa Rate Limits
  slug: wecasa-rate-limits
score:
  band: emerging
  composite: 14.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: domain-security
  name: Wecasa Domain Security
  slug: wecasa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wecasa
tags:
- Company
- Consumer
- Marketplace
- Home Services
- Beauty and Wellness
- Cleaning
- Childcare
- On Demand
- France
- Mobile Apps
website: https://www.wecasa.fr/
---
