---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.registrum.co.uk
  baseurl_source: declared
  description: Registrum API provides UK Companies House data, financials, director networks, and enriched company profiles.
  name: Registrum API
  slug: registrum-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/registrum-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/registrum-co-uk/security/registrum-co-uk-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/registrum-co-uk-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/registrum-co-uk/conformance/registrum-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/registrum-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/registrum-co-uk/llms/registrum-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/registrum-co-uk-llms.txt
- group: auth
  href: https://artifacts.apis.io/registrum-co-uk/well-known/registrum-co-uk-staging-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/registrum-co-uk-staging-security.txt
- group: auth
  href: https://artifacts.apis.io/registrum-co-uk/well-known/registrum-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/registrum-co-uk-security.txt
- group: auth
  href: https://artifacts.apis.io/registrum-co-uk/well-known/registrum-co-uk-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/registrum-co-uk-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/registrum-co-uk/well-known/registrum-co-uk-eccta-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/registrum-co-uk-eccta-security.txt
- group: auth
  href: https://artifacts.apis.io/registrum-co-uk/well-known/registrum-co-uk-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/registrum-co-uk-api-security.txt
- group: agent
  href: https://artifacts.apis.io/registrum-co-uk/well-known/registrum-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/registrum-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/registrum-co-uk/hosts/registrum-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/registrum-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/registrum-co-uk/vendors/registrum-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/registrum-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://registrum.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://registrum.co.uk/privacy
- group: auth
  href: https://artifacts.apis.io/registrum-co-uk/security/registrum-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/registrum-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/registrum-co-uk/security/registrum-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/registrum-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://registrum.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://api.registrum.co.uk/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.registrum.co.uk/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://registrum.co.uk/guides/how-to-get-a-companies-house-api-key
- group: operate
  title: ''
  type: Support
  url: https://registrum.co.uk/report
- group: company
  title: ''
  type: Blog
  url: https://registrum.co.uk/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://registrum.co.uk/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://registrum.co.uk/#get-key
created: '2026-10-31'
description: Registrum provides a UK Companies House data API delivering financials, turnover, accounts, PSC chains, and director networks as clean JSON. The service parses iXBRL filings, resolves ownership structures, and offers rate‑limit‑proof access without requiring a Companies House API key. Users can start for free with a keyless MCP endpoint, and paid plans add higher volume and SLA support.
image: https://registrum.co.uk/brand/icon-512.png
layout: provider
modified: '2026-10-31'
name: registrum-co-uk
nav: Providers
network: true
overview: 'registrum-co-uk is listed with 1 API on the [APIs.io](https://apis.io/) network: Registrum API. Tagged areas include Companies House, Financial Data, JSON API, UK, and Business Intelligence.


  registrum-co-uk''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 6
scopes:
- name: Registrum Co Uk Scopes
  scope_count: 0
  slug: registrum-co-uk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 16.4
    contract_quality: 30.5
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Registrum Co Uk Authentication
  slug: registrum-co-uk-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Registrum Co Uk Domain Security
  slug: registrum-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Registrum Co Uk Vulnerability Disclosure
  slug: registrum-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: registrum-co-uk
tags:
- Companies House
- Financial Data
- JSON API
- UK
- Business Intelligence
website: https://registrum.co.uk/
---
