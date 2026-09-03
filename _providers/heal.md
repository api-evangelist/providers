---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - '{''url'': ''https://www.heal.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.centerwell.com/ — a different registrable domain (heal.com -> centerwell.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.heal.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getheal
- group: other
  title: ''
  type: ParentCompany
  url: https://www.centerwell.com/
coverage:
  checked: '2026-08-22'
  detail: 'Heal was fully absorbed into Humana''s CenterWell brand and no longer operates as an independent company: every path on heal.com now 301-redirects to centerwell.com, no developer, docs or status host exists (all subdomains resolve on a wildcard into the same redirect), and the one surviving technical host, api.heal.com, is a blanket HTTP 401 gateway that returns the identical 58-byte NOT_AUTHORIZED body for invented paths as for real ones.'
  evidence:
  - status: 301
    url: https://www.heal.com/
  - status: 401
    url: https://api.heal.com/openapi.json
  - status: 401
    url: https://api.heal.com/.well-known/agent-card.json
  - status: 301
    url: https://www.heal.com/.well-known/security.txt
  - status: 200
    url: https://github.com/getheal
  reason: defunct
  state: none
created: '2026-08-22'
description: 'Heal (legally Get Heal, Inc.) was a Los Angeles based in-home primary care practice founded in 2014 that delivered on-demand doctor house calls, one-touch telemedicine, telepsychology and remote patient monitoring, aimed largely at Medicare Advantage members. Humana took a $100M stake in the company in July 2020 and then acquired it outright, folding the practice into its CenterWell primary care brand. Heal never ran a public developer program: it published no OpenAPI, no developer portal and no SDKs. As of this profile heal.com issues a 301 redirect to centerwell.com for every path, and the one surviving technical host, api.heal.com, answers every request with a blanket HTTP 401.'
image: https://avatars.githubusercontent.com/u/40704705?v=4
layout: provider
modified: '2026-08-22'
name: Heal
nav: Providers
network: true
overview: Heal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telehealth, and Primary Care.
random_paper: 11
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heal/refs/heads/main/screenshots/heal-2026-09-02T145713.png
security:
- kind: domain-security
  name: Heal Domain Security
  slug: heal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: heal
tags:
- Company
- Health
- Healthcare
- Telehealth
- Primary Care
- Remote Patient Monitoring
- Medicare
- Home Health
- Acquired
website: https://www.heal.com/
---
