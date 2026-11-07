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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Whoisgeni Us Agentic Access
  operation_count: 52
  slug: whoisgeni-us-agentic-access
  summary_line: 52 operations · 22 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The account API from whoisgeni-us — 2 operation(s) for account.
  name: whoisgeni-us Account API
  slug: whoisgeni-us-account-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The analysis API from whoisgeni-us — 3 operation(s) for analysis.
  name: whoisgeni-us Analysis API
  slug: whoisgeni-us-analysis-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The authentication API from whoisgeni-us — 6 operation(s) for authentication.
  name: whoisgeni-us Authentication API
  slug: whoisgeni-us-authentication-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The billing API from whoisgeni-us — 9 operation(s) for billing.
  name: whoisgeni-us Billing API
  slug: whoisgeni-us-billing-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The byok API from whoisgeni-us — 2 operation(s) for byok.
  name: whoisgeni-us Byok API
  slug: whoisgeni-us-byok-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The correlation API from whoisgeni-us — 2 operation(s) for correlation.
  name: whoisgeni-us Correlation API
  slug: whoisgeni-us-correlation-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The domains API from whoisgeni-us — 2 operation(s) for domains.
  name: whoisgeni-us Domains API
  slug: whoisgeni-us-domains-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The entities API from whoisgeni-us — 2 operation(s) for entities.
  name: whoisgeni-us Entities API
  slug: whoisgeni-us-entities-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The health API from whoisgeni-us — 4 operation(s) for health.
  name: whoisgeni-us Health API
  slug: whoisgeni-us-health-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The jobs API from whoisgeni-us — 5 operation(s) for jobs.
  name: whoisgeni-us Jobs API
  slug: whoisgeni-us-jobs-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The mcp API from whoisgeni-us — 1 operation(s) for mcp.
  name: whoisgeni-us MCP API
  slug: whoisgeni-us-mcp-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The schema-templates API from whoisgeni-us — 2 operation(s) for schema-templates.
  name: whoisgeni-us Schema Templates API
  slug: whoisgeni-us-schema-templates-api
- baseURL: https://api.whoisgeni.us
  baseurl_source: declared
  description: The webhooks API from whoisgeni-us — 4 operation(s) for webhooks.
  name: whoisgeni-us Webhooks API
  slug: whoisgeni-us-webhooks-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/whoisgeni-us/agentic-access/whoisgeni-us-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/whoisgeni-us-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/whoisgeni-us/rules/whoisgeni-us-rules.yml
  title: ''
  type: Spectral
  url: rules/whoisgeni-us-rules.yml
- group: design
  href: https://artifacts.apis.io/whoisgeni-us/json-ld/whoisgeni-us-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/whoisgeni-us-context.jsonld
- group: design
  href: https://artifacts.apis.io/whoisgeni-us/vocabulary/whoisgeni-us-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/whoisgeni-us-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/whoisgeni-us/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/whoisgeni-us/data-model/whoisgeni-us-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whoisgeni-us-data-model.yml
- group: design
  href: https://artifacts.apis.io/whoisgeni-us/conventions/whoisgeni-us-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/whoisgeni-us-conventions.yml
- group: design
  href: https://artifacts.apis.io/whoisgeni-us/conventions/whoisgeni-us-conventions.yml
  title: ''
  type: Conventions
  url: conventions/whoisgeni-us-conventions.yml
- group: auth
  href: https://artifacts.apis.io/whoisgeni-us/security/whoisgeni-us-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/whoisgeni-us-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/whoisgeni-us/authentication/whoisgeni-us-authentication.yml
  title: ''
  type: Authentication
  url: authentication/whoisgeni-us-authentication.yml
- group: design
  href: https://artifacts.apis.io/whoisgeni-us/errors/whoisgeni-us-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whoisgeni-us-problem-types.yml
- group: design
  href: https://artifacts.apis.io/whoisgeni-us/conformance/whoisgeni-us-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whoisgeni-us-conformance.yml
- group: agent
  href: https://artifacts.apis.io/whoisgeni-us/llms/whoisgeni-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whoisgeni-us-llms.txt
- group: auth
  href: https://artifacts.apis.io/whoisgeni-us/well-known/whoisgeni-us-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/whoisgeni-us-security.txt
- group: agent
  href: https://artifacts.apis.io/whoisgeni-us/well-known/whoisgeni-us-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whoisgeni-us-well-known.yml
- group: other
  href: https://artifacts.apis.io/whoisgeni-us/hosts/whoisgeni-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whoisgeni-us-hosts.yml
- group: other
  href: https://artifacts.apis.io/whoisgeni-us/vendors/whoisgeni-us-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whoisgeni-us-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://whoisgeni.us/login/?redirect=%2Fpricing%2F
- group: operate
  title: ''
  type: ChangeLog
  url: https://whoisgeni.us/changelog/
- group: docs
  title: ''
  type: APIReference
  url: https://whoisgeni.us/llms.txt
- group: auth
  href: https://artifacts.apis.io/whoisgeni-us/security/whoisgeni-us-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/whoisgeni-us-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/whoisgeni-us/security/whoisgeni-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whoisgeni-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whoisgeni.us/
- group: docs
  title: ''
  type: Documentation
  url: https://whoisgeni.us/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://whoisgeni.us/get-started/
- group: company
  title: ''
  type: Blog
  url: https://whoisgeni.us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://whoisgeni.us/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whoisgeni.us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whoisgeni.us/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://whoisgeni.us/status/
created: '2026-10-31'
description: WhoisGenius provides a Domain Intelligence API that attributes domain ownership, bypasses GDPR redactions, and reveals hidden operators behind CDNs. It aggregates over 20 signals, delivering confidence scores with full evidence chains for security, compliance, and research use cases. The service offers real-time analysis, historical data, and portfolio discovery across hundreds of millions of domains, supporting teams in phishing attribution, trademark enforcement, and vendor screening.
image: https://whoisgeni.us/og-image.png
json_schemas:
- name: AutoRechargeUpdateRequest
  property_count: 4
  slug: whoisgeni-us-auto-recharge-update-request
- name: BatchSubmitRequest
  property_count: 6
  slug: whoisgeni-us-batch-submit-request
- name: BulkSubmitRequest
  property_count: 2
  slug: whoisgeni-us-bulk-submit-request
- name: CorrelateRequest
  property_count: 2
  slug: whoisgeni-us-correlate-request
- name: SubmitRequest
  property_count: 7
  slug: whoisgeni-us-submit-request
- name: UpdateTemplateRequest
  property_count: 4
  slug: whoisgeni-us-update-template-request
jsonld:
- class_count: 105
  name: Whoisgeni Us Context
  property_count: 190
  slug: whoisgeni-us-context
layout: provider
modified: '2026-10-31'
name: whoisgeni-us
nav: Providers
network: true
overview: 'whoisgeni-us publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Analysis API, Authentication API, and 10 more. Tagged areas include Company, Domain Intelligence, Security, Compliance, and Data Enrichment.


  The whoisgeni-us catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  whoisgeni-us'' developer surface includes authentication, changelog, API reference, documentation, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: whoisgeni-us API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: whoisgeni-us-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 60.2
    developer_ergonomics: 29.2
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Whoisgeni Us Authentication
  slug: whoisgeni-us-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Whoisgeni Us Domain Security
  slug: whoisgeni-us-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Whoisgeni Us Vulnerability Disclosure
  slug: whoisgeni-us-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: whoisgeni-us-correlation
  slug: whoisgeni-us-correlation
- name: whoisgeni-us-manage-api-keys
  slug: whoisgeni-us-manage-api-keys
- name: whoisgeni-us-manage-webhook-secret
  slug: whoisgeni-us-manage-webhook-secret
- name: whoisgeni-us-submit-analysis
  slug: whoisgeni-us-submit-analysis
slug: whoisgeni-us
tags:
- Company
- Domain Intelligence
- Security
- Compliance
- Data Enrichment
website: https://whoisgeni.us/
---
