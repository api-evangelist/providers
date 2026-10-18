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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudwick/refs/heads/main/well-known/cloudwick-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudwick-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cloudwick.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudwick/refs/heads/main/security/cloudwick-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cloudwick-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudwick/refs/heads/main/hosts/cloudwick-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudwick-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudwick/refs/heads/main/vendors/cloudwick-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudwick-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudwick/refs/heads/main/security/cloudwick-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudwick-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudwick/refs/heads/main/security/cloudwick-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudwick-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudwick/refs/heads/main/security/cloudwick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudwick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudwick.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudwick.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://cloudwick.com/support-services-and-legal
- group: auth
  title: ''
  type: TrustCenter
  url: https://cloudwick.com/trust-center
- group: operate
  title: ''
  type: Contact
  url: https://cloudwick.com/contact-us
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://cloudwick.com/mcp
  - status: 200
    url: https://cloudwick.com
  - status: 403
    url: https://equityzen.com/company/cloudwick
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Cloudwick is a practitioner‑led data and AI company that builds governed data foundations for public sector agencies. Their Amorphic platform deploys into agency AWS accounts, providing data infrastructure for modern applications, analytics, and AI. Founded in 2010, Cloudwick serves government, public health, energy, and regulated industries, helping modernize operations and deliver better services through data‑driven solutions.
layout: provider
modified: '2026-10-09'
name: Cloudwick
nav: Providers
network: true
overview: 'Cloudwick is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Artificial Intelligence, Government, and Cloud.


  Cloudwick''s developer surface includes support and 12 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudwick Domain Security
  slug: cloudwick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudwick Vulnerability Disclosure
  slug: cloudwick-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cloudwick Trust Center
  slug: cloudwick-trust-center
  summary_line: SOC 2, HIPAA
slug: cloudwick
tags:
- Company
- Data
- Artificial Intelligence
- Government
- Cloud
website: https://cloudwick.com
---
