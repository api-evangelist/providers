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
- description: API for MindFlows platform, documented at the interface docs page.
  name: MindFlows API
  slug: mindflows-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/mindflows-us/llms/mindflows-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mindflows-us-llms.txt
- group: other
  href: https://artifacts.apis.io/mindflows-us/hosts/mindflows-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mindflows-us-hosts.yml
- group: other
  href: https://artifacts.apis.io/mindflows-us/vendors/mindflows-us-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mindflows-us-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.mindflows.us/signup.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LogicLabsAI
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mindflows.us/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/mindflows-us/security/mindflows-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mindflows-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mindflows.us/
- group: docs
  title: ''
  type: Documentation
  url: https://mindflows.us/docs.html
- group: company
  title: ''
  type: Blog
  url: https://mindflows.us/blog.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mindflows.us/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mindflows.us/privacy.html
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered via JavaScript, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 200
    url: https://www.mindflows.us/docs/interface/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: MindFlows provides a visual workflow and knowledge‑management platform that aggregates content from YouTube, Notion, Google Docs, PDFs and the web into a single space. Its AI Spark Search uses semantic AI to retrieve saved material by meaning, allowing users to locate videos, documents, and notes instantly. The service is aimed at individuals and teams who need to organize and recall scattered research and ideas.
image: https://www.mindflows.us/images/og-image.png
layout: provider
modified: '2026-10-30'
name: mindflows-us
nav: Providers
network: true
overview: 'mindflows-us is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Knowledge Management, Visual Workflow, and AI Search.


  mindflows-us'' developer surface includes signup flow, getting-started guide, documentation, engineering blog, and 8 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 16.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mindflows-us/mindflows-us-2026-11-03T135629.png
security:
- kind: domain-security
  name: Mindflows Us Domain Security
  slug: mindflows-us-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mindflows-us
tags:
- Knowledge Management
- Visual Workflow
- AI Search
website: https://mindflows.us/
---
