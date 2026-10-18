---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleoai/refs/heads/main/hosts/cleoai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleoai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleoai/refs/heads/main/vendors/cleoai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleoai-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleoai/refs/heads/main/security/cleoai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleoai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/cleoai
- group: docs
  title: ''
  type: Documentation
  url: https://cleoai.io
- group: start
  title: ''
  type: GettingStarted
  url: https://cleoai.io/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://cleoai.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleoai.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleoai.io/privacy
coverage:
  checked: '2026-10-09'
  detail: The API reference page returns HTML shells for /openapi.json and /openapi.yaml, providing no machine‑readable spec.
  evidence:
  - status: 200
    url: https://cleoai.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: 'Cleoai provides AI-powered customer support agents that automate ticket handling, email responses, and even code bug fixes. Their platform offers two main agents: a Support Agent for handling customer inquiries and an AI Engineer that can understand and patch software code. Built for SaaS companies, support teams, and agencies, CleoAI integrates with email inboxes, knowledge bases, and GitHub repositories to streamline support workflows, reduce response times, and improve customer satisfaction.'
layout: provider
modified: '2026-10-08'
name: Cleoai
nav: Providers
network: true
overview: 'Cleoai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Customer Service, Software-as-a-Service, and Automation.


  Cleoai''s developer surface includes documentation, getting-started guide, pricing, and 6 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleoai Domain Security
  slug: cleoai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cleoai
tags:
- Company
- Artificial Intelligence
- Customer Service
- Software-as-a-Service
- Automation
website: https://equityzen.com/company/cleoai
---
