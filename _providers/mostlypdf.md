---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Run any MostlyPDF tool programmatically via a single POST endpoint.
  name: MostlyPDF API
  slug: mostlypdf-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mostlypdf/refs/heads/main/well-known/mostlypdf-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mostlypdf-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mostlypdf/refs/heads/main/well-known/mostlypdf-mostly-pdf-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mostlypdf-mostly-pdf-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mostlypdf/refs/heads/main/well-known/mostlypdf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mostlypdf-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mostlypdf/refs/heads/main/authentication/mostlypdf-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mostlypdf-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mostlypdf/refs/heads/main/llms/mostlypdf-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mostlypdf-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mostlypdf/refs/heads/main/hosts/mostlypdf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mostlypdf-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mostlypdf/refs/heads/main/vendors/mostlypdf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mostlypdf-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://mostlypdf.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mostlypdf/refs/heads/main/security/mostlypdf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mostlypdf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mostlypdf.com
- group: docs
  title: ''
  type: Documentation
  url: https://mostlypdf.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mostlypdf.com/docs
- group: operate
  title: ''
  type: Support
  url: https://mostlypdf.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mostlypdf.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mostlypdf.com/legal/privacy
- group: other
  title: ''
  type: SignIn
  url: https://mostlypdf.com/signin
created: '2026-10-02'
description: MostlyPDF provides a free online suite of PDF tools and a flat‑priced API that consolidates 38 PDF operations—merge, split, compress, OCR, conversion and more—into a single endpoint. Users can process files via base64 payloads with a bearer token, enabling automation of everyday document workflows without per‑operation credit weighting. The service is offered by Mostly Tiny Ltd and includes a free plan with no sign‑up, watermark, or daily limits.
image: https://mostlypdf.com/og.png
layout: provider
modified: '2026-10-02'
name: MostlyPDF
nav: Providers
network: true
overview: 'MostlyPDF publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PDF, Automation, and Free Tools.


  MostlyPDF''s developer surface includes authentication, engineering blog, documentation, API reference, support, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mostlypdf Authentication
  slug: mostlypdf-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mostlypdf Domain Security
  slug: mostlypdf-domain-security
  summary_line: TLSv1.3 · HSTS
slug: mostlypdf
tags:
- Company
- PDF
- Automation
- Free Tools
website: https://mostlypdf.com
---
