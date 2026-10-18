---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://account.abblix.com
  baseurl_source: declared
  description: The Connect API from Abblix — 2 operation(s) for connect.
  name: Abblix Connect API
  slug: abblix-connect-api
artifact_total: 6
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/rules/abblix-rules.yml
  title: ''
  type: Spectral
  url: rules/abblix-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/json-ld/abblix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/abblix-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/vocabulary/abblix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/abblix-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/data-model/abblix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/abblix-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/security/abblix-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/abblix-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/conformance/abblix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abblix-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/llms/abblix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abblix-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/well-known/abblix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/abblix-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/well-known/abblix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abblix-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/hosts/abblix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abblix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/vendors/abblix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abblix-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/security/abblix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/abblix-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/abblix/refs/heads/main/security/abblix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abblix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.abblix.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.abblix.com/en/docs/introduction-to-abblix-oidc-server
- group: start
  title: ''
  type: GettingStarted
  url: https://www.abblix.com/en/docs/getting-started-guide
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.abblix.com/en/docs/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Abblix
- group: commercial
  title: ''
  type: Pricing
  url: https://www.abblix.com/en/oidc-server/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abblix.com/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abblix.com/en/terms
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.abblix.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'Abblix builds identity infrastructure for .NET: Abblix OIDC Server, an OpenID Foundation certified OpenID Connect / OAuth 2.0 server library distributed on NuGet and deployed inside the customer''s own perimeter, and Abblix Account, a free hosted authentication service (passkeys, MFA) whose OpenID Provider publishes discovery metadata at account.abblix.com. Licensing is tiered Community (free), Pro and Enterprise, priced by company size.'
image: https://www.abblix.com/og/default.png
json_schemas:
- name: PostConnectTokenRequest
  property_count: 5
  slug: abblix-post-connect-token-request
jsonld:
- class_count: 1
  name: Abblix Context
  property_count: 5
  slug: abblix-context
layout: provider
modified: '2026-10-14'
name: Abblix
nav: Providers
network: true
overview: 'Abblix is listed with 1 API on the [APIs.io](https://apis.io/) network: Connect API. Tagged areas include Company, Identity, OpenID Connect, Authentication, and .NET.


  The Abblix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Abblix''s developer surface includes documentation, getting-started guide, changelog, pricing, and 17 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Abblix API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: abblix-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 21.4
    discoverability: 73.2
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Abblix Domain Security
  slug: abblix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Abblix Vulnerability Disclosure
  slug: abblix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: abblix
tags:
- Company
- Identity
- OpenID Connect
- Authentication
- .NET
- Shared Signals
website: https://www.abblix.com
---
