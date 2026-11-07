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
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/hubbroker/llms/hubbroker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hubbroker-llms.txt
- group: agent
  href: https://artifacts.apis.io/hubbroker/well-known/hubbroker-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hubbroker-well-known.yml
- group: other
  href: https://artifacts.apis.io/hubbroker/hosts/hubbroker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hubbroker-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://hubbroker.com/blog/register-danish-business-on-nemhandel/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hubbroker.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://hubbroker.com/blog/
- group: auth
  href: https://artifacts.apis.io/hubbroker/security/hubbroker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hubbroker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hubbroker.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://hubbroker.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: HubBroker ApS provides an iPaaS EDI integration service that automates orders, invoices, ASNs and trading partner data across ERP systems, suppliers and customers. It offers solutions such as PDF to XML conversion, Peppol e‑invoicing, AI document processing, and ERP API integration, serving over 120,000 monthly transactions for global clients.
image: https://hubbroker.com/media/0u0jgjgu/gemini_generated_image_cx7qk2cx7qk2cx7q-photoroom.png
layout: provider
modified: '2026-10-20'
name: HubBroker ApS
nav: Providers
network: true
overview: 'HubBroker ApS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EDI, Integration, iPaaS, and Automation.


  HubBroker ApS''s developer surface includes signup flow, engineering blog, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hubbroker/hubbroker-2026-11-03T133515.png
security:
- kind: domain-security
  name: Hubbroker Domain Security
  slug: hubbroker-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hubbroker
tags:
- Company
- EDI
- Integration
- iPaaS
- Automation
website: https://hubbroker.com/
---
