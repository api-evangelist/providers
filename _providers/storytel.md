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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Storytel provides audiobook and e‑book streaming services, but no public developer documentation or API contracts were found.
  name: Storytel API
  slug: storytel-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/storytel/refs/heads/main/well-known/storytel-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/storytel-www-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/storytel/refs/heads/main/security/storytel-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/storytel-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/storytel/refs/heads/main/llms/storytel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/storytel-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/storytel/refs/heads/main/well-known/storytel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/storytel-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/storytel/refs/heads/main/well-known/storytel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/storytel-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/storytel/refs/heads/main/hosts/storytel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/storytel-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/storytel/refs/heads/main/vendors/storytel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/storytel-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storytel.com/pl/pl/documents/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.storytel.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.storytel.com/pl/pl/documents/privacy-policy?request_locale=pl
- group: start
  title: ''
  type: Login
  url: https://www.storytel.com/pl/pl/login
- group: company
  title: ''
  type: Blog
  url: https://blog.storytel.com/pl
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Storytel
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/storytel/refs/heads/main/security/storytel-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/storytel-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/storytel/refs/heads/main/security/storytel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/storytel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://storytel.com/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discovered at api.storytel.com or other hosts.
  evidence:
  - status: 0
    url: https://api.storytel.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Storytel is a leading subscription-based audiobook and e‑book streaming service, founded in Sweden. It offers a vast library of titles across multiple languages, allowing users to listen to or read on mobile apps, web, and compatible devices. Storytel operates in dozens of countries, providing personalized recommendations, offline listening, and family plans. The platform focuses on delivering high‑quality audio productions and exclusive content, catering to readers and listeners worldwide.
image: https://www.storytel.com/assets/images/open-graph-logo-storytel.png
layout: provider
modified: '2026-10-14'
name: Storytel
nav: Providers
network: true
overview: 'Storytel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audiobook, eBook, Subscription, and Streaming.


  Storytel''s developer surface includes support, engineering blog, and 14 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Storytel Domain Security
  slug: storytel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Storytel Vulnerability Disclosure
  slug: storytel-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: storytel
tags:
- Company
- Audiobook
- eBook
- Subscription
- Streaming
website: https://storytel.com/
---
