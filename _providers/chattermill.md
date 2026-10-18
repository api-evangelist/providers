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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Customer feedback analysis API referenced in documentation
  name: Chattermill API
  slug: chattermill-api
artifact_total: 4
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chattermill.com/en/articles/16973573-getting-started-with-lyra-agent
- group: auth
  title: ''
  type: Compliance
  url: https://trust.chattermill.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chattermill/refs/heads/main/conformance/chattermill-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chattermill-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chattermill/refs/heads/main/llms/chattermill-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chattermill-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chattermill/refs/heads/main/well-known/chattermill-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chattermill-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chattermill/refs/heads/main/well-known/chattermill-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chattermill-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chattermill/refs/heads/main/hosts/chattermill-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chattermill-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chattermill/refs/heads/main/vendors/chattermill-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chattermill-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chattermill.com/legal/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://chattermill.com/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chattermill.com/legal/privacy-cookie-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chattermill/refs/heads/main/security/chattermill-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chattermill-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chattermill/refs/heads/main/security/chattermill-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chattermill-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chattermill/refs/heads/main/security/chattermill-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chattermill-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chattermill.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chattermill.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.chattermill.com/?version=latest
- group: company
  title: ''
  type: Blog
  url: https://chattermill.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://chattermill.com/pricing
coverage:
  checked: '2026-10-08'
  detail: Documentation at https://docs.chattermill.com/en/ provides HTML only and no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.chattermill.com/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chattermill provides AI‑native Voice of Customer and feedback analysis software that unifies feedback from every source, applies Lyra AI to generate precise insights, and offers automation, reporting, and security features for enterprises seeking to turn customer data into actionable business outcomes.
image: https://cdn.prod.website-files.com/6a36b907304a6968500f05b9/6a7f2c6579555c6be68523f6_f9ab554c6ff526118cdf01238894ccb6_OpenGraph.png
layout: provider
modified: '2026-10-08'
name: Chattermill
nav: Providers
network: true
overview: 'Chattermill is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Voice of Customer, Feedback Analysis, and Enterprise.


  Chattermill''s developer surface includes getting-started guide, documentation, API reference, engineering blog, pricing, and 14 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 64.3
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chattermill Domain Security
  slug: chattermill-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chattermill Vulnerability Disclosure
  slug: chattermill-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Chattermill Trust Center
  slug: chattermill-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: chattermill
tags:
- Company
- Artificial Intelligence
- Voice of Customer
- Feedback Analysis
- Enterprise
website: https://chattermill.com
---
