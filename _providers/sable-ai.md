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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/sable-ai/llms/sable-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sable-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/sable-ai/well-known/sable-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sable-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/sable-ai/hosts/sable-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sable-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/sable-ai/vendors/sable-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sable-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.withsable.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.withsable.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://sable.ai/releases
- group: company
  title: ''
  type: Blog
  url: https://sable.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withsable.com/
- group: auth
  href: https://artifacts.apis.io/sable-ai/security/sable-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sable-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withsable.com/
coverage:
  checked: '2026-10-29'
  detail: Docs at https://docs.withsable.com return redirects and require login, providing no machine‑readable spec.
  evidence:
  - status: 302
    url: https://docs.withsable.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Sable AI provides AI‑led product demos and sales calls through its virtual employee, Aidan. Leveraging real‑time browser automation and computer‑vision, Aidan can understand product contexts, conduct interactive demos, answer questions, and continuously improve via a knowledge graph built from every customer interaction. Backed by Sequoia Capital and 8VC, Sable serves enterprises seeking scalable, personalized product experiences, offering secure, GDPR‑compliant solutions with ISO 27001 and SOC 2 certifications.
layout: provider
modified: '2026-10-29'
name: Sable AI
nav: Providers
network: true
overview: 'Sable AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Product Demos, Sales Automation, and Enterprise.


  Sable AI''s developer surface includes changelog, engineering blog, documentation, and 8 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 51.8
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.3
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sable-ai/sable-ai-2026-11-03T142625.png
security:
- kind: domain-security
  name: Sable Ai Domain Security
  slug: sable-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sable-ai
tags:
- Company
- Artificial Intelligence
- Product Demos
- Sales Automation
- Enterprise
website: https://withsable.com/
---
