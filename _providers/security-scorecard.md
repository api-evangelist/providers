---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 98
  human_in_the_loop: 0
  name: Security Scorecard Agentic Access
  operation_count: 581
  slug: security-scorecard-agentic-access
  summary_line: 581 operations · 98 acting
api_count: 8
apis:
- description: REST API for security ratings, portfolios, scorecards, factor and issue data, historical scores, industry benchmarks, reporting, and webhook Rules.
  name: SecurityScorecard API
  slug: securityscorecard-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The Scorecard Multiscores API from SecurityScorecard — 4 operation(s) for scorecard multiscores.
  name: SecurityScorecard Scorecard Multiscores API
  slug: security-scorecard-multiscores-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The action plans API from SecurityScorecard — 12 operation(s) for action plans.
  name: SecurityScorecard action plans API
  slug: security-scorecard-action-plans-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The active findings API from SecurityScorecard — 193 operation(s) for active findings.
  name: SecurityScorecard active findings API
  slug: security-scorecard-active-findings-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: Active Infections
  name: SecurityScorecard Active Infections API
  slug: security-scorecard-active-infections-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The alerts API from SecurityScorecard — 1 operation(s) for alerts.
  name: SecurityScorecard Alerts API
  slug: security-scorecard-alerts-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: Operations about all followed companies
  name: SecurityScorecard All Companies API
  slug: security-scorecard-all-companies-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The Apps API from SecurityScorecard — 2 operation(s) for apps.
  name: SecurityScorecard Apps API
  slug: security-scorecard-apps-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: asset behind the IP address
  name: SecurityScorecard Asset API
  slug: security-scorecard-asset-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The compliance API from SecurityScorecard — 2 operation(s) for compliance.
  name: SecurityScorecard Compliance API
  slug: security-scorecard-compliance-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The custom scorecards API from SecurityScorecard — 4 operation(s) for custom scorecards.
  name: SecurityScorecard custom scorecards API
  slug: security-scorecard-custom-scorecards-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The customer API from SecurityScorecard — 10 operation(s) for customer.
  name: SecurityScorecard Customer API
  slug: security-scorecard-customer-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: Vulnerabilities
  name: SecurityScorecard Cve API
  slug: security-scorecard-cve-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The event log API from SecurityScorecard — 2 operation(s) for event log.
  name: SecurityScorecard event log API
  slug: security-scorecard-event-log-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The feedback API from SecurityScorecard — 2 operation(s) for feedback.
  name: SecurityScorecard Feedback API
  slug: security-scorecard-feedback-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The footprint API from SecurityScorecard — 1 operation(s) for footprint.
  name: SecurityScorecard Footprint API
  slug: security-scorecard-footprint-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The historical findings API from SecurityScorecard — 192 operation(s) for historical findings.
  name: SecurityScorecard historical findings API
  slug: security-scorecard-historical-findings-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The invites API from SecurityScorecard — 1 operation(s) for invites.
  name: SecurityScorecard Invites API
  slug: security-scorecard-invites-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The ip-domain-tags API from SecurityScorecard — 11 operation(s) for ip-domain-tags.
  name: SecurityScorecard Ip Domain Tags API
  slug: security-scorecard-ip-domain-tags-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The issues API from SecurityScorecard — 1 operation(s) for issues.
  name: SecurityScorecard Issues API
  slug: security-scorecard-issues-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The metadata API from SecurityScorecard — 3 operation(s) for metadata.
  name: SecurityScorecard Metadata API
  slug: security-scorecard-metadata-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The partner API from SecurityScorecard — 35 operation(s) for partner.
  name: SecurityScorecard Partner API
  slug: security-scorecard-partner-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The portfolios API from SecurityScorecard — 8 operation(s) for portfolios.
  name: SecurityScorecard Portfolios API
  slug: security-scorecard-portfolios-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: Ransomware
  name: SecurityScorecard Ransomware API
  slug: security-scorecard-ransomware-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The reports API from SecurityScorecard — 13 operation(s) for reports.
  name: SecurityScorecard Reports API
  slug: security-scorecard-reports-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The SAML API from SecurityScorecard — 1 operation(s) for saml.
  name: SecurityScorecard SAML API
  slug: security-scorecard-saml-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: Operations about scorecard notes
  name: SecurityScorecard Scorecard Notes API
  slug: security-scorecard-scorecard-notes-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: Operations about scorecard tags
  name: SecurityScorecard Scorecard Tags API
  slug: security-scorecard-scorecard-tags-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The scores API from SecurityScorecard — 13 operation(s) for scores.
  name: SecurityScorecard Scores API
  slug: security-scorecard-scores-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: Search endpoint
  name: SecurityScorecard Search API
  slug: security-scorecard-search-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: Threat-actors
  name: SecurityScorecard Threat Actors API
  slug: security-scorecard-threat-actors-api
- baseURL: https://api.securityscorecard.io
  baseurl_source: declared
  description: The vendor-detection API from SecurityScorecard — 5 operation(s) for vendor-detection.
  name: SecurityScorecard Vendor Detection API
  slug: security-scorecard-vendor-detection-api
artifact_total: 68
asyncapis:
- description: ''
  name: Security Scorecard Webhooks
  slug: security-scorecard-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/agentic-access/security-scorecard-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/security-scorecard-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/rules/security-scorecard-rules.yml
  title: ''
  type: Spectral
  url: rules/security-scorecard-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/json-ld/security-scorecard-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/security-scorecard-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/vocabulary/security-scorecard-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/security-scorecard-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/data-model/security-scorecard-data-model.yml
  title: ''
  type: DataModel
  url: data-model/security-scorecard-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/conformance/security-scorecard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/security-scorecard-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/hosts/security-scorecard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/security-scorecard-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/integrations/security-scorecard-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/security-scorecard-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/vendors/security-scorecard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/security-scorecard-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.securityscorecard.com/hc/en-us
- group: company
  title: ''
  type: Newsroom
  url: https://securityscorecard.com/company/press
- group: other
  title: ''
  type: Leadership
  url: https://securityscorecard.com/company/leadership
- group: company
  title: ''
  type: BlogRSS
  url: https://securityscorecard.com/feed/
- group: company
  title: ''
  type: Website
  url: https://securityscorecard.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://securityscorecard.readme.io
- group: docs
  title: ''
  type: Documentation
  url: https://securityscorecard.readme.io/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://securityscorecard.readme.io/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://securityscorecard.readme.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://securityscorecard.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://securityscorecard.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://securityscorecard.com/free-account-trial/
- group: start
  title: ''
  type: Login
  url: https://platform.securityscorecard.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://securityscorecard.com/eusa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://securityscorecard.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/securityscorecard
- group: operate
  title: ''
  type: StatusPage
  url: https://securityscorecard.statuspage.io/
- group: operate
  title: ''
  type: Deprecation
  url: https://securityscorecard.readme.io/reference/backwards-compatibility
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/llms/security-scorecard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/security-scorecard-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/authentication/security-scorecard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/security-scorecard-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/conventions/security-scorecard-conventions.yml
  title: ''
  type: Conventions
  url: conventions/security-scorecard-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/errors/security-scorecard-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/security-scorecard-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/lifecycle/security-scorecard-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/security-scorecard-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/asyncapi/security-scorecard-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/security-scorecard-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/well-known/security-scorecard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/security-scorecard-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/packages/security-scorecard-packages.yml
  title: ''
  type: Packages
  url: packages/security-scorecard-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/packages/security-scorecard-packages.yml
  title: ''
  type: SDKs
  url: packages/security-scorecard-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/cli/security-scorecard-cli.yml
  title: ''
  type: CLI
  url: cli/security-scorecard-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/mcp/security-scorecard-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/security-scorecard-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/security/security-scorecard-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/security-scorecard-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/security/security-scorecard-trust-center.yml
  title: ''
  type: Compliance
  url: security/security-scorecard-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/security/security-scorecard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/security-scorecard-domain-security.yml
created: '2026-07-17'
description: 'SecurityScorecard is a cybersecurity ratings and third-party risk management platform that continuously rates the security posture of any company from the outside in, producing an A-F security score across ten risk factors. Its REST API (base https://api.securityscorecard.io) lets customers manage portfolios of monitored companies, pull scorecards, factor scores, historical trends, issues/findings, industry benchmarks, and generate reports, and react to changes through webhook-driven Rules. Authentication is a static API token ("Authorization: Token <key>"), and first-party npm SDK and CLI packages are published under the @securityscorecard organization. Originally surfaced as a GV (Google Ventures) portfolio company, this profile has been enriched from SecurityScorecard''s public developer documentation.'
image: https://securityscorecard.com/wp-content/uploads/2023/01/ssc-logo.png
json_schemas:
- name: ActionPlanList
  property_count: 3
  slug: security-scorecard-action-plan-list
- name: ActionPlansList
  property_count: 4
  slug: security-scorecard-action-plans-list
- name: AddVendorDomainsResult
  property_count: 6
  slug: security-scorecard-add-vendor-domains-result
- name: AllCompaniesBulkUpdate
  property_count: 0
  slug: security-scorecard-all-companies-bulk-update
- name: AllCompaniesResponse
  property_count: 4
  slug: security-scorecard-all-companies-response
- name: asiSearchRequest
  property_count: 8
  slug: security-scorecard-asi-search-request
- name: asiSearchResponse
  property_count: 8
  slug: security-scorecard-asi-search-response
- name: BreachesList
  property_count: 4
  slug: security-scorecard-breaches-list
- name: CompanyByDomainResponse
  property_count: 18
  slug: security-scorecard-company-by-domain-response
- name: CompanySummary
  property_count: 17
  slug: security-scorecard-company-summary
- name: createCustomScorecardRequest
  property_count: 8
  slug: security-scorecard-create-custom-scorecard-request
- name: customScorecardSchema
  property_count: 20
  slug: security-scorecard-custom-scorecard-schema
- name: deleteCustomScorecardFilters
  property_count: 1
  slug: security-scorecard-delete-custom-scorecard-filters
- name: FindingsList
  property_count: 4
  slug: security-scorecard-findings-list
- name: getActionPlanByIdSchemaResponse
  property_count: 31
  slug: security-scorecard-get-action-plan-by-id-schema-response
- name: getAsiAssetIpResponse
  property_count: 9
  slug: security-scorecard-get-asi-asset-ip-response
- name: getAsiAssetPortResponse
  property_count: 11
  slug: security-scorecard-get-asi-asset-port-response
- name: getAsiThreatActorsResponse
  property_count: 8
  slug: security-scorecard-get-asi-threat-actors-response
- name: getCveResponse
  property_count: 8
  slug: security-scorecard-get-cve-response
- name: LikelihoodAssessmentV2GetResponse
  property_count: 0
  slug: security-scorecard-likelihood-assessment-v2-get-response
- name: MultiscorePaginatedResponse
  property_count: 4
  slug: security-scorecard-multiscore-paginated-response
- name: Note
  property_count: 6
  slug: security-scorecard-note
- name: PortfolioBatchRequest
  property_count: 8
  slug: security-scorecard-portfolio-batch-request
- name: PortfolioBatchResponse
  property_count: 6
  slug: security-scorecard-portfolio-batch-response
- name: ReportsSchema
  property_count: 3
  slug: security-scorecard-reports-schema
- name: ScorecardMultiscoresResponse
  property_count: 2
  slug: security-scorecard-scorecard-multiscores-response
- name: updateCompanyFieldsByDomain
  property_count: 9
  slug: security-scorecard-update-company-fields-by-domain
- name: updateCompanyFields
  property_count: 9
  slug: security-scorecard-update-company-fields
jsonld:
- class_count: 120
  name: Security Scorecard Context
  property_count: 225
  slug: security-scorecard-context
layout: provider
mcp_servers:
- description: A community-built MCP server that wraps the SecurityScorecard API. It is NOT affiliated with or published by SecurityScorecard, Inc. No first-party SecurityScorecard-hosted or -published MCP server wa
  name: SecurityScorecard MCP Server
  slug: securityscorecard-mcp
modified: '2026-10-06'
name: SecurityScorecard
nav: Providers
network: true
overview: 'SecurityScorecard publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Scorecard Multiscores API, action plans API, active findings API, and 29 more. Tagged areas include Company, Enterprise, Cybersecurity, Security Ratings, and Third-Party Risk Management.


  The SecurityScorecard catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SecurityScorecard''s developer surface includes support, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 34 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: SecurityScorecard API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: security-scorecard-rules
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.5
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 71.1
    developer_ergonomics: 52.4
    discoverability: 80.0
    operational_transparency: 30.3
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 31
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/security-scorecard/refs/heads/main/screenshots/security-scorecard-2026-08-17T081750.png
security:
- kind: authentication
  name: Security Scorecard Authentication
  slug: security-scorecard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Security Scorecard Domain Security
  slug: security-scorecard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Security Scorecard Trust Center
  slug: security-scorecard-trust-center
  summary_line: ISO 27001, PCI DSS, HIPAA, GDPR
slug: security-scorecard
tags:
- Company
- Enterprise
- Cybersecurity
- Security Ratings
- Third-Party Risk Management
- Risk Management
- Attack Surface
- Compliance
website: https://securityscorecard.com
---
