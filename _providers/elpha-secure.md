---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.elphasecure.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.elphasecure.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.elphasecure.com/rss/
- group: operate
  title: ''
  type: Support
  url: https://help.elphasecure.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.elphasecure.com/en
- group: start
  title: ''
  type: Login
  url: https://my.elphasecure.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elphasecure.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elphasecure.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elphasecure
- group: company
  title: ''
  type: Newsroom
  url: https://www.elphasecure.com/newsroom
- group: auth
  title: ''
  type: Compliance
  url: https://www.elphasecure.com/about
- group: design
  title: ''
  type: Conformance
  url: conformance/elpha-secure-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elpha-secure-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elpha-secure-domain-security.yml
coverage:
  checked: '2026-08-12'
  detail: Elpha Secure's Terms of Service section 9 defines "Elpha Secure API's" as SOAP- or REST-based interfaces and says Sample Code and API documentation sit on "the Site" for third parties building integrations, but no such page is publicly linked or reachable — the only entry point is the my.elphasecure.com portal sign-in behind a broker appointment, and api/docs/developer.elphasecure.com do not resolve at all.
  evidence:
  - status: 200
    url: https://www.elphasecure.com/terms
  - status: 200
    url: https://my.elphasecure.com/
  - status: 404
    url: https://www.elphasecure.com/openapi.json
  - status: 0
    url: https://developer.elphasecure.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-12'
description: Elpha Secure is a New York-based cyber insurance managing general agent (MGA) for small and midsize businesses that bundles a first-party cybersecurity software agent with the insurance policy itself. The Elpha Agent ships endpoint detection and response, Malware Guard anti-malware, encrypted offsite backup, multi-factor authentication for remote desktop access, email security (ES Mail), financial fraud detection, vulnerability and security-posture scoring, and XDR integrations with SentinelOne, Sophos, Trend Micro and CrowdStrike, all managed from the Elpha Secure Portal. Policies are distributed through appointed brokers who quote and bind in the broker portal. Elpha Secure publishes no public developer portal, API reference or machine-readable specification; its Terms of Service define "Elpha Secure API's" as SOAP- or REST-based interfaces made available to customers and integrators under agreement.
image: https://cdn.prod.website-files.com/613b6b937db59c019880acd9/6195561e2839dc1c1ad55691_OpenGraph%20Img.jpg
layout: provider
modified: '2026-08-12'
name: Elpha Secure
nav: Providers
network: true
overview: 'Elpha Secure is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Cyber Insurance, Insurance, and Insurtech.


  Elpha Secure''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Elpha Secure Plans Pricing
  plan_count: 0
  slug: elpha-secure-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Elpha Secure Rate Limits
  slug: elpha-secure-rate-limits
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elpha-secure/refs/heads/main/screenshots/elpha-secure-2026-09-02T145346.png
security:
- kind: domain-security
  name: Elpha Secure Domain Security
  slug: elpha-secure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elpha-secure
tags:
- Company
- Cybersecurity
- Cyber Insurance
- Insurance
- Insurtech
- Endpoint Security
- Managed Detection and Response
- Email Security
- Backup and Recovery
- Risk Management
- Small Business
website: https://www.elphasecure.com/
---
