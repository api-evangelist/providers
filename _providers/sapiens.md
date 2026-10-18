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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sapiens/refs/heads/main/integrations/sapiens-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/sapiens-integration-edges.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sapiens.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sapiens/refs/heads/main/hosts/sapiens-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sapiens-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sapiens/refs/heads/main/vendors/sapiens-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sapiens-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sapiens/refs/heads/main/security/sapiens-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sapiens-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sapiens/refs/heads/main/security/sapiens-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sapiens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sapiens.com
- group: company
  title: ''
  type: Blog
  url: https://sapiens.com/resource/blog/
- group: other
  title: ''
  type: Leadership
  url: https://sapiens.com/about/leadership/
- group: company
  title: ''
  type: Newsroom
  url: https://sapiens.com/newsroom/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sapiens.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.sapiens.com/sapiens/?id=csm_login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sapiens.com/legal-notice/
created: '2026-10-13'
description: 'Sapiens International (NASDAQ: SPNS) provides core, digital and data software for the insurance industry, including IDITSuite (P&C), CoreSuite (Life & Pensions) and ReinsuranceMaster. Sapiens describes its platform as API-based, but publishes no public developer portal, API reference or machine-readable contract; API access is through customer and partner engagements. The website returned a bot challenge (HTTP 403) to automated reads on 2026-10-13.'
image: https://sapiens.com/wp-content/uploads/2026/05/Sapiens_Logo_full_color_RGB-scaled.png
layout: provider
modified: '2026-10-13'
name: Sapiens International
nav: Providers
network: true
overview: 'Sapiens International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurance Software, and Financial Services.


  Sapiens International''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 42.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sapiens Domain Security
  slug: sapiens-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sapiens Trust Center
  slug: sapiens-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: sapiens
tags:
- Company
- Insurance
- Insurance Software
- Financial Services
website: https://sapiens.com
---
