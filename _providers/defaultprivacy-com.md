---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read-only public API for searching privacy tools and browsing categories.
  name: Default Privacy API
  slug: default-privacy-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://github.com/default-privacy/DefaultPrivacy.com/security/policy
- group: design
  href: https://artifacts.apis.io/defaultprivacy-com/conformance/defaultprivacy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/defaultprivacy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/defaultprivacy-com/llms/defaultprivacy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defaultprivacy-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/defaultprivacy-com/well-known/defaultprivacy-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/defaultprivacy-com-security.txt
- group: agent
  href: https://artifacts.apis.io/defaultprivacy-com/well-known/defaultprivacy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/defaultprivacy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/defaultprivacy-com/hosts/defaultprivacy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/defaultprivacy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/defaultprivacy-com/vendors/defaultprivacy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/defaultprivacy-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://defaultprivacy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://defaultprivacy.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://defaultprivacy.com/guides
- group: auth
  href: https://artifacts.apis.io/defaultprivacy-com/security/defaultprivacy-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/defaultprivacy-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/defaultprivacy-com/security/defaultprivacy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defaultprivacy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://defaultprivacy.com/
created: '2026-11-05'
description: Default Privacy is an independent, vetted directory of privacy tools that offers free tools to check your exposure, a privacy glossary, and practical guides. It curates over 860 privacy tools with no paid placements, providing users with unbiased recommendations. The site also features a privacy score, stacks, and field guides to help individuals protect their digital lives. Its mission is to empower users with transparent, open-source resources for digital privacy.
image: https://defaultprivacy.com/og.png
layout: provider
modified: '2026-11-05'
name: Default Privacy
nav: Providers
network: true
overview: 'Default Privacy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Directory, Privacy Tools, Guides, Stacks, and Free Tools.


  Default Privacy''s developer surface includes API reference and 12 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Defaultprivacy Com Domain Security
  slug: defaultprivacy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Defaultprivacy Com Vulnerability Disclosure
  slug: defaultprivacy-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: defaultprivacy-com
tags:
- Directory
- Privacy Tools
- Guides
- Stacks
- Free Tools
- Open Source
website: https://defaultprivacy.com/
---
