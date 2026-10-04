---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-10-03'
api_count: 2
apis:
- baseURL: https://api.askattest.com
  baseurl_source: declared
  description: The Studies API from Attest — 1 operation(s) for studies.
  name: Attest Studies API
  slug: attest-studies-api
- baseURL: https://api.askattest.com
  baseurl_source: declared
  description: The Study API from Attest — 1 operation(s) for study.
  name: Attest Study API
  slug: attest-study-api
artifact_total: 5
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/attest/refs/heads/main/rules/attest-rules.yml
  title: ''
  type: Spectral
  url: rules/attest-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/attest/refs/heads/main/authentication/attest-authentication.yml
  title: ''
  type: Authentication
  url: authentication/attest-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/attest/refs/heads/main/conformance/attest-conformance.yml
  title: ''
  type: Conformance
  url: conformance/attest-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/attest/refs/heads/main/llms/attest-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/attest-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/attest/refs/heads/main/well-known/attest-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/attest-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/attest/refs/heads/main/well-known/attest-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/attest-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/attest/refs/heads/main/hosts/attest-hosts.yml
  title: ''
  type: Hosts
  url: hosts/attest-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/attest/refs/heads/main/vendors/attest-vendors.yml
  title: ''
  type: Vendors
  url: vendors/attest-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.askattest.com/en/
- group: auth
  title: ''
  type: Security
  url: https://www.askattest.com/legal/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.askattest.com/press
- group: docs
  title: ''
  type: APIReference
  url: https://developers.askattest.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.askattest.com/en/articles/3494059-getting-started-with-your-first-survey
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.attest.com/reference/getstudystructure
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/attest/refs/heads/main/security/attest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/attest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.askattest.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.askattest.com/platform-features
- group: commercial
  title: ''
  type: Pricing
  url: https://www.askattest.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.askattest.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.askattest.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.askattest.com/legal/privacy-policy
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found after probing common spec endpoints.
  evidence:
  - status: 404
    url: https://api.askattest.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Attest provides an AI‑powered consumer insights platform that helps B2C brands understand market trends, test concepts, and measure campaign performance. Their solution combines data quality, research tools, and analytics to enable product development, brand tracking, and advertising effectiveness across multiple industries.
image: https://emx2zzfzxax.exactdn.com/wp-content/uploads/2026/06/attest-open-graph.png?strip=all
layout: provider
modified: '2026-09-26'
name: Attest
nav: Providers
network: true
overview: 'Attest publishes 2 APIs on the [APIs.io](https://apis.io/) network: Studies API and Study API. Tagged areas include Artificial Intelligence, Consumer Insights, Market Research, Consumer, and Analytics.


  The Attest catalog on APIs.io includes 1 Spectral governance ruleset.


  Attest''s developer surface includes authentication, support, API reference, getting-started guide, documentation, pricing, engineering blog, and 14 more developer resources.'
random_paper: 1
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Attest API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: attest-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 12.9
    developer_ergonomics: 57.1
    discoverability: 75.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Attest Authentication
  slug: attest-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Attest Domain Security
  slug: attest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: attest
tags:
- Artificial Intelligence
- Consumer Insights
- Market Research
- Consumer
- Analytics
website: https://www.askattest.com/
---
