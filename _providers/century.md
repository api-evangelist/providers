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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/century/refs/heads/main/well-known/century-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/century-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/century/refs/heads/main/hosts/century-hosts.yml
  title: ''
  type: Hosts
  url: hosts/century-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/century/refs/heads/main/vendors/century-vendors.yml
  title: ''
  type: Vendors
  url: vendors/century-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centuryaluminum.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centuryaluminum.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/century/refs/heads/main/security/century-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/century-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centuryaluminum.com
coverage:
  checked: '2026-10-07'
  detail: No public developer program or API documentation was found on the company's website.
  evidence:
  - status: 200
    url: https://centuryaluminum.com
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Century Aluminum produces and sells alumina and primary aluminum. It supplies these metals to the automotive, aerospace, defense, and consumer‑goods sectors. The company operates vertically integrated facilities, including a bauxite mine, alumina refinery, anode plant, and smelters in the United States, Jamaica, Iceland, and the Netherlands. Its products are positioned as critical metals for modern life and national security.
image: https://centuryaluminum.com/wp-content/uploads/2026/02/2026_Century-Aluminum_SebreeKY_Proof_180.webp
layout: provider
modified: '2026-10-07'
name: Century
nav: Providers
network: true
overview: Century is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aluminum, Manufacturing, Metals, and PublicCompany.
random_paper: 8
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
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
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Century Domain Security
  slug: century-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: century
tags:
- Company
- Aluminum
- Manufacturing
- Metals
- PublicCompany
website: https://centuryaluminum.com
---
