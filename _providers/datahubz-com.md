---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DataHubz provides compliance infrastructure APIs across Attest, Hubz platform, Rubro, GuardGit, VeriCode and the CSE Registry.
  name: DataHubz API
  slug: datahubz-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://www.datahubz.com/security-policy
- group: agent
  href: https://artifacts.apis.io/datahubz-com/llms/datahubz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datahubz-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/datahubz-com/well-known/datahubz-com-verify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datahubz-com-verify-security.txt
- group: auth
  href: https://artifacts.apis.io/datahubz-com/well-known/datahubz-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datahubz-com-security.txt
- group: auth
  href: https://artifacts.apis.io/datahubz-com/well-known/datahubz-com-datahubz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datahubz-com-datahubz-security.txt
- group: auth
  href: https://artifacts.apis.io/datahubz-com/well-known/datahubz-com-attest-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datahubz-com-attest-security.txt
- group: agent
  href: https://artifacts.apis.io/datahubz-com/well-known/datahubz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datahubz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/datahubz-com/hosts/datahubz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datahubz-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/datahubz-com/vendors/datahubz-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datahubz-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datahubz.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datahubz.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.datahubz.com/blog
- group: auth
  href: https://artifacts.apis.io/datahubz-com/security/datahubz-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datahubz-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datahubz-com/security/datahubz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datahubz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datahubz.com/
coverage:
  checked: '2026-10-30'
  detail: API reference requires a sales request; the MCP endpoint https://attest.datahubz.com/mcp returns 401 without credentials.
  evidence:
  - status: 401
    url: https://attest.datahubz.com/mcp
  reason: sales-gate
  state: gated
created: '2026-10-30'
description: DataHubz builds compliance infrastructure so organizations can prove what they do, not just claim it. Their platform includes Attest, the Hubz platform, Rubro, GuardGit, VeriCode and the CSE Registry open standard, enabling automated compliance, audit readiness, and security governance across ISO 27001, SOC 2, GDPR and more.
image: https://datahubz.com/DataHubz-share.png?v=2
layout: provider
modified: '2026-10-30'
name: datahubz-com
nav: Providers
network: true
overview: 'datahubz-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, Security, Software-as-a-Service, Automation, and DataHubz.


  datahubz-com''s developer surface includes engineering blog and 14 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 64.3
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/datahubz-com/datahubz-com-2026-11-03T130159.png
security:
- kind: domain-security
  name: Datahubz Com Domain Security
  slug: datahubz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datahubz Com Vulnerability Disclosure
  slug: datahubz-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: datahubz-com
tags:
- Compliance
- Security
- Software-as-a-Service
- Automation
- DataHubz
website: https://datahubz.com/
---
