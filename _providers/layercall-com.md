---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Layercall Com Agentic Access
  operation_count: 19
  slug: layercall-com-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 1
apis:
- baseURL: https://www.layercall.com
  baseurl_source: declared
  description: The AI agents API from layercall-com — 3 operation(s) for ai agents.
  name: layercall-com AI agents API
  slug: layercall-com-ai-agents-api
- baseURL: https://www.layercall.com
  baseurl_source: declared
  description: The Batch API from layercall-com — 1 operation(s) for batch.
  name: layercall-com Batch API
  slug: layercall-com-batch-api
- baseURL: https://www.layercall.com
  baseurl_source: declared
  description: Fingerprint reputation and bot detection.
  name: layercall-com Device API
  slug: layercall-com-device-api
- baseURL: https://www.layercall.com
  baseurl_source: declared
  description: The Reputation API from layercall-com — 2 operation(s) for reputation.
  name: layercall-com Reputation API
  slug: layercall-com-reputation-api
- baseURL: https://www.layercall.com
  baseurl_source: declared
  description: The Rules API from layercall-com — 3 operation(s) for rules.
  name: layercall-com Rules API
  slug: layercall-com-rules-api
- baseURL: https://www.layercall.com
  baseurl_source: declared
  description: Risk scores for a single signal type.
  name: layercall-com Scoring API
  slug: layercall-com-scoring-api
- baseURL: https://www.layercall.com
  baseurl_source: declared
  description: One call across every signal on a signup.
  name: layercall-com Unified API
  slug: layercall-com-unified-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/layercall-com/agentic-access/layercall-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/layercall-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/layercall-com/plans/layercall-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/layercall-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/layercall-com/rules/layercall-com-rules.yml
  title: ''
  type: Spectral
  url: rules/layercall-com-rules.yml
- group: design
  href: https://artifacts.apis.io/layercall-com/json-ld/layercall-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/layercall-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/layercall-com/vocabulary/layercall-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/layercall-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/layercall-com/data-model/layercall-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/layercall-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.layercall.com/terms
- group: design
  href: https://artifacts.apis.io/layercall-com/errors/layercall-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/layercall-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/layercall-com/conformance/layercall-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/layercall-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/layercall-com/llms/layercall-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/layercall-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/layercall-com/mcp/layercall-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/layercall-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/layercall-com/well-known/layercall-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/layercall-com-security.txt
- group: auth
  href: https://artifacts.apis.io/layercall-com/well-known/layercall-com-layercall-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/layercall-com-layercall-security.txt
- group: agent
  href: https://artifacts.apis.io/layercall-com/well-known/layercall-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/layercall-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/layercall-com/hosts/layercall-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/layercall-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/layercall-com/vendors/layercall-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/layercall-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.layercall.com/integrations/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://www.layercall.com/status
- group: start
  title: ''
  type: SignUp
  url: https://www.layercall.com/demo/signup
- group: start
  title: ''
  type: Sandbox
  url: https://www.layercall.com/playground
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LayerCall
- group: auth
  href: https://artifacts.apis.io/layercall-com/authentication/layercall-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/layercall-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/layercall-com/security/layercall-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/layercall-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/layercall-com/security/layercall-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/layercall-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.layercall.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.layercall.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.layercall.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.layercall.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.layercall.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.layercall.com/privacy
created: '2026-10-30'
description: LayerCall provides a trust intelligence API that scores IPs, emails, phones, domains, and devices for fraud risk in a single call. It offers free and paid tiers, detecting VPNs, proxies, Tor, bots, and device fingerprints, helping prevent fake signups and account takeover. The service is RESTful, supports any platform, and includes detailed risk scores from 0 to 100.
image: https://www.layercall.com/opengraph-image?90b5402459d9ca5e
json_schemas:
- name: DeviceScore
  property_count: 11
  slug: layercall-com-device-score
- name: DomainResult
  property_count: 13
  slug: layercall-com-domain-result
- name: EmailResult
  property_count: 22
  slug: layercall-com-email-result
- name: IpScore
  property_count: 16
  slug: layercall-com-ip-score
- name: PhoneResult
  property_count: 13
  slug: layercall-com-phone-result
- name: UserScore
  property_count: 12
  slug: layercall-com-user-score
jsonld:
- class_count: 8
  name: Layercall Com Context
  property_count: 40
  slug: layercall-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.layercall.com requiring an API key.
  name: layercall-com MCP Server
  slug: layercall-com-mcp-yml
modified: '2026-10-30'
name: layercall-com
nav: Providers
network: true
overview: 'layercall-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI agents API, Batch API, Device API, and 4 more. Tagged areas include Company, FraudDetection, TrustIntelligence, API, and Security.


  The layercall-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  layercall-com''s developer surface includes signup flow, sandbox, authentication, documentation, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Layercall Com Plans Pricing
  plan_count: 4
  slug: layercall-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Layercall Com Rate Limits
  slug: layercall-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: layercall-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: layercall-com-rules
scopes:
- name: Layercall Com Scopes
  scope_count: 0
  slug: layercall-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 95.7
    catalog_earned_first_party: 0.0
    catalog_gap: 19.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 62.5
    developer_ergonomics: 31.0
    discoverability: 65.0
    operational_transparency: 58.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Layercall Com Authentication
  slug: layercall-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Layercall Com Domain Security
  slug: layercall-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Layercall Com Vulnerability Disclosure
  slug: layercall-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 7
skills:
- name: lookup-phone
  slug: layercall-com-lookup-phone
- name: score-device
  slug: layercall-com-score-device
- name: score-domain
  slug: layercall-com-score-domain
- name: score-ip
  slug: layercall-com-score-ip
- name: score-user
  slug: layercall-com-score-user
- name: verify-agent
  slug: layercall-com-verify-agent
- name: verify-email
  slug: layercall-com-verify-email
slug: layercall-com
tags:
- Company
- FraudDetection
- TrustIntelligence
- API
- Security
website: https://www.layercall.com/
---
