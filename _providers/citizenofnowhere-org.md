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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/citizenofnowhere-org/llms/citizenofnowhere-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citizenofnowhere-org-llms.txt
- group: other
  href: https://artifacts.apis.io/citizenofnowhere-org/hosts/citizenofnowhere-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citizenofnowhere-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/citizenofnowhere-org/vendors/citizenofnowhere-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citizenofnowhere-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/citizenofnowhere-org/security/citizenofnowhere-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citizenofnowhere-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citizenofnowhere.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.citizenofnowhere.org/pricing
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing known hosts.
  evidence:
  - status: 404
    url: https://rankings.citizenofnowhere.org/api/openapi.json
  - status: 404
    url: https://rankings.citizenofnowhere.org/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Citizen of Nowhere is a studio and consultancy founded by Ashwin Desikan, focusing on data, identity, measurement and audience systems. It offers advisory services across sports, AdTech, and major platforms, and publishes insights, tools, and a clean‑room API for public use.
image: https://www.citizenofnowhere.org/og.png
layout: provider
modified: '2026-11-03'
name: Citizen of Nowhere
nav: Providers
network: true
overview: 'Citizen of Nowhere is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Identity, Consultancy, SportsTech, and AdTech.


  Citizen of Nowhere''s developer surface includes pricing and 5 more developer resources.'
plans:
- name: Citizenofnowhere Org Plans Pricing
  plan_count: 0
  slug: citizenofnowhere-org-plans-pricing
random_paper: 16
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citizenofnowhere Org Domain Security
  slug: citizenofnowhere-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citizenofnowhere-org
tags:
- Data
- Identity
- Consultancy
- SportsTech
- AdTech
website: https://citizenofnowhere.org/
---
