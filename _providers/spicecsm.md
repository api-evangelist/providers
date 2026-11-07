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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SpiceCSM platform API (no public contract discovered)
  name: SpiceCSM API
  slug: spicecsm-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/spicecsm/llms/spicecsm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spicecsm-llms.txt
- group: other
  href: https://artifacts.apis.io/spicecsm/hosts/spicecsm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spicecsm-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spicex.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.spicex.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpiceCSM
- group: company
  title: ''
  type: Website
  url: https://spicecsm.com/
- group: auth
  href: https://artifacts.apis.io/spicecsm/security/spicecsm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spicecsm-domain-security.yml
created: '2026-10-21'
description: SpiceCSM provides a customer success management platform that helps SaaS businesses streamline onboarding, adoption, and retention. The solution offers tools for workflow automation, health scoring, and proactive engagement, enabling teams to reduce churn and increase product usage. SpiceCSM integrates with popular CRMs, support desks, and analytics platforms, delivering a unified view of customer health and facilitating data‑driven decision making across the organization.
image: https://www.spicex.com/wp-content/uploads/2022/11/logo-site.png
layout: provider
modified: '2026-10-21'
name: SpiceCSM
nav: Providers
network: true
overview: 'SpiceCSM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Success, Software-as-a-Service, Platform, Automation, and Analytics.


  SpiceCSM''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 64.3
    operational_transparency: 2.6
  previous_composite: 8.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/spicecsm/spicecsm-2026-11-03T143631.png
security:
- kind: domain-security
  name: Spicecsm Domain Security
  slug: spicecsm-domain-security
  summary_line: TLSv1.3
slug: spicecsm
tags:
- Customer Success
- Software-as-a-Service
- Platform
- Automation
- Analytics
website: https://spicecsm.com/
---
