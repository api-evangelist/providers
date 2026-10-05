---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
  score: 4.5
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augustinus-bader/refs/heads/main/well-known/augustinus-bader-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/augustinus-bader-clarity-security.txt
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/augustinus-bader/refs/heads/main/llms/augustinus-bader-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/augustinus-bader-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augustinus-bader/refs/heads/main/well-known/augustinus-bader-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/augustinus-bader-support-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/augustinus-bader/refs/heads/main/well-known/augustinus-bader-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/augustinus-bader-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augustinus-bader/refs/heads/main/hosts/augustinus-bader-hosts.yml
  title: ''
  type: Hosts
  url: hosts/augustinus-bader-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augustinus-bader/refs/heads/main/vendors/augustinus-bader-vendors.yml
  title: ''
  type: Vendors
  url: vendors/augustinus-bader-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://augustinusbader.com/en-uk/pages/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.augustinusbader.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://augustinusbader.com/en-uk/pages/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augustinus-bader/refs/heads/main/security/augustinus-bader-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/augustinus-bader-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augustinus-bader/refs/heads/main/security/augustinus-bader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augustinus-bader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://augustinusbader.com/en-uk
coverage:
  checked: 2026-09-26
  detail: GraphQL endpoint returns schema but cannot verify ownership as it appears to be a generic Shopify API.
  evidence:
  - status: 200
    url: https://augustinusbader.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Augustinus Bader is a luxury skincare brand founded by Dr. Augustinus Bader, a German stem cell researcher. The company combines scientific research with premium ingredients to create anti‑aging products such as the Rich Cream, The Cream, and The Elixir. Their website offers detailed product information, brand story, and a portal for professional partners. The brand is known for its advanced TFC8® technology and collaborations with high‑end fashion and hospitality partners.
layout: provider
modified: '2026-09-26'
name: Augustinus Bader
nav: Providers
network: true
overview: 'Augustinus Bader is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Skincare, Luxury, Beauty, and Anti-Aging.


  Augustinus Bader''s developer surface includes support and 12 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Augustinus Bader Domain Security
  slug: augustinus-bader-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Augustinus Bader Vulnerability Disclosure
  slug: augustinus-bader-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: augustinus-bader
tags:
- Company
- Skincare
- Luxury
- Beauty
- Anti-Aging
website: https://augustinusbader.com/en-uk
---
