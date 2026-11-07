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
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/cintaporbit/conformance/cintaporbit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cintaporbit-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cintaporbit/llms/cintaporbit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cintaporbit-llms.txt
- group: other
  href: https://artifacts.apis.io/cintaporbit/hosts/cintaporbit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cintaporbit-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://cintaporbit.com/login
- group: auth
  href: https://artifacts.apis.io/cintaporbit/security/cintaporbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cintaporbit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cintaporbit.com/
- group: company
  title: ''
  type: Blog
  url: https://cintaporbit.com/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cintaporbit.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cintaporbit.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://cintaporbit.com/contact
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cintaporbit.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: CINTAP provides an enterprise integration platform (iPaaS) that connects applications, APIs, files, documents, and partners through a no-code environment. Their suite includes products like Orbit, Kepler, Nova, and AI Mapping Engine, enabling data flow automation, B2B integration, and document intelligence. CINTAP serves businesses seeking to streamline integration, reduce handoffs, and accelerate digital transformation with a unified platform.
image: https://cintaporbit.com/og/orbit-suite-og.png
layout: provider
modified: '2026-10-20'
name: CINTAP
nav: Providers
network: true
overview: 'CINTAP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, iPaaS, Automation, and B2B.


  CINTAP''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cintaporbit/cintaporbit-2026-11-03T124150.png
security:
- kind: domain-security
  name: Cintaporbit Domain Security
  slug: cintaporbit-domain-security
  summary_line: TLSv1.3
slug: cintaporbit
tags:
- Company
- Integration
- iPaaS
- Automation
- B2B
website: https://cintaporbit.com/
---
