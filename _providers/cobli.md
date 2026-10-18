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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.3
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Fleet management API documented at Cobli developer reference.
  name: Cobli API
  slug: cobli-api-2
- baseURL: https://api.cobli.co
  baseurl_source: declared
  description: The Public API from Cobli — 2 operation(s) for public.
  name: Cobli Public API
  slug: cobli-public-api
artifact_total: 7
asyncapis:
- description: ''
  name: Cobli Webhooks
  slug: cobli-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/rules/cobli-rules.yml
  title: ''
  type: Spectral
  url: rules/cobli-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/json-ld/cobli-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cobli-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/vocabulary/cobli-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cobli-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/asyncapi/cobli-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cobli-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/data-model/cobli-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cobli-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/conformance/cobli-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cobli-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/llms/cobli-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cobli-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/well-known/cobli-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cobli-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/hosts/cobli-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cobli-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/vendors/cobli-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cobli-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.cobli.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cobli.co/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cobli.co/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cobli/refs/heads/main/security/cobli-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cobli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cobli.co
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://blog.cobli.co/graphql
  - status: 401
    url: https://docs.cobli.co/mcp
  - status: 403
    url: https://painel.cobli.co/mcp
  - status: 200
    url: https://www.cobli.co
  - status: 403
    url: https://equityzen.com/company/cobli
  reason: partner-login
  state: gated
created: '2026-10-09'
description: Cobli provides a fleet management platform that combines video telematics, traditional telematics, and mobile applications to give operators real‑time visibility, reduce costs, improve driver safety, and optimize routes. The solution includes video‑based driver monitoring, AI‑driven analytics, fuel and maintenance tracking, and compliance tools, serving logistics companies and vehicle fleets across Brazil and Latin America.
image: https://www.cobli.co/share-image.png
json_schemas:
- name: GetPublicV1PathsResponse
  property_count: 4
  slug: cobli-get-public-v1-paths-response
jsonld:
- class_count: 1
  name: Cobli Context
  property_count: 0
  slug: cobli-context
layout: provider
modified: '2026-10-09'
name: Cobli
nav: Providers
network: true
overview: 'Cobli is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Public API, and 1 more. Tagged areas include Company.


  The Cobli catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cobli''s developer surface includes engineering blog, API reference, documentation, and 12 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Cobli API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: cobli-rules
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 43.2
    catalog_earned_first_party: 0.0
    catalog_gap: 56.9
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.6
    developer_ergonomics: 19.0
    discoverability: 55.4
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Cobli Domain Security
  slug: cobli-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cobli
tags:
- Company
website: https://www.cobli.co
---
