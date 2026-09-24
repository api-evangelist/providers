---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-24'
api_count: 4
apis:
- description: Local business data collection via geo point + radius sweep with deduplication on place ID; optional email extraction. Billed per place returned.
  name: Places
  slug: places
- description: Job posting collection that segments by publish window/area to exceed the public 1,000-result cap. Billed per posting returned.
  name: Jobs
  slug: jobs
- description: Timestamped/segmented video transcript retrieval, up to 50 videos per call. Billed per transcript returned.
  name: Captions
  slug: captions
- description: Email verification via syntax, disposable-domain, MX and SMTP dialogue checks (no message sent), up to 100 addresses per call. Billed per address settled.
  name: Verify
  slug: verify
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://rankfabrik.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rankfabrik/refs/heads/main/security/rankfabrik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rankfabrik-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rankfabrik/refs/heads/main/plans/rankfabrik-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rankfabrik-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rankfabrik/refs/heads/main/rate-limits/rankfabrik-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rankfabrik-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rankfabrik/refs/heads/main/authentication/rankfabrik-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rankfabrik-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rankfabrik/refs/heads/main/conventions/rankfabrik-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rankfabrik-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rankfabrik/refs/heads/main/errors/rankfabrik-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rankfabrik-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rankfabrik/refs/heads/main/lifecycle/rankfabrik-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rankfabrik-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rankfabrik/refs/heads/main/llms/rankfabrik-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rankfabrik-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://rankfabrik.com/tarifs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rankfabrik.com/conditions
- group: start
  title: ''
  type: SignUp
  url: https://rankfabrik.com/inscription
- group: start
  title: ''
  type: Login
  url: https://rankfabrik.com/connexion
- group: docs
  title: ''
  type: Documentation
  url: https://rankfabrik.com/documentation
created: '2026-09-14'
description: Four independent data-collection REST APIs run from Paris — Places (local businesses), Jobs (job postings), Captions (video transcripts), and Verify (email verification). Each response reports a per-field fill-rate/completeness percentage, and calls returning no result are never billed.
image: https://rankfabrik.com/og-en.png
layout: provider
modified: '2026-09-14'
name: RankFabrik
nav: Providers
network: true
overview: 'RankFabrik publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Web Scraping, Local Business, Places, and Job.


  RankFabrik''s developer surface includes authentication, pricing, signup flow, documentation, and 10 more developer resources.'
plans:
- name: Rankfabrik Plans Pricing
  plan_count: 0
  slug: rankfabrik-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Rankfabrik Rate Limits
  slug: rankfabrik-rate-limits
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    operational_transparency: 21.1
  previous_composite: 20.7
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rankfabrik Authentication
  slug: rankfabrik-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Rankfabrik Domain Security
  slug: rankfabrik-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rankfabrik
tags:
- Data
- Web Scraping
- Local Business
- Places
- Job
- Job Postings
- video-transcripts
- Captions
- Email Verification
- Data Enrichment
- Lead Generation
- REST API
website: https://rankfabrik.com
---
