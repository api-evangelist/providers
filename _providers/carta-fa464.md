---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Carta provides a developer API platform for managing private fund data and investor relations.
  name: Carta API
  slug: carta-api
- description: The V1Alpha1 API from Carta Fa464 — 10 operation(s) for v1alpha1.
  name: Carta Fa464 V1Alpha1 API
  slug: carta-fa464-v1alpha1-api
artifact_total: 11
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/rate-limits/carta-fa464-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/carta-fa464-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/rules/carta-fa464-rules.yml
  title: ''
  type: Spectral
  url: rules/carta-fa464-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/json-ld/carta-fa464-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carta-fa464-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/vocabulary/carta-fa464-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carta-fa464-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/data-model/carta-fa464-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carta-fa464-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.carta.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/authentication/carta-fa464-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carta-fa464-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/conformance/carta-fa464-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carta-fa464-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/llms/carta-fa464-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carta-fa464-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/well-known/carta-fa464-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carta-fa464-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/well-known/carta-fa464-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carta-fa464-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/hosts/carta-fa464-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carta-fa464-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/vendors/carta-fa464-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carta-fa464-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.carta.com/
- group: auth
  title: ''
  type: Security
  url: https://carta.com/security/generative-ai-at-carta/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carta.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://carta.com/press/
- group: start
  title: ''
  type: Login
  url: https://login.app.carta.com/credentials/login/
- group: other
  title: ''
  type: Leadership
  url: https://carta.com/learn/private-funds/management/
- group: company
  title: ''
  type: Blog
  url: https://carta.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.carta.com/api-platform/reference/v-1-alpha-1-draft-issuers-create-draft-issuer
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.carta.com/api-platform/guides/getting-started/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.carta.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carta
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/security/carta-fa464-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/carta-fa464-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carta-fa464/refs/heads/main/security/carta-fa464-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carta-fa464-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carta.com
coverage:
  checked: '2026-10-07'
  detail: API documentation is served as a JavaScript-rendered site without a machine-readable spec.
  evidence:
  - status: 401
    url: https://api.carta.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Carta provides an end‑to‑end software suite that manages equity, cap tables, 409A valuations, SAFE financings, and secondary liquidity for private companies and funds. It also offers fund administration tools, tax and compliance workflows, and legal transaction automation for venture capital, private equity, and other private‑capital firms. The platform integrates AI‑native features and connectors for CRM, ERP, and other enterprise systems.
image: https://images.ctfassets.net/y88td1zx1ufe/6RvXq471HohgYLlne9iKay/1e1a7d9f63a73e279fb38ab589210422/OG.png
json_schemas:
- name: GetV1Alpha1InvestorsFirmsFirmidFundsFundidInvestmentsInvestm
  property_count: 6
  slug: carta-fa464-get-v1-alpha1-investors-firms-firmid-funds-fundid-investments-investm
- name: PostV1Alpha1FilesUploadRequest
  property_count: 1
  slug: carta-fa464-post-v1-alpha1-files-upload-request
- name: PostV1Alpha1FilesUploadResponse
  property_count: 6
  slug: carta-fa464-post-v1-alpha1-files-upload-response
jsonld:
- class_count: 3
  name: Carta Fa464 Context
  property_count: 2
  slug: carta-fa464-context
layout: provider
modified: '2026-10-07'
name: Carta Fa464
nav: Providers
network: true
overview: 'Carta Fa464 is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including V1Alpha1 API, and 1 more. Tagged areas include Equity Management, Fund Administration, Legal Compliance, Cap Table, and Valuation.


  The Carta Fa464 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Carta Fa464''s developer surface includes authentication, engineering blog, API reference, getting-started guide, documentation, and 22 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 2
  name: Carta Fa464 Rate Limits
  slug: carta-fa464-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Carta Fa464 API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: carta-fa464-rules
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 42.9
    discoverability: 67.9
    operational_transparency: 52.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Carta Fa464 Authentication
  slug: carta-fa464-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Carta Fa464 Domain Security
  slug: carta-fa464-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carta Fa464 Trust Center
  slug: carta-fa464-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: carta-fa464
tags:
- Equity Management
- Fund Administration
- Legal Compliance
- Cap Table
- Valuation
- Private Capital
- CRM Integration
- AI Automation
website: https://carta.com
---
