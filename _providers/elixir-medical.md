---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The WordPress core REST API (wp/v2 namespace) served by elixirmedical.com, the Elixir Medical corporate website. It exposes the site's pages, news posts, media library, categories, tags, comments, aut
  name: Elixir Medical Website Content API (WordPress REST)
  slug: elixir-medical-wordpress-content
artifact_total: 6
collections:
- collection_type: open
  name: Elixir Medical Website Content API (WordPress REST wp/v2)
  slug: open-elixir-medical-wordpress-content
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elixir-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elixirmedical.com/
- group: company
  title: ''
  type: About
  url: https://elixirmedical.com/us/about-us/
- group: operate
  title: ''
  type: Support
  url: https://elixirmedical.com/us/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://elixirmedical.com/ous/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elixirmedical.com/us/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elixirmedical.com/us/terms-of-use/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/elixir-medical_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elixir-medical-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elixir-medical-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elixir-medical-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elixir-medical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elixir-medical-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elixir-medical-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elixir-medical-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elixir-medical-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elixir-medical-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: Elixir Medical Corporation is a privately held medical device company headquartered in Milpitas, California, developing implant and interventional platforms for coronary and peripheral artery disease. Its DynamX sirolimus-eluting coronary bioadaptor is designed to restore vessel pulsatility and compliance rather than permanently cage the artery, and holds a European CE mark, Japanese PMDA approval and a U.S. FDA Breakthrough Device designation; the LithiX Hertz Contact intravascular lithotripsy system and the DESyne family of drug-eluting stents round out the portfolio. Elixir Medical operates no developer program and publishes no product, device or clinical API. The only machine-readable surface it serves is the default WordPress REST API of its corporate marketing site, alongside an SEO-plugin-generated llms.txt.
image: https://elixirmedical.com/wp-content/uploads/2023/09/New-Elixir-Logo.png
layout: provider
modified: '2026-08-12'
name: Elixir Medical
nav: Providers
network: true
overview: 'Elixir Medical publishes 1 API on the [APIs.io](https://apis.io/) network: Website Content API (WordPress REST). Tagged areas include Company, Medical Devices, Health, Cardiovascular, and Coronary Intervention.


  Elixir Medical''s developer surface includes support, engineering blog, authentication, and 15 more developer resources.'
plans:
- name: Elixir Medical Plans Pricing
  plan_count: 0
  slug: elixir-medical-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Elixir Medical Rate Limits
  slug: elixir-medical-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 18.2
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 24.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Elixir Medical Authentication
  slug: elixir-medical-authentication
  summary_line: http/none · 2 schemes
- kind: domain-security
  name: Elixir Medical Domain Security
  slug: elixir-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: elixir-medical
tags:
- Company
- Medical Devices
- Health
- Cardiovascular
- Coronary Intervention
- Implants
- Life Sciences
- Content
- WordPress
website: https://elixirmedical.com/
---
