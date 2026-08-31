---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: A live Azure API Management gateway operated by Solera Health on its own api.soleranetwork.com domain, used for payer, employer and digital-health-partner integrations into the HALO platform. Every an
  name: Solera Health Integrations API
  slug: solera-health-integrations-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.soleranetwork.com/
- group: company
  title: ''
  type: Blog
  url: https://www.soleranetwork.com/news-and-updates
- group: operate
  title: ''
  type: Support
  url: https://www.soleranetwork.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.gosolera.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soleranetwork.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soleranetwork.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.soleranetwork.com/trust-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SoleraHealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/solera-health
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solera-health-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/solera-health-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/solera-health-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/solera-health-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solera-health-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/solera-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solera-health-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solera-health-llms.txt
coverage:
  checked: '2026-08-28'
  detail: api.soleranetwork.com is a live Azure API Management gateway on Solera Health's own domain, but its developer portal at solera-api-gateway.developer.azure-api.net still serves Azure's default "The content hasn't been published yet" placeholder, so the reference and spec exist only inside a signed payer or digital-health-partner integration and every anonymous path returns the APIM JSON 404.
  evidence:
  - status: 200
    url: https://solera-api-gateway.developer.azure-api.net/
  - status: 404
    url: https://api.soleranetwork.com/openapi.json
  - status: 404
    url: https://api.soleranetwork.com/swagger.json
  - status: 404
    url: https://www.soleranetwork.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-28'
description: Solera Health is a Phoenix, Arizona based preventive-care benefits manager that acts as a single integration point between health plans, employers and a curated network of non-clinical digital health providers. Its HALO omni-condition management platform lets a payer or employer contract, configure, enroll and report across eight condition networks - weight management, diabetes prevention and management, hypertension, behavioral and mental health, musculoskeletal, tobacco cessation, women's health and digestive health - spanning 25+ partner point solutions including Calm, Headspace, Lyra Health, Sword Health, WeightWatchers and Dario Health, alongside customer contracted solutions Solera did not source. Solera operates an Azure API Management gateway on its own domain for those partner and payer integrations, but publishes no public developer portal, API reference or machine-readable contract.
image: https://cdn.prod.website-files.com/66a2aeab52cd6404170ea41b/66c8b934c5e0cc64b9bbd10c_Solera.svg
layout: provider
modified: '2026-08-28'
name: Solera Health
nav: Providers
network: true
overview: 'Solera Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Benefits.


  Solera Health''s developer surface includes engineering blog, support, signup flow, and 14 more developer resources.'
plans:
- name: Solera Health Plans Pricing
  plan_count: 0
  slug: solera-health-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Solera Health Rate Limits
  slug: solera-health-rate-limits
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.6
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Solera Health Domain Security
  slug: solera-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Solera Health Trust Center
  slug: solera-health-trust-center
  summary_line: SOC 2 Type 2, HITRUST CSF Certified (r2), HIPAA, FIPS 140-2 (key management)
slug: solera-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Benefits
- Employee Benefits
- Health Plans
- Payer
- Provider Network
- Chronic Condition Management
- Preventive Care
- Telehealth
website: https://www.soleranetwork.com/
---
