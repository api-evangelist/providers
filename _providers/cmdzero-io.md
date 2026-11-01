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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Command Zero platform API (no public machine‑readable contract discovered).
  name: Command Zero API
  slug: command-zero-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/cmdzero-io/llms/cmdzero-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cmdzero-io-llms.txt
- group: other
  href: https://artifacts.apis.io/cmdzero-io/hosts/cmdzero-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cmdzero-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/cmdzero-io/vendors/cmdzero-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cmdzero-io-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commandzero.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.commandzero.ai/press
- group: company
  title: ''
  type: Blog
  url: https://www.commandzero.ai/blog
- group: auth
  href: https://artifacts.apis.io/cmdzero-io/security/cmdzero-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cmdzero-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.commandzero.ai/
coverage:
  checked: '2026-10-22'
  detail: Main site renders content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.commandzero.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Command Zero provides an autonomous AI-driven Security Operations Center (SOC) investigation platform. It offers AI‑assisted and fully autonomous investigation modes, covering the full Tier‑1 to Tier‑3 lifecycle across identity, endpoint, cloud, and SaaS environments. The platform enables rapid threat detection, response automation, and deep forensic analysis, helping security teams reduce mean‑time‑to‑detect and mean‑time‑to‑respond.
image: https://www.commandzero.ai/og-default.jpg
layout: provider
modified: '2026-10-22'
name: Command Zero
nav: Providers
network: true
overview: 'Command Zero is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Security, SOC, and Automation.


  Command Zero''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cmdzero Io Domain Security
  slug: cmdzero-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cmdzero-io
tags:
- Company
- AI
- Security
- SOC
- Automation
website: https://www.commandzero.ai/
---
