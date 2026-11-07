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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/easyonward-com/llms/easyonward-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easyonward-com-llms.txt
- group: other
  href: https://artifacts.apis.io/easyonward-com/hosts/easyonward-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easyonward-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/easyonward-com/vendors/easyonward-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easyonward-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easyonward.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easyonward.com/legal/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://easyonward.com/guides/freedom-of-movement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EasyOnward
- group: auth
  href: https://artifacts.apis.io/easyonward-com/security/easyonward-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easyonward-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easyonward.com/
coverage:
  checked: '2026-11-06'
  detail: Provider documentation is markdown without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://easyonward.com/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Travel risk intelligence – passport, visa, transit, and baggage analysis for every itinerary. EasyOnward provides comprehensive travel risk assessments, helping travelers and businesses understand visa requirements, transit restrictions, and baggage allowances across global destinations. The platform offers real-time updates and detailed insights to ensure safe and compliant journeys.
image: https://easyonward.com/opengraph-image?ca2c145e8c4b203e
layout: provider
modified: '2026-11-06'
name: EasyOnward
nav: Providers
network: true
overview: 'EasyOnward is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Risk Management, Intelligence, Visa, and Baggage.


  EasyOnward''s developer surface includes documentation and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Easyonward Com Domain Security
  slug: easyonward-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easyonward-com
tags:
- Travel
- Risk Management
- Intelligence
- Visa
- Baggage
website: https://easyonward.com/
---
