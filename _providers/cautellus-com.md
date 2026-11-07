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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Cautellus API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cautellus API
  slug: cautellus-com-api
artifact_total: 10
common:
- group: docs
  title: ''
  type: Documentation
  url: https://cautellus.com/guides/scam-safety
- group: commercial
  href: https://artifacts.apis.io/cautellus-com/plans/cautellus-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cautellus-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cautellus-com/rules/cautellus-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cautellus-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cautellus-com/json-ld/cautellus-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cautellus-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cautellus-com/vocabulary/cautellus-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cautellus-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cautellus-com/data-model/cautellus-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cautellus-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cautellus.com/security
- group: design
  href: https://artifacts.apis.io/cautellus-com/conformance/cautellus-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cautellus-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cautellus-com/llms/cautellus-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cautellus-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cautellus-com/mcp/cautellus-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cautellus-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/cautellus-com/hosts/cautellus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cautellus-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cautellus-com/vendors/cautellus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cautellus-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cautellus.com/terms
- group: auth
  title: ''
  type: Security
  url: https://cautellus.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cautellus.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://cautellus.com/news
- group: start
  title: ''
  type: Login
  url: https://cautellus.com/login
- group: auth
  href: https://artifacts.apis.io/cautellus-com/security/cautellus-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cautellus-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cautellus-com/security/cautellus-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cautellus-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cautellus-com/security/cautellus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cautellus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cautellus.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://cautellus.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://cautellus.com/blog
coverage:
  checked: '2026-11-04'
  detail: Developer portal provides HTML docs but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://cautellus.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Cautellus provides an AI-powered scam detection platform that analyzes texts, emails, links, phone numbers, screenshots, and images to assess fraud risk. It offers real‑time scoring, Chrome extension scanning, and shareable results, helping users avoid phishing, deep‑fake, and other online scams. The service includes a web dashboard, API access, and integrates with browsers for instant protection.
image: https://cautellus.com/opengraph-image?aeb280eb52f42aed
json_schemas:
- name: PostApiV1ScanRequest
  property_count: 2
  slug: cautellus-com-post-api-v1-scan-request
- name: PostApiV1ScanResponse
  property_count: 5
  slug: cautellus-com-post-api-v1-scan-response
jsonld:
- class_count: 2
  name: Cautellus Com Context
  property_count: 7
  slug: cautellus-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at cautellus.com.
  name: Cautellus MCP Server
  slug: cautellus-com-mcp-yml
modified: '2026-11-04'
name: Cautellus
nav: Providers
network: true
overview: 'Cautellus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Scam Detection, Artificial Intelligence, Cybersecurity, Consumer Protection, and Chrome Extension.


  The Cautellus catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cautellus'' developer surface includes documentation, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Cautellus Com Plans Pricing
  plan_count: 6
  slug: cautellus-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Cautellus API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: cautellus-com-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 20.7
    developer_ergonomics: 6.0
    discoverability: 57.5
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cautellus Com Domain Security
  slug: cautellus-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cautellus Com Vulnerability Disclosure
  slug: cautellus-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cautellus Com Trust Center
  slug: cautellus-com-trust-center
  summary_line: PCI DSS, GDPR
slug: cautellus-com
tags:
- Scam Detection
- Artificial Intelligence
- Cybersecurity
- Consumer Protection
- Chrome Extension
- Company
website: https://cautellus.com/
---
