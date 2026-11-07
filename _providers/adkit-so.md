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
api_count: 1
apis:
- description: AdKit provides an API for AI agents to manage ads, as described in the documentation.
  name: AdKit API
  slug: adkit-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/adkit-so/llms/adkit-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adkit-so-llms.txt
- group: agent
  href: https://artifacts.apis.io/adkit-so/well-known/adkit-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adkit-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/adkit-so/hosts/adkit-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adkit-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/adkit-so/vendors/adkit-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adkit-so-vendors.yml
- group: build
  href: https://artifacts.apis.io/adkit-so/packages/adkit-so-packages.yml
  title: ''
  type: SDKs
  url: packages/adkit-so-packages.yml
- group: build
  href: https://artifacts.apis.io/adkit-so/packages/adkit-so-packages.yml
  title: ''
  type: Packages
  url: packages/adkit-so-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://adkit.so/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adkit.so/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://adkit.so/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adkit.so/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://adkit.so/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://adkit.so/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://adkit.so/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/adkit-so/security/adkit-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adkit-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adkit.so/
coverage:
  checked: '2026-10-31'
  detail: MCP endpoint https://app.adkit.so/api/mcp returns 401 Unauthorized, indicating API access is gated behind authentication.
  evidence:
  - status: 401
    url: https://app.adkit.so/api/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: AdKit provides a comprehensive ads toolbox for marketers and AI agents, enabling them to research competitors, create ad copy, launch advertising campaigns, and track performance. The platform integrates with popular AI models such as Claude, ChatGPT, Perplexity, Gemini, and more, offering client libraries for each. Users can manage multiple ad accounts, collaborate with team members, set access levels, and upload creative media directly through the interface. Documentation includes detailed getting‑started guides, pricing information, privacy policy, terms of service, and a trust & security center.
image: https://adkit.so/images/og-image.png
layout: provider
modified: '2026-10-31'
name: AdKit
nav: Providers
network: true
overview: 'AdKit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketing, Artificial Intelligence, AdTech, and Automation.


  AdKit''s developer surface includes support, pricing, documentation, getting-started guide, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 19.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 21.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adkit So Domain Security
  slug: adkit-so-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adkit-so
tags:
- Advertising
- Marketing
- Artificial Intelligence
- AdTech
- Automation
website: https://adkit.so/
---
