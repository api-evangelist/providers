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
  scored_at: '2026-10-04'
api_count: 2
apis:
- description: API security solution protecting APIs throughout the software development lifecycle.
  name: API Secure
  slug: api-secure
- description: The Llm Query API from Data Theorem — 1 operation(s) for llm query.
  name: Data Theorem Llm Query API
  slug: datatheorem-llm-query-api
artifact_total: 4
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datatheorem/refs/heads/main/rules/datatheorem-rules.yml
  title: ''
  type: Spectral
  url: rules/datatheorem-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datatheorem/refs/heads/main/conformance/datatheorem-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datatheorem-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datatheorem/refs/heads/main/llms/datatheorem-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datatheorem-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datatheorem/refs/heads/main/hosts/datatheorem-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datatheorem-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datatheorem/refs/heads/main/vendors/datatheorem-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datatheorem-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datatheorem.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.datatheorem.com/news/awards
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datatheorem/refs/heads/main/security/datatheorem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datatheorem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datatheorem.com
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the API host or docs pages.
  evidence:
  - status: 404
    url: https://api.datatheorem.com/openapi.json
  - status: 404
    url: https://www.datatheorem.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Data Theorem provides application security solutions that protect APIs, cloud-native applications, and mobile apps throughout the software development lifecycle. Their platform offers API security, code security, cloud security, and mobile security, leveraging AI to detect and remediate vulnerabilities, enforce compliance, and secure runtime environments.
layout: provider
modified: '2026-10-03'
name: Data Theorem
nav: Providers
network: true
overview: 'Data Theorem publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Llm Query API, and 1 more. Tagged areas include Company, Application Security, API Security, Cloud Security, and Mobile Security.


  The Data Theorem catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 0
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Data Theorem API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: datatheorem-rules
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 65.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.6
    contract_governance: 31.8
    contract_quality: 9.4
    developer_ergonomics: 0.0
    discoverability: 62.5
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
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Datatheorem Domain Security
  slug: datatheorem-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: datatheorem
tags:
- Company
- Application Security
- API Security
- Cloud Security
- Mobile Security
website: https://www.datatheorem.com
---
