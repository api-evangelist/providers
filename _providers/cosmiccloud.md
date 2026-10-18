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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for building and managing cloud applications via Cosmiccloud platform.
  name: Cosmiccloud API
  slug: cosmiccloud-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosmiccloud/refs/heads/main/authentication/cosmiccloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cosmiccloud-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosmiccloud/refs/heads/main/llms/cosmiccloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cosmiccloud-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosmiccloud/refs/heads/main/well-known/cosmiccloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cosmiccloud-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cosmiccloud/refs/heads/main/hosts/cosmiccloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cosmiccloud-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cosmiccloud/refs/heads/main/vendors/cosmiccloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cosmiccloud-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cosmocloud.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cosmocloud.io/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cosmocloud.io/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cosmocloud.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cosmocloud
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosmiccloud/refs/heads/main/security/cosmiccloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cosmiccloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cosmocloud.io
coverage:
  detail: Documentation pages are served as JavaScript‑rendered single‑page apps, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.cosmocloud.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Cosmiccloud provides an auto‑DevOps platform that enables developers to deploy, scale, and monitor applications across multiple cloud providers with minimal effort. Their solution offers a no‑code backend, automated release and rollback, logging, DNS integration, and comprehensive monitoring, targeting startups and small‑scale companies seeking to reduce operational overhead and accelerate delivery.
image: https://cosmocloud.io/opengraph-image.png?a133d11a1c5c7b13
layout: provider
modified: '2026-10-11'
name: Cosmiccloud
nav: Providers
network: true
overview: 'Cosmiccloud is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, DevOps, Automation, Deployment, and Startups.


  Cosmiccloud''s developer surface includes authentication, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 18.7
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
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cosmiccloud Authentication
  slug: cosmiccloud-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cosmiccloud Domain Security
  slug: cosmiccloud-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cosmiccloud
tags:
- Cloud
- DevOps
- Automation
- Deployment
- Startups
- Company
website: https://cosmocloud.io
---
