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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vida-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vida-health-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/vida-health-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vida-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/vida-health-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.vida.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vida.com/resource-library/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vida.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://support.vida.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vidahealth
- group: start
  title: ''
  type: SignUp
  url: https://www.vida.com/clients/onboarding/step/account-creation
- group: start
  title: ''
  type: Login
  url: https://vida.com/accounts/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vida.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vida.com/privacy-policy/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.vida.com/contact-us/
- group: company
  title: ''
  type: NewsRoom
  url: https://www.vida.com/news-center/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/vida-health_stock/
coverage:
  checked: '2026-08-15'
  detail: 'Vida''s production API host api.vida.com is live but returns a uniform HTTP 401 ({"error": "Invalid or expired access token"}) on every path — including /openapi.json, /graphql, /mcp and the whole /.well-known/ tree, so even the anonymous OAuth discovery documents RFC 8414 and RFC 9728 require are behind the token wall — and there is no developer host at all (developer.vida.com, developers.vida.com and docs.vida.com have no DNS record); the Partners page advertises "streamlined integrations with existing healthcare ecosystems" and "smooth and secure data sharing" but publishes no reference, spec or standard, routing every technical question to a get-a-demo form.'
  evidence:
  - status: 401
    url: https://api.vida.com/openapi.json
  - status: 401
    url: https://api.vida.com/.well-known/oauth-protected-resource
  - status: 401
    url: https://api.vida.com/graphql
  - status: 401
    url: https://api.vida.com/mcp
  - status: 404
    url: https://www.vida.com/.well-known/agent-card.json
  - status: 404
    url: https://www.vida.com/llms.txt
  - status: 404
    url: https://www.vida.com/pricing/
  - status: 200
    url: https://www.vida.com/partners/
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: 'Vida Health is a San Francisco-based virtual care company founded in 2014 that combines an AI-powered mobile app with a national network of licensed clinicians, coaches and therapists to prevent, manage and reverse chronic cardiometabolic and behavioral health conditions including obesity, diabetes, hypertension, depression and anxiety. Vida sells a turnkey enterprise programme to employers and health plans, layering GLP-1 prescribing and clinical oversight on top of behavioral coaching, and its platform ingests real-time readings from more than 100 connected devices and consumer health apps to feed outcome reporting back to its enterprise buyers. Vida publishes no public developer portal or API documentation: the API host api.vida.com is live but returns 401 on every path, and data/EHR integration for health plans and employers is arranged through enterprise sales rather than self-service onboarding.'
image: https://static.vida.com/wp-content/uploads/2025/03/20211650/Enterprise-3.png
layout: provider
modified: '2026-08-15'
name: Vida Health
nav: Providers
network: true
overview: 'Vida Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Virtual Care.


  Vida Health''s developer surface includes engineering blog, support, signup flow, and 14 more developer resources.'
plans:
- name: Vida Health Plans Pricing
  plan_count: 0
  slug: vida-health-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Vida Health Rate Limits
  slug: vida-health-rate-limits
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 20.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Vida Health Domain Security
  slug: vida-health-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: vida-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Virtual Care
- Chronic Care
- Behavioral Health
- Telehealth
- Employee Benefits
- Health Plans
website: https://www.vida.com/
---
