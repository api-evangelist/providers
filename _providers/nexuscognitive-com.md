---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/nexuscognitive-com/security/nexuscognitive-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/nexuscognitive-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/nexuscognitive-com/llms/nexuscognitive-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nexuscognitive-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/nexuscognitive-com/well-known/nexuscognitive-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nexuscognitive-com-security.txt
- group: agent
  href: https://artifacts.apis.io/nexuscognitive-com/well-known/nexuscognitive-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nexuscognitive-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/nexuscognitive-com/hosts/nexuscognitive-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nexuscognitive-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nx1.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nexuscognitive/
- group: company
  title: ''
  type: Blog
  url: https://www.nx1.io/blog
- group: auth
  href: https://artifacts.apis.io/nexuscognitive-com/security/nexuscognitive-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nexuscognitive-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nexuscognitive-com/security/nexuscognitive-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nexuscognitive-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nx1.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nexuscognitive.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Nexus One provides a composable, out‑of‑the‑box data architecture that gives organizations complete freedom to build, adapt, and scale any data workload—from legacy databases to real‑time AI pipelines—without vendor lock‑in. The platform serves as the data layer for AI, enabling seamless integration of diverse data sources, robust automation, and scalable analytics for modern enterprises.
image: https://framerusercontent.com/images/MbZO5oDZKpXVCQMJE9h7N4rTcY.png
layout: provider
modified: '2026-10-22'
name: Nexus One
nav: Providers
network: true
overview: 'Nexus One is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, AI, Platform, and Integration.


  Nexus One''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nexuscognitive Com Domain Security
  slug: nexuscognitive-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nexuscognitive Com Vulnerability Disclosure
  slug: nexuscognitive-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nexuscognitive-com
tags:
- Company
- Data
- AI
- Platform
- Integration
website: https://www.nx1.io/
---
