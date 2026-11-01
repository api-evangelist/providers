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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: eMudhra provides PKI and digital trust services; the website lists API‑first KYC, OCR, face‑match and other verification APIs.
  name: eMudhra API
  slug: emudhra-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/emudhra/llms/emudhra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emudhra-llms.txt
- group: other
  href: https://artifacts.apis.io/emudhra/hosts/emudhra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emudhra-hosts.yml
- group: other
  href: https://artifacts.apis.io/emudhra/vendors/emudhra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/emudhra-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emudhra.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.emudhra.com/portal/en/home
- group: start
  title: ''
  type: SignUp
  url: https://emudhra.com/en/certinext/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emudhra.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://emudhra.com/en-us/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://emudhra.com/en/emsigner/developer-portal/
- group: company
  title: ''
  type: Blog
  url: https://emudhra.com/en-us/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emudhra
- group: auth
  href: https://artifacts.apis.io/emudhra/security/emudhra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emudhra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emudhra.com/
coverage:
  checked: '2026-10-27'
  detail: Main website renders content via JavaScript, preventing machine‑readable API specs from being discovered.
  evidence:
  - status: 200
    url: https://emudhra.com/en-us/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: eMudhra provides enterprise-grade Public Key Infrastructure (PKI) solutions, including post‑quantum cryptography, digital signatures, e‑signing, identity verification, and secure document workflow services. Their platform supports enterprises, governments, and financial institutions with compliance‑ready digital trust tools, offering products such as emSigner, SecurePass, and IDBroker for robust authentication and electronic signing.
layout: provider
modified: '2026-10-27'
name: eMudhra
nav: Providers
network: true
overview: 'eMudhra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PKI, DigitalTrust, EnterpriseSoftware, and Security.


  eMudhra''s developer surface includes support, signup flow, engineering blog, and 10 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Emudhra Domain Security
  slug: emudhra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emudhra
tags:
- Company
- PKI
- DigitalTrust
- EnterpriseSoftware
- Security
website: https://emudhra.com/
---
