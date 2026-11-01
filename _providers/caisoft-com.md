---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Parsable Connected Worker platform
  name: Parsable API
  slug: parsable-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/caisoft-com/llms/caisoft-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caisoft-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/caisoft-com/well-known/caisoft-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caisoft-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/caisoft-com/hosts/caisoft-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caisoft-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/caisoft-com/vendors/caisoft-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caisoft-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caisoft.com/legal/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://support.caisoft.com/s/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caisoft.com/legal/privacy-notice/
- group: company
  title: ''
  type: Blog
  url: https://caisoft.com/blog/
- group: auth
  href: https://artifacts.apis.io/caisoft-com/security/caisoft-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caisoft-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caisoft.com/product/parsable-connected-worker/
coverage:
  checked: '2026-10-29'
  detail: Docs pages redirect to captcha challenges preventing access to OpenAPI specs.
  evidence:
  - status: 200
    url: https://portal.caisoft.com/openapi.json
  - status: 200
    url: https://portal.caisoft.com/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Parsable, part of CAI Software, provides a Connected Worker platform that digitizes frontline workflows for manufacturers and food & beverage companies. Their AI‑driven solution replaces paper procedures with guided digital tasks, improving safety, speed, and data capture while giving leaders real‑time visibility into operations.
image: https://caisoft.com/wp-content/uploads/whyCAI-parsable-connected-worker.jpg
layout: provider
modified: '2026-10-29'
name: Parsable
nav: Providers
network: true
overview: 'Parsable is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, ConnectedWorker, AI, and Frontline.


  Parsable''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
- kind: domain-security
  name: Caisoft Com Domain Security
  slug: caisoft-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caisoft-com
tags:
- Company
- Manufacturing
- ConnectedWorker
- AI
- Frontline
website: https://caisoft.com/product/parsable-connected-worker/
---
