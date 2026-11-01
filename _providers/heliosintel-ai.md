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
- group: other
  href: https://artifacts.apis.io/heliosintel-ai/hosts/heliosintel-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/heliosintel-ai-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://heliosintel.ai/newsroom/what-is-a-policy-intelligence-platform
- group: auth
  href: https://artifacts.apis.io/heliosintel-ai/security/heliosintel-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heliosintel-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://heliosintel.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.heliosintel.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.heliosintel.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.heliosintel.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HeliosIntel
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heliosintel.ai/legal-terms/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heliosintel.ai/legal-terms/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Developer portal at https://dev.heliosintel.ai/ serves a JavaScript‑rendered SPA with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://dev.heliosintel.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Helios provides sovereign AI solutions for critical government missions, offering policy monitoring, decision intelligence, and customizable deployment platforms. Their Proxi applications enable agencies to track legislation, regulations, and procurement signals, delivering sourced answers and briefing tools for modern governance. Helios focuses on secure, mission‑critical AI deployments for the United States.
image: https://framerusercontent.com/assets/6WyFFjMLdlO1paTOxy6CoSGqYYo.jpg
layout: provider
modified: '2026-10-29'
name: Helios
nav: Providers
network: true
overview: 'Helios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Sovereign, Government, and Policy.


  Helios'' developer surface includes documentation, API reference, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Heliosintel Ai Domain Security
  slug: heliosintel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: heliosintel-ai
tags:
- Company
- AI
- Sovereign
- Government
- Policy
website: https://heliosintel.ai/
---
