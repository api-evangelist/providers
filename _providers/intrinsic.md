---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://withintrinsic.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.variance.com/ — a different registrable domain (withintrinsic.com -> variance.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 1
apis:
- description: Unified Trust & Safety API exposing ML classifiers, enrichments, account graph lineage, and real-time rule evaluation for anti-abuse workflows. Access is gated behind an issued API key; developer docu
  name: Intrinsic API
  slug: intrinsic-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://withintrinsic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.intrinsicapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.intrinsicapi.com/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/intrinsic-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/intrinsic-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/intrinsic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/intrinsic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intrinsic-domain-security.yml
created: '2026-07-17'
description: Intrinsic is a unified Trust & Safety platform that gives safety teams a single API and dashboard to detect, investigate, and enforce against abuse across user- and AI-generated content, fraud, and marketplace abuse. The platform surfaces machine-learning classifiers (for example text toxicity and IP trust scoring), account graph lineage for linkage analysis, geo enrichers, and global intelligence signals through a synchronous API, and lets teams author, version, deploy, and monitor real-time anti-abuse rules from a hosted dashboard. Founded in 2022 in San Francisco by Karine Mellata and Michael Lin (previously on Trust & Safety ML and data-engineering infrastructure at Apple and Discord), Intrinsic has since rebranded to Variance (variance.co); the Intrinsic-branded developer surfaces at docs.intrinsicapi.com and api.intrinsicapi.com remain in service.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intrinsic.png
layout: provider
modified: '2026-07-19'
name: Intrinsic
nav: Providers
network: true
overview: 'Intrinsic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trust and Safety, Content Moderation, Anti-Abuse, and Fraud Detection.


  Intrinsic''s developer surface includes documentation and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intrinsic/refs/heads/main/screenshots/intrinsic-2026-07-25T222730.png
security:
- kind: domain-security
  name: Intrinsic Domain Security
  slug: intrinsic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Intrinsic Vulnerability Disclosure
  slug: intrinsic-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: intrinsic
tags:
- Company
- Trust and Safety
- Content Moderation
- Anti-Abuse
- Fraud Detection
- Machine-Learning
- Risk Intelligence
website: https://withintrinsic.com
---
