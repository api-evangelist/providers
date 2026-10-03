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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Artax Biopharma provides data on its pipeline and progress via a developer portal.
  name: Artax Biopharma API
  slug: artax-biopharma-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artax-biopharma/refs/heads/main/hosts/artax-biopharma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artax-biopharma-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://artaxbiopharma.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artax-biopharma/refs/heads/main/security/artax-biopharma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artax-biopharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artaxbiopharma.com
- group: docs
  title: ''
  type: Documentation
  url: https://artaxbiopharma.com/our-pipeline-and-progress/
- group: company
  title: ''
  type: About
  url: https://artaxbiopharma.com/about-artax/
- group: other
  title: ''
  type: Resources
  url: https://artaxbiopharma.com/resources/
- group: operate
  title: ''
  type: PressReleases
  url: https://artaxbiopharma.com/press-releases/
- group: operate
  title: ''
  type: Contact
  url: https://artaxbiopharma.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artaxbiopharma.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artaxbiopharma.com/privacy-policy/
coverage:
  checked: 2026-09-26
  detail: Documentation pages return 403 errors, preventing machine-readable access.
  evidence:
  - status: 403
    url: https://artaxbiopharma.com/our-pipeline-and-progress/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Artax Biopharma is a Phase 2 clinical-stage biotechnology company dedicated to developing safe and effective treatments for autoimmune diseases. Their approach modulates T cell activation through Signal 1, aiming to prevent self-activation without causing immune suppression. The company has a pipeline of first‑in‑class Nck modulator candidates, with lead program AX‑158 showing promising biomarker and clinical data.
image: https://artaxbiopharma.com/wp-content/uploads/2024/06/Default-Social-Image.jpg
layout: provider
modified: '2026-09-26'
name: Artax Biopharma
nav: Providers
network: true
overview: 'Artax Biopharma publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Clinical Stage, Autoimmune, Immunomodulation, and Nck-modulators.


  Artax Biopharma''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artax Biopharma Domain Security
  slug: artax-biopharma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: artax-biopharma
tags:
- Biotechnology
- Clinical Stage
- Autoimmune
- Immunomodulation
- Nck-modulators
website: https://artaxbiopharma.com
---
