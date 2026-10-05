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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/americaninjuryattorneygroup/refs/heads/main/llms/americaninjuryattorneygroup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/americaninjuryattorneygroup-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/americaninjuryattorneygroup/refs/heads/main/hosts/americaninjuryattorneygroup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/americaninjuryattorneygroup-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.theinjurygroup.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.theinjurygroup.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/americaninjuryattorneygroup/refs/heads/main/security/americaninjuryattorneygroup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/americaninjuryattorneygroup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.theinjurygroup.com
coverage:
  checked: 2026-09-24
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's website or API host.
  evidence:
  - status: 0
    url: https://api.theinjurygroup.com/openapi.json
  - status: 0
    url: https://api.theinjurygroup.com/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: American Injury Attorney Group is a personal injury law firm serving New York and New Jersey, offering legal representation for car accidents, truck accidents, workers compensation, rideshare incidents, bicycle accidents, construction accidents, pedestrian accidents, motorcycle injuries, medical malpractice, wrongful death, premises liability, brain injuries, birth injuries, and product liability claims. The firm provides free 24/7 consultations and aims to help injured individuals obtain compensation.
image: https://www.theinjurygroup.com/wp-content/uploads/2025/01/margarita_small-v3.png
layout: provider
modified: '2026-09-24'
name: Americaninjuryattorneygroup
nav: Providers
network: true
overview: Americaninjuryattorneygroup is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Law, Personal Injury, New York, and New Jersey.
random_paper: 0
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 8.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Americaninjuryattorneygroup Domain Security
  slug: americaninjuryattorneygroup-domain-security
  summary_line: TLSv1.3 · DMARC
slug: americaninjuryattorneygroup
tags:
- Company
- Law
- Personal Injury
- New York
- New Jersey
website: https://www.theinjurygroup.com
---
