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
api_count: 3
apis:
- description: Machine-readable API providing tools list and healthcare job data via JSON-RPC.
  name: CareJobs.Now MCP API
  slug: carejobs-now-mcp-api
- baseURL: https://api.carejobs.now
  baseurl_source: declared
  description: The Pay API from CareJobs.Now — 1 operation(s) for pay.
  name: CareJobs.Now Pay API
  slug: carejobs-now-pay-api
- baseURL: https://api.carejobs.now
  baseurl_source: declared
  description: The Roles API from CareJobs.Now — 1 operation(s) for roles.
  name: CareJobs.Now Roles API
  slug: carejobs-now-roles-api
artifact_total: 5
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carejobs-now/refs/heads/main/rules/carejobs-now-rules.yml
  title: ''
  type: Spectral
  url: rules/carejobs-now-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carejobs-now/refs/heads/main/conformance/carejobs-now-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carejobs-now-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carejobs-now/refs/heads/main/llms/carejobs-now-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carejobs-now-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carejobs-now/refs/heads/main/hosts/carejobs-now-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carejobs-now-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carejobs-now/refs/heads/main/vendors/carejobs-now-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carejobs-now-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://carejobs.now/occupations/registered-nurse
- group: start
  title: ''
  type: GettingStarted
  url: https://carejobs.now/learn/how-hospital-hiring-works
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carejobs-now/refs/heads/main/security/carejobs-now-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carejobs-now-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carejobs.now
- group: docs
  title: ''
  type: Documentation
  url: https://carejobs.now/data
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carejobs.now/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carejobs.now/legal/privacy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://carejobs.now/api/mcp
  - status: 200
    url: https://carejobs.now
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: CareJobs.Now aggregates US healthcare job listings and posted pay rates from over 258 employers, providing open datasets of hourly wages, job types, and employer information. Users can browse jobs, explore pay research, and download JSON/CSV files without authentication. The platform aims to increase transparency in healthcare compensation and simplify job search for nurses, CNAs, therapists, and other care professionals.
image: https://carejobs.now/opengraph-image
layout: provider
modified: '2026-10-15'
name: CareJobs.Now
nav: Providers
network: true
overview: 'CareJobs.Now is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Pay API, Roles API, and 1 more. Tagged areas include Healthcare, Job, Data, Transparency, and US.


  The CareJobs.Now catalog on APIs.io includes 1 Spectral governance ruleset.


  CareJobs.Now''s developer surface includes signup flow, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: CareJobs.Now API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: carejobs-now-rules
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 21.4
    discoverability: 78.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Carejobs Now Domain Security
  slug: carejobs-now-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carejobs-now
tags:
- Healthcare
- Job
- Data
- Transparency
- US
website: https://carejobs.now
---
