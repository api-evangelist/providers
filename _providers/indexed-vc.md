---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Indexed Vc Agentic Access
  operation_count: 19
  slug: indexed-vc-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
apis:
- baseURL: https://indexed.vc/api/v1
  baseurl_source: declared
  description: The Companies API from Indexed — 3 operation(s) for companies.
  name: Indexed Companies API
  slug: indexed-vc-companies-api
- baseURL: https://indexed.vc/api/v1
  baseurl_source: declared
  description: The Enrich API from Indexed — 1 operation(s) for enrich.
  name: Indexed Enrich API
  slug: indexed-vc-enrich-api
- baseURL: https://indexed.vc/api/v1
  baseurl_source: declared
  description: The Industries API from Indexed — 1 operation(s) for industries.
  name: Indexed Industries API
  slug: indexed-vc-industries-api
- baseURL: https://indexed.vc/api/v1
  baseurl_source: declared
  description: The Investors API from Indexed — 2 operation(s) for investors.
  name: Indexed Investors API
  slug: indexed-vc-investors-api
- baseURL: https://indexed.vc/api/v1
  baseurl_source: declared
  description: The Reveal API from Indexed — 1 operation(s) for reveal.
  name: Indexed Reveal API
  slug: indexed-vc-reveal-api
- baseURL: https://indexed.vc/api/v1
  baseurl_source: declared
  description: The Scheduled Exports API from Indexed — 2 operation(s) for scheduled exports.
  name: Indexed Scheduled Exports API
  slug: indexed-vc-scheduled-exports-api
- baseURL: https://indexed.vc/api/v1
  baseurl_source: declared
  description: The Usage API from Indexed — 1 operation(s) for usage.
  name: Indexed Usage API
  slug: indexed-vc-usage-api
- baseURL: https://indexed.vc/api/v1
  baseurl_source: declared
  description: The Webhooks API from Indexed — 4 operation(s) for webhooks.
  name: Indexed Webhooks API
  slug: indexed-vc-webhooks-api
artifact_total: 20
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/agentic-access/indexed-vc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/indexed-vc-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/plans/indexed-vc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/indexed-vc-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/rules/indexed-vc-rules.yml
  title: ''
  type: Spectral
  url: rules/indexed-vc-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/json-ld/indexed-vc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/indexed-vc-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/vocabulary/indexed-vc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/indexed-vc-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/data-model/indexed-vc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/indexed-vc-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/errors/indexed-vc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/indexed-vc-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/conformance/indexed-vc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/indexed-vc-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/llms/indexed-vc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/indexed-vc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/hosts/indexed-vc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/indexed-vc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/vendors/indexed-vc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/indexed-vc-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/authentication/indexed-vc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/indexed-vc-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/indexed-vc/refs/heads/main/security/indexed-vc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/indexed-vc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://indexed.vc
- group: docs
  title: ''
  type: Documentation
  url: https://indexed.vc/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://indexed.vc/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://indexed.vc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://indexed.vc/privacy
- group: operate
  title: ''
  type: Support
  url: https://indexed.vc/contact
created: '2026-10-02'
description: Indexed provides a private-company intelligence platform offering searchable data on companies, investors, and funding rounds. Users can look up companies by name or domain, explore detailed funding histories, investor relationships, and export data via a REST API. The service includes tiered pricing with free credits and paid plans for higher usage, API keys for authentication, and features such as bulk enrichment, webhooks, and scheduled exports.
image: https://indexed.vc/opengraph-image?2ed8c04617ed383e
json_schemas:
- name: CompanyCard
  property_count: 14
  slug: indexed-vc-company-card
- name: CompanyDomainLookupItem
  property_count: 0
  slug: indexed-vc-company-domain-lookup-item
- name: CompanyProfile
  property_count: 23
  slug: indexed-vc-company-profile
- name: InvestorProfile
  property_count: 19
  slug: indexed-vc-investor-profile
- name: SearchPageMeta
  property_count: 13
  slug: indexed-vc-search-page-meta
- name: UsageData
  property_count: 12
  slug: indexed-vc-usage-data
jsonld:
- class_count: 14
  name: Indexed Vc Context
  property_count: 93
  slug: indexed-vc-context
layout: provider
modified: '2026-10-02'
name: Indexed
nav: Providers
network: true
overview: 'Indexed publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Enrich API, Industries API, and 5 more. Tagged areas include Company, Data, Private Company, and Funding.


  The Indexed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Indexed''s developer surface includes authentication, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Indexed Vc Plans Pricing
  plan_count: 5
  slug: indexed-vc-plans-pricing
random_paper: 9
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Indexed API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 1
  slug: indexed-vc-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 67.1
    developer_ergonomics: 28.0
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Indexed Vc Authentication
  slug: indexed-vc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Indexed Vc Domain Security
  slug: indexed-vc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: indexed-vc
tags:
- Company
- Data
- Private Company
- Funding
website: https://indexed.vc
---
