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
api_count: 1
apis:
- description: Azimuth GRC offers the VALIDATOR platform with API access for compliance automation, as described on the developer page.
  name: Azimuth GRC API
  slug: azimuth-grc-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azimuth-grc/refs/heads/main/llms/azimuth-grc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azimuth-grc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azimuth-grc/refs/heads/main/hosts/azimuth-grc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azimuth-grc-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azimuth-grc/refs/heads/main/security/azimuth-grc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azimuth-grc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.azimuthgrc.com
- group: company
  title: ''
  type: Blog
  url: https://www.azimuthgrc.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.azimuthgrc.com/val
- group: docs
  title: ''
  type: APIReference
  url: https://www.azimuthgrc.com/val
- group: start
  title: ''
  type: GettingStarted
  url: https://www.azimuthgrc.com/val-registration
- group: operate
  title: ''
  type: Support
  url: https://www.azimuthgrc.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.azimuthgrc.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.azimuthgrc.com/subscription-agreement
- group: start
  title: ''
  type: SignUp
  url: https://www.azimuthgrc.com/book-a-demo
coverage:
  checked: '2026-09-27'
  detail: Developer pages are HTML with no machine‑readable OpenAPI or other contract discovered despite probing common spec URLs.
  evidence:
  - status: 0
    url: https://api.azimuthgrc.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Azimuth GRC provides automated compliance management software that transforms complex regulatory requirements into clear, actionable guidance. Their platform, VALIDATOR, offers real‑time monitoring, audit automation, and curated legal content to help organizations maintain continuous compliance across industries. With features like ROI calculators, detailed reporting, and integration capabilities, Azimuth GRC serves enterprises seeking to streamline governance, risk, and compliance processes.
image: https://irp.cdn-website.com/b6676fb3/dms3rep/multi/opt/Untitled+design+-+2025-05-08T154514.455-1920w.png
layout: provider
modified: '2026-09-27'
name: Azimuth GRC
nav: Providers
network: true
overview: 'Azimuth GRC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, Governance, Risk Management, and Automation.


  Azimuth GRC''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, signup flow, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
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
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Azimuth Grc Domain Security
  slug: azimuth-grc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azimuth-grc
tags:
- Company
- Compliance
- Governance
- Risk Management
- Automation
- Software-as-a-Service
website: https://www.azimuthgrc.com
---
