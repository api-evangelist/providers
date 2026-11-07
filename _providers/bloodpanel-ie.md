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
- description: API reference for BloodPanel services
  name: BloodPanel API
  slug: bloodpanel-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bloodpanel-ie/llms/bloodpanel-ie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bloodpanel-ie-llms.txt
- group: other
  href: https://artifacts.apis.io/bloodpanel-ie/hosts/bloodpanel-ie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloodpanel-ie-hosts.yml
- group: other
  href: https://artifacts.apis.io/bloodpanel-ie/vendors/bloodpanel-ie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bloodpanel-ie-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bloodpanel-ie/security/bloodpanel-ie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloodpanel-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloodpanel.ie/
- group: docs
  title: ''
  type: Documentation
  url: https://bloodpanel.ie/about
- group: operate
  title: ''
  type: Support
  url: https://bloodpanel.ie/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloodpanel.ie/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloodpanel.ie/terms
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite API reference page.
  evidence:
  - status: 200
    url: https://bloodpanel.ie/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BloodPanel is an Irish digital health platform that helps users find and compare blood tests across Ireland. It aggregates public listings, shows prices, and guides users to providers. The service includes AI‑assisted chat to suggest suitable tests and locations, while offering privacy‑focused data handling.
layout: provider
modified: '2026-11-02'
name: BloodPanel
nav: Providers
network: true
overview: 'BloodPanel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Ireland, Digital Health, BloodTests, and Artificial Intelligence.


  BloodPanel''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bloodpanel Ie Domain Security
  slug: bloodpanel-ie-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloodpanel-ie
tags:
- Health
- Ireland
- Digital Health
- BloodTests
- Artificial Intelligence
website: https://bloodpanel.ie/
---
