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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public MCP endpoint providing tools to search schools, get stats, and calculate match scores without authentication.
  name: AdmitBase MCP API
  slug: admitbase-mcp-api
- description: 'AdmitBase API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: AdmitBase API
  slug: admitbase-com-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/admitbase-com/rules/admitbase-com-rules.yml
  title: ''
  type: Spectral
  url: rules/admitbase-com-rules.yml
- group: design
  href: https://artifacts.apis.io/admitbase-com/vocabulary/admitbase-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/admitbase-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/admitbase-com/conformance/admitbase-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/admitbase-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/admitbase-com/llms/admitbase-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/admitbase-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/admitbase-com/mcp/admitbase-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/admitbase-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/admitbase-com/well-known/admitbase-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/admitbase-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/admitbase-com/hosts/admitbase-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/admitbase-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/admitbase-com/vendors/admitbase-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/admitbase-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/admitbase-com/security/admitbase-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/admitbase-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://admitbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://admitbase.com/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://admitbase.com/.well-known/mcp.json
- group: operate
  title: ''
  type: Support
  url: https://admitbase.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://admitbase.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://admitbase.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://admitbase.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://admitbase.com/privacy
created: '2026-10-31'
description: AdmitBase is a professional-school admissions data platform. It compares an applicant's GPA and standardised test score against the admitted‑student figures each school itself published, and returns a 0‑100 match score classified as Safety, Target, Reach or Far Reach. See your real chances at every law, medical, and dental school — your GPA and test score against admitted‑student data from official disclosures.
image: https://admitbase.com/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at admitbase.com.
  name: AdmitBase MCP Server
  slug: admitbase-com-mcp-yml
modified: '2026-10-31'
name: AdmitBase
nav: Providers
network: true
overview: 'AdmitBase is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Admissions, Law, Medical, Dental, and Education.


  The AdmitBase catalog on APIs.io includes 1 Spectral governance ruleset.


  AdmitBase''s developer surface includes documentation, API reference, support, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Admitbase Com Plans Pricing
  plan_count: 0
  slug: admitbase-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Admitbase Com Rate Limits
  slug: admitbase-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: AdmitBase API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: admitbase-com-rules
scopes:
- name: Admitbase Com Scopes
  scope_count: 0
  slug: admitbase-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 10.7
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 25.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Admitbase Com Authentication
  slug: admitbase-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Admitbase Com Domain Security
  slug: admitbase-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: admitbase-com
tags:
- Admissions
- Law
- Medical
- Dental
- Education
website: https://admitbase.com/
---
