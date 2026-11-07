---
access_model:
  confidence: low
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 8
asyncapis:
- description: ''
  name: Linxule Com Webhooks
  slug: linxule-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/linxule-com/llms/linxule-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/linxule-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/linxule-com/well-known/linxule-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/linxule-com-security.txt
- group: agent
  href: https://artifacts.apis.io/linxule-com/well-known/linxule-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/linxule-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/linxule-com/vendors/linxule-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linxule-com-vendors.yml
- group: design
  href: https://artifacts.apis.io/linxule-com/rules/linxule-com-rules.yml
  title: ''
  type: Spectral
  url: rules/linxule-com-rules.yml
- group: design
  href: https://artifacts.apis.io/linxule-com/json-ld/linxule-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linxule-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/linxule-com/vocabulary/linxule-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/linxule-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/linxule-com/asyncapi/linxule-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/linxule-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/linxule-com/data-model/linxule-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/linxule-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/linxule-com/security/linxule-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/linxule-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/linxule-com/errors/linxule-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/linxule-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/linxule-com/conformance/linxule-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/linxule-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/linxule-com/hosts/linxule-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linxule-com-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linxule
- group: company
  title: ''
  type: Website
  url: https://linxule.com/
- group: auth
  href: https://artifacts.apis.io/linxule-com/security/linxule-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/linxule-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/linxule-com/security/linxule-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linxule-com-domain-security.yml
coverage:
  checked: '2026-10-30'
  detail: The only OpenAPI file found in the provider's GitHub repo describes a sample Plant Store and does not belong to Linxule.
  evidence:
  - status: 200
    url: https://raw.githubusercontent.com/linxule/docs/main/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: linxule-com appears in the API Evangelist harvest as a stub. Attempts to locate an official corporate website resulted in https://linxule.com/, which hosts a personal blog and llms.txt belonging to Xule Lin, focusing on human‑AI collaboration and organizational theory. No evidence was found that this domain represents a commercial entity or that the company provides an API service. The site does not list a company name, address, contact information, or any API documentation. Therefore the company's identity, official website, and public description remain unverified.
image: https://linxule.com/assets/og-cards/default-r2.jpg
jsonld:
- class_count: 2
  name: Linxule Com Context
  property_count: 4
  slug: linxule-com-context
layout: provider
modified: '2026-10-30'
name: linxule-com
nav: Providers
network: true
overview: 'linxule-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Human-AI Collaboration, Research, Personal Blog, and Unverified.


  The linxule-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.'
random_paper: 5
rate_limits:
- limit_count: 0
  name: Linxule Com Rate Limits
  slug: linxule-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: linxule-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: linxule-com-rules
scopes:
- name: Linxule Com Scopes
  scope_count: 0
  slug: linxule-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 45.5
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/linxule-com/linxule-com-2026-11-03T134920.png
security:
- kind: authentication
  name: Linxule Com Authentication
  slug: linxule-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Linxule Com Domain Security
  slug: linxule-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Linxule Com Vulnerability Disclosure
  slug: linxule-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: linxule-com
tags:
- Artificial Intelligence
- Human-AI Collaboration
- Research
- Personal Blog
- Unverified
website: https://linxule.com/
---
