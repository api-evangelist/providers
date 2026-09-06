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
  url: security/pharmazz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pharmazz.com/
- group: company
  title: ''
  type: About
  url: https://www.pharmazz.com/about-us.php
- group: operate
  title: ''
  type: Contact
  url: https://www.pharmazz.com/contact-us.php
- group: company
  title: ''
  type: Careers
  url: https://www.pharmazz.com/career.php
- group: company
  title: ''
  type: Press
  url: https://www.pharmazz.com/press-releases.php
- group: company
  title: ''
  type: Investors
  url: https://www.pharmazz.com/investors.php
- group: other
  title: ''
  type: Publications
  url: https://www.pharmazz.com/publications.php
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pharmazz
- group: other
  title: ''
  type: Sitemap
  url: https://www.pharmazz.com/sitemap.xml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pharmazz-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Pharmazz is a clinical-stage drug developer whose entire public presence is a 33-page static PHP brochure site listing its centhaquine and sovateltide trial programs; there is no /developers, /docs or /api path, no GitHub organization, and every contract-discovery probe against www.pharmazz.com returned the site's standard 404 page.
  evidence:
  - status: 404
    url: https://www.pharmazz.com/developers
  - status: 404
    url: https://www.pharmazz.com/openapi.json
  - status: 404
    url: https://www.pharmazz.com/.well-known/agent-card.json
  - status: 200
    url: https://www.pharmazz.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Pharmazz, Inc. is a privately held, clinical-stage biopharmaceutical company headquartered in Willowbrook, Illinois, founded and led by pharmacologist Dr. Anil Gulati. The company discovers, develops and commercializes first-in-class therapeutics for critical care and neurovascular medicine, built around two lead small-molecule candidates: centhaquine (Lyfaquin), a resuscitative agent for hypovolemic shock that holds marketing authorization from the Drugs Controller General of India and is licensed to Dr. Reddy''s Laboratories for the Indian market, and sovateltide (Tycamzzi), an endothelin-B receptor agonist for cerebral ischemic stroke. Additional pipeline programs target septic shock, acute kidney injury, cardiac arrest, acute spinal cord injury, hypoxic-ischemic encephalopathy and Alzheimer''s disease. Pharmazz is a drug-development company, not a software vendor; its public web presence is a corporate and investor brochure site and it operates no developer program, public
  API, SDK or machine-readable interface.'
layout: provider
modified: '2026-08-26'
name: Pharmazz
nav: Providers
network: true
overview: Pharmazz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Healthcare.
random_paper: 16
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pharmazz/refs/heads/main/screenshots/pharmazz-2026-09-02T151137.png
security:
- kind: domain-security
  name: Pharmazz Domain Security
  slug: pharmazz-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: pharmazz
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Healthcare
- Clinical Trials
- Critical Care
- Drug Development
website: https://www.pharmazz.com/
---
