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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/brafinder-com/well-known/brafinder-com-brafinder-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brafinder-com-brafinder-security.txt
- group: auth
  href: https://artifacts.apis.io/brafinder-com/security/brafinder-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/brafinder-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/brafinder-com/conformance/brafinder-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brafinder-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brafinder-com/llms/brafinder-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brafinder-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/brafinder-com/well-known/brafinder-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brafinder-com-www-security.txt
- group: auth
  href: https://artifacts.apis.io/brafinder-com/well-known/brafinder-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brafinder-com-security.txt
- group: agent
  href: https://artifacts.apis.io/brafinder-com/well-known/brafinder-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brafinder-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brafinder-com/hosts/brafinder-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brafinder-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brafinder-com/vendors/brafinder-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brafinder-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brafinder.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brafinder.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.brafinder.com/guides
- group: auth
  href: https://artifacts.apis.io/brafinder-com/security/brafinder-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brafinder-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/brafinder-com/security/brafinder-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brafinder-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brafinder.com/
coverage:
  checked: '2026-11-03'
  detail: BraFinder provides a consumer‑facing size‑finder website with no public API.
  evidence:
  - status: 200
    url: https://www.brafinder.com/guides
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: BraFinder helps consumers find bras that truly fit by aggregating real fit data across 12 brands and 34 size translations. The service offers a free, no‑account‑required size‑finder, guides, and product recommendations, covering over 1,500 bras including large‑cup options often omitted by retailers. It aims to simplify bra shopping with accurate sizing and brand comparisons.
image: https://www.brafinder.com/opengraph-image?83733642a239165d
layout: provider
modified: '2026-11-02'
name: BraFinder
nav: Providers
network: true
overview: 'BraFinder is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include BraFinder, E-Commerce, Fashion, Size‑finder, and Consumer Tech.


  BraFinder''s developer surface includes documentation and 14 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brafinder Com Domain Security
  slug: brafinder-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brafinder Com Vulnerability Disclosure
  slug: brafinder-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brafinder-com
tags:
- BraFinder
- E-Commerce
- Fashion
- Size‑finder
- Consumer Tech
website: https://brafinder.com/
---
