---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Forsakringskassan Agentic Access
  operation_count: 2
  slug: forsakringskassan-agentic-access
  summary_line: 2 operations · 1 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The RtfKompletteringController API from Försäkringskassan — 1 operation(s) for rtfkompletteringcontroller.
  name: Försäkringskassan Rtf Komplettering Controller API
  slug: forsakringskassan-rtfkompletteringcontroller-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/agentic-access/forsakringskassan-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/forsakringskassan-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/rules/forsakringskassan-rules.yml
  title: ''
  type: Spectral
  url: rules/forsakringskassan-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/json-ld/forsakringskassan-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/forsakringskassan-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/vocabulary/forsakringskassan-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/forsakringskassan-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/data-model/forsakringskassan-data-model.yml
  title: ''
  type: DataModel
  url: data-model/forsakringskassan-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/errors/forsakringskassan-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/forsakringskassan-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/conformance/forsakringskassan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/forsakringskassan-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/overlays/forsakringskassan-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/forsakringskassan-openapi-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/hosts/forsakringskassan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/forsakringskassan-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/packages/forsakringskassan-packages.yml
  title: ''
  type: SDKs
  url: packages/forsakringskassan-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/packages/forsakringskassan-packages.yml
  title: ''
  type: Packages
  url: packages/forsakringskassan-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.forsakringskassan.se/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Forsakringskassan
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/forsakringskassan/refs/heads/main/security/forsakringskassan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forsakringskassan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forsakringskassan.se/
created: '2026-10-15'
description: Försäkringskassan is Sweden’s national social insurance agency responsible for administering health insurance, parental benefits, pensions, and other welfare services. It provides digital services and APIs for citizens and businesses to access information, submit applications, and retrieve status updates. The agency focuses on secure, reliable, and user-friendly digital interactions, supporting a wide range of social security processes across the country.
image: https://www.forsakringskassan.se/images/18.a5da6b31762d40d899891e/1613485730443/fk-dela-sociala-medier-1200x630.png
json_schemas:
- name: RtfKompletteringData
  property_count: 2
  slug: forsakringskassan-rtf-komplettering-data
jsonld:
- class_count: 1
  name: Forsakringskassan Context
  property_count: 2
  slug: forsakringskassan-context
layout: provider
modified: '2026-10-15'
name: Försäkringskassan
nav: Providers
network: true
overview: 'Försäkringskassan publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Rtf Komplettering Controller API. Tagged areas include Government, SocialSecurity, Sweden, and PublicSector.


  The Försäkringskassan catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Försäkringskassan API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: forsakringskassan-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 43.2
    catalog_earned_first_party: 0.0
    catalog_gap: 71.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 46.9
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Forsakringskassan Domain Security
  slug: forsakringskassan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: forsakringskassan
tags:
- Government
- SocialSecurity
- Sweden
- PublicSector
website: https://forsakringskassan.se/
---
