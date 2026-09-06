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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/myhealthteams-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.myhealthteam.com
created: '2026-07-17'
description: MyHealthTeam operates condition-specific patient social networks that connect roughly 4 million members across 80+ chronic-condition communities (from multiple sclerosis and rheumatoid arthritis to autism and cancer) with peer support, practical advice, and trusted health information to help them better manage life with a chronic condition. It is a consumer-facing web and mobile platform rather than a developer-oriented API provider; as of January 2025 MyHealthTeam is a Swoop company. This API Evangelist profile was surfaced as a 500 Global portfolio company. Enrichment found no public developer API, developer portal, OpenAPI, SDKs, or /.well-known discovery surface on myhealthteam.com — only the consumer marketing site (which now redirects its blog to swoop.com), so this entry carries identity and domain-security signal only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/myhealthteams.png
layout: provider
modified: '2026-07-20'
name: MyHealthTeam
nav: Providers
network: true
overview: MyHealthTeam is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Chronic Conditions, and Patient Community.
random_paper: 12
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/myhealthteams/refs/heads/main/screenshots/myhealthteams-2026-08-07T184524.png
security:
- kind: domain-security
  name: Myhealthteams Domain Security
  slug: myhealthteams-domain-security
  summary_line: TLSv1.3 · DMARC
slug: myhealthteams
tags:
- Company
- Health
- Healthcare
- Chronic Conditions
- Patient Community
- Social Network
- Digital Health
website: https://www.myhealthteam.com
---
