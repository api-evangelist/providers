---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pitchbook Agentic Access
  operation_count: 130
  slug: pitchbook-agentic-access
  summary_line: 130 operations
api_count: 1
apis:
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Account Information
  name: PitchBook Account Information API
  slug: pitchbook-account-information-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Companies
  name: PitchBook Companies API
  slug: pitchbook-companies-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Credit Analysis
  name: PitchBook Credit Analysis API
  slug: pitchbook-credit-analysis-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Deals
  name: PitchBook Deals API
  slug: pitchbook-deals-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Fundamentals
  name: PitchBook Fundamentals API
  slug: pitchbook-fundamentals-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Funds
  name: PitchBook Funds API
  slug: pitchbook-funds-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: General
  name: PitchBook General API
  slug: pitchbook-general-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Investors
  name: PitchBook Investors API
  slug: pitchbook-investors-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Limited Partners
  name: PitchBook Limited Partners API
  slug: pitchbook-limited-partners-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Patents
  name: PitchBook Patents API
  slug: pitchbook-patents-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: People
  name: PitchBook People API
  slug: pitchbook-people-api
- baseURL: https://api.pitchbook.com
  baseurl_source: declared
  description: Service Providers
  name: PitchBook Service Providers API
  slug: pitchbook-service-providers-api
artifact_total: 23
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/agentic-access/pitchbook-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pitchbook-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/rules/pitchbook-rules.yml
  title: ''
  type: Spectral
  url: rules/pitchbook-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/json-ld/pitchbook-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pitchbook-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/vocabulary/pitchbook-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pitchbook-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/data-model/pitchbook-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pitchbook-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/errors/pitchbook-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pitchbook-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/conformance/pitchbook-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pitchbook-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/overlays/pitchbook-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pitchbook-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/authentication/pitchbook-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pitchbook-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pitchbook/refs/heads/main/security/pitchbook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pitchbook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pitchbook.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pitchbook.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://pitchbook.com/free-trial
- group: operate
  title: ''
  type: Support
  url: https://pitchbook.com/contact
- group: company
  title: ''
  type: Blog
  url: https://pitchbook.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://pitchbook.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pitchbook.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pitchbook.com/privacy
created: '2026-09-21'
description: PitchBook provides comprehensive data and analysis on private market companies, investors, and deals. It offers a platform for market intelligence, deal sourcing, due diligence, and portfolio management, helping users explore use cases such as market intelligence, deal sourcing, fundraising, and benchmarking. The service includes products like PitchBook Data, Platform, and Luminary, and supports free trials and login for deeper insights.
image: https://pitchbook.com/favicon.ico
json_schemas:
- name: CompanyBioDto
  property_count: 23
  slug: pitchbook-company-bio-dto
- name: CompanySocialAnalyticsDto
  property_count: 20
  slug: pitchbook-company-social-analytics-dto
- name: DealDetailedDto
  property_count: 39
  slug: pitchbook-deal-detailed-dto
- name: FundBioDto
  property_count: 24
  slug: pitchbook-fund-bio-dto
- name: LimitedPartnerCommitmentAggregatesDto
  property_count: 20
  slug: pitchbook-limited-partner-commitment-aggregates-dto
- name: PatentDetailedDto
  property_count: 23
  slug: pitchbook-patent-detailed-dto
jsonld:
- class_count: 120
  name: Pitchbook Context
  property_count: 339
  slug: pitchbook-context
layout: provider
modified: '2026-09-21'
name: PitchBook
nav: Providers
network: true
overview: 'PitchBook publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account Information API, Companies API, Credit Analysis API, and 9 more. Tagged areas include Company, Data, Finance, Private-Market, and Analytics.


  The PitchBook catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PitchBook''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
random_paper: 17
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: PitchBook API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: pitchbook-rules
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 71.1
    developer_ergonomics: 42.3
    discoverability: 68.5
    operational_transparency: 0.0
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Pitchbook Authentication
  slug: pitchbook-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pitchbook Domain Security
  slug: pitchbook-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pitchbook
tags:
- Company
- Data
- Finance
- Private-Market
- Analytics
website: https://pitchbook.com/
---
