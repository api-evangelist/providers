---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
- description: Authority.md provides a curated marketplace of AI thinking frameworks, tools, and playbooks for large language models.
  name: Authority API
  slug: authority-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/authority-md/plans/authority-md-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/authority-md-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/authority-md/llms/authority-md-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authority-md-llms.txt
- group: other
  href: https://artifacts.apis.io/authority-md/hosts/authority-md-hosts.yml
  title: ''
  type: Hosts
  url: hosts/authority-md-hosts.yml
- group: other
  href: https://artifacts.apis.io/authority-md/vendors/authority-md-vendors.yml
  title: ''
  type: Vendors
  url: vendors/authority-md-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://authority.md/security
- group: docs
  title: ''
  type: Documentation
  url: https://authority.md/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://authority.md/category/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://authority.md/playbooks/release-notes
- group: auth
  href: https://artifacts.apis.io/authority-md/security/authority-md-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authority-md-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://authority.md/
- group: commercial
  title: ''
  type: Pricing
  url: https://authority.md/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://authority.md/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://authority.md/privacy
coverage:
  checked: '2026-11-02'
  detail: Provider documentation is HTML pages without any machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://authority.md/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Authority.md provides a curated marketplace of AI thinking frameworks, tools, and playbooks for large language models like Claude and ChatGPT. It offers bundles of curated mental models, skill files, and prompts across categories such as investing, leadership, and creativity, enabling users to integrate structured reasoning into AI agents. The platform sells individual frameworks and bundle packages, and includes free skills and guides for building AI‑augmented workflows.
image: https://authority.md/api/og/home?v=2
layout: provider
modified: '2026-11-02'
name: Authority.md
nav: Providers
network: true
overview: 'Authority.md is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Tools, Playbooks, and Framework.


  Authority.md''s developer surface includes documentation, changelog, pricing, and 10 more developer resources.'
plans:
- name: Authority Md Plans Pricing
  plan_count: 5
  slug: authority-md-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 25.2
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Authority Md Domain Security
  slug: authority-md-domain-security
  summary_line: TLSv1.3 · DMARC
slug: authority-md
tags:
- Artificial Intelligence
- Marketplace
- Tools
- Playbooks
- Framework
website: https://authority.md/
---
