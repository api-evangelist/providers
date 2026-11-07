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
- description: API for CatchUI UI pattern identification service
  name: CatchUI API
  slug: catchui-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/catchui-com/conventions/catchui-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/catchui-com-conventions.yml
- group: agent
  href: https://artifacts.apis.io/catchui-com/llms/catchui-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catchui-com-llms.txt
- group: other
  href: https://artifacts.apis.io/catchui-com/hosts/catchui-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catchui-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/catchui-com/vendors/catchui-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catchui-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://catchui.com/guides/ui-icon-names
- group: auth
  href: https://artifacts.apis.io/catchui-com/security/catchui-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catchui-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catchui.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://catchui.com/guides/identify-ui-patterns-from-screenshot
- group: commercial
  title: ''
  type: TermsOfService
  url: https://catchui.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catchui.com/legal/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://catchui.com/about
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing known API hosts.
  evidence:
  - status: 404
    url: https://api.catchui.com/openapi.json
  - status: 404
    url: https://catchui.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CatchUI is a bilingual UI pattern identifier and learning library that uses model‑assisted screenshot recognition to name UI elements. Users can upload interface screenshots, receive pattern names with evidence, and save cards to a personal library for spaced‑repetition learning. The service offers a free tier with limited scans and paid Pro plans for higher daily usage.
image: https://catchui.com/og.png
layout: provider
modified: '2026-11-04'
name: CatchUI
nav: Providers
network: true
overview: 'CatchUI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include UI, Design, Education, Artificial Intelligence, and Tool.


  CatchUI''s developer surface includes documentation, getting-started guide, support, and 8 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Catchui Com Domain Security
  slug: catchui-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: catchui-com
tags:
- UI
- Design
- Education
- Artificial Intelligence
- Tool
website: https://catchui.com/
---
