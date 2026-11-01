---
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fileread.com/
- group: agent
  href: https://artifacts.apis.io/fileread/llms/fileread-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fileread-llms.txt
- group: auth
  href: https://artifacts.apis.io/fileread/well-known/fileread-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fileread-www-security.txt
- group: auth
  href: https://artifacts.apis.io/fileread/well-known/fileread-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fileread-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/fileread/well-known/fileread-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fileread-well-known.yml
- group: other
  href: https://artifacts.apis.io/fileread/hosts/fileread-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fileread-hosts.yml
- group: other
  href: https://artifacts.apis.io/fileread/vendors/fileread-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fileread-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.fileread.com/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://fileread.com/security
- group: auth
  href: https://artifacts.apis.io/fileread/security/fileread-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fileread-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fileread/security/fileread-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fileread-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fileread.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fileread.com/
- group: company
  title: ''
  type: Blog
  url: https://fileread.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://fileread.com/product
- group: company
  title: ''
  type: Careers
  url: https://fileread.com/careers
coverage:
  checked: '2026-10-29'
  detail: Fileread does not provide a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://docs.fileread.com/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Fileread provides an AI‑powered legal data intelligence platform that automates fact‑finding for litigation and investigations. By ingesting the full record of case materials, Fileread reads, analyzes, and cites every answer to its source, enabling lawyers to quickly locate relevant evidence, generate insights, and streamline discovery workflows. Backed by Gradient Ventures, the service combines natural language processing with a searchable knowledge base to improve accuracy and efficiency for legal teams.
image: https://framerusercontent.com/assets/jHfJLsAkMVWEWfdxd5KBs03QfM.png
layout: provider
modified: '2026-10-29'
name: Fileread
nav: Providers
network: true
overview: 'Fileread is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, LegalTech, Litigation, DataIntelligence, and Automation.


  Fileread''s developer surface includes documentation, engineering blog, getting-started guide, and 13 more developer resources.'
random_paper: 12
scopes:
- name: Fileread Scopes
  scope_count: 0
  slug: fileread-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fileread Authentication
  slug: fileread-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fileread Domain Security
  slug: fileread-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fileread Trust Center
  slug: fileread-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: fileread
tags:
- AI
- LegalTech
- Litigation
- DataIntelligence
- Automation
website: https://fileread.com/
---
