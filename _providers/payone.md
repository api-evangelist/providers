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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/payone/well-known/payone-payone-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payone-payone-security.txt
- group: operate
  href: https://artifacts.apis.io/payone/changelog/payone-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/payone-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://worldline.com/en/home/responsible-disclosure-program.html
- group: agent
  href: https://artifacts.apis.io/payone/llms/payone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/payone-llms.txt
- group: auth
  href: https://artifacts.apis.io/payone/well-known/payone-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payone-www-security.txt
- group: auth
  href: https://artifacts.apis.io/payone/well-known/payone-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payone-security.txt
- group: agent
  href: https://artifacts.apis.io/payone/well-known/payone-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/payone-well-known.yml
- group: other
  href: https://artifacts.apis.io/payone/hosts/payone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/payone-hosts.yml
- group: other
  href: https://artifacts.apis.io/payone/vendors/payone-vendors.yml
  title: ''
  type: Vendors
  url: vendors/payone-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.payone.com/DE-en/terms-and-conditions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PAYONE-GmbH
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.payone.com/en/index
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.payone.com/en/about/release-notes
- group: docs
  title: ''
  type: APIReference
  url: https://developer.payone.com/en/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://developer.payone.com/
- group: auth
  href: https://artifacts.apis.io/payone/security/payone-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/payone-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/payone/security/payone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/payone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payone.com/
coverage:
  checked: '2026-10-27'
  detail: The provider's website offers HTML documentation but no discoverable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.payone.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: PAYONE provides payment solutions for various industries, offering card readers, apps, and e‑commerce integrations. Their platform supports retail, gastronomy, healthcare, hospitality, and online shops, enabling merchants to accept cashless payments both in‑store and on‑the‑go. PAYONE emphasizes comprehensive packages, including hardware, software, and support services, tailored to large and small businesses alike.
image: https://www.payone.com/payone-logo.png
layout: provider
modified: '2026-10-27'
name: PAYONE
nav: Providers
network: true
overview: 'PAYONE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, E‑Commerce, Point‑of‑Sale, Card Payments, and Retail.


  PAYONE''s developer surface includes changelog, API reference, documentation, and 15 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Payone Domain Security
  slug: payone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Payone Vulnerability Disclosure
  slug: payone-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: payone
tags:
- Payments
- E‑Commerce
- Point‑of‑Sale
- Card Payments
- Retail
- Hospitality
website: https://payone.com/
---
