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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bannerflow/refs/heads/main/llms/bannerflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bannerflow-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bannerflow/refs/heads/main/well-known/bannerflow-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bannerflow-support-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bannerflow/refs/heads/main/well-known/bannerflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bannerflow-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bannerflow/refs/heads/main/hosts/bannerflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bannerflow-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bannerflow/refs/heads/main/vendors/bannerflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bannerflow-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bannerflow/refs/heads/main/packages/bannerflow-packages.yml
  title: ''
  type: SDKs
  url: packages/bannerflow-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bannerflow/refs/heads/main/packages/bannerflow-packages.yml
  title: ''
  type: Packages
  url: packages/bannerflow-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bannerflow.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.bannerflow.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bannerflow.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.bannerflow.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bannerflow
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bannerflow/refs/heads/main/security/bannerflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bannerflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bannerflow.com/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at known API hosts.
  evidence:
  - status: 404
    url: https://api.bannerflow.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Bannerflow provides a creative automation platform that enables marketers and agencies to design, produce, and scale digital ads across multiple channels. The solution supports dynamic creative optimization, localization, real‑time campaign management, and integration with data feeds, helping brands launch personalized creatives faster and improve performance. Bannerflow serves industries such as retail, finance, travel, telecom, entertainment, and iGaming, offering tools for both in‑house teams and agencies.
image: https://www.bannerflow.com/hubfs/Featured%20image_Bannerflow.webp
layout: provider
modified: '2026-10-15'
name: Bannerflow
nav: Providers
network: true
overview: 'Bannerflow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Creative Automation, Ad Production, Dynamic Creative Optimization, Localization, and Real‑time Campaign Management.


  Bannerflow''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bannerflow Domain Security
  slug: bannerflow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bannerflow
tags:
- Creative Automation
- Ad Production
- Dynamic Creative Optimization
- Localization
- Real‑time Campaign Management
- Marketing Technology
website: https://bannerflow.com/
---
