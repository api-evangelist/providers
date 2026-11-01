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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/next-insurance-com/llms/next-insurance-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/next-insurance-com-llms.txt
- group: other
  href: https://artifacts.apis.io/next-insurance-com/hosts/next-insurance-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/next-insurance-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/next-insurance-com/vendors/next-insurance-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/next-insurance-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.next-insurance.com/
- group: auth
  href: https://artifacts.apis.io/next-insurance-com/security/next-insurance-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/next-insurance-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.next-insurance.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nextinsurance.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.nextinsurance.com/help-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nextinsurance.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextinsurance.com/privacy-policy/
coverage:
  checked: '2026-10-29'
  detail: MCP endpoint https://help.next-insurance.com/mcp returns 401 Unauthorized, indicating the API is behind authentication.
  evidence:
  - status: 401
    url: https://help.next-insurance.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Next Insurance (ERGO NEXT Insurance) provides small business insurance solutions with fast quotes, instant coverage, and competitive rates tailored for over 1,300 professions. Founded in 2016 and part of ERGO Group AG under Munich Re, the company offers a digital platform for businesses to obtain insurance quickly and efficiently.
image: https://www.nextinsurance.com/wp-content/uploads/2026/01/OpenGraph_1200x630.jpg
layout: provider
modified: '2026-10-28'
name: Next Insurance
nav: Providers
network: true
overview: 'Next Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Small Business, FinTech, and US.


  Next Insurance''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 0
scopes:
- name: Next Insurance Com Scopes
  scope_count: 0
  slug: next-insurance-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 27.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Next Insurance Com Authentication
  slug: next-insurance-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Next Insurance Com Domain Security
  slug: next-insurance-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: next-insurance-com
tags:
- Company
- Insurance
- Small Business
- FinTech
- US
website: https://www.next-insurance.com/
---
