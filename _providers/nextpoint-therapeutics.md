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
  url: security/nextpoint-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nextpointtx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nextpointtx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nextpointtx.com/terms-of-use/
- group: company
  title: ''
  type: News
  url: https://nextpointtx.com/news-publications/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextpoint-therapeutics/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/NextPointTX
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/nextpoint-therapeutics_stock/
coverage:
  checked: '2026-08-26'
  detail: NextPoint Therapeutics is a clinical-stage drug developer whose entire web presence is a seven-page WordPress marketing site with no developer program — every /openapi.json, /swagger.json, /graphql, /api-docs and /.well-known/* path returns the byte-identical 158,191-byte catch-all homepage rather than a document, and the only machine-readable surface on the host is the default WordPress /wp-json/ CMS route index, which is WordPress plumbing and not a NextPoint API product.
  evidence:
  - status: 200
    url: https://nextpointtx.com/openapi.json
  - status: 200
    url: https://nextpointtx.com/definitely-not-a-real-path-abc123
  - status: 404
    url: https://nextpointtx.com/.well-known/security.txt
  - status: 404
    url: https://nextpointtx.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/nextpointtx
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: NextPoint Therapeutics is a clinical-stage biotechnology company based at 238 Main Street in Cambridge, Massachusetts, developing precision immuno-oncology therapeutics built on its scientific work on the novel B7-H7/HHLA2 checkpoint axis. Its pipeline includes a T-cell engager engineered for an improved therapeutic index, an antibody-drug conjugate using proprietary linker technology, and a multi-functional checkpoint inhibitor, each aimed at tumors that upregulate B7-H7. The company publishes a seven-page corporate marketing site covering its science, pipeline, leadership, and news; it operates no developer program, publishes no API, SDK, or machine-readable specification, and is profiled here for network completeness rather than for an API surface.
image: https://nextpointtx.com/wp-content/uploads/2025/08/logo-nextpoint.png
layout: provider
modified: '2026-08-26'
name: NextPoint Therapeutics
nav: Providers
network: true
overview: 'NextPoint Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Immunotherapy.


  NextPoint Therapeutics'' developer surface includes product news and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nextpoint-therapeutics/refs/heads/main/screenshots/nextpoint-therapeutics-2026-09-02T150749.png
security:
- kind: domain-security
  name: Nextpoint Therapeutics Domain Security
  slug: nextpoint-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nextpoint-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Immunotherapy
- Life Sciences
- Healthcare
- Clinical Trials
website: https://nextpointtx.com/
---
