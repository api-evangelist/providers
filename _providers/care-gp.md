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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/care-gp/refs/heads/main/plans/care-gp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/care-gp-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/care-gp/refs/heads/main/security/care-gp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/care-gp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caregp.com.au/
- group: start
  title: ''
  type: Login
  url: https://agent.caregp.com.au/login
- group: commercial
  title: ''
  type: Pricing
  url: https://caregp.com.au/pricing
- group: auth
  title: ''
  type: Compliance
  url: https://caregp.com.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caregp/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@CareGP-aus
created: '2026-07-17'
description: Care GP is a Sydney-based healthcare technology company (Y Combinator Summer 2026) building a suite of AI agents that automate the administrative and operational work of Australian general practice clinics. Its products include Samantha (medical document allocation that files inbound emails, faxes, and scans), Veronica (24/7 inbound and outbound phone and booking management), and a Billing beta for billing and debt-collection automation. Care GP states it is ISO 27001 certified with onshore Australian data storage, multi-factor authentication, and encryption, and reports serving 400+ clinic operators. As of this enrichment pass the company exposes a customer web application (agent.caregp.com.au) but no public developer portal, API documentation, or OpenAPI definition.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/care-gp.png
layout: provider
modified: '2026-07-18'
name: Care GP
nav: Providers
network: true
overview: 'Care GP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Tech, Artificial Intelligence, and AI Agents.


  Care GP''s developer surface includes pricing, YouTube channel, and 6 more developer resources.'
plans:
- name: Care Gp Plans Pricing
  plan_count: 3
  slug: care-gp-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.3
  facets:
    access_clarity: 56.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 8.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/care-gp/refs/heads/main/screenshots/care-gp-2026-07-25T204525.png
security:
- kind: domain-security
  name: Care Gp Domain Security
  slug: care-gp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: care-gp
tags:
- Company
- Healthcare
- Health Tech
- Artificial Intelligence
- AI Agents
- Primary Care
- Medical Practice
- Automation
- Australia
- Y Combinator
website: https://caregp.com.au/
---
