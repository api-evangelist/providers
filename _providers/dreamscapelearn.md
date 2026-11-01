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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dreamscapelearn/llms/dreamscapelearn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreamscapelearn-llms.txt
- group: other
  href: https://artifacts.apis.io/dreamscapelearn/hosts/dreamscapelearn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreamscapelearn-hosts.yml
- group: other
  href: https://artifacts.apis.io/dreamscapelearn/vendors/dreamscapelearn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dreamscapelearn-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dreamscapelearn.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/dreamscapelearn/security/dreamscapelearn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreamscapelearn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dreamscapelearn.com
coverage:
  checked: '2026-10-24'
  detail: The provider's website does not expose any developer or API documentation.
  evidence:
  - status: 200
    url: https://www.dreamscapelearn.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Dreamscape Learn provides immersive, cinematic learning experiences that transport students into virtual worlds where they become scientists, explorers, and investigators. By integrating VR curricula aligned to educational standards, the platform enhances engagement, critical thinking, and retention across K‑12 and higher education. Partner institutions report measurable gains in performance and persistence, supported by research from Arizona State University.
image: https://static.wixstatic.com/media/761417_eab5fd8068df4e3aacdad8509358f971~mv2.jpg/v1/fill/w_2500,h_1667,al_c/761417_eab5fd8068df4e3aacdad8509358f971~mv2.jpg
layout: provider
modified: '2026-10-24'
name: Dreamscapelearn
nav: Providers
network: true
overview: Dreamscapelearn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, VirtualReality, ImmersiveLearning, K-12, and HigherEducation.
random_paper: 15
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dreamscapelearn Domain Security
  slug: dreamscapelearn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dreamscapelearn
tags:
- Education
- VirtualReality
- ImmersiveLearning
- K-12
- HigherEducation
- Company
website: https://www.dreamscapelearn.com
---
