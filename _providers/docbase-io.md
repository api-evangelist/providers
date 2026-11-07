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
    mcp_server: documented
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
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DocBase provides a wiki and knowledge‑sharing platform with AI assistance.
  name: DocBase API
  slug: docbase-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://docbase.io/security
- group: agent
  href: https://artifacts.apis.io/docbase-io/llms/docbase-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docbase-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/docbase-io/well-known/docbase-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docbase-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/docbase-io/hosts/docbase-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docbase-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/docbase-io/packages/docbase-io-packages.yml
  title: ''
  type: SDKs
  url: packages/docbase-io-packages.yml
- group: build
  href: https://artifacts.apis.io/docbase-io/packages/docbase-io-packages.yml
  title: ''
  type: Packages
  url: packages/docbase-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docbase.io/terms
- group: auth
  title: ''
  type: Security
  url: https://docbase.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docbase.io/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://docbase.io/media
- group: docs
  title: ''
  type: Documentation
  url: https://help.docbase.io/
- group: auth
  href: https://artifacts.apis.io/docbase-io/security/docbase-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/docbase-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/docbase-io/security/docbase-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docbase-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docbase.io/
coverage:
  checked: '2026-11-05'
  detail: Help site renders a JavaScript shell with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://help.docbase.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DocBase is an internal wiki and knowledge‑sharing platform that enables teams to create, organize, and collaborate on documentation with AI assistance. It offers three editing modes, enterprise‑grade security, and supports seamless knowledge management across organizations of any size. Over 12,000 companies use DocBase to improve information flow, with a 99 % retention rate and robust AI integration for safe, efficient content creation.
image: https://docbase.io/ogp.png
layout: provider
modified: '2026-11-05'
name: DocBase
nav: Providers
network: true
overview: 'DocBase is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wiki, Knowledge Management, Artificial Intelligence, and Collaboration.


  DocBase''s developer surface includes documentation and 13 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docbase Io Domain Security
  slug: docbase-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Docbase Io Trust Center
  slug: docbase-io-trust-center
  summary_line: ISO 27001
slug: docbase-io
tags:
- Company
- Wiki
- Knowledge Management
- Artificial Intelligence
- Collaboration
website: https://docbase.io/
---
