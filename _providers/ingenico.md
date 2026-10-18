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
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ingenico/refs/heads/main/well-known/ingenico-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ingenico-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ingenico/refs/heads/main/hosts/ingenico-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ingenico-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ingenico/refs/heads/main/vendors/ingenico-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ingenico-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.ingenico.com/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ingenico.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://ingenico.com/us-en/newsroom
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ingenico.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.ingenico.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ingenico/refs/heads/main/security/ingenico-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ingenico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ingenico.com
coverage:
  checked: '2026-10-13'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on api.ingenico.com despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.ingenico.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Ingenico is a global leader in seamless payment solutions, offering a wide range of point‑of‑sale terminals, digital payment services, and integrated commerce platforms. The company serves merchants across retail, hospitality, transportation, and other industries, enabling secure, fast, and flexible transactions both in‑store and online. With a focus on innovation, Ingenio supports emerging payment methods, tokenization, and omnichannel experiences, backed by robust security and compliance frameworks.
image: https://ingenico.com/themes/custom/ingenico/build/images/share/ingenico_og_default.webp
layout: provider
modified: '2026-10-13'
name: Ingenico
nav: Providers
network: true
overview: 'Ingenico is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Point-of-Sale, and E-Commerce.


  Ingenico''s developer surface includes documentation and 9 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ingenico Domain Security
  slug: ingenico-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ingenico
tags:
- Company
- Payments
- Fintech
- Point-of-Sale
- E-Commerce
- Security
website: https://ingenico.com
---
