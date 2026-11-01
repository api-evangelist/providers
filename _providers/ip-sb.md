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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Free REST API for IP address information, providing endpoints for caller IP, GeoIP lookup, DNS queries, WHOIS, speed tests, and more. No authentication or API key required.
  name: IP.SB API
  slug: ip-sb-api-2
- baseURL: https://api-ipv4.ip.sb
  baseurl_source: declared
  description: 'IP.SB API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: IP.SB API
  slug: ip-sb-api
artifact_total: 10
common:
- group: operate
  href: https://artifacts.apis.io/ip-sb/rate-limits/ip-sb-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ip-sb-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ip-sb/plans/ip-sb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ip-sb-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ip-sb/rules/ip-sb-rules.yml
  title: ''
  type: Spectral
  url: rules/ip-sb-rules.yml
- group: design
  href: https://artifacts.apis.io/ip-sb/json-ld/ip-sb-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ip-sb-context.jsonld
- group: design
  href: https://artifacts.apis.io/ip-sb/vocabulary/ip-sb-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ip-sb-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ip-sb/data-model/ip-sb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ip-sb-data-model.yml
- group: design
  href: https://artifacts.apis.io/ip-sb/errors/ip-sb-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ip-sb-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ip-sb/conformance/ip-sb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ip-sb-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ip-sb/llms/ip-sb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ip-sb-llms.txt
- group: other
  href: https://artifacts.apis.io/ip-sb/hosts/ip-sb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ip-sb-hosts.yml
- group: other
  href: https://artifacts.apis.io/ip-sb/vendors/ip-sb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ip-sb-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ip-sb/security/ip-sb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ip-sb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ip.sb/
- group: docs
  title: ''
  type: Documentation
  url: https://ip.sb/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://ip.sb/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ip.sb/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ip.sb/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://ip.sb/contact/
coverage:
  checked: '2026-10-28'
  detail: The public API documentation at https://ip.sb/api/ describes endpoints but provides no OpenAPI or other machine‑readable specification.
  evidence:
  - status: 200
    url: https://ip.sb/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: IP.SB provides a free REST API for IP address information, offering endpoints to retrieve the caller's IP address in plain text or JSON, perform GeoIP lookups, DNS queries, domain WHOIS, speed tests, and more. The service requires no authentication, no API key, and supports CORS and JSONP for browser usage. Documentation is available at https://ip.sb/api/, pricing information at https://ip.sb/pricing/, and terms of use and privacy policy at the respective pages.
image: https://ip.sb/favicon.ico
json_schemas:
- name: GetIpResponse
  property_count: 1
  slug: ip-sb-get-ip-response
jsonld:
- class_count: 1
  name: Ip Sb Context
  property_count: 0
  slug: ip-sb-context
layout: provider
modified: '2026-10-28'
name: IP.SB
nav: Providers
network: true
overview: 'IP.SB is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, IP, GeoIP, and DNS.


  The IP.SB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  IP.SB''s developer surface includes documentation, pricing, support, and 15 more developer resources.'
plans:
- name: Ip Sb Plans Pricing
  plan_count: 2
  slug: ip-sb-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Ip Sb Rate Limits
  slug: ip-sb-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: IP.SB API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: ip-sb-rules
scopes:
- name: Ip Sb Scopes
  scope_count: 0
  slug: ip-sb-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 69.2
    catalog_earned_first_party: 16.0
    catalog_gap: 45.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 21.1
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
    score: 28.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ip Sb Authentication
  slug: ip-sb-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ip Sb Domain Security
  slug: ip-sb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ip-sb
tags:
- Company
- API
- IP
- GeoIP
- DNS
website: https://ip.sb/
---
