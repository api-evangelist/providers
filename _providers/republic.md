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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/republic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/republic-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://republic.com/security
- group: company
  title: ''
  type: Website
  url: https://republic.com
created: '2026-07-17'
description: 'Republic is a New York-based fintech and private investing platform (republic.com) that lets retail and accredited investors access early-stage startups, private companies, real estate, crypto, and other alternative assets through regulated investment crowdfunding offerings. Backed by prosus-ventures, Republic operates a consumer investing marketplace rather than a public developer platform: it publishes a security and compliance posture (SOC 2, ISO 27001) at republic.com/security but exposes no public API, developer portal, SDKs, or documentation surface at the time of this enrichment pass. This profile was surfaced as a portfolio-company lead and enriched with the provider-security signals that could be probed directly.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/republic.png
layout: provider
modified: '2026-07-20'
name: Republic
nav: Providers
network: true
overview: Republic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investing, Crowdfunding, and Private Markets.
random_paper: 14
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/republic/refs/heads/main/screenshots/republic-2026-09-02T153512.png
security:
- kind: domain-security
  name: Republic Domain Security
  slug: republic-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Republic Trust Center
  slug: republic-trust-center
  summary_line: SOC 2, ISO 27001
slug: republic
tags:
- Company
- Fintech
- Investing
- Crowdfunding
- Private Markets
- Startups
- Crypto
website: https://republic.com
---
