---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 67
  human_in_the_loop: 2
  name: Godaddy Agentic Access
  operation_count: 119
  slug: godaddy-agentic-access
  summary_line: 119 operations · 67 acting · 2 human-in-the-loop
api_count: 7
apis:
- description: The Actions API from GoDaddy — 2 operation(s) for actions.
  name: GoDaddy Actions API
  slug: godaddy-actions-api
- description: The Contacts API from GoDaddy — 1 operation(s) for contacts.
  name: GoDaddy Contacts API
  slug: godaddy-contacts-api
- description: The Domains API from GoDaddy — 24 operation(s) for domains.
  name: GoDaddy Domains API
  slug: godaddy-domains-api
- description: API for auction-related actions exclusive to whitelisted partners.
  name: 'GoDaddy Expiry Auctions: Registrar Partners API'
  slug: godaddy-expiry-auctions-registrar-partners-api
- description: The Notifications API from GoDaddy — 4 operation(s) for notifications.
  name: GoDaddy Notifications API
  slug: godaddy-notifications-api
- description: The v1 API from GoDaddy — 49 operation(s) for v1.
  name: GoDaddy v1 API
  slug: godaddy-v1-api
- description: An incremental update that keeps the endpoints largely the same, but deprecates some commonly misused parameters and add some features to ensure reports can be worked quicker.
  name: GoDaddy v2 API
  slug: godaddy-v2-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Abuse API
  slug: open-godaddy-abuse
- collection_type: open
  name: Abuse Actions API
  slug: open-godaddy-actions-api
- collection_type: open
  name: Aftermarket API
  slug: open-godaddy-aftermarket
- collection_type: open
  name: API Collection
  slug: open-godaddy-agreements
- collection_type: open
  name: API Collection
  slug: open-godaddy-certificates
- collection_type: open
  name: Abuse Actions Contacts API
  slug: open-godaddy-contacts-api
- collection_type: open
  name: API Collection
  slug: open-godaddy-countries
- collection_type: open
  name: Abuse Actions Domains API
  slug: open-godaddy-domains-api
- collection_type: open
  name: Domains API
  slug: open-godaddy-domains
- collection_type: open
  name: 'Abuse Actions Expiry Auctions: Registrar Partners API'
  slug: open-godaddy-expiry-auctions-registrar-partners-api
- collection_type: open
  name: Abuse Actions Notifications API
  slug: open-godaddy-notifications-api
- collection_type: open
  name: API Collection
  slug: open-godaddy-orders
- collection_type: open
  name: API Collection
  slug: open-godaddy-shoppers
- collection_type: open
  name: API Collection
  slug: open-godaddy-subscriptions
- collection_type: open
  name: Abuse Actions v1 API
  slug: open-godaddy-v1-api
- collection_type: open
  name: Abuse Actions v2 API
  slug: open-godaddy-v2-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/godaddy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/godaddy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/godaddy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/godaddy
- group: company
  title: ''
  type: Website
  url: https://www.godaddy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.godaddy.com/doc
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.godaddy.com/getstarted
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.godaddy.com/legal/agreements/developer-api-terms
- group: operate
  title: ''
  type: Support
  url: https://developer.godaddy.com/support
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.godaddy.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.godaddy.com/resources/feed
created: '2026-03-16'
description: GoDaddy is a domain registrar and web hosting company offering REST APIs for domain registration, DNS management, certificates, shopper accounts, subscriptions, aftermarket auctions, and abuse reporting.
finops:
- name: Godaddy Finops
  service_category: Domains / DNS / Hosting
  slug: godaddy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/godaddy.png
json_structures:
- name: Godaddy Structure
  property_count: 0
  slug: godaddy-structure
layout: provider
modified: '2026-05-19'
name: GoDaddy
nav: Providers
network: true
overview: 'GoDaddy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Contacts API, Domains API, and 4 more. Tagged areas include Aftermarket, Certificates, DNS, Domains, and Hosting.


  GoDaddy''s developer surface includes documentation, getting-started guide, support, engineering blog, and 7 more developer resources.'
plans:
- name: Godaddy Plans Pricing
  plan_count: 2
  slug: godaddy-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Godaddy Rate Limits
  slug: godaddy-rate-limits
score:
  band: thin
  composite: 28.5
  delta: -2.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 43.5
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/screenshots/godaddy-2026-06-20T181947.png
security:
- kind: domain-security
  name: Godaddy Domain Security
  slug: godaddy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: godaddy
tags:
- Aftermarket
- Certificates
- DNS
- Domains
- Hosting
- Registrar
website: https://www.godaddy.com/
---
