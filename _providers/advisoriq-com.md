---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP (Machine-Readable API) server providing tools for CE requirements, calculations, compliance deadlines, webinars, and research.
  name: AdvisorIQ MCP
  slug: advisoriq-mcp
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/advisoriq-com/llms/advisoriq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/advisoriq-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/advisoriq-com/well-known/advisoriq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/advisoriq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/advisoriq-com/hosts/advisoriq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/advisoriq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/advisoriq-com/vendors/advisoriq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/advisoriq-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://advisoriq.com/signin/
- group: auth
  href: https://artifacts.apis.io/advisoriq-com/security/advisoriq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/advisoriq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advisoriq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://advisoriq.com/mcp/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://advisoriq.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://advisoriq.com/privacy/
- group: other
  title: ''
  type: Standards
  url: https://advisoriq.com/standards/
created: '2026-10-31'
description: AdvisorIQ provides free, independent continuing education for U.S. financial advisors, offering live webinars, on-demand replays, and a comprehensive CE tracker. As of Oct 31 2026, it tracks CE requirements for 17 designations across 25 jurisdictions, delivering up-to-date compliance deadlines, designation-specific calculators, and a searchable directory of RIAs. All content is sponsored but remains editorially independent, with no product pitches. The platform also supplies research articles, succession resources, and tools to help advisors manage their practice.
layout: provider
modified: '2026-10-31'
name: AdvisorIQ
nav: Providers
network: true
overview: 'AdvisorIQ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Financial Services, Continuing Education, CE Tracker, and Webinars.


  AdvisorIQ''s developer surface includes documentation and 10 more developer resources.'
random_paper: 22
scopes:
- name: Advisoriq Com Scopes
  scope_count: 0
  slug: advisoriq-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 15.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Advisoriq Com Authentication
  slug: advisoriq-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Advisoriq Com Domain Security
  slug: advisoriq-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: advisoriq-com
tags:
- Education
- Financial Services
- Continuing Education
- CE Tracker
- Webinars
website: https://advisoriq.com/
---
