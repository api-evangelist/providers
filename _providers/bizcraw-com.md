---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bizcraw-com/plans/bizcraw-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bizcraw-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bizcraw-com/llms/bizcraw-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bizcraw-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bizcraw-com/well-known/bizcraw-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bizcraw-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bizcraw-com/hosts/bizcraw-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bizcraw-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bizcraw-com/vendors/bizcraw-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bizcraw-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://bizcraw.com/security
- group: auth
  href: https://artifacts.apis.io/bizcraw-com/security/bizcraw-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bizcraw-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bizcraw.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bizcraw.com/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://bizcraw.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://bizcraw.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bizcraw.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bizcraw.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://bizcraw.com/contact
coverage:
  checked: '2026-11-02'
  detail: The documentation site is heavily JavaScript‑rendered, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://bizcraw.com/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Bizcraw provides a web scraping and AI‑powered sales workspace that helps teams collect fresh market data, transform it into structured leads, and push those leads directly into CRM systems. The platform offers repeatable scraping workflows, AI‑assisted data enrichment, role‑based access controls, and audit trails, enabling accountable sales operations from discovery through quoting and closing.
image: https://bizcraw.com/landing/bizcraw-dashboard-hero.png
layout: provider
modified: '2026-11-02'
name: Bizcraw
nav: Providers
network: true
overview: 'Bizcraw is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Web Scraping, AI Sales, Lead Generation, CRM Integration, and Software-as-a-Service.


  Bizcraw''s developer surface includes documentation, pricing, signup flow, support, and 10 more developer resources.'
plans:
- name: Bizcraw Com Plans Pricing
  plan_count: 4
  slug: bizcraw-com-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bizcraw Com Domain Security
  slug: bizcraw-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bizcraw-com
tags:
- Web Scraping
- AI Sales
- Lead Generation
- CRM Integration
- Software-as-a-Service
- Automation
website: https://bizcraw.com/
---
