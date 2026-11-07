---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Convert PDF bank statements to CSV, Excel, OFX, QFX and JSON.
  name: NoRekey API
  slug: norekey-api
- baseURL: https://norekey.com
  baseurl_source: declared
  description: 'Four endpoints: upload a statement, poll its status, download the result in any supported format, and check the team''s page balance. Authentication is a bearer API key (created under Settings → Team →'
  name: NoRekey API API
  slug: norekey-api-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/norekey/rules/norekey-rules.yml
  title: ''
  type: Spectral
  url: rules/norekey-rules.yml
- group: design
  href: https://artifacts.apis.io/norekey/json-ld/norekey-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/norekey-context.jsonld
- group: design
  href: https://artifacts.apis.io/norekey/vocabulary/norekey-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/norekey-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/norekey/conformance/norekey-conformance.yml
  title: ''
  type: Conformance
  url: conformance/norekey-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/norekey/plans/norekey-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/norekey-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/norekey/data-model/norekey-data-model.yml
  title: ''
  type: DataModel
  url: data-model/norekey-data-model.yml
- group: design
  href: https://artifacts.apis.io/norekey/errors/norekey-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/norekey-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/norekey/llms/norekey-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/norekey-llms.txt
- group: other
  href: https://artifacts.apis.io/norekey/hosts/norekey-hosts.yml
  title: ''
  type: Hosts
  url: hosts/norekey-hosts.yml
- group: other
  href: https://artifacts.apis.io/norekey/vendors/norekey-vendors.yml
  title: ''
  type: Vendors
  url: vendors/norekey-vendors.yml
- group: auth
  href: https://artifacts.apis.io/norekey/security/norekey-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/norekey-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://norekey.com/
- group: docs
  title: ''
  type: Documentation
  url: https://norekey.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://norekey.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://norekey.com/api
- group: operate
  title: ''
  type: Support
  url: https://norekey.com/help
- group: company
  title: ''
  type: Blog
  url: https://norekey.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://norekey.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://norekey.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://norekey.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://norekey.com/privacy
created: '2026-10-18'
description: NoRekey provides a SaaS platform that converts bank statement PDFs into structured data formats such as CSV, Excel, OFX, and QFX. Users can upload statements from a wide range of banks, and the service extracts transaction details, validates balances, and returns clean data ready for accounting software. The tool emphasizes privacy by deleting uploaded files after processing and offers a free tier for quick conversions. It targets fintech developers, accountants, and small businesses needing automated statement processing.
image: https://norekey.com/og.png
json_schemas:
- name: Conversion
  property_count: 16
  slug: norekey-conversion
- name: Usage
  property_count: 5
  slug: norekey-usage
jsonld:
- class_count: 3
  name: Norekey Context
  property_count: 22
  slug: norekey-context
layout: provider
modified: '2026-10-18'
name: NoRekey
nav: Providers
network: true
overview: 'NoRekey publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company, Fintech, Data Conversion, Software-as-a-Service, and Banking.


  The NoRekey catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NoRekey''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Norekey Plans Pricing
  plan_count: 4
  slug: norekey-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: NoRekey API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: norekey-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 57.5
    developer_ergonomics: 17.9
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 46.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/norekey/norekey-2026-11-03T140302.png
security:
- kind: domain-security
  name: Norekey Domain Security
  slug: norekey-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: norekey
tags:
- Company
- Fintech
- Data Conversion
- Software-as-a-Service
- Banking
website: https://norekey.com/
---
