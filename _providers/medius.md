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
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/vendors/medius-vendors.yml
  title: ''
  type: Vendors
  url: vendors/medius-vendors.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/plans/medius-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/medius-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.medius.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/security/medius-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/medius-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/llms/medius-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/medius-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/well-known/medius-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/medius-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/well-known/medius-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/medius-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/well-known/medius-medius-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/medius-medius-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/well-known/medius-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/medius-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/hosts/medius-hosts.yml
  title: ''
  type: Hosts
  url: hosts/medius-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.medius.com/support/home
- group: operate
  title: ''
  type: StatusPage
  url: https://status.medius.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medius.com/legal/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.medius.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.medius.com/about/management/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.medius.com/solutions/supplier-onboarding/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/security/medius-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/medius-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/security/medius-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/medius-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medius/refs/heads/main/security/medius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/medius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://medius.com/
- group: company
  title: ''
  type: Blog
  url: https://www.medius.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.medius.com/pricing/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discovered despite public documentation pages.
  evidence:
  - status: 404
    url: https://api.medius.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Medius provides cloud‑based AP automation and global payment software, helping enterprises streamline invoice processing, e‑invoicing, and payment workflows. The platform offers AI‑driven fraud detection, multi‑currency support, and integration with major ERP systems like Microsoft Dynamics, SAP, and Oracle. Medius serves large and midsize businesses across industries, delivering compliance tools, supplier collaboration, and analytics to improve financial operations and reduce manual effort.
image: https://www.medius.com/media/qwicpkbv/medius-social-share-1440-x-1440.png?width=1200&height=630&v=1d9561da6e55cf0
layout: provider
modified: '2026-10-15'
name: Medius
nav: Providers
network: true
overview: 'Medius is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AP Automation, Payments, Artificial Intelligence, and ERP Integration.


  Medius'' developer surface includes support, getting-started guide, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Medius Plans Pricing
  plan_count: 1
  slug: medius-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 58.9
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Medius Domain Security
  slug: medius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Medius Vulnerability Disclosure
  slug: medius-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Medius Trust Center
  slug: medius-trust-center
  summary_line: SOC 2, ISO 27001
slug: medius
tags:
- Company
- AP Automation
- Payments
- Artificial Intelligence
- ERP Integration
website: https://medius.com/
---
