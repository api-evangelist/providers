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
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Provides Data Standards Cloud API and Classification API as described in the Getting Started guide.
  name: Claravine API
  slug: claravine-api-2
- baseURL: https://api.claravine.com
  baseurl_source: declared
  description: 'Claravine API as documented publicly: 0 operations. Contract generated from the documentation by API Evangelist (2026-10-08); not the provider''s own document.'
  name: Claravine API
  slug: claravine-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/claravine/refs/heads/main/plans/claravine-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claravine-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/claravine/refs/heads/main/security/claravine-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/claravine-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/claravine/refs/heads/main/conformance/claravine-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claravine-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/claravine/refs/heads/main/well-known/claravine-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/claravine-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/claravine/refs/heads/main/well-known/claravine-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claravine-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/claravine/refs/heads/main/hosts/claravine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claravine-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/claravine/refs/heads/main/vendors/claravine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claravine-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claravine.com/legal/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.claravine.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claravine.com/legal/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.claravine.com/company/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/claravine/refs/heads/main/security/claravine-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/claravine-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/claravine/refs/heads/main/security/claravine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claravine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.claravine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.claravine.com/platform/
- group: docs
  title: ''
  type: APIReference
  url: https://www.claravine.com/platform/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.claravine.com/platform/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.claravine.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.claravine.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.claravine.com/hc/en-us/
coverage:
  checked: '2026-10-08'
  detail: The provider's documentation pages contain no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://api.claravine.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Claravine provides a Data Standards Platform that helps enterprises govern taxonomy and naming standards across marketing campaigns, content, and data pipelines. Their SaaS solution integrates with major ad platforms, CRM, and analytics tools, offering APIs for submitting and reading standardized data, security features like SOC 2 Type II, SSO, and RBAC, and tools for AI‑assisted taxonomy management. The company serves agencies, retailers, CPG, healthcare, automotive, and other industries, emphasizing data consistency at scale.
image: https://www.claravine.com/og/index.png
layout: provider
modified: '2026-10-08'
name: Claravine
nav: Providers
network: true
overview: 'Claravine is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data-Standards, Marketing, and Software-as-a-Service.


  Claravine''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Claravine Plans Pricing
  plan_count: 3
  slug: claravine-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 7.5
    developer_ergonomics: 35.7
    discoverability: 50.0
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claravine Domain Security
  slug: claravine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Claravine Vulnerability Disclosure
  slug: claravine-vulnerability-disclosure
  summary_line: no policy recorded
slug: claravine
tags:
- Company
- Data-Standards
- Marketing
- Software-as-a-Service
website: https://www.claravine.com/
---
