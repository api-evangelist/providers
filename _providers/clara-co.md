---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/clara-co/conformance/clara-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clara-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clara-co/llms/clara-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clara-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/clara-co/well-known/clara-co-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clara-co-help-security.txt
- group: agent
  href: https://artifacts.apis.io/clara-co/well-known/clara-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clara-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/clara-co/hosts/clara-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clara-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/clara-co/vendors/clara-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clara-co-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.clara.co/
- group: auth
  href: https://artifacts.apis.io/clara-co/security/clara-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clara-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clara.co
- group: commercial
  title: ''
  type: Pricing
  url: https://clara.co/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://clara.co/get-started/enquire-now
- group: operate
  title: ''
  type: Support
  url: https://clara.co/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clara.co/info/terms-and-privacy-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clara.co/info/terms-and-privacy-policy
coverage:
  checked: '2026-10-25'
  detail: The Clara website provides no machine‑readable API specification despite having a developer portal link.
  evidence:
  - status: 200
    url: https://clara.co
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Clara provides seamless digital formation services for companies, offering incorporation, equity management, data room, and visa solutions across multiple jurisdictions. The platform serves startups, investors, SMEs, and legal advisors with tools for company formation, equity management, data room access, and specialized visa programs such as ADGM, DIFC, BVI, Cayman, and Golden Visa. Clara also offers pricing transparency, partner integrations, and a knowledge hub to help businesses navigate legal and financial processes efficiently.
layout: provider
modified: '2026-10-25'
name: Clara
nav: Providers
network: true
overview: 'Clara is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, LegalTech, Incorporation, and EquityManagement.


  Clara''s developer surface includes documentation, pricing, getting-started guide, support, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 44.6
    operational_transparency: 10.5
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
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clara Co Domain Security
  slug: clara-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clara-co
tags:
- Company
- FinTech
- LegalTech
- Incorporation
- EquityManagement
website: https://clara.co
---
