---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/may-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.may.app/
- group: company
  title: ''
  type: About
  url: https://www.may.app/mission-may/
- group: company
  title: ''
  type: Blog
  url: https://www.may.app/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.may.app/feed/
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/may-fdff94332145/fr/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.may.app/cgu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.may.app/politique-de-confidentialite/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/may-sante/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/MaySanteParentalite/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/may-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/may-conformance.yml
coverage:
  checked: '2026-08-17'
  detail: May is a direct-to-consumer mobile health app for parents — the whole public surface is a 51-page WordPress marketing site in three locales plus a seven-collection Intercom help center whose only partner-facing section routes health professionals, press and partnerships to an email conversation, and the sole backend hostname in the company's public DNS (capig.may.app, found in certificate-transparency logs) is a dangling CNAME to a deleted AWS Kubernetes ingress load balancer in eu-west-3.
  evidence:
  - status: 404
    url: https://www.may.app/openapi.json
  - status: 404
    url: https://www.may.app/graphql
  - status: 404
    url: https://www.may.app/.well-known/agent-card.json
  - status: 404
    url: https://www.may.app/.well-known/agent.json
  - status: 404
    url: https://www.may.app/.well-known/security.txt
  - status: 404
    url: https://www.may.app/llms.txt
  - status: 200
    url: https://www.may.app/page-sitemap.xml
  - status: 200
    url: https://www.may.app/wp-json/
  - status: 301
    url: https://may-sante.com/
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: May is a French digital-health company, operated by LN CARE SAS, whose mobile app supports future and new parents from fertility and pregnancy through the first years of a child's life. It pairs a medical messaging service staffed by French-qualified midwives, pediatric nurses and doctors — answering questions seven days a week from 8am to 10pm — with an expert-reviewed content library, roughly hour-long audio masterclasses, everyday tracking tools for sleep, feeding and weight, and Mya, an in-app AI medical assistant. Founded in Paris in 2020 by Cécilia Creuzet, Antoine Creuzet and Adrien Brunet, it reported more than 400,000 users and a team of around 80 health professionals, raised €7M in September 2024 to expand into Spain and the United Kingdom, and also sells a parental-support benefit to employers. It was surfaced as a portfolio company of Serena and profiled in the API Evangelist network; it publishes a consumer marketing site, a blog and an Intercom help center, but
  no public developer program, no API reference and no machine-readable API contract of any kind.
image: https://www.may.app/wp-content/uploads/2025/05/logo_may_sapin_fond_transparent.png
layout: provider
modified: '2026-08-17'
name: May
nav: Providers
network: true
overview: 'May is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Parenting, and Pregnancy.


  May''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: May Plans Pricing
  plan_count: 0
  slug: may-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: May Rate Limits
  slug: may-rate-limits
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 13.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/may/refs/heads/main/screenshots/may-2026-09-02T150443.png
security:
- kind: domain-security
  name: May Domain Security
  slug: may-domain-security
  summary_line: TLSv1.3 · DMARC
slug: may
tags:
- Company
- Health
- Digital Health
- Parenting
- Pregnancy
- Maternal Health
- Consumer Health
- Mobile Application
- Employee Benefits
- France
website: https://www.may.app/
---
