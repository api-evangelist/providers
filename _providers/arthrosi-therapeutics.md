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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arthrosi-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arthrosi.com/
- group: company
  title: ''
  type: About
  url: https://arthrosi.com/company/
- group: other
  title: ''
  type: Team
  url: https://arthrosi.com/team/
- group: company
  title: ''
  type: Blog
  url: https://arthrosi.com/news-media/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arthrosi-therapeutics-inc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/arthrosi-therapeutics_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arthrosi-therapeutics-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Arthrosi is a San Diego drug developer whose product is a Phase 3 oral gout molecule (pozdeutinurad/AR882, acquired by Sobi in February 2026), not software — there is no GitHub org, no package on any registry and no api/docs/developer subdomain in DNS, and its single web property is a WordPress marketing site that answers HTTP 202 with a SiteGround sgcaptcha interstitial to every path including /robots.txt and a bogus control path, so even the marketing copy is machine-unreadable.
  evidence:
  - status: 202
    url: https://arthrosi.com/robots.txt
  - status: 202
    url: https://arthrosi.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/arthrosi
  - status: 404
    url: https://pypi.org/pypi/arthrosi/json
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Arthrosi Therapeutics, Inc. is a late-stage clinical biotechnology company founded in 2018 and headquartered in San Diego, California, by a team of gout specialists who previously led first-generation urate-transporter development at Ardea Biosciences. Its lead candidate, pozdeutinurad (AR882), is a once-daily oral next-generation URAT1 inhibitor in two fully enrolled replicate global Phase 3 trials (REDUCE 1 and REDUCE 2) for progressive and tophaceous gout, backed by roughly $299M in venture financing including a $153M Series E led by Prime Eight Capital. Sobi (Swedish Orphan Biovitrum) completed its acquisition of Arthrosi on 9 February 2026. Arthrosi is a drug developer, not a software company: it operates a WordPress corporate site with company, leadership and news pages, and publishes no developer portal, public API, SDK, package or machine-readable specification of any kind.'
layout: provider
modified: '2026-08-06'
name: Arthrosi Therapeutics
nav: Providers
network: true
overview: 'Arthrosi Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Arthrosi Therapeutics'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 5
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
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arthrosi-therapeutics/refs/heads/main/screenshots/arthrosi-therapeutics-2026-08-07T161737.png
security:
- kind: domain-security
  name: Arthrosi Therapeutics Domain Security
  slug: arthrosi-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arthrosi-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Drug Development
- Gout
- Rheumatology
- Healthcare
website: https://arthrosi.com/
---
