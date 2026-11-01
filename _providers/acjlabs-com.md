---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: MCP servers and APIs for agentic commerce — catalog attribute normalization, AU GST-aware receipt extraction, x402 Bazaar listing monitoring.
  name: ACJ Labs API
  slug: acj-labs-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/acjlabs-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/acjlabs-com/llms/acjlabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acjlabs-com-llms.txt
- group: other
  href: https://artifacts.apis.io/acjlabs-com/hosts/acjlabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acjlabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/acjlabs-com/vendors/acjlabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acjlabs-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/acjlabs-com/packages/acjlabs-com-packages.yml
  title: ''
  type: SDKs
  url: packages/acjlabs-com-packages.yml
- group: build
  href: https://artifacts.apis.io/acjlabs-com/packages/acjlabs-com-packages.yml
  title: ''
  type: Packages
  url: packages/acjlabs-com-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://acjlabs.com/news
- group: auth
  href: https://artifacts.apis.io/acjlabs-com/security/acjlabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acjlabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acjlabs.com/
- group: company
  title: ''
  type: Blog
  url: https://acjlabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acjlabs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acjlabs.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://acjlabs.com/contact
coverage:
  checked: '2026-10-29'
  detail: No public API documentation or machine‑readable spec was found on acjlabs.com or its subdomains.
  evidence:
  - status: 200
    url: https://acjlabs.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: ACJ Labs (Agentic Commerce Junction Labs) is an Australian‑based portfolio lab building focused, inspectable software tools for the agentic‑commerce ecosystem. Their products include catalog attribute normalization, receipt extraction, and other MCP‑style APIs that provide transparent confidence scores and plain‑English rationales. All tools are open‑source, MIT‑licensed, and offered on a free tier with no credit‑card required. The company operates under IMD Solutions Pty Ltd (ABN 72 124 377 635).
image: https://acjlabs.com/brand/acj-lockup-e-ink.svg
layout: provider
modified: '2026-10-29'
name: acjlabs-com
nav: Providers
network: true
overview: 'acjlabs-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, AgenticCommerce, OpenSource, and Australia.


  acjlabs-com''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 4
scopes:
- name: Acjlabs Com Scopes
  scope_count: 0
  slug: acjlabs-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.7
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acjlabs Com Authentication
  slug: acjlabs-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Acjlabs Com Domain Security
  slug: acjlabs-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acjlabs-com
tags:
- Company
- AI
- AgenticCommerce
- OpenSource
- Australia
website: https://acjlabs.com/
---
