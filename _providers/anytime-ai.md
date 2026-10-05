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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.anytimeai.ai/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.anytimeai.ai/resources/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.anytimeai.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.anytimeai.ai/resources/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anytime-ai/refs/heads/main/security/anytime-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/anytime-ai-trust-center.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anytime-ai/refs/heads/main/hosts/anytime-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anytime-ai-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anytime-ai/refs/heads/main/security/anytime-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anytime-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anytimeai.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.anytimeai.ai/security/
- group: start
  title: ''
  type: Login
  url: https://enterprise.anytimeai.ai/auth/amplify/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.anytimeai.ai/book-demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anytimeai-wordpress-storage.s3.us-east-1.amazonaws.com/2025/08/29161539/Anytime-AI-Data-Privacy-and-Security.pdf
coverage:
  checked: 2026-09-25
  detail: Developer portal pages render via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 404
    url: https://dev.anytimeai.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Anytime AI provides an AI‑powered legal assistant platform for plaintiff lawyers, offering tools for case analysis, discovery, demand letters, and settlement strategy. The company focuses on complex litigation, delivering a personalized agentic co‑worker that helps settle cases faster and at higher values. Its SaaS solution includes practice‑area specific modules such as personal injury, nursing‑home litigation, medical malpractice, truck accidents, and traumatic brain injury, with a roadmap for version 3.0.
image: https://framerusercontent.com/assets/8LZa600hJwt5uutnkTkBsVkPu1s.png
layout: provider
modified: '2026-09-25'
name: Anytime AI
nav: Providers
network: true
overview: 'Anytime AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Legal Tech, Litigation, Software-as-a-Service, and PlaintiffLawyers.


  Anytime AI''s developer surface includes engineering blog, documentation, getting-started guide, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anytime Ai Domain Security
  slug: anytime-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Anytime Ai Trust Center
  slug: anytime-ai-trust-center
  summary_line: SOC 2, HIPAA
slug: anytime-ai
tags:
- Artificial Intelligence
- Legal Tech
- Litigation
- Software-as-a-Service
- PlaintiffLawyers
website: https://www.anytimeai.ai/
---
