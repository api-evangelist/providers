---
agent_readiness:
  band: agent-aware
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for VXT AI-powered call and meeting note automation platform
  name: VXT API
  slug: vxt-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/vxt/plans/vxt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vxt-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vxt/conformance/vxt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vxt-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vxt/llms/vxt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vxt-llms.txt
- group: other
  href: https://artifacts.apis.io/vxt/hosts/vxt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vxt-hosts.yml
- group: other
  href: https://artifacts.apis.io/vxt/vendors/vxt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vxt-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.vxt.ai/integrations/webhooks
- group: company
  title: ''
  type: Newsroom
  url: https://www.vxt.ai/media
- group: other
  title: ''
  type: Leadership
  url: https://www.vxt.ai/products/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.vxt.ai/changelog
- group: auth
  href: https://artifacts.apis.io/vxt/security/vxt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vxt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vxt.ai/
- group: operate
  title: ''
  type: Support
  url: https://support.vxt.co.nz/
- group: company
  title: ''
  type: Blog
  url: https://www.vxt.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vxt.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vxt.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vxt.ai/legal/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Provider documentation at https://www.vxt.ai is HTML only and does not expose a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract.
  evidence:
  - status: 200
    url: https://www.vxt.ai
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: VXT provides AI-powered call and meeting note automation for law firms, turning conversations into structured legal paperwork, call recordings, time tracking, and email drafts. Integrated with major legal software, it aims to recover extra billable minutes and streamline workflow for lawyers.
image: https://cdn.prod.website-files.com/610ddb83766d492e4422c09f/6a8bceb28505e9c8f0cf7465_OG%20image%20(1).jpg
layout: provider
modified: '2026-10-28'
name: VXT
nav: Providers
network: true
overview: 'VXT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, LegalTech, CallAutomation, and SaaS.


  VXT''s developer surface includes changelog, support, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Vxt Plans Pricing
  plan_count: 3
  slug: vxt-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 60.7
    operational_transparency: 23.7
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vxt Domain Security
  slug: vxt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vxt
tags:
- Company
- AI
- LegalTech
- CallAutomation
- SaaS
website: https://www.vxt.ai/
---
