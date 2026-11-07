---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/draftboard-com/llms/draftboard-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/draftboard-com-llms.txt
- group: other
  href: https://artifacts.apis.io/draftboard-com/hosts/draftboard-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/draftboard-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/draftboard-com/vendors/draftboard-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/draftboard-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.draftboard.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.draftboard.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://intros.draftboard.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.draftboard.com/blog
- group: auth
  href: https://artifacts.apis.io/draftboard-com/security/draftboard-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/draftboard-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://draftboard.com/
coverage:
  checked: '2026-11-06'
  detail: Documentation at https://intros.draftboard.com/api is a JavaScript‑rendered HTML page with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://intros.draftboard.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Draftboard provides a platform that automatically maps your network and delivers warm introductions to enterprise prospects. It eliminates the need for CSV exports by integrating directly with target accounts, offering insights into each connection’s value. The service focuses on account‑based marketing, helping sales teams discover and engage potential customers efficiently.
image: https://www.draftboard.com/og-image.png
layout: provider
modified: '2026-11-05'
name: Draftboard
nav: Providers
network: true
overview: 'Draftboard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B, Sales, Marketing, and Account Based Marketing.


  Draftboard''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Draftboard Com Domain Security
  slug: draftboard-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: draftboard-com
tags:
- Company
- B2B
- Sales
- Marketing
- Account Based Marketing
- Warm Introductions
website: https://draftboard.com/
---
