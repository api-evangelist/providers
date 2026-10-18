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
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Provides RESTful access to articles and grants.
  name: Europe PMC API
  slug: europe-pmc-api-2
- baseURL: https://dev.europepmc.org
  baseurl_source: declared
  description: The Europepmc API from Europe PMC — 2 operation(s) for europepmc.
  name: Europe PMC Europepmc API
  slug: europe-pmc-europepmc-api
artifact_total: 4
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/europe-pmc/refs/heads/main/rules/europe-pmc-rules.yml
  title: ''
  type: Spectral
  url: rules/europe-pmc-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/europe-pmc/refs/heads/main/conformance/europe-pmc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/europe-pmc-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/europe-pmc/refs/heads/main/well-known/europe-pmc-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/europe-pmc-www-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/europe-pmc/refs/heads/main/well-known/europe-pmc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/europe-pmc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/europe-pmc/refs/heads/main/hosts/europe-pmc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/europe-pmc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/europe-pmc/refs/heads/main/vendors/europe-pmc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/europe-pmc-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/europe-pmc/refs/heads/main/packages/europe-pmc-packages.yml
  title: ''
  type: SDKs
  url: packages/europe-pmc-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/europe-pmc/refs/heads/main/packages/europe-pmc-packages.yml
  title: ''
  type: Packages
  url: packages/europe-pmc-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.europepmc.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EuropePMC
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/europe-pmc/refs/heads/main/security/europe-pmc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/europe-pmc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://europepmc.org
created: '2026-10-13'
description: 'Europe PMC is a company surfaced via the API Evangelist harvest backlog (source: tag-qc) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-13'
name: Europe PMC
nav: Providers
network: true
overview: 'Europe PMC is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Europepmc API, and 1 more. Tagged areas include Company.


  The Europe PMC catalog on APIs.io includes 1 Spectral governance ruleset.


  Europe PMC''s developer surface includes documentation and 11 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Europe PMC API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: europe-pmc-rules
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 29.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 11.7
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 5.3
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
  name: Europe Pmc Domain Security
  slug: europe-pmc-domain-security
  summary_line: TLSv1.3
slug: europe-pmc
tags:
- Company
website: https://europepmc.org
---
