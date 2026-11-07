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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/blocsmith-io/llms/blocsmith-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blocsmith-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/blocsmith-io/well-known/blocsmith-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blocsmith-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/blocsmith-io/hosts/blocsmith-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blocsmith-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/blocsmith-io/vendors/blocsmith-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blocsmith-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blocsmith.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blocsmith.io/privacy
- group: auth
  href: https://artifacts.apis.io/blocsmith-io/security/blocsmith-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blocsmith-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blocsmith.io/
coverage:
  checked: '2026-11-02'
  detail: API reference redirects to login page, no machine-readable spec found.
  evidence:
  - status: 307
    url: https://www.blocsmith.io/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Blocsmith provides an AI-powered website builder that lets users describe their business in natural language, then automatically designs, builds, and maintains a fully functional website. It handles real content, brand colors, SEO, analytics, and ongoing updates, offering a hands‑off solution for businesses seeking an online presence without technical effort. The platform emphasizes conversational input, rapid deployment, and continuous care, positioning itself as a modern, AI‑driven alternative to traditional web development services.
layout: provider
modified: '2026-11-02'
name: Blocsmith
nav: Providers
network: true
overview: Blocsmith is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Website Builder, No-Code, Software-as-a-Service, and Automation.
random_paper: 2
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blocsmith Io Domain Security
  slug: blocsmith-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blocsmith-io
tags:
- Artificial Intelligence
- Website Builder
- No-Code
- Software-as-a-Service
- Automation
website: https://www.blocsmith.io/
---
