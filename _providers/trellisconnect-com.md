---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
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
  score: 8.5
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/trellisconnect-com/authentication/trellisconnect-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trellisconnect-com-authentication.yml
- group: other
  href: https://artifacts.apis.io/trellisconnect-com/hosts/trellisconnect-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trellisconnect-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/trellisconnect-com/vendors/trellisconnect-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trellisconnect-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://savvy.insure/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://savvy.insure/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trellisconnect.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trellisconnect
- group: auth
  href: https://artifacts.apis.io/trellisconnect-com/security/trellisconnect-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trellisconnect-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://savvy.insure
coverage:
  checked: '2026-10-29'
  detail: Docs page returns HTML instead of a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.trellisconnect.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Trellis, operating under the Savvy brand, offers an AI‑driven insurance marketplace that helps consumers compare and purchase car insurance. By anonymously gathering rate estimates and presenting personalized quotes, Savvy aims to simplify the insurance buying process while protecting user data. The platform partners with over 80 insurers across the United States, providing a streamlined, commission‑free experience for shoppers seeking better rates.
image: https://savvy.insure/img/og-card.png
json_schemas:
- name: GetAccountAccountidPoliciesResponse
  property_count: 3
  slug: trellisconnect-com-get-account-accountid-policies-response
- name: GetAccountAccountidResponse
  property_count: 5
  slug: trellisconnect-com-get-account-accountid-response
- name: GetTrellisConnect110AccountAccountidPoliciesResponse
  property_count: 3
  slug: trellisconnect-com-get-trellis-connect110-account-accountid-policies-response
- name: GetTrellisConnect110AccountAccountidResponse
  property_count: 3
  slug: trellisconnect-com-get-trellis-connect110-account-accountid-response
jsonld:
- class_count: 4
  name: Trellisconnect Com Context
  property_count: 11
  slug: trellisconnect-com-context
layout: provider
modified: '2026-10-29'
name: Trellis
nav: Providers
network: true
overview: 'Trellis publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Car Insurance, Licensed Agency, and AI Assistants.


  The Trellis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Trellis'' developer surface includes authentication, documentation, and 7 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Trellis API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: trellisconnect-com-rules
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 12.3
    developer_ergonomics: 21.4
    discoverability: 39.3
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Trellisconnect Com Authentication
  slug: trellisconnect-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Trellisconnect Com Domain Security
  slug: trellisconnect-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trellisconnect-com
tags:
- Insurance
- Car Insurance
- Licensed Agency
- AI Assistants
website: https://savvy.insure
---
