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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.renibus.com/
- group: company
  title: ''
  type: About
  url: https://www.renibus.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.renibus.com/news-and-events/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.renibus.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.renibus.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.renibus.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.renibus.com/terms-and-conditions/
- group: company
  title: ''
  type: Careers
  url: https://www.renibus.com/careers/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/renibus-therapeutics-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/renibus-therapeutics_stock/
coverage:
  checked: '2026-08-05'
  detail: Rénibus is a clinical-stage drug developer whose entire public web presence is a ten-page WordPress/Avada marketing site (about, approach, patients, news, careers, contact, policies) with no developer, docs, or API section; api./developer./docs./portal.renibus.com do not resolve in DNS and every contract-discovery path returns 404 — the only machine-readable endpoint on the host is the generic WordPress /wp-json/ CMS route, which is not a product API.
  evidence:
  - status: 404
    url: https://www.renibus.com/openapi.json
  - status: 404
    url: https://www.renibus.com/.well-known/agent-card.json
  - status: 404
    url: https://www.renibus.com/.well-known/security.txt
  - status: 404
    url: https://www.renibus.com/llms.txt
  - status: 200
    url: https://www.renibus.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Rénibus Therapeutics is a privately held clinical-stage biopharmaceutical company headquartered in Southlake, Texas, developing treatments for cardio, renal and metabolic disease. Its pipeline is led by veverimer, a non-absorbed polymer in Phase 3 for metabolic acidosis in chronic kidney disease, and RBT-1 (stannic protoporfin / iron sucrose), a first-in-class intravenous pharmacologic preconditioning agent given 24-48 hours before non-emergent cardiac surgery to reduce post-operative complications, which holds FDA Breakthrough Therapy and Fast Track designations and completed the pivotal Phase 3 PROTECT trial. The company publishes a corporate marketing site, a news and events feed, an expanded access policy and patient information, but operates no developer program, public API, or machine-readable API contract.
image: https://www.renibus.com/wp-content/uploads/2022/10/renibus-therapeutics-logo-retina.png
layout: provider
modified: '2026-08-05'
name: Rénibus Therapeutics
nav: Providers
network: true
overview: 'Rénibus Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharmaceutical, Pharmaceuticals, Life Sciences, and Healthcare.


  Rénibus Therapeutics'' developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Renibus Therapeutics Domain Security
  slug: renibus-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: renibus-therapeutics
tags:
- Company
- Biopharmaceutical
- Pharmaceuticals
- Life Sciences
- Healthcare
- Clinical Trials
- Nephrology
- Cardiovascular
website: https://www.renibus.com/
---
