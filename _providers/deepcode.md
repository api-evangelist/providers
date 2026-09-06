---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.deepcode.ai'', ''status'': 301, ''note'': ''declared website redirects to https://snyk.io/platform/deepcode-ai/ — a different registrable domain (deepcode.ai -> snyk.io), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 1
apis:
- description: AI for code review
  name: Deepcode
  slug: deepcode
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deepcode-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepcode-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deepcode.ai
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: AI for code review
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepcode.png
layout: provider
modified: '2026-05-28'
name: Deepcode
nav: Providers
network: true
overview: Deepcode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Machine-Learning and Public APIs.
random_paper: 6
score:
  band: minimal
  composite: 7.6
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
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepcode/refs/heads/main/screenshots/deepcode-2026-06-20T175803.png
security:
- kind: domain-security
  name: Deepcode Domain Security
  slug: deepcode-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Deepcode Vulnerability Disclosure
  slug: deepcode-vulnerability-disclosure
  summary_line: disclosure policy published
slug: deepcode
tags:
- Machine-Learning
- Public APIs
website: https://www.deepcode.ai
---
