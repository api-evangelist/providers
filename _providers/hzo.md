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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://hzo.com/
- group: company
  title: ''
  type: Blog
  url: https://hzo.com/blog
- group: operate
  title: ''
  type: Support
  url: https://hzo.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hzo.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hzo.com/terms
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hzo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hzo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hzo-security.txt
- group: auth
  title: ''
  type: Security
  url: https://hzo.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hzo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hzo-domain-security.yml
coverage:
  checked: '2026-08-22'
  detail: HZO is a physical Parylene / thin-film conformal-coating manufacturer and contract coating service; hzo.com serves marketing, blog, and legal pages plus an llms.txt and security.txt but exposes no developer portal, API host, or machine-readable contract.
  evidence:
  - status: 404
    url: https://hzo.com/openapi.json
  - status: 200
    url: https://hzo.com/llms.txt
  - status: 200
    url: https://hzo.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'HZO is a protective coating company specializing in Parylene and thin-film conformal coatings that safeguard electronics from moisture, humidity, salt fog, corrosion, and harsh chemicals. Founded in Salt Lake City and now headquartered in Raleigh, North Carolina, HZO delivers turnkey coating services and manufacturing solutions across consumer electronics, automotive and mobility, industrial, medical device, IoT, and battery markets, with coating facilities and centers of excellence in the United States, Hungary, China, and Vietnam. HZO is a physical-materials and contract-manufacturing business ("Protection from the Inside Out") rather than a software vendor: it publishes no public developer program, API, or machine-readable API contract. This profile records the public web hygiene surface it does serve — an llms.txt discovery file, an RFC 9116 security.txt, and domain security posture.'
image: https://hzo.com/hs-fs/hubfs/hzo-logo-1.png
layout: provider
modified: '2026-08-22'
name: HZO
nav: Providers
network: true
overview: 'HZO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electronics, Manufacturing, Coatings, and Parylene.


  HZO''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Hzo Domain Security
  slug: hzo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hzo Vulnerability Disclosure
  slug: hzo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hzo
tags:
- Company
- Electronics
- Manufacturing
- Coatings
- Parylene
- Materials Science
- Conformal Coating
- Hardware
website: https://hzo.com/
---
