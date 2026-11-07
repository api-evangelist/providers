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
  href: https://artifacts.apis.io/diplometre-fr/security/diplometre-fr-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/diplometre-fr-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/diplometre-fr/llms/diplometre-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diplometre-fr-llms.txt
- group: auth
  href: https://artifacts.apis.io/diplometre-fr/well-known/diplometre-fr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/diplometre-fr-security.txt
- group: agent
  href: https://artifacts.apis.io/diplometre-fr/well-known/diplometre-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/diplometre-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/diplometre-fr/hosts/diplometre-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diplometre-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/diplometre-fr/vendors/diplometre-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diplometre-fr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/diplometre-fr/security/diplometre-fr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/diplometre-fr-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/diplometre-fr/security/diplometre-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diplometre-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diplometre.fr/
- group: other
  title: ''
  type: Description
  url: https://diplometre.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://diplometre.fr/api-et-donnees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://diplometre.fr/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diplometre.fr/confidentialite
- group: company
  title: ''
  type: Blog
  url: https://diplometre.fr/blog
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite probing known API hosts.
  evidence:
  - status: 404
    url: https://diplometre.fr/api/openapi.json
  - status: 404
    url: https://api.diplometre.fr/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: 'diplometre-fr is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://diplometre.fr/opengraph-image.png?opengraph-image.0339ycb6_-q0a.png
layout: provider
modified: '2026-11-05'
name: Diplomètre
nav: Providers
network: true
overview: 'Diplomètre is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Orientation, and Parents.


  Diplomètre''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 30.4
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Diplometre Fr Domain Security
  slug: diplometre-fr-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Diplometre Fr Vulnerability Disclosure
  slug: diplometre-fr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: diplometre-fr
tags:
- Data
- Orientation
- Parents
website: https://diplometre.fr/
---
