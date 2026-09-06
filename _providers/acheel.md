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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acheel-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acheel-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acheel-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/acheel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acheel-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/acheel-components.yml
- group: company
  title: ''
  type: Website
  url: https://www.acheel.com/
- group: company
  title: ''
  type: About
  url: https://v2.acheel.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://faq.acheel.com/fr
- group: operate
  title: ''
  type: FAQ
  url: https://faq.acheel.com/fr
- group: start
  title: ''
  type: Login
  url: https://v2.acheel.com/customer-areas
- group: company
  title: ''
  type: Partners
  url: https://www.charlee.fr/
- group: company
  title: ''
  type: Careers
  url: https://v2.acheel.com/join-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://v2.acheel.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://v2.acheel.com/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://v2.acheel.com/legal-notice
coverage:
  checked: '2026-08-17'
  detail: Acheel's own partner FAQ answered "Avez-vous des APIs ?" with "nous mettons à votre disposition nos APIs", but that partner site (partners.acheel.com) now 301s to the Charlee broker marketing brand and the only route to the API is the broker partnership form at charlee.fr/registration — no reference, no base URL and no spec was ever published, and the broker console back.charlee.fr is a noindex login.
  evidence:
  - status: 301
    url: https://partners.acheel.com/
  - status: 200
    url: https://www.charlee.fr/registration
  - status: 200
    url: https://back.charlee.fr/
  - status: 404
    url: https://v2.acheel.com/openapi.json
  - status: 0
    url: https://api.acheel.com/
  reason: sales-gate
  state: gated
created: '2026-08-17'
description: 'Acheel is a French digital insurance company — a néo-assureur that carries its own insurance licence rather than broking someone else''s. Founded in 2020 by Ralph Ruimy and Francky Défossé, it received its ACPR agrément and launched in 2021, and now reports more than 800,000 policyholders. ACHEEL SA (879 605 350 RCS Paris) underwrites; ACHEEL FRANCE (ORIAS 21003575) distributes. The range spans nine lines — habitation, auto, santé, animaux, PNO (propriétaire non occupant), emprunteur, scolaire, protection juridique and RC pro — sold 100% digitally, with a quote in about two minutes and subscription in five. Roughly 70% of revenue comes from B2B2C distribution: partner brokers are served under the Charlee brand (charlee.fr, broker portal "Acheel Omega" at back.charlee.fr) and partners embed a per-tenant white-label customer area served from *.widget.acheel.com. Acheel''s own partner FAQ stated it makes its APIs available to partners ("nous mettons à votre disposition nos APIs
  afin de vous faire bénéficier de notre Tech et de nos produits"), but no developer portal, API reference, base URL or machine-readable specification is published anywhere on its public surface; API access travels with a brokerage partnership. Acheel is a certified B Corp.'
image: https://v2.acheel.com/assets/images/footer/acheel_footer_logo.svg
layout: provider
modified: '2026-08-17'
name: Acheel
nav: Providers
network: true
overview: 'Acheel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech Insurtech, Insurance, Insurtech, and Digital Insurance.


  Acheel''s developer surface includes support, FAQ, legal docs, and 13 more developer resources.'
plans:
- name: Acheel Plans Pricing
  plan_count: 0
  slug: acheel-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Acheel Rate Limits
  slug: acheel-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 14.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acheel/refs/heads/main/screenshots/acheel-2026-09-02T144111.png
security:
- kind: domain-security
  name: Acheel Domain Security
  slug: acheel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acheel
tags:
- Company
- Fintech Insurtech
- Insurance
- Insurtech
- Digital Insurance
- Home Insurance
- Auto Insurance
- Health Insurance
- Pet Insurance
- White Label
- B2B2C
- Embedded Insurance
- France
website: https://www.acheel.com/
---
