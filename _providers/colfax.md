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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/colfaxcorporation
- group: other
  title: ''
  type: Successor (Enovis)
  url: https://enovis.com
- group: other
  title: ''
  type: Successor (ESAB)
  url: https://www.esabcorporation.com
- group: other
  title: ''
  type: History
  url: https://enovis.com/corporate-info/our-company/history
- group: other
  title: ''
  type: Spin-Off Announcement
  url: https://ir.enovis.com/news-releases/news-release-details/enovis-formerly-colfax-completes-spin-esab-corporation
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Enovis
coverage:
  checked: '2026-09-05'
  detail: Colfax Corporation stopped existing on 2022-04-04 — it spun off ESAB and renamed itself Enovis — and its corporate domain colfaxcorp.com is now a mail-only shell run by ESAB that publishes no A record at all, so every HTTP probe fails at DNS; the only surviving Colfax-branded host, ir.colfaxcorp.com, is a pre-2022 press-release archive on Q4's IR platform that returns 403 to every non-browser client including /robots.txt.
  evidence:
  - status: 0
    url: https://colfaxcorp.com/
  - status: 0
    url: https://colfaxcorp.com/.well-known/security.txt
  - status: 403
    url: https://ir.colfaxcorp.com/robots.txt
  - status: 403
    url: https://ir.colfaxcorp.com/.well-known/agent-card.json
  - status: 200
    url: https://enovis.com/corporate-info/our-company/history
  reason: defunct
  state: none
created: '2025-03-23'
description: 'Colfax Corporation was a diversified global manufacturer founded in 1995 in Richmond, Virginia by Steven and Mitchell Rales. In April 2022, Colfax completed the spin-off of its fabrication technology business as ESAB Corporation (NYSE: ESAB) and renamed itself Enovis Corporation (NYSE: ENOV), refocusing on specialty medical technologies. The Colfax brand and corporate entity no longer exists as an operating company. This profile is preserved for historical reference and routes to the two successor entities. No Colfax-branded developer APIs were ever published; any successor APIs would fall under Enovis or ESAB.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/colfax.png
layout: provider
modified: '2026-09-15'
name: Colfax Corporation (Historical)
nav: Providers
network: true
overview: Colfax Corporation (Historical) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fabrication Technology, Historical, Industrial, Medical Technology, and Spin-Off.
press:
- date: ''
  title: 'Equitable Algorithms: How Human-Centered AI Can ...'
  url: https://www.relmanlaw.com/media/news/1090_2021.05_Hayes_HFSC_AI_Task_Force_Testimony.pdf
- date: ''
  title: HOW HUMAN-CENTERED AI CAN ADDRESS SYSTEMIC ...
  url: https://www.govinfo.gov/content/pkg/CHRG-117hhrg44838/html/CHRG-117hhrg44838.htm
- date: ''
  title: LDF, SBPC, and Upstart Announce Final Monitorship ...
  url: https://www.naacpldf.org/press-release/ldf-sbpc-and-upstart-announce-final-monitorship-report-on-ai-and-fair-lending/
- date: ''
  title: Disparate Impact as Uniquely Relevant in the Age of AI
  url: https://civilrights.org/disparate-impact-age-of-ai/
- date: ''
  title: Untether AI Partners with Colfax International to Provide ...
  url: https://www.businesswire.com/news/home/20210204005099/en/Untether-AI-Partners-with-Colfax-International-to-Provide-Peak-Performance-in-AI-Edge-Servers
random_paper: 21
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/colfax/refs/heads/main/screenshots/colfax-2026-06-20T174743.png
slug: colfax
tags:
- Fabrication Technology
- Historical
- Industrial
- Medical Technology
- Spin-Off
- Defunct
---
