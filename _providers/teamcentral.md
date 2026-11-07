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
    mcp_server: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teamcentral.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.teamcentral.io/
- group: agent
  href: https://artifacts.apis.io/teamcentral/llms/teamcentral-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/teamcentral-llms.txt
- group: agent
  href: https://artifacts.apis.io/teamcentral/well-known/teamcentral-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teamcentral-well-known.yml
- group: other
  href: https://artifacts.apis.io/teamcentral/hosts/teamcentral-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teamcentral-hosts.yml
- group: other
  href: https://artifacts.apis.io/teamcentral/vendors/teamcentral-vendors.yml
  title: ''
  type: Vendors
  url: vendors/teamcentral-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamcentral
- group: auth
  href: https://artifacts.apis.io/teamcentral/security/teamcentral-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teamcentral-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teamcentral.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.teamcentral.ai/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.teamcentral.ai/category/articles/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teamcentral.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teamcentral.ai/privacy-policy/
coverage:
  checked: '2026-10-21'
  detail: Documentation pages return 404 HTML shells, no machine‑readable spec found.
  evidence:
  - status: 404
    url: https://www.teamcentral.ai/documentation/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: TeamCentral provides an AI‑powered integration platform that connects enterprise systems such as ERP, CRM, WMS, and TMS into a unified data layer. Their CORBI AI agent automates data synchronization, offers real‑time insights, and supports no‑code workflow building for supply‑chain intelligence, finance, and operations. The platform emphasizes secure, governed data exchange and AI readiness across a wide range of connectors and industry solutions, targeting large enterprises seeking to streamline processes and leverage AI at scale.
image: https://www.teamcentral.ai/wp-content/uploads/2021/03/cropped-favicon2.png
layout: provider
modified: '2026-10-21'
name: TeamCentral
nav: Providers
network: true
overview: 'TeamCentral is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Integration, Supply Chain, and Enterprise.


  TeamCentral''s developer surface includes documentation, support, engineering blog, and 10 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 55.4
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.2
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/teamcentral/teamcentral-2026-11-03T144345.png
security:
- kind: domain-security
  name: Teamcentral Domain Security
  slug: teamcentral-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: teamcentral
tags:
- Company
- Artificial Intelligence
- Integration
- Supply Chain
- Enterprise
website: https://teamcentral.ai/
---
