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
    dynamic_client_registration: true
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
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for 765T Flow AI tools for Autodesk Revit as described in the documentation.
  name: 765T Flow API
  slug: 765t-flow-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/765tflow-com/llms/765tflow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/765tflow-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/765tflow-com/well-known/765tflow-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/765tflow-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/765tflow-com/hosts/765tflow-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/765tflow-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/765tflow-com/vendors/765tflow-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/765tflow-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://765tflow.com/media/765t-flow-demo.mp4
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meococ
- group: operate
  title: ''
  type: ChangeLog
  url: https://765tflow.com/releases
- group: auth
  href: https://artifacts.apis.io/765tflow-com/security/765tflow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/765tflow-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://765tflow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://765tflow.com/docs
- group: operate
  title: ''
  type: Support
  url: https://765tflow.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://765tflow.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://765tflow.com/terms
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://765tflow.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: 765T Flow provides AI-powered tools for Autodesk Revit, enabling users to automate BIM workflows, perform quality checks, and integrate AI-driven design assistance directly within Revit. The platform offers a suite of features including parameter management, sheet completion, automated tagging, and export of reports in CSV, IFC, and PDF formats. It connects AI applications to Revit via a hosted MCP endpoint, supporting standard MCP connectors and facilitating seamless AI integration for architects and engineers.
image: https://765tflow.com/og.jpg
layout: provider
modified: '2026-10-31'
name: 765T Flow
nav: Providers
network: true
overview: '765T Flow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Revit, BIM, and Automation.


  765T Flow''s developer surface includes changelog, documentation, support, and 10 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.0
    operational_transparency: 10.5
  previous_composite: 16.2
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 765Tflow Com Domain Security
  slug: 765tflow-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 765tflow-com
tags:
- Company
- Artificial Intelligence
- Revit
- BIM
- Automation
website: https://765tflow.com/
---
