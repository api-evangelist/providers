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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.moonactive.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moonactive-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/moonactive-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moonactive-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moonactive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.moonactive.com/security-report
created: '2026-07-17'
description: MoonActive is a mobile game developer and publisher best known for the casual titles Coin Master and Pet Master. It was surfaced as a portfolio company of Insight Partners and added to the API Evangelist network for enrichment. As a consumer gaming company MoonActive publishes no public developer API, SDK, or documentation surface; the enrichment pass captured its security and domain posture only (a published RFC 9116 security.txt with a security contact and disclosure page, plus probed TLS/SPF/DMARC).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moonactive.png
layout: provider
modified: '2026-07-20'
name: MoonActive
nav: Providers
network: true
overview: MoonActive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gaming, Mobile Games, and Entertainment.
random_paper: 6
score:
  band: minimal
  composite: 6.4
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
    operational_transparency: 10.5
  previous_composite: 6.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moonactive/refs/heads/main/screenshots/moonactive-2026-08-07T184234.png
security:
- kind: domain-security
  name: Moonactive Domain Security
  slug: moonactive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Moonactive Vulnerability Disclosure
  slug: moonactive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: moonactive
tags:
- Company
- Consumer
- Gaming
- Mobile Games
- Entertainment
- Casual Games
website: https://www.moonactive.com/
---
