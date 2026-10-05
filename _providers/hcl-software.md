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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: The Stwebapi API from HCLSoftware — 1 operation(s) for stwebapi.
  name: HCLSoftware Stwebapi API
  slug: hcl-software-stwebapi-api
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hcl-software/refs/heads/main/rules/hcl-software-rules.yml
  title: ''
  type: Spectral
  url: rules/hcl-software-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hcl-software/refs/heads/main/conformance/hcl-software-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hcl-software-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hcl-software/refs/heads/main/llms/hcl-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hcl-software-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hcl-software/refs/heads/main/well-known/hcl-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hcl-software-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hcl-software/refs/heads/main/hosts/hcl-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hcl-software-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hcl-software/refs/heads/main/vendors/hcl-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hcl-software-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hcl-software.com/legal/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hcl-software.com/legal/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hcl-software.com/developer
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hcl-software/refs/heads/main/security/hcl-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hcl-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hcl-software.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.hcl-software.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.hcl-software.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.hcl-software.com/resources/trust-center
coverage:
  checked: '2026-10-03'
  detail: Developer portal pages are HTML without downloadable OpenAPI or other machine‑readable contracts.
  evidence:
  - status: 200
    url: https://www.hcl-software.com/developer
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: HCLSoftware, part of HCLTech, delivers a broad portfolio of enterprise software solutions spanning AI-driven operations, cybersecurity, data analytics, and low-code development platforms. The company focuses on orchestrating experiences, data, and operations at scale for large organizations, offering products such as HCL BigFix, HCL Cloud, and HCL Volt MX. Through its extensive suite, HCLSoftware enables digital transformation, secure endpoint management, and intelligent automation across industries.
image: https://www.hcl-software.com/wps/wcm/connect/8016b3f3-45f1-4b0b-b254-19206c7a4e12/hcl-software-logo-1200x630White.png?MOD=AJPERES&CACHEID=ROOTWORKSPACE-8016b3f3-45f1-4b0b-b254-19206c7a4e12-pTP27gt
layout: provider
modified: '2026-10-03'
name: HCLSoftware
nav: Providers
network: true
overview: 'HCLSoftware publishes 1 API on the [APIs.io](https://apis.io/) network: Stwebapi API. Tagged areas include Company, Software, Enterprise, Artificial Intelligence, and Cloud.


  The HCLSoftware catalog on APIs.io includes 1 Spectral governance ruleset.


  HCLSoftware''s developer surface includes documentation, engineering blog, support, and 11 more developer resources.'
random_paper: 21
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: HCLSoftware API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: hcl-software-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 9.4
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Hcl Software Domain Security
  slug: hcl-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hcl-software
tags:
- Company
- Software
- Enterprise
- Artificial Intelligence
- Cloud
website: https://www.hcl-software.com
---
