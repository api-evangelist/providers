---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alertmedia/refs/heads/main/llms/alertmedia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alertmedia-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alertmedia/refs/heads/main/well-known/alertmedia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alertmedia-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alertmedia/refs/heads/main/hosts/alertmedia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alertmedia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alertmedia/refs/heads/main/vendors/alertmedia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alertmedia-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.alertmedia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alertmedia.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alertmedia.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alertmedia.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.alertmedia.com/about/news/
- group: start
  title: ''
  type: Login
  url: https://dashboard.alertmedia.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.alertmedia.com/about/team/
- group: company
  title: ''
  type: Blog
  url: https://www.alertmedia.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alertmedia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.alertmedia.com/password
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alertmedia/refs/heads/main/security/alertmedia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alertmedia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alertmedia.com/
created: '2026-09-24'
description: AlertMedia offers a unified risk intelligence and response platform that provides mass notification, threat intelligence, travel risk management, employee safety monitoring, incident response, and social intelligence. The platform is designed for organizations that need to protect people and operations across global locations. It delivers real‑time risk visibility, analyst‑verified alerts, and built‑in workflows to coordinate and resolve incidents.
image: https://www.alertmedia.com/wp-content/uploads/2016/05/052616-7MustHaves-EmergencyNotificationSystem.jpg
layout: provider
modified: '2026-09-24'
name: AlertMedia
nav: Providers
network: true
overview: 'AlertMedia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mass Notification, Threat Intelligence, Travel Risk Management, Employee Safety Monitoring, and Incident Response.


  AlertMedia''s developer surface includes pricing, engineering blog, documentation, and 13 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alertmedia Domain Security
  slug: alertmedia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alertmedia
tags:
- Mass Notification
- Threat Intelligence
- Travel Risk Management
- Employee Safety Monitoring
- Incident Response
- Social Intelligence
- Risk Intelligence Platform
website: https://www.alertmedia.com/
---
