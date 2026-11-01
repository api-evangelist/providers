---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/veolia/llms/veolia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veolia-llms.txt
- group: other
  href: https://artifacts.apis.io/veolia/hosts/veolia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/veolia-hosts.yml
- group: build
  href: https://artifacts.apis.io/veolia/integrations/veolia-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/veolia-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/veolia/vendors/veolia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/veolia-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.veolia.com/fr/newsroom/actualites
- group: auth
  href: https://artifacts.apis.io/veolia/security/veolia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veolia-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veolia-environnement
- group: company
  title: ''
  type: Website
  url: https://www.veolia.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://www.veolia.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.veolia.com/en/rss-press-releases
- group: company
  title: ''
  type: Blog
  url: https://www.veolia.com/fr/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veolia.com/en/privacy-policy
coverage:
  checked: '2026-10-20'
  detail: Veolia publishes corporate, press and careers sites but no developer portal or public API; api.veolia.com returns 404 at its root and no contract was found on any of its six probed hosts.
  evidence:
  - status: 404
    url: https://api.veolia.com/
  - status: 200
    url: https://www.veolia.com/
  reason: no-developer-program
  state: none
created: '2026-05-05'
description: A French multinational corporation and the global leader in environmental services including water management, waste management, and energy services. Operates in nearly 50 countries providing solutions for water treatment, waste recycling, and pollution remediation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veolia.png
layout: provider
modified: '2026-10-20'
name: Veolia
nav: Providers
network: true
overview: 'Veolia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Waste Management, Water Treatment, Environmental Services, Energy, and Recycling.


  Veolia''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 24.0
    catalog_earned_first_party: 0.0
    catalog_gap: 91.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  previous_composite: 7.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/veolia/veolia-2026-06-20T200919.png
security:
- kind: domain-security
  name: Veolia Domain Security
  slug: veolia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: veolia
tags:
- Waste Management
- Water Treatment
- Environmental Services
- Energy
- Recycling
website: https://www.veolia.com/
---
