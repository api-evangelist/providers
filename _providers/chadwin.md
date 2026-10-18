---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Financial data API for US-listed companies, KPIs, reports, and more.
  name: Chadwin API
  slug: chadwin-api
- baseURL: https://api.chadwin.co
  baseurl_source: declared
  description: Search US-listed companies by name, ticker, or CIK, and retrieve company details.
  name: Chadwin Companies API
  slug: chadwin-companies-api
- baseURL: https://api.chadwin.co
  baseurl_source: declared
  description: Issuer-specific operating KPIs with annual, half-year and quarterly values from original SEC filing documents. Free subscriber beta.
  name: Chadwin Company KPIs API
  slug: chadwin-company-kpis-api
- baseURL: https://api.chadwin.co
  baseurl_source: declared
  description: Retrieve annual and quarterly company reports as cleaned HTML, and follow updates for Forms 10-K, 10-Q, 20-F, and 40-F and their amendments.
  name: Chadwin Company reports API
  slug: chadwin-company-reports-api
- baseURL: https://api.chadwin.co
  baseurl_source: declared
  description: Retrieve 8-K and 6-K reports with readable exhibits in one HTML response, and follow new reports and amendments through the update feed.
  name: Chadwin Current reports API
  slug: chadwin-current-reports-api
- baseURL: https://api.chadwin.co
  baseurl_source: declared
  description: Find transactions on Forms 4 and 5, retrieve Form 3, 4, and 5 filings, and find proposed sales on Form 144. Use the insider activity feed for new Forms 3, 4, 5, and 144, or the insider transaction fee
  name: Chadwin Insider activity API
  slug: chadwin-insider-activity-api
- baseURL: https://api.chadwin.co
  baseurl_source: declared
  description: Find institutional managers and reporting periods, retrieve Form 13F filings and holdings, and view a manager's holdings and consolidated positions. Follow new Forms 13F-HR and 13F-NT and their amendm
  name: Chadwin Institutional holdings API
  slug: chadwin-institutional-holdings-api
- baseURL: https://api.chadwin.co
  baseurl_source: declared
  description: Annual financial statements and financial metrics.
  name: Chadwin Normalized financial statements API
  slug: chadwin-normalized-financial-statements-api
artifact_total: 19
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/rules/chadwin-rules.yml
  title: ''
  type: Spectral
  url: rules/chadwin-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/json-ld/chadwin-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chadwin-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/vocabulary/chadwin-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chadwin-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/conformance/chadwin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chadwin-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/plans/chadwin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chadwin-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/data-model/chadwin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chadwin-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/security/chadwin-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/chadwin-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/errors/chadwin-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chadwin-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/llms/chadwin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chadwin-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/well-known/chadwin-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chadwin-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/well-known/chadwin-chadwin-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chadwin-chadwin-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/well-known/chadwin-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chadwin-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/well-known/chadwin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chadwin-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/hosts/chadwin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chadwin-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/vendors/chadwin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chadwin-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chadwinco
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.chadwin.co</span
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/security/chadwin-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chadwin-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chadwin/refs/heads/main/security/chadwin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chadwin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chadwin.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.chadwin.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.chadwin.co/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chadwin.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.chadwin.co/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.chadwin.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chadwin.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chadwin.co/privacy
created: '2026-10-16'
description: Chadwin is a technology company specializing in advanced data analytics and integration solutions for enterprises. Founded in 2020, Chadwin provides a suite of APIs that enable seamless data ingestion, transformation, and real-time analytics across multiple platforms. Their platform supports robust security features, scalable architecture, and comprehensive documentation to help developers integrate their services quickly and efficiently. The company focuses on delivering high-performance, reliable APIs that empower businesses to unlock insights from their data and drive informed decision-making.
image: https://www.chadwin.co/open-graph.png
json_schemas:
- name: CompanyReportPage
  property_count: 3
  slug: chadwin-company-report-page
- name: CompanyReportResponse
  property_count: 9
  slug: chadwin-company-report-response
- name: InsiderFilingDocument
  property_count: 17
  slug: chadwin-insider-filing-document
- name: InstitutionalFilingDetailResponse
  property_count: 13
  slug: chadwin-institutional-filing-detail-response
- name: ProposedSaleFilingDetail
  property_count: 13
  slug: chadwin-proposed-sale-filing-detail
- name: ProposedSalesResponse
  property_count: 3
  slug: chadwin-proposed-sales-response
jsonld:
- class_count: 91
  name: Chadwin Context
  property_count: 299
  slug: chadwin-context
layout: provider
modified: '2026-10-16'
name: Chadwin
nav: Providers
network: true
overview: 'Chadwin publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Company KPIs API, Company reports API, and 5 more. Tagged areas include Company, Data Analytics, Integration, and Enterprise.


  The Chadwin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chadwin''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, and 23 more developer resources.'
plans:
- name: Chadwin Plans Pricing
  plan_count: 2
  slug: chadwin-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Chadwin API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: chadwin-rules
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 66.6
    developer_ergonomics: 35.0
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Chadwin Domain Security
  slug: chadwin-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Chadwin Vulnerability Disclosure
  slug: chadwin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chadwin
tags:
- Company
- Data Analytics
- Integration
- Enterprise
website: https://chadwin.co/
---
