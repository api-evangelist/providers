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
- group: company
  title: ''
  type: Website
  url: https://www.corwave.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.corwave.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corwave.com/legal-notice/
- group: company
  title: ''
  type: Press
  url: https://www.corwave.com/press/
- group: company
  title: ''
  type: Careers
  url: https://www.corwave.com/application/careers/
- group: other
  title: ''
  type: Research
  url: https://www.corwave.com/scientific-communication/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/corwave_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corwave-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corwave-domain-security.yml
coverage:
  checked: '2026-08-11'
  detail: CorWave SA manufactures implantable wave-membrane heart pumps — the CorWave LVAS and Nemo, still investigational devices — so its product is hardware in a patient's chest, not software; its 18-URL sitemap contains no developer, API, or pricing page and every api/developer/docs/portal subdomain of corwave.com is NXDOMAIN.
  evidence:
  - status: 200
    url: https://www.corwave.com/
  - status: 200
    url: https://www.corwave.com/page-sitemap.xml
  - status: 404
    url: https://www.corwave.com/openapi.json
  - status: 404
    url: https://www.corwave.com/api-docs
  - status: 404
    url: https://www.corwave.com/graphql
  - status: 404
    url: https://www.corwave.com/.well-known/agent-card.json
  - status: 404
    url: https://www.corwave.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-11'
description: CorWave SA is a French clinical-stage medical device company, incorporated in 2012 by the startup studio MD Start and headquartered in Clichy, France, that develops implantable cardiac assist pumps for patients with advanced heart failure. Its patented wave membrane technology — a biomimetic polymer membrane driven by an electromagnetic actuator, inspired by the undulating movement of marine animals — produces truly pulsatile, physiological blood flow, differentiating the CorWave LVAS and Nemo pumps from commercially available rotary-pump LVADs. The company has raised more than EUR 80 million, operates an urban manufacturing facility in Clichy, employs more than 90 people, and announced the first in-human implantation of its Left Ventricular Assist System in 2025. CorWave LVAS remains an investigational device and is not approved for commercial use in any country. CorWave publishes no public API, SDK, developer portal, or machine-readable specification.
image: https://www.corwave.com/wp-content/uploads/2018/10/opengraph.jpg
layout: provider
modified: '2026-08-11'
name: CorWave
nav: Providers
network: true
overview: CorWave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health, Cardiology, and Heart Failure.
plans:
- name: Corwave Plans Pricing
  plan_count: 0
  slug: corwave-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Corwave Rate Limits
  slug: corwave-rate-limits
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corwave/refs/heads/main/screenshots/corwave-2026-09-02T145150.png
security:
- kind: domain-security
  name: Corwave Domain Security
  slug: corwave-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: corwave
tags:
- Company
- Medical Devices
- Health
- Cardiology
- Heart Failure
- Implantable Devices
- MedTech
- France
- Clinical Stage
website: https://www.corwave.com/
---
