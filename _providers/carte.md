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
- description: API platform for private capital markets, providing endpoints for equity data, valuations, and workflow automation.
  name: Carta API
  slug: carta-api
- description: The V1Alpha1 API from Carte — 10 operation(s) for v1alpha1.
  name: Carte V1Alpha1 API
  slug: carte-v1alpha1-api
artifact_total: 9
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/rate-limits/carte-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/carte-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/rules/carte-rules.yml
  title: ''
  type: Spectral
  url: rules/carte-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/json-ld/carte-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carte-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/vocabulary/carte-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carte-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/data-model/carte-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carte-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.carta.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/authentication/carte-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carte-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/conformance/carte-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carte-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/llms/carte-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carte-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/well-known/carte-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carte-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/well-known/carte-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carte-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/hosts/carte-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carte-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/vendors/carte-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carte-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/security/carte-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/carte-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carte/refs/heads/main/security/carte-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carte-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carta.com
coverage:
  checked: '2026-10-07'
  detail: Docs at https://docs.carta.com provide API reference but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 404
    url: https://docs.carta.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Carta provides an end‑to‑end suite for private capital markets, offering cap table management, equity plan administration, fund accounting, compliance, and a robust API platform for developers to integrate equity data, valuations, and workflow automation across investors, companies, and service providers.
image: https://images.ctfassets.net/y88td1zx1ufe/6RvXq471HohgYLlne9iKay/1e1a7d9f63a73e279fb38ab589210422/OG.png
json_schemas:
- name: PostV1Alpha1FilesUploadResponse
  property_count: 6
  slug: carte-post-v1-alpha1-files-upload-response
jsonld:
- class_count: 1
  name: Carte Context
  property_count: 1
  slug: carte-context
layout: provider
modified: '2026-10-07'
name: Carte
nav: Providers
network: true
overview: 'Carte is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including V1Alpha1 API, and 1 more. Tagged areas include Company, Finance, Equity, and FundManagement.


  The Carte catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Carte''s developer surface includes authentication, engineering blog, API reference, getting-started guide, documentation, and 22 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 2
  name: Carte Rate Limits
  slug: carte-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Carte API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: carte-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 51.2
    catalog_earned_first_party: 8.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 42.9
    discoverability: 58.9
    operational_transparency: 52.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
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
  name: Carte Authentication
  slug: carte-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Carte Domain Security
  slug: carte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carte Trust Center
  slug: carte-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: carte
tags:
- Company
- Finance
- Equity
- FundManagement
website: https://carta.com
---
