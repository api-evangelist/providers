---
agent_readiness:
  band: human-only
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Safe Software's FME platform, enabling data integration and automation.
  name: FME Platform API
  slug: fme-platform-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/safe-software/refs/heads/main/well-known/safe-software-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/safe-software-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/safe-software/refs/heads/main/well-known/safe-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/safe-software-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.safe.com/site/terms
- group: auth
  title: ''
  type: Compliance
  url: https://trust.safe.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/safe-software/refs/heads/main/conformance/safe-software-conformance.yml
  title: ''
  type: Conformance
  url: conformance/safe-software-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/safe-software/refs/heads/main/llms/safe-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/safe-software-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/safe-software/refs/heads/main/hosts/safe-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/safe-software-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/safe-software/refs/heads/main/vendors/safe-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/safe-software-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.safe.com/
- group: start
  title: ''
  type: SignUp
  url: https://community.safe.com/member/register
- group: auth
  title: ''
  type: Security
  url: https://fme.safe.com/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/safe-software/refs/heads/main/security/safe-software-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/safe-software-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/safe-software/refs/heads/main/security/safe-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/safe-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.safe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fme.safe.com
- group: docs
  title: ''
  type: Documentation
  url: https://fme.safe.com/get-started/
- group: docs
  title: ''
  type: APIReference
  url: https://fme.safe.com/platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://fme.safe.com/get-started/
- group: operate
  title: ''
  type: Support
  url: https://support.safe.com/hc/en-us/p/Support
- group: company
  title: ''
  type: Blog
  url: https://fme.safe.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://fme.safe.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.safe.com/legal/privacy-policy/
coverage:
  checked: '2026-10-03'
  detail: Developer portal pages render via JavaScript, preventing retrieval of a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://fme.safe.com/platform/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Safe Software builds FME, a powerful data integration platform that connects any data source to any destination, enabling organizations to automate complex workflows, perform spatial analytics, and leverage AI. With over 25,000 customers worldwide, Safe Software helps turn data into actionable insights across industries such as transportation, utilities, government, and more.
image: https://cdn.safe.com/wp-content/uploads/2023/03/18102711/safe-social.jpg
layout: provider
modified: '2026-10-03'
name: Safe Software
nav: Providers
network: true
overview: 'Safe Software publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, Spatial Analytics, Artificial Intelligence, and Enterprise.


  Safe Software''s developer surface includes signup flow, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 64.3
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: derived
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
    score: 21.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Safe Software Domain Security
  slug: safe-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Safe Software Trust Center
  slug: safe-software-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: safe-software
tags:
- Company
- Data Integration
- Spatial Analytics
- Artificial Intelligence
- Enterprise
website: https://www.safe.com
---
