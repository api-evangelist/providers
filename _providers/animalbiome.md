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
api_count: 1
apis:
- description: GraphQL API for AnimalBiome services
  name: AnimalBiome API
  slug: animalbiome-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/animalbiome/refs/heads/main/llms/animalbiome-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/animalbiome-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/animalbiome/refs/heads/main/well-known/animalbiome-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/animalbiome-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/animalbiome/refs/heads/main/hosts/animalbiome-hosts.yml
  title: ''
  type: Hosts
  url: hosts/animalbiome-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/animalbiome/refs/heads/main/vendors/animalbiome-vendors.yml
  title: ''
  type: Vendors
  url: vendors/animalbiome-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.animalbiome.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.animalbiome.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.animalbiome.com/pages/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/animalbiome/refs/heads/main/security/animalbiome-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/animalbiome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.animalbiome.com/
coverage:
  checked: 2026-09-24
  detail: API documentation pages return HTML shells for typical spec URLs, no machine‑readable OpenAPI found.
  evidence:
  - status: 200
    url: https://app.animalbiome.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: AnimalBiome provides microbiome-based health solutions for pets, offering gut health supplements, microbiome testing kits, and probiotic products. Their platform educates owners on gut health, supports veterinarians, and leverages scientific research to improve animal wellbeing through targeted microbiome interventions.
layout: provider
modified: '2026-09-24'
name: AnimalBiome
nav: Providers
network: true
overview: AnimalBiome publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Microbiome, Pet Health, Veterinary Products, Probiotics, and Gut Health.
random_paper: 6
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 71.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Animalbiome Domain Security
  slug: animalbiome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: animalbiome
tags:
- Microbiome
- Pet Health
- Veterinary Products
- Probiotics
- Gut Health
website: https://www.animalbiome.com/
---
