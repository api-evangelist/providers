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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/applybolt-app/llms/applybolt-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applybolt-app-llms.txt
- group: other
  href: https://artifacts.apis.io/applybolt-app/hosts/applybolt-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applybolt-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/applybolt-app/vendors/applybolt-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applybolt-app-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.applybolt.app/signin
- group: auth
  href: https://artifacts.apis.io/applybolt-app/security/applybolt-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applybolt-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.applybolt.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.applybolt.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.applybolt.app/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.applybolt.app/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.applybolt.app/guide
- group: start
  title: ''
  type: GettingStarted
  url: https://www.applybolt.app/start
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing known API hosts.
  evidence:
  - status: 403
    url: https://api.applybolt.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ApplyBolt is an AI-powered job search platform that automates resume building, job application submissions, and follow‑up communications. Users can create tailored resumes, discover job listings, and let the service apply on their behalf across multiple employer sites, delivering confirmations to their inbox. The platform also offers tools like LinkedIn email finding, visa sponsorship filtering, and interview scheduling assistance, aiming to streamline the entire hiring process for candidates ranging from new graduates to experienced professionals.
image: https://www.applybolt.app/opengraph-image.jpg?opengraph-image.850c18b2.jpg
layout: provider
modified: '2026-11-01'
name: ApplyBolt
nav: Providers
network: true
overview: 'ApplyBolt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Job Search, ResumeAutomation, Careers, and Hiring.


  ApplyBolt''s developer surface includes engineering blog, documentation, getting-started guide, and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 16.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Applybolt App Domain Security
  slug: applybolt-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: applybolt-app
tags:
- Artificial Intelligence
- Job Search
- ResumeAutomation
- Careers
- Hiring
website: https://www.applybolt.app/
---
