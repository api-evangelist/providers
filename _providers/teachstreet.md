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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teachstreet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teachstreet.com
created: '2026-07-17'
description: TeachStreet was an online learning marketplace that, in its own words, "helps people find great classes, courses, teachers, and instructors who help them learn new things," while "teachers use TeachStreet to find more students" (teachstreet.com homepage, archived June 2011). Surfaced in the API Evangelist network as a 500 Global portfolio company, TeachStreet was acquired by Amazon on February 2, 2012 and subsequently wound down. The teachstreet.com domain is now a dormant, Amazon-controlled brand-protection asset — MarkMonitor nameservers, a locked-down mail posture (SPF "v=spf1 -all", DMARC "p=reject" reporting to dmarc.amazon.com), and no A/AAAA/MX records — so there is no live website, developer portal, or API surface to enrich. This record is retained as a historical, defunct-company profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teachstreet.png
layout: provider
modified: '2026-07-21'
name: TeachStreet
nav: Providers
network: true
overview: TeachStreet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Online Learning, Marketplace, and Classes.
random_paper: 4
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 1
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
    operational_transparency: 0.0
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Teachstreet Domain Security
  slug: teachstreet-domain-security
  summary_line: DMARC
slug: teachstreet
tags:
- Company
- Education
- Online Learning
- Marketplace
- Classes
- Defunct
website: https://teachstreet.com
---
