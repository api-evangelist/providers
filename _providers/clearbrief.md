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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Clearbrief provides a developer API for its legal AI platform, documented in HTML guides.
  name: Clearbrief API
  slug: clearbrief-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/clearbrief/hosts/clearbrief-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearbrief-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://clearbrief.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://clearbrief.com/guides
- group: auth
  href: https://artifacts.apis.io/clearbrief/security/clearbrief-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearbrief-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearbrief.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://clearbrief.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clearbrief.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clearbrief.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://clearbrief.com/contact
- group: company
  title: ''
  type: Blog
  url: https://clearbrief.com/blog
coverage:
  checked: '2026-10-28'
  detail: Clearbrief provides HTML guides but no machine‑readable OpenAPI, GraphQL or AsyncAPI specifications.
  evidence:
  - status: 200
    url: https://clearbrief.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Clearbrief provides a legal AI platform that automates citation checking and fact verification within Microsoft Word documents. The service builds dynamic tables of authorities, exhibits, timelines, and fact sections, ensuring that briefs and motions are fully sourced and free of hallucinations. Clearbrief offers hyperlinked briefs, instant summaries of large document collections, and integrates with Microsoft Office to streamline legal drafting and review processes.
image: https://clearbrief.com/images/logos/icon.webp
layout: provider
modified: '2026-10-28'
name: Clearbrief
nav: Providers
network: true
overview: 'Clearbrief is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LegalTech, AI, DocumentAutomation, and CitationChecking.


  Clearbrief''s developer surface includes documentation, pricing, engineering blog, and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clearbrief Domain Security
  slug: clearbrief-domain-security
  summary_line: TLSv1.3 · HSTS
slug: clearbrief
tags:
- Company
- LegalTech
- AI
- DocumentAutomation
- CitationChecking
- MicrosoftWord
website: https://clearbrief.com/
---
