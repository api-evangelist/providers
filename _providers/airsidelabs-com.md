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
- description: Documentation for Airside Labs aviation tools MCP server, covering tool answers, plans, limits and support.
  name: Airside Labs Tools API
  slug: airside-labs-tools-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/airsidelabs-com/llms/airsidelabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airsidelabs-com-llms.txt
- group: other
  href: https://artifacts.apis.io/airsidelabs-com/hosts/airsidelabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airsidelabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/airsidelabs-com/vendors/airsidelabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/airsidelabs-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/airsidelabs-com/security/airsidelabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airsidelabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airsidelabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://airsidelabs.com/resources
- group: company
  title: ''
  type: Blog
  url: https://airsidelabs.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airsidelabs.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airsidelabs.com/tools/terms
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are HTML rendered with JavaScript, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 200
    url: https://airsidelabs.com/tools/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Airside Labs provides AI-driven infrastructure for the travel and aviation industry, building and validating AI systems that integrate legacy aviation data into mission-critical operations. They offer use case resources, advisory services, and a platform for developing agentic workflows, aiming to orchestrate the future of aviation and travel through advanced AI solutions.
image: https://airsidelabs.com/assets/airsidelabs-logo-CZkMJ2td.png
layout: provider
modified: '2026-11-01'
name: Airside Labs
nav: Providers
network: true
overview: 'Airside Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Aviation, Travel, and Infrastructure.


  Airside Labs'' developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 12.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airsidelabs Com Domain Security
  slug: airsidelabs-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airsidelabs-com
tags:
- Company
- Artificial Intelligence
- Aviation
- Travel
- Infrastructure
- Platform
website: https://airsidelabs.com/
---
