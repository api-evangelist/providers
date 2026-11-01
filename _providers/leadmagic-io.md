---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 47
  human_in_the_loop: 8
  name: Leadmagic Io Agentic Access
  operation_count: 90
  slug: leadmagic-io-agentic-access
  summary_line: 90 operations · 47 acting · 8 human-in-the-loop
api_count: 2
apis:
- description: LeadMagic provides a B2B data enrichment API that transforms incomplete lead information into verified work emails, mobile numbers, company data, and buying signals. The platform offers email validati
  name: LeadMagic B2B Enrichment API
  slug: leadmagic-enrichment-api
- baseURL: https://api.leadmagic.io
  baseurl_source: declared
  description: Search advertising data across platforms
  name: leadmagic-io Ads Data API
  slug: leadmagic-io-ads-data-api
- baseURL: https://api.leadmagic.io
  baseurl_source: declared
  description: Monitor your API usage with comprehensive analytics endpoints (FREE - no credits consumed)
  name: leadmagic-io Analytics API
  slug: leadmagic-io-analytics-api
- baseURL: https://api.leadmagic.io
  baseurl_source: declared
  description: Campaign-oriented batch enrichment with budgets, clients, suppression lists, and webhooks
  name: leadmagic-io Batch API
  slug: leadmagic-io-batch-api
- baseURL: https://api.leadmagic.io
  baseurl_source: declared
  description: Submit and manage bulk enrichment jobs for processing CSV files at scale
  name: leadmagic-io Bulk Jobs API
  slug: leadmagic-io-bulk-jobs-api
- baseURL: https://api.leadmagic.io
  baseurl_source: declared
  description: Discover company information and intelligence
  name: leadmagic-io Company Data API
  slug: leadmagic-io-company-data-api
- baseURL: https://api.leadmagic.io
  baseurl_source: declared
  description: Preview costs, manage credit budgets, and maintain suppression lists to control spend
  name: leadmagic-io Cost Control API
  slug: leadmagic-io-cost-control-api
- baseURL: https://api.leadmagic.io
  baseurl_source: declared
  description: Manage and check your credit balance
  name: leadmagic-io Credits API
  slug: leadmagic-io-credits-api
- baseURL: https://api.leadmagic.io
  baseurl_source: declared
  description: Search job listings and detect career changes
  name: leadmagic-io Jobs Data API
  slug: leadmagic-io-jobs-data-api
- baseURL: https://api.leadmagic.io
  baseurl_source: declared
  description: Find and validate contact information for individuals
  name: leadmagic-io People Enrichment API
  slug: leadmagic-io-people-enrichment-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/leadmagic-io/agentic-access/leadmagic-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/leadmagic-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/leadmagic-io/rules/leadmagic-io-rules.yml
  title: ''
  type: Spectral
  url: rules/leadmagic-io-rules.yml
- group: design
  href: https://artifacts.apis.io/leadmagic-io/json-ld/leadmagic-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/leadmagic-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/leadmagic-io/vocabulary/leadmagic-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/leadmagic-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/leadmagic-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/leadmagic-io/data-model/leadmagic-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leadmagic-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://leadmagic.io/company/security
- group: auth
  href: https://artifacts.apis.io/leadmagic-io/authentication/leadmagic-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leadmagic-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/leadmagic-io/errors/leadmagic-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leadmagic-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/leadmagic-io/conformance/leadmagic-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leadmagic-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/leadmagic-io/llms/leadmagic-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leadmagic-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/leadmagic-io/well-known/leadmagic-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/leadmagic-io-security.txt
- group: auth
  href: https://artifacts.apis.io/leadmagic-io/well-known/leadmagic-io-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/leadmagic-io-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/leadmagic-io/well-known/leadmagic-io-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/leadmagic-io-app-security.txt
- group: agent
  href: https://artifacts.apis.io/leadmagic-io/well-known/leadmagic-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leadmagic-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/leadmagic-io/hosts/leadmagic-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/leadmagic-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/leadmagic-io/vendors/leadmagic-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/leadmagic-io-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://leadmagic.io/status
- group: auth
  title: ''
  type: Security
  url: https://leadmagic.io/company/security
- group: start
  title: ''
  type: Login
  url: https://leadmagic.io/sign-in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.leadmagic.io`\n\n
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LeadMagic
- group: auth
  href: https://artifacts.apis.io/leadmagic-io/security/leadmagic-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/leadmagic-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/leadmagic-io/security/leadmagic-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/leadmagic-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/leadmagic-io/security/leadmagic-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leadmagic-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leadmagic.io/
- group: docs
  title: ''
  type: Documentation
  url: https://leadmagic.io/docs/v1/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://leadmagic.io/docs/v1/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://leadmagic.io/docs/v1/introduction
- group: operate
  title: ''
  type: Support
  url: mailto:support@leadmagic.io
- group: company
  title: ''
  type: Blog
  url: https://leadmagic.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://leadmagic.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leadmagic.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leadmagic.io/legal/privacy
created: '2026-10-30'
description: LeadMagic provides a B2B data enrichment API that transforms incomplete lead information into verified work emails, mobile numbers, company data, and buying signals. The platform offers email validation, email finding, profile search, company intelligence, and other enrichment services to help sales teams improve outreach. It operates via a RESTful API hosted at https://api.leadmagic.io, with comprehensive documentation at https://leadmagic.io/docs/v1/introduction. The service emphasizes accuracy, real-time verification, and flexible pricing plans, and includes rate-limit guidelines and support contact.
image: https://leadmagic.io/logo/icon.svg
json_schemas:
- name: Budget
  property_count: 7
  slug: leadmagic-io-budget
- name: BulkSubmissionRequest
  property_count: 14
  slug: leadmagic-io-bulk-submission-request
- name: BulkSubmissionResponse
  property_count: 19
  slug: leadmagic-io-bulk-submission-response
- name: JobDetailResponse
  property_count: 0
  slug: leadmagic-io-job-detail-response
- name: PreviewCostRequest
  property_count: 5
  slug: leadmagic-io-preview-cost-request
- name: PreviewCostResponse
  property_count: 7
  slug: leadmagic-io-preview-cost-response
jsonld:
- class_count: 32
  name: Leadmagic Io Context
  property_count: 120
  slug: leadmagic-io-context
layout: provider
modified: '2026-10-30'
name: leadmagic-io
nav: Providers
network: true
overview: 'leadmagic-io publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ads Data API, Analytics API, Batch API, and 7 more. Tagged areas include B2B, Data Enrichment, Lead Generation, Email Verification, and Company Intelligence.


  The leadmagic-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  leadmagic-io''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Leadmagic Io Plans Pricing
  plan_count: 0
  slug: leadmagic-io-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Leadmagic Io Rate Limits
  slug: leadmagic-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: leadmagic-io API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 2
  slug: leadmagic-io-rules
scopes:
- name: Leadmagic Io Scopes
  scope_count: 0
  slug: leadmagic-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 66.7
    developer_ergonomics: 63.6
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Leadmagic Io Authentication
  slug: leadmagic-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Leadmagic Io Domain Security
  slug: leadmagic-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Leadmagic Io Vulnerability Disclosure
  slug: leadmagic-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Leadmagic Io Trust Center
  slug: leadmagic-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 3
skills:
- name: company-search
  slug: leadmagic-io-company-search
- name: email-finder
  slug: leadmagic-io-email-finder
- name: email-validation
  slug: leadmagic-io-email-validation
slug: leadmagic-io
tags:
- B2B
- Data Enrichment
- Lead Generation
- Email Verification
- Company Intelligence
website: https://leadmagic.io/
---
