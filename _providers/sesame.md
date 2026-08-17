---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://sesamecare.com
- group: company
  title: ''
  type: Blog
  url: https://sesamecare.com/blog
- group: operate
  title: ''
  type: Support
  url: https://sesamecare.com/faq
- group: start
  title: ''
  type: SignUp
  url: https://sesamecare.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sesamecare.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sesamecare.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sesamecare
- group: commercial
  title: ''
  type: Pricing
  url: https://sesamecare.com/join/membership
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sesame-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/sesame-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sesame-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sesame-llms.txt
coverage:
  checked: '2026-08-15'
  detail: 'Sesame ships only an end-user telehealth product: the single API host it operates, https://api.sesamecare.com/graphql, answers 401 to an anonymous GET and rejects introspection with "GraphQL introspection is not allowed by Apollo Server", and there is no developer portal, reference, spec or SDK anywhere — the partner page offers an email address (partners@sesamecare.com) instead of an integration surface.'
  evidence:
  - status: 401
    url: https://api.sesamecare.com/graphql
  - status: 404
    url: https://api.sesamecare.com/openapi.json
  - status: 404
    url: https://sesamecare.com/openapi.json
  - status: 404
    url: https://sesamecare.com/llms.txt
  - status: 404
    url: https://sesamecare.com/.well-known/agent-card.json
  - status: 404
    url: https://developer.sesamecare.com/
  - status: 200
    url: https://sesamecare.com/partners/partner-with-sesame
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Sesame is a direct-to-consumer telehealth marketplace that connects patients with board-certified clinicians for affordable, transparent, cash-pay virtual and in-person care. Patients browse and book pay-per-visit appointments starting around $34 across urgent care, prescription refills, weight loss and GLP-1 treatment, mental health, women's health, dermatology, pediatrics and more, with no insurance required and up-front pricing. The company also offers a SesamePlus membership, a mobile app, provider tooling for listing a practice, and Sesame @ Work employer plans. Sesame is backed by General Catalyst, GV, Matrix Partners, Redpoint Ventures, Spark Capital and SV Angel. As of this enrichment pass Sesame publishes a consumer web and mobile experience but no public developer API, developer portal, SDKs, or OpenAPI surface. It operates a private Apollo GraphQL endpoint at api.sesamecare.com/graphql that backs its own apps — anonymous requests return 401 and introspection is disabled
  in production — and its public GitHub organization publishes 17 general-purpose Node/TypeScript utility packages under the @sesamecare-oss npm scope rather than first-party API client SDKs.
image: https://sesamecare.com/assets/sesame-twitter.png
layout: provider
modified: '2026-08-15'
name: Sesame
nav: Providers
network: true
overview: 'Sesame is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telehealth, Healthcare, Digital Health, and Telemedicine.


  Sesame''s developer surface includes engineering blog, support, signup flow, pricing, and 8 more developer resources.'
plans:
- name: Sesame Plans Pricing
  plan_count: 3
  slug: sesame-plans-pricing
random_paper: 42
score:
  band: emerging
  composite: 22.2
  delta: 7.8
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: domain-security
  name: Sesame Domain Security
  slug: sesame-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sesame
tags:
- Company
- Telehealth
- Healthcare
- Digital Health
- Telemedicine
- Marketplace
- Consumer Health
- Prescriptions
website: https://sesamecare.com
---
