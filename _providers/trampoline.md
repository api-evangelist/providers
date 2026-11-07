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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Programmatic access to Trampoline's AI workflow platform (no public documentation found).
  name: Trampoline API
  slug: trampoline-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/trampoline/llms/trampoline-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trampoline-llms.txt
- group: other
  href: https://artifacts.apis.io/trampoline/hosts/trampoline-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trampoline-hosts.yml
- group: other
  href: https://artifacts.apis.io/trampoline/vendors/trampoline-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trampoline-vendors.yml
- group: auth
  href: https://artifacts.apis.io/trampoline/security/trampoline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trampoline-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trampoline.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Trampoline-AI/avalanche
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trampoline.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trampoline.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://trampoline.ai/#contact
coverage:
  checked: '2026-10-29'
  detail: No public API documentation or machine‑readable contract was found on trampoline.ai or its subdomains.
  evidence:
  - status: 404
    url: https://trampoline.ai/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Trampoline provides a platform for building, deploying, operating, and governing reliable AI workflows for products, services, and business operations. It enables users to describe desired outcomes, connect data and tools, and run AI-driven processes with monitoring, governance, and security. The platform offers open-source developer packages, integrations with popular AI models, and a control tower for observability, supporting enterprise-scale automation and compliance.
image: https://trampoline.ai/img/og.png
layout: provider
modified: '2026-10-29'
name: Trampoline
nav: Providers
network: true
overview: 'Trampoline is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Workflows, Platform, and Enterprise.


  Trampoline''s developer surface includes support and 8 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 0
  name: Trampoline Rate Limits
  slug: trampoline-rate-limits
scopes:
- name: Trampoline Scopes
  scope_count: 0
  slug: trampoline-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trampoline/trampoline-2026-11-03T145016.png
security:
- kind: authentication
  name: Trampoline Authentication
  slug: trampoline-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Trampoline Domain Security
  slug: trampoline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trampoline
tags:
- Artificial Intelligence
- Automation
- Workflows
- Platform
- Enterprise
website: https://trampoline.ai
---
