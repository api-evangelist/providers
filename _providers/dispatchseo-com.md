---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documented at DispatchSEO docs
  name: DispatchSEO API
  slug: dispatchseo-api
- description: 'DispatchSEO API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DispatchSEO API
  slug: dispatchseo-com-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/dispatchseo-com/rules/dispatchseo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dispatchseo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dispatchseo-com/vocabulary/dispatchseo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dispatchseo-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/dispatchseo-com/changelog/dispatchseo-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dispatchseo-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/dispatchseo-com/authentication/dispatchseo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dispatchseo-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dispatchseo-com/conformance/dispatchseo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dispatchseo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dispatchseo-com/llms/dispatchseo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dispatchseo-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dispatchseo-com/hosts/dispatchseo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dispatchseo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dispatchseo-com/vendors/dispatchseo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dispatchseo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dispatchseo.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://dispatchseo.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dispatchseo.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://dispatchseo.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://dispatchseo.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://dispatchseo.com/docs
- group: auth
  href: https://artifacts.apis.io/dispatchseo-com/security/dispatchseo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dispatchseo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dispatchseo.com/
coverage:
  detail: No OpenAPI or other machine‑readable contract is published; attempts to fetch common spec URLs returned HTML pages.
  evidence:
  - status: 200
    url: https://dispatchseo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DispatchSEO provides an SEO automation platform for developers and indie founders. It integrates with Google Search Console to research keywords, drafts articles and tools as pull requests, tracks rankings, and offers a dashboard for review and scheduled publishing. The service is open‑source (AGPL‑3.0) and can be self‑hosted, with a hosted version at dispatchseo.com.
image: https://dispatchseo.com/opengraph-image.png?opengraph-image.379bs40_4vevv.png
layout: provider
modified: '2026-11-05'
name: DispatchSEO
nav: Providers
network: true
overview: 'DispatchSEO is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, Automation, Open Source, Developers, and Indie.


  The DispatchSEO catalog on APIs.io includes 1 Spectral governance ruleset.


  DispatchSEO''s developer surface includes changelog, authentication, signup flow, engineering blog, getting-started guide, and 11 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: DispatchSEO API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: dispatchseo-com-rules
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dispatchseo Com Authentication
  slug: dispatchseo-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dispatchseo Com Domain Security
  slug: dispatchseo-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dispatchseo-com
tags:
- SEO
- Automation
- Open Source
- Developers
- Indie
website: https://dispatchseo.com/
---
