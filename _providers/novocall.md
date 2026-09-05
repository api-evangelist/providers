---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novocall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://novocall.co
- group: build
  title: ''
  type: Packages
  url: packages/novocall-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/novocall-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://sg.linkedin.com/company/novocall
coverage:
  checked: '2026-08-13'
  detail: Novocall was absorbed into EasyStore in March 2023 and its infrastructure has since been switched off — the apex novocall.co has no A record, the www, app and call.novocall.co hosts all return Cloudflare 530 with no origin behind them, the help center returns Cloudflare error 1027, and novocall.com is now an Afternic for-sale lander that answers 200 with HTML for every path including /openapi.json.
  evidence:
  - status: 530
    url: https://www.novocall.co/
  - status: 530
    url: https://call.novocall.co/
  - status: 530
    url: https://app.novocall.co/
  - status: 429
    url: https://help.novocall.co/
  - status: 200
    url: https://novocall.com/openapi.json
  - status: 200
    url: https://wordpress.org/plugins/novocall-callback-widget/
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Novocall was a Singapore-based callback and lead-conversion SaaS (a click-to-call and callback-scheduling widget that turned website visitors into inbound phone calls and booked meetings), surfaced as a 500 Global portfolio company and added to the API Evangelist network as a stub for enrichment. It was acquired by Malaysian commerce platform EasyStore in March 2023, alongside sibling product NovoChat, and has been marketed since as "Novocall, an EasyStore company". As of the August 2026 enrichment pass every Novocall host is dead: the apex novocall.co keeps live email DNS (Google Workspace MX, SPF, DMARC quarantine, CAA) but has no A record at all, www.novocall.co, app.novocall.co and call.novocall.co — the widget/dashboard host hardcoded in Novocall''s own WordPress plugin — all return a Cloudflare 530 (edge up, origin gone), help.novocall.co returns 429 with Cloudflare error 1027 (account daily request limit reached), getnovocall.com times out, and novocall.com is now an
  Afternic parked domain whose catch-all answers 200 with an HTML lander for every path including /openapi.json and /.well-known/agent-card.json. No API, specification, developer portal, .well-known document or documentation surface exists on any reachable host. The only first-party artifact Novocall ever published that survives is a WordPress callback-widget plugin, stuck at version 1.0.0 since 2019-04-08.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novocall.png
layout: provider
modified: '2026-08-13'
name: Novocall
nav: Providers
network: true
overview: Novocall is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Callback, Lead Conversion, Click To Call, and Sales.
plans:
- name: Novocall Plans Pricing
  plan_count: 0
  slug: novocall-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Novocall Rate Limits
  slug: novocall-rate-limits
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Novocall Domain Security
  slug: novocall-domain-security
  summary_line: DMARC
slug: novocall
tags:
- Company
- Callback
- Lead Conversion
- Click To Call
- Sales
- Marketing
- Software-as-a-Service
website: https://novocall.co
---
