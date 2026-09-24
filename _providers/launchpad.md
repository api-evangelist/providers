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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/launchpad/refs/heads/main/plans/launchpad-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/launchpad-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/launchpad/refs/heads/main/conformance/launchpad-conformance.yml
  title: ''
  type: Conformance
  url: conformance/launchpad-conformance.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/launchpad
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/launchpad/refs/heads/main/security/launchpad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/launchpad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://launchpad.net/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.ubuntu.com/launchpad/
- group: docs
  title: ''
  type: APIReference
  url: https://api.launchpad.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://launchpad.net/+tour
- group: operate
  title: ''
  type: Support
  url: https://launchpad.net/feedback
- group: company
  title: ''
  type: Blog
  url: https://blog.launchpad.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ubuntu.com/legal/launchpad-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ubuntu.com/legal/dataprivacy
coverage:
  checked: 2026-09-21
  detail: API host https://api.launchpad.net returns 404 for common OpenAPI endpoints, and no machine‑readable contract was found.
  evidence:
  - status: 404
    url: https://api.launchpad.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-21'
description: Launchpad is a software collaboration platform operated by Canonical Ltd. It provides bug tracking, code hosting with Git, code reviews, package building, translations, mailing lists, answers, blueprints, and a web service API for developers to automate interactions with projects hosted on Launchpad.
image: https://launchpad.net/@@/launchpad-og-image.png
layout: provider
modified: '2026-09-21'
name: Launchpad
nav: Providers
network: true
overview: 'Launchpad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Collaboration, Open Source, Bug Tracking, and Code Hosting.


  Launchpad''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 7 more developer resources.'
plans:
- name: Launchpad Plans Pricing
  plan_count: 5
  slug: launchpad-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 50.0
    operational_transparency: 5.3
  previous_composite: 25.5
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Launchpad Domain Security
  slug: launchpad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: launchpad
tags:
- Company
- Collaboration
- Open Source
- Bug Tracking
- Code Hosting
website: https://launchpad.net/
---
