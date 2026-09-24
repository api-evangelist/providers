---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://platform-api.aixplain.com
  baseurl_source: declared
  description: 'aiXplain API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: aiXplain API
  slug: aixplain-api
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/plans/aixplain-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aixplain-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/rules/aixplain-rules.yml
  title: ''
  type: Spectral
  url: rules/aixplain-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/json-ld/aixplain-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aixplain-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/vocabulary/aixplain-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aixplain-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/data-model/aixplain-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aixplain-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.aixplain.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/conformance/aixplain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aixplain-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/llms/aixplain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aixplain-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/vendors/aixplain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aixplain-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/packages/aixplain-packages.yml
  title: ''
  type: Packages
  url: packages/aixplain-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aixplain.com/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.aixplain.com/security
- group: build
  title: ''
  type: SDKs
  url: https://www.aixplain.com/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aixplain.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/aixplain/aiXplain/releases
- group: company
  title: ''
  type: Blog
  url: https://www.aixplain.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aixplain.com/getting-started/quick-start/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/security/aixplain-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aixplain-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aixplain/refs/heads/main/security/aixplain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aixplain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aixplain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aixplain.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aixplain.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aixplain.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.aixplain.com/contact
- group: company
  title: ''
  type: About
  url: https://www.aixplain.com/about
coverage:
  checked: 2026-09-22
  detail: The provider's documentation at https://docs.aixplain.com/ does not expose any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://docs.aixplain.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-22'
description: aiXplain provides an operating system for autonomous work, enabling enterprises to build, orchestrate, and govern AI agents at scale while maintaining data privacy and compliance. The platform offers tools such as Studio for visual building, SDKs, on‑prem and air‑gapped deployments, and integrates with thousands of models across 63 countries. It targets regulated industries with SOC 2 Type II certification and supports enterprise, research, and pricing tiers.
image: https://www.aixplain.com/aixplain-og.png
json_schemas:
- name: GetV1SessionsResponse
  property_count: 4
  slug: aixplain-get-v1-sessions-response
jsonld:
- class_count: 1
  name: Aixplain Context
  property_count: 4
  slug: aixplain-context
layout: provider
modified: '2026-09-22'
name: aiXplain
nav: Providers
network: true
overview: 'aiXplain publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Autonomous-Work, Enterprise, and Platform.


  The aiXplain catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aiXplain''s developer surface includes changelog, engineering blog, getting-started guide, documentation, API reference, pricing, support, and 18 more developer resources.'
plans:
- name: Aixplain Plans Pricing
  plan_count: 3
  slug: aixplain-plans-pricing
random_paper: 18
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: aiXplain API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: aixplain-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.1
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 18.2
    developer_ergonomics: 42.9
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 54.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aixplain Domain Security
  slug: aixplain-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Aixplain Trust Center
  slug: aixplain-trust-center
  summary_line: SOC 2, GDPR
slug: aixplain
tags:
- Company
- Artificial Intelligence
- Autonomous-Work
- Enterprise
- Platform
website: https://www.aixplain.com/
---
