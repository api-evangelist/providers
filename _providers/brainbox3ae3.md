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
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-04'
api_count: 2
apis:
- description: API reference for Brainboxes products and services
  name: Brainboxes API
  slug: brainboxes-api
- baseURL: http://bb400-xxxx:9000
  baseurl_source: declared
  description: The Io API from Brainbox3ae3 — 1 operation(s) for io.
  name: Brainbox3ae3 Io API
  slug: brainbox3ae3-io-api
artifact_total: 5
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/rules/brainbox3ae3-rules.yml
  title: ''
  type: Spectral
  url: rules/brainbox3ae3-rules.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/changelog/brainbox3ae3-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brainbox3ae3-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/security/brainbox3ae3-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/brainbox3ae3-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/conformance/brainbox3ae3-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brainbox3ae3-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/llms/brainbox3ae3-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brainbox3ae3-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/well-known/brainbox3ae3-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brainbox3ae3-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/well-known/brainbox3ae3-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brainbox3ae3-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/well-known/brainbox3ae3-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brainbox3ae3-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/hosts/brainbox3ae3-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainbox3ae3-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/vendors/brainbox3ae3-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainbox3ae3-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/packages/brainbox3ae3-packages.yml
  title: ''
  type: SDKs
  url: packages/brainbox3ae3-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/packages/brainbox3ae3-packages.yml
  title: ''
  type: Packages
  url: packages/brainbox3ae3-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.brainboxes.com/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brainboxes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/security/brainbox3ae3-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brainbox3ae3-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainbox3ae3/refs/heads/main/security/brainbox3ae3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainbox3ae3-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brainboxes.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brainboxes.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.brainboxes.com/api
- group: operate
  title: ''
  type: Support
  url: https://www.brainboxes.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brainboxes.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brainboxes.com/terms-and-conditions
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brainboxes.com/where-to-buy
- group: company
  title: ''
  type: Blog
  url: https://www.brainboxes.com/company/news
- group: start
  title: ''
  type: SignUp
  url: https://www.brainboxes.com/my-account
coverage:
  checked: '2026-10-03'
  detail: Docs are rendered with Docusaurus JavaScript, preventing easy spec discovery
  evidence:
  - status: 200
    url: https://docs.brainboxes.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Brainboxes Ltd is a UK‑based designer and manufacturer of rugged industrial‑grade data connectivity solutions, including Ethernet switches, serial device servers, edge controllers and remote I/O modules. Founded in 1984, the company provides lifetime support, in‑house design and testing, and serves sectors such as automation, transportation and manufacturing with hardware that withstands extreme conditions.
image: https://www.brainboxes.com/wp-content/uploads/2026/02/logo-social-card.png
layout: provider
modified: '2026-10-03'
name: Brainbox3ae3
nav: Providers
network: true
overview: 'Brainbox3ae3 publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Io API, and 1 more. Tagged areas include Company, Industrial, Connectivity, IoT, and Automation.


  The Brainbox3ae3 catalog on APIs.io includes 1 Spectral governance ruleset.


  Brainbox3ae3''s developer surface includes changelog, getting-started guide, documentation, API reference, support, pricing, engineering blog, and 18 more developer resources.'
random_paper: 9
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Brainbox3ae3 API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: brainbox3ae3-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 9.9
    developer_ergonomics: 42.9
    discoverability: 64.3
    operational_transparency: 31.6
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
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Brainbox3Ae3 Domain Security
  slug: brainbox3ae3-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Brainbox3Ae3 Vulnerability Disclosure
  slug: brainbox3ae3-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brainbox3ae3
tags:
- Company
- Industrial
- Connectivity
- IoT
- Automation
website: https://www.brainboxes.com
---
