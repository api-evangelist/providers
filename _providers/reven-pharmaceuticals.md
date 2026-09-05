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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reven-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reven.com/
- group: company
  title: ''
  type: Blog
  url: https://reven.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://reven.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://reven.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revenpharmaceuticals
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/reven-pharmaceuticals_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reven-pharmaceuticals-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Reven is a 15-person clinical-stage drug developer whose product is an IV pharmaceutical (RJX), not software - reven.com is a WordPress corporate/investor site where every contract-discovery path 404s and the only machine-readable endpoint is the CMS's own default /wp-json/ (228 WordPress core and plugin routes, no Reven product).
  evidence:
  - status: 404
    url: https://reven.com/openapi.json
  - status: 404
    url: https://reven.com/graphql
  - status: 404
    url: https://reven.com/.well-known/agent-card.json
  - status: 404
    url: https://reven.com/llms.txt
  - status: 200
    url: https://reven.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Reven Pharmaceuticals is a privately held, clinical-stage biopharmaceutical company founded in 1999 and headquartered in Broomfield, Colorado. Reven develops medicines from its proprietary RJX Technology platform - a patented, first-in-class intravenous composition of anti-oxidant and anti-inflammatory ingredients - and is advancing candidates for sepsis, multi-system inflammation, cytokine release syndrome, ARDS and vascular, oncology, CNS and ocular indications. Its lead candidate, Rejuveinix (RJX), completed a double-blind, placebo-controlled Phase 1 dose-escalation study in healthy volunteers and received FDA clearance of an Investigational New Drug application for the treatment of COVID-19. Reven publishes a corporate and investor website at reven.com covering its pipeline, modalities, clinical trials, expanded-access program and news, but operates no public developer program, API, SDK or machine-readable interface of any kind.
image: https://reven.com/wp-content/uploads/2021/12/Reven_Logo_Header-1.png
layout: provider
modified: '2026-08-26'
name: Reven Pharmaceuticals
nav: Providers
network: true
overview: 'Reven Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Clinical Trials.


  Reven Pharmaceuticals'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reven-pharmaceuticals/refs/heads/main/screenshots/reven-pharmaceuticals-2026-09-02T153703.png
security:
- kind: domain-security
  name: Reven Pharmaceuticals Domain Security
  slug: reven-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: reven-pharmaceuticals
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Clinical Trials
- Drug Development
- Health
website: https://reven.com/
---
