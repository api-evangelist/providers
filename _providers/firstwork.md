---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Firstwork API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Firstwork API
  slug: firstwork-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/firstwork/well-known/firstwork-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/firstwork-api-security.txt
- group: design
  href: https://artifacts.apis.io/firstwork/rules/firstwork-rules.yml
  title: ''
  type: Spectral
  url: rules/firstwork-rules.yml
- group: design
  href: https://artifacts.apis.io/firstwork/vocabulary/firstwork-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/firstwork-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/firstwork/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.firstwork.com/
- group: design
  href: https://artifacts.apis.io/firstwork/conformance/firstwork-conformance.yml
  title: ''
  type: Conformance
  url: conformance/firstwork-conformance.yml
- group: other
  href: https://artifacts.apis.io/firstwork/overlays/firstwork-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/firstwork-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/firstwork/llms/firstwork-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/firstwork-llms.txt
- group: other
  href: https://artifacts.apis.io/firstwork/a2a/firstwork-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/firstwork-a2a.yml
- group: agent
  href: https://artifacts.apis.io/firstwork/well-known/firstwork-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/firstwork-well-known.yml
- group: other
  href: https://artifacts.apis.io/firstwork/hosts/firstwork-hosts.yml
  title: ''
  type: Hosts
  url: hosts/firstwork-hosts.yml
- group: other
  href: https://artifacts.apis.io/firstwork/vendors/firstwork-vendors.yml
  title: ''
  type: Vendors
  url: vendors/firstwork-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.firstwork.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firstwork.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.firstwork.com/newsroom
- group: auth
  href: https://artifacts.apis.io/firstwork/security/firstwork-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/firstwork-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/firstwork/security/firstwork-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/firstwork-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.firstwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firstwork.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.firstwork.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.firstwork.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@firstwork.com
- group: company
  title: ''
  type: Blog
  url: https://www.firstwork.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.firstwork.com/book-demo
created: '2026-10-29'
description: Firstwork provides AI‑powered agents that automate frontline workforce operations, including document verification, browser automation, workflow orchestration, continuous compliance, and right‑to‑work screening, enabling enterprises to streamline hiring, onboarding, and ongoing employee management within existing systems. Their platform leverages applied artificial intelligence to reduce manual effort, improve accuracy, and ensure regulatory compliance, serving institutions with over 300+ deployments worldwide.
image: https://cdn.prod.website-files.com/6796783f35faa4c61a224a54/6a62271953b0458d9c1d9725_ChatGPT%20Image%20Jul%2023%2C%202026%2C%2008_06_57%20PM.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.firstwork.com over HTTP.
  name: Firstwork MCP Server
  slug: firstwork
modified: '2026-10-29'
name: Firstwork
nav: Providers
network: true
overview: 'Firstwork publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Human Resources, Frontline, Automation, and Compliance.


  The Firstwork catalog on APIs.io includes 1 Spectral governance ruleset.


  Firstwork''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Firstwork Plans Pricing
  plan_count: 0
  slug: firstwork-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Firstwork Rate Limits
  slug: firstwork-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Firstwork API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: firstwork-rules
scopes:
- name: Firstwork Scopes
  scope_count: 0
  slug: firstwork-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 26.7
    discoverability: 65.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/firstwork/firstwork-2026-11-03T132058.png
security:
- kind: authentication
  name: Firstwork Authentication
  slug: firstwork-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Firstwork Domain Security
  slug: firstwork-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Firstwork Trust Center
  slug: firstwork-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: get-slack-cli-install
  slug: firstwork-get-slack-cli-install
slug: firstwork
tags:
- Artificial Intelligence
- Human Resources
- Frontline
- Automation
- Compliance
website: https://www.firstwork.com/
---
