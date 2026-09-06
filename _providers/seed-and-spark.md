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
  url: security/seed-and-spark-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seed-and-spark-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://seedandspark.com/
created: '2026-07-17'
description: Seed&Spark is a crowdfunding and streaming platform for independent film and episodic content, combining a project crowdfunding marketplace for filmmakers with a subscription streaming service for independent films and series. Founded in 2012 and backed by Techstars, the company helps independent creators raise funds, build audiences, and distribute their work. It was added to the API Evangelist network as a portfolio-company lead; no public developer API surface was found during enrichment (homepage and app paths sit behind Cloudflare bot protection; no api.* or developers.* subdomain resolves and no well-known API documents are published).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seed-and-spark.png
layout: provider
modified: '2026-07-21'
name: Seed&Spark
nav: Providers
network: true
overview: Seed&Spark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crowdfunding, Film, Streaming, and Entertainment.
random_paper: 15
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seed-and-spark/refs/heads/main/screenshots/seed-and-spark-2026-09-02T154730.png
security:
- kind: domain-security
  name: Seed And Spark Domain Security
  slug: seed-and-spark-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: seed-and-spark
tags:
- Company
- Crowdfunding
- Film
- Streaming
- Entertainment
- Media
- Independent Film
website: https://seedandspark.com/
---
