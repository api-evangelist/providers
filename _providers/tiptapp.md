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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tiptapp/refs/heads/main/conformance/tiptapp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tiptapp-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tiptapp/refs/heads/main/llms/tiptapp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tiptapp-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tiptapp/refs/heads/main/well-known/tiptapp-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tiptapp-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tiptapp/refs/heads/main/well-known/tiptapp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tiptapp-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tiptapp/refs/heads/main/hosts/tiptapp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tiptapp-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tiptapp/refs/heads/main/vendors/tiptapp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tiptapp-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tiptapp/refs/heads/main/packages/tiptapp-packages.yml
  title: ''
  type: SDKs
  url: packages/tiptapp-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tiptapp/refs/heads/main/packages/tiptapp-packages.yml
  title: ''
  type: Packages
  url: packages/tiptapp-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tiptapp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tiptapp/refs/heads/main/security/tiptapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tiptapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tiptapp.com/
- group: company
  title: ''
  type: Blog
  url: https://tiptapp.com/en-gb/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.tiptapp.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tiptapp.com/en-gb/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tiptapp.com/en-gb/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://help.tiptapp.com/en/
coverage:
  checked: '2026-10-15'
  detail: Documentation at https://help.tiptapp.com/en/ provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://help.tiptapp.com/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Tiptapp provides an on-demand platform for moving, delivery, and recycling services across multiple European markets. Users can schedule moves, request shopping assistance, arrange item removal and recycling, and even give away items through the app. The service emphasizes safety, sustainability, and circular economy principles, supporting cities and promoting reuse of goods.
image: https://a.storyblok.com/f/198708/720x378/0131e135cb/default-og-image.jpg/m/1200x0
layout: provider
modified: '2026-10-15'
name: Tiptapp
nav: Providers
network: true
overview: 'Tiptapp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Moving, Delivery, Recycling, and Sustainability.


  Tiptapp''s developer surface includes engineering blog, documentation, support, and 13 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 55.4
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tiptapp Domain Security
  slug: tiptapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tiptapp
tags:
- Company
- Moving
- Delivery
- Recycling
- Sustainability
website: https://tiptapp.com/
---
