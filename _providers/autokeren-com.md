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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AutoKeren provides an AI-powered developer platform; documentation is available but no machine‑readable contract was found.
  name: AutoKeren API
  slug: autokeren-api
artifact_total: 2
common:
- group: build
  href: https://artifacts.apis.io/autokeren-com/cli/autokeren-com-cli.yml
  title: ''
  type: CLI
  url: cli/autokeren-com-cli.yml
- group: agent
  href: https://artifacts.apis.io/autokeren-com/llms/autokeren-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autokeren-com-llms.txt
- group: other
  href: https://artifacts.apis.io/autokeren-com/hosts/autokeren-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autokeren-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/autokeren-com/vendors/autokeren-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autokeren-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://autokeren.com/solutions/security/
- group: build
  title: ''
  type: SDKs
  url: https://autokeren.com/solutions/libraries/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autokeren.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://autokeren.com/solutions/media/
- group: auth
  href: https://artifacts.apis.io/autokeren-com/security/autokeren-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autokeren-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autokeren.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.autokeren.com/
- group: operate
  title: ''
  type: Support
  url: https://autokeren.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://autokeren.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autokeren
coverage:
  checked: '2026-10-30'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developers.autokeren.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: AutoKeren provides AI-powered products for creators, developers, and organizations, including video generation from PDFs, PPTs, SOPs, and real-time translation. Their platform offers tools like Ghostfox stealth browsing, Dialro AI voice calls, and NinjaAudit social media intelligence, targeting enterprise video generation across industries such as manufacturing, healthcare, education, finance, technology, and hospitality. The company emphasizes AI-driven automation to transform knowledge sources into engaging video content, supporting developers via a dedicated portal and offering various AI services for communication and content creation.
image: https://autokeren.com/og-image.png
layout: provider
modified: '2026-10-30'
name: autokeren-com
nav: Providers
network: true
overview: 'autokeren-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video Generation, Automation, and Enterprise.


  autokeren-com''s developer surface includes CLI, support, engineering blog, and 11 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 58.0
    operational_transparency: 7.9
  previous_composite: 15.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/autokeren-com/autokeren-com-2026-11-03T121403.png
security:
- kind: domain-security
  name: Autokeren Com Domain Security
  slug: autokeren-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: autokeren-com
tags:
- Company
- Artificial Intelligence
- Video Generation
- Automation
- Enterprise
website: https://autokeren.com/
---
