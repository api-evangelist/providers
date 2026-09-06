---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cagent-vascular-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cagentvascular.com/
- group: company
  title: ''
  type: About
  url: https://cagentvascular.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://cagentvascular.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://cagentvascular.com/news?format=rss
- group: operate
  title: ''
  type: Support
  url: https://cagentvascular.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cagentvascular.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cagentvascular.com/privacy-policy
- group: operate
  title: ''
  type: FAQ
  url: https://cagentvascular.com/faqs
- group: company
  title: ''
  type: Careers
  url: https://cagentvascular.com/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cagent-vascular-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cagent-vascular_stock/
coverage:
  checked: '2026-08-08'
  detail: Cagent Vascular manufactures the Serranator peripheral angioplasty balloon catheter; its 124-URL Squarespace sitemap covers clinical studies, webinars and reimbursement material with no developer, API, or integration page, and no api./developer./docs./portal. subdomain resolves in DNS.
  evidence:
  - status: 200
    url: https://cagentvascular.com/sitemap.xml
  - status: 404
    url: https://cagentvascular.com/openapi.json
  - status: 404
    url: https://cagentvascular.com/.well-known/agent-card.json
  - status: 404
    url: https://cagentvascular.com/.well-known/security.txt
  - status: 404
    url: https://cagentvascular.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-08'
description: 'Cagent Vascular is a privately held endovascular medical device company based in Wayne, Pennsylvania, that develops and commercializes Serration Remodeling Therapy (SRT). Its flagship product, the Serranator PTA Serration Balloon Catheter, embeds stainless-steel serrated strips into a semi-compliant angioplasty balloon to create linear, interrupted micro-fissures along the artery wall, producing controlled lumen expansion at lower pressures when treating peripheral artery disease (PAD) and chronic limb-threatening ischemia (CLTI). The Serranator is FDA 510(k) cleared and CE marked, and the portfolio has expanded to include Serranator SL-PRO and the Serranator SONIC intravascular lithotripsy (IVL) system. Cagent Vascular is a device manufacturer rather than a software or platform company: it publishes clinical data, case studies, webinars and reimbursement material on its website, but no public developer program, API, or machine-readable interface.'
image: http://static1.squarespace.com/static/698f6db578da291d277a114a/t/69d341f3ef6422769dae3be2/1775452659672/CV-sharing.png?format=1500w
layout: provider
modified: '2026-08-08'
name: Cagent Vascular
nav: Providers
network: true
overview: 'Cagent Vascular is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Vascular, and Peripheral Artery Disease.


  Cagent Vascular''s developer surface includes engineering blog, support, FAQ, and 9 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cagent-vascular/refs/heads/main/screenshots/cagent-vascular-2026-09-02T145003.png
security:
- kind: domain-security
  name: Cagent Vascular Domain Security
  slug: cagent-vascular-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cagent-vascular
tags:
- Company
- Medical Devices
- Healthcare
- Vascular
- Peripheral Artery Disease
- Endovascular
- Angioplasty
- MedTech
website: https://cagentvascular.com/
---
