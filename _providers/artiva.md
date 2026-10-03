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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/artiva/refs/heads/main/llms/artiva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artiva-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artiva/refs/heads/main/hosts/artiva-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artiva-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artiva/refs/heads/main/vendors/artiva-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artiva-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.artivabio.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artiva/refs/heads/main/security/artiva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artiva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.artivabio.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.artivabio.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.artivabio.com/careers/
- group: company
  title: ''
  type: News
  url: https://www.artivabio.com/news/
- group: company
  title: ''
  type: Investors
  url: https://investors.artivabio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.artivabio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.artivabio.com/terms-of-use/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on the company's domains.
  evidence:
  - status: 0
    url: https://api.artivabio.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Artiva Biotherapeutics is a clinical‑stage biotechnology company focused on developing natural killer (NK) cell‑based therapies for autoimmune diseases and cancers. Their lead candidate AlloNK® is an off‑the‑shelf, allogeneic NK cell therapy evaluated in combination with B‑cell‑targeted antibodies, aiming to provide safe, scalable treatments accessible to patients worldwide.
layout: provider
modified: '2026-09-26'
name: Artiva
nav: Providers
network: true
overview: 'Artiva is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Biopharma, Cell Therapy, Autoimmune Diseases, and Oncology.


  Artiva''s developer surface includes product news and 11 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artiva Domain Security
  slug: artiva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artiva
tags:
- Biotechnology
- Biopharma
- Cell Therapy
- Autoimmune Diseases
- Oncology
website: https://www.artivabio.com/
---
