---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Dmarc Examiner Com Agentic Access
  operation_count: 42
  slug: dmarc-examiner-com-agentic-access
  summary_line: 42 operations · 18 acting
api_count: 1
apis:
- baseURL: https://api.dmarc-examiner.com
  baseurl_source: declared
  description: View and manage security alerts
  name: DMARC Examiner Alerts API
  slug: dmarc-examiner-com-alerts-api
- baseURL: https://api.dmarc-examiner.com
  baseurl_source: declared
  description: Manage monitored domains
  name: DMARC Examiner Domains API
  slug: dmarc-examiner-com-domains-api
- baseURL: https://api.dmarc-examiner.com
  baseurl_source: declared
  description: Access DMARC RUF (forensic) reports — Pro plan and above
  name: DMARC Examiner Forensic Reports API
  slug: dmarc-examiner-com-forensic-reports-api
- baseURL: https://api.dmarc-examiner.com
  baseurl_source: declared
  description: Access DMARC aggregate reports and statistics
  name: DMARC Examiner Reports API
  slug: dmarc-examiner-com-reports-api
- baseURL: https://api.dmarc-examiner.com
  baseurl_source: declared
  description: Free DMARC utilities
  name: DMARC Examiner Tools API
  slug: dmarc-examiner-com-tools-api
- baseURL: https://api.dmarc-examiner.com
  baseurl_source: declared
  description: 'Subscribe to events via outbound HTTPS webhooks — Pro plan and above. ## Events emitted The system currently emits a single event: - **`alert.created`** — fired whenever an Alert is created in the org'
  name: DMARC Examiner Webhooks API
  slug: dmarc-examiner-com-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Dmarc Examiner Com Webhooks
  slug: dmarc-examiner-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/dmarc-examiner-com/agentic-access/dmarc-examiner-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dmarc-examiner-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dmarc-examiner-com/plans/dmarc-examiner-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dmarc-examiner-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dmarc-examiner-com/rules/dmarc-examiner-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dmarc-examiner-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dmarc-examiner-com/json-ld/dmarc-examiner-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dmarc-examiner-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dmarc-examiner-com/vocabulary/dmarc-examiner-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dmarc-examiner-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dmarc-examiner-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dmarc-examiner-com/asyncapi/dmarc-examiner-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dmarc-examiner-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dmarc-examiner-com/data-model/dmarc-examiner-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dmarc-examiner-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dmarc-examiner-com/authentication/dmarc-examiner-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dmarc-examiner-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dmarc-examiner-com/errors/dmarc-examiner-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dmarc-examiner-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dmarc-examiner-com/conformance/dmarc-examiner-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dmarc-examiner-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dmarc-examiner-com/llms/dmarc-examiner-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dmarc-examiner-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dmarc-examiner-com/well-known/dmarc-examiner-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dmarc-examiner-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dmarc-examiner-com/hosts/dmarc-examiner-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dmarc-examiner-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dmarc-examiner.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dmarc-examiner.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://api.dmarc-examiner.com/api/doc/
- group: auth
  href: https://artifacts.apis.io/dmarc-examiner-com/security/dmarc-examiner-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dmarc-examiner-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dmarc-examiner.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.dmarc-examiner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dmarc-examiner.com/docs
- group: company
  title: ''
  type: Blog
  url: https://dmarc-examiner.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dmarc-examiner.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://dmarc-examiner.com/docs#getting-started
created: '2026-11-05'
description: DMARC Examiner provides professional DMARC monitoring and email authentication services, helping organizations protect their domains from spoofing and phishing attacks. The platform offers free tools, detailed reporting, and easy integration to ensure email security compliance across SPF, DKIM, and DMARC standards.
image: https://dmarc-examiner.com/og-image.png
json_schemas:
- name: Alert
  property_count: 11
  slug: dmarc-examiner-com-alert
- name: ForensicReport
  property_count: 11
  slug: dmarc-examiner-com-forensic-report
- name: ReportRecord
  property_count: 13
  slug: dmarc-examiner-com-report-record
- name: Report
  property_count: 20
  slug: dmarc-examiner-com-report
- name: ReportStatistics
  property_count: 3
  slug: dmarc-examiner-com-report-statistics
- name: Webhook
  property_count: 10
  slug: dmarc-examiner-com-webhook
jsonld:
- class_count: 18
  name: Dmarc Examiner Com Context
  property_count: 84
  slug: dmarc-examiner-com-context
layout: provider
modified: '2026-11-05'
name: DMARC Examiner
nav: Providers
network: true
overview: 'DMARC Examiner publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Domains API, Forensic Reports API, and 3 more. Tagged areas include Email Security, DMARC, SPF, DKIM, and Anti-Phishing.


  The DMARC Examiner catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DMARC Examiner''s developer surface includes authentication, API reference, documentation, engineering blog, pricing, getting-started guide, and 18 more developer resources.'
plans:
- name: Dmarc Examiner Com Plans Pricing
  plan_count: 4
  slug: dmarc-examiner-com-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: DMARC Examiner API Rules
  rule_count: 69
  severity_counts:
    error: 59
    hint: 0
    info: 4
    warn: 6
  slug: dmarc-examiner-com-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 71.5
    developer_ergonomics: 54.2
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dmarc Examiner Com Authentication
  slug: dmarc-examiner-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dmarc Examiner Com Domain Security
  slug: dmarc-examiner-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: dmarc-examiner-com-create-and-verify-domain
  slug: dmarc-examiner-com-create-and-verify-domain
slug: dmarc-examiner-com
tags:
- Email Security
- DMARC
- SPF
- DKIM
- Anti-Phishing
- Monitoring
website: https://dmarc-examiner.com/
---
