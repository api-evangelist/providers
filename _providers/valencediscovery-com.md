---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/valencediscovery-com/llms/valencediscovery-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/valencediscovery-com-llms.txt
- group: other
  href: https://artifacts.apis.io/valencediscovery-com/a2a/valencediscovery-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/valencediscovery-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/valencediscovery-com/well-known/valencediscovery-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/valencediscovery-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/valencediscovery-com/hosts/valencediscovery-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/valencediscovery-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/valencediscovery-com/vendors/valencediscovery-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/valencediscovery-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.valencelabs.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mintlify
- group: company
  title: ''
  type: Blog
  url: https://www.valencelabs.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://tegx.mintlify.app/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.valencediscovery.com/
- group: auth
  href: https://artifacts.apis.io/valencediscovery-com/security/valencediscovery-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/valencediscovery-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.valencelabs.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://docs.valencediscovery.com/mcp
  - status: 200
    url: https://valencediscovery.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Valence Discovery provides a platform that enables researchers and clinicians to discover, access, and integrate biomedical data from diverse sources. The company focuses on aggregating genomic, proteomic, and clinical trial information to accelerate scientific insights and drug development. Backed by Techstars and part of the VC portfolio, Valence Discovery aims to streamline data workflows and support advanced analytics in the life sciences sector.
image: https://www.valencelabs.com/wp-content/uploads/2025/04/Website-preview_ver-2-scaled.png
layout: provider
modified: '2026-10-24'
name: Valence Discovery
nav: Providers
network: true
overview: 'Valence Discovery is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Life-Sciences, Platform, and Discovery.


  Valence Discovery''s developer surface includes engineering blog, getting-started guide, API reference, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Valencediscovery Com Domain Security
  slug: valencediscovery-com-domain-security
  summary_line: TLSv1.3
slug: valencediscovery-com
tags:
- Company
- Data
- Life-Sciences
- Platform
- Discovery
website: https://www.valencelabs.com/
---
