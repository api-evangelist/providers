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
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: COMSPOC provides API access to space situational awareness data, but no machine‑readable contract was found.
  name: COMSPOC API
  slug: comspoc-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/comspoc/refs/heads/main/llms/comspoc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/comspoc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/comspoc/refs/heads/main/hosts/comspoc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comspoc-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comspoc/refs/heads/main/security/comspoc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comspoc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://comspoc.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://comspoc.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://comspoc.com/legal/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://comspoc.com/legal/cookie-policy
created: '2026-09-23'
description: COMSPOC provides commercial off‑the‑shelf software for Space Situational Awareness (SSA). Their platform includes SSASuite, a comprehensive space object catalog, and desktop products such as Spacebook for visualization, SEG for event simulation, and tools for threat assessment. COMSPOC also runs a research center advancing SSA standards and offers data downloads via APIs. The company focuses on delivering actionable space data to support operators, researchers, and policymakers.
image: https://comspoc.blob.core.windows.net/public/comspoc-og-home.jpg
layout: provider
modified: '2026-09-23'
name: COMSPOC
nav: Providers
network: true
overview: COMSPOC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, SSA, Software, and Data.
random_paper: 8
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Comspoc Domain Security
  slug: comspoc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: comspoc
tags:
- Company
- Space
- SSA
- Software
- Data
- Research
website: https://comspoc.com/
---
