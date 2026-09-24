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
  band: agent-aware
  dimensions:
    agent_card: flavored
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: AI/ML engineering job aggregator with REST, RSS, and MCP endpoints
  name: AI Dev Jobs
  slug: ai-dev-jobs
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ai-dev-jobs/refs/heads/main/a2a/ai-dev-jobs-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ai-dev-jobs-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-dev-jobs/refs/heads/main/security/ai-dev-jobs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ai-dev-jobs-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-dev-jobs/refs/heads/main/security/ai-dev-jobs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-dev-jobs-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://aidevboard.com/feed.xml
- group: company
  title: ''
  type: Website
  url: https://aidevboard.com/openapi.yaml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: operate
  title: ''
  type: Support
  url: mailto:hello@aidevboard.com
created: '2026-05-28'
description: AI/ML engineering job aggregator with REST, RSS, and MCP endpoints
layout: provider
modified: '2026-05-28'
name: AI Dev Jobs
nav: Providers
network: true
overview: 'AI Dev Jobs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Job, Public APIs, and A2A.


  AI Dev Jobs'' developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 53.7
    operational_transparency: 0.0
  previous_composite: 8.7
  provenance:
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ai-dev-jobs/refs/heads/main/screenshots/ai-dev-jobs-2026-06-20T170624.png
security:
- kind: domain-security
  name: Ai Dev Jobs Domain Security
  slug: ai-dev-jobs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ai Dev Jobs Vulnerability Disclosure
  slug: ai-dev-jobs-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ai-dev-jobs
tags:
- Job
- Public APIs
- A2A
website: https://aidevboard.com/openapi.yaml
---
