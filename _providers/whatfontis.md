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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/whatfontis/refs/heads/main/hosts/whatfontis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whatfontis-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/whatfontis/refs/heads/main/vendors/whatfontis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whatfontis-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whatfontis/refs/heads/main/packages/whatfontis-packages.yml
  title: ''
  type: SDKs
  url: packages/whatfontis-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whatfontis/refs/heads/main/packages/whatfontis-packages.yml
  title: ''
  type: Packages
  url: packages/whatfontis-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whatfontis.com/terms.html
- group: start
  title: ''
  type: GettingStarted
  url: https://whatfontis.com/getting-started.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whatfontis/refs/heads/main/security/whatfontis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whatfontis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whatfontis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.whatfontis.com/API-identify-fonts-from-image.html
coverage:
  checked: '2026-10-08'
  detail: The provider only offers HTML documentation with no machine‑readable OpenAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://www.whatfontis.com/API-identify-fonts-from-image.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: WhatFontIS provides an AI‑powered font identification service that lets users upload an image and receive matching typefaces from a database of over 1.2 million fonts, both commercial and free. The platform offers tools such as a font analyzer, similar‑font suggestions, font pairing generator, and web‑font generation, targeting designers, developers, and typographers. Users can sign up for free or upgrade to a PRO membership for additional features and higher usage limits.
layout: provider
modified: '2026-10-08'
name: WhatFontIS
nav: Providers
network: true
overview: 'WhatFontIS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Font Identification, Artificial Intelligence, Design Tools, and Typography.


  WhatFontIS''s developer surface includes getting-started guide, documentation, and 7 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Whatfontis Domain Security
  slug: whatfontis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: whatfontis
tags:
- Company
- Font Identification
- Artificial Intelligence
- Design Tools
- Typography
website: https://whatfontis.com/
---
