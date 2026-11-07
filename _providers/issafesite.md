---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://issafesite.com
  baseurl_source: declared
  description: 'IsSafeSite API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: IsSafeSite API
  slug: issafesite-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/issafesite/plans/issafesite-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/issafesite-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/issafesite/rules/issafesite-rules.yml
  title: ''
  type: Spectral
  url: rules/issafesite-rules.yml
- group: design
  href: https://artifacts.apis.io/issafesite/json-ld/issafesite-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/issafesite-context.jsonld
- group: design
  href: https://artifacts.apis.io/issafesite/vocabulary/issafesite-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/issafesite-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/issafesite/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/issafesite/data-model/issafesite-data-model.yml
  title: ''
  type: DataModel
  url: data-model/issafesite-data-model.yml
- group: auth
  href: https://artifacts.apis.io/issafesite/security/issafesite-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/issafesite-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/issafesite/conformance/issafesite-conformance.yml
  title: ''
  type: Conformance
  url: conformance/issafesite-conformance.yml
- group: other
  href: https://artifacts.apis.io/issafesite/hosts/issafesite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/issafesite-hosts.yml
- group: other
  href: https://artifacts.apis.io/issafesite/vendors/issafesite-vendors.yml
  title: ''
  type: Vendors
  url: vendors/issafesite-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.issafesite.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.issafesite.com/changelog
- group: auth
  href: https://artifacts.apis.io/issafesite/security/issafesite-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/issafesite-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/issafesite/security/issafesite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/issafesite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://issafesite.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.issafesite.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://issafesite.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://issafesite.com/#how-it-works
- group: operate
  title: ''
  type: Support
  url: https://issafesite.com/docs#support
- group: company
  title: ''
  type: Blog
  url: https://issafesite.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://issafesite.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://issafesite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://issafesite.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Harries
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://issafesite.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: IsSafeSite offers an AI‑powered website security scanner that evaluates SSL configuration, security headers, CORS settings, exposed files, CMS plugins, and privacy compliance. Users can run up to three free scans per day and receive detailed PDF reports with actionable remediation steps. Paid plans provide additional scans, advanced features, and API access for integration into workflows.
image: https://issafesite.com/icon.svg
json_schemas:
- name: PostApiV1ScanRequest
  property_count: 2
  slug: issafesite-post-api-v1-scan-request
- name: PostApiV1ScanResponse
  property_count: 7
  slug: issafesite-post-api-v1-scan-response
jsonld:
- class_count: 2
  name: Issafesite Context
  property_count: 7
  slug: issafesite-context
layout: provider
modified: '2026-11-02'
name: IsSafeSite
nav: Providers
network: true
overview: 'IsSafeSite is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Websites, Scanner, Artificial Intelligence, and Compliance.


  The IsSafeSite catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  IsSafeSite''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Issafesite Plans Pricing
  plan_count: 3
  slug: issafesite-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Issafesite Rate Limits
  slug: issafesite-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: IsSafeSite API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: issafesite-rules
scopes:
- name: Issafesite Scopes
  scope_count: 0
  slug: issafesite-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 24.3
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Issafesite Authentication
  slug: issafesite-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Issafesite Domain Security
  slug: issafesite-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Issafesite Vulnerability Disclosure
  slug: issafesite-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: scan
  slug: issafesite-scan
slug: issafesite
tags:
- Security
- Websites
- Scanner
- Artificial Intelligence
- Compliance
- Monitoring
website: https://issafesite.com
---
